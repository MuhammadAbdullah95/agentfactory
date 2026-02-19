#!/usr/bin/env python3
"""Authenticate with Panaversity SSO using RFC 8628 Device Authorization Flow.

Uses only Python stdlib -- no pip install required.
Saves tokens to ~/.agentfactory/credentials.json (chmod 600).
"""

import json
import os
import sys
import time
import webbrowser
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

SSO_URL = "https://sso.panaversity.org"
CLIENT_ID = "learn-skill-cli-client"
CREDENTIALS_PATH = Path.home() / ".agentfactory" / "credentials.json"


def main():
    sso_url = os.environ.get("PANAVERSITY_SSO_URL", SSO_URL)

    # Step 1: Request device code
    data = json.dumps({"client_id": CLIENT_ID}).encode()
    req = Request(
        f"{sso_url}/api/auth/device/code", data=data, method="POST"
    )
    req.add_header("Content-Type", "application/json")

    try:
        resp = urlopen(req)
    except HTTPError as e:
        print(f"Failed to start device flow: {e.code} {e.reason}", file=sys.stderr)
        sys.exit(1)

    result = json.loads(resp.read())

    device_code = result["device_code"]
    user_code = result["user_code"]
    verification_uri = result.get("verification_uri", f"{sso_url}/device")
    interval = result.get("interval", 5)

    # Step 2: Show user code and open browser
    print(f"\nTo authenticate, open: {verification_uri}")
    print(f"And enter code: {user_code}\n")

    try:
        webbrowser.open(verification_uri)
    except Exception:
        pass  # Browser open is best-effort

    # Step 3: Poll for token
    print("Waiting for authorization...", end="", flush=True)
    while True:
        time.sleep(interval)
        print(".", end="", flush=True)

        poll_data = json.dumps(
            {
                "client_id": CLIENT_ID,
                "device_code": device_code,
                "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            }
        ).encode()
        poll_req = Request(
            f"{sso_url}/api/auth/device/token", data=poll_data, method="POST"
        )
        poll_req.add_header("Content-Type", "application/json")

        try:
            poll_resp = urlopen(poll_req)
            tokens = json.loads(poll_resp.read())

            # Step 4: Save credentials
            CREDENTIALS_PATH.parent.mkdir(parents=True, exist_ok=True)
            CREDENTIALS_PATH.write_text(json.dumps(tokens, indent=2))
            CREDENTIALS_PATH.chmod(0o600)

            print(f"\n\nAuthenticated successfully!")
            print(f"Credentials saved to {CREDENTIALS_PATH}")
            return

        except HTTPError as e:
            body = json.loads(e.read())
            error = body.get("error", "")
            if error == "authorization_pending":
                continue
            elif error == "slow_down":
                interval += 5
                continue
            elif error == "expired_token":
                print("\n\nDevice code expired. Please try again.")
                sys.exit(1)
            elif error == "access_denied":
                print("\n\nAuthorization denied.")
                sys.exit(1)
            else:
                print(f"\n\nError: {body}")
                sys.exit(1)


if __name__ == "__main__":
    main()
