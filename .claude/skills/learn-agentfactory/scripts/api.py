#!/usr/bin/env python3
"""Content API client for learn-agentfactory skill.

Single entry point for all Content API operations.
Handles token loading, auth headers, auto-refresh on 401, and error responses.

Uses only Python stdlib — no pip install required.

Usage:
    python3 scripts/api.py tree
    python3 scripts/api.py lesson <part> <chapter> <lesson>
    python3 scripts/api.py complete <chapter> <lesson> [duration_secs]
    python3 scripts/api.py progress
    python3 scripts/api.py health
"""

import json
import os
import stat
import sys
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

CREDENTIALS_PATH = Path.home() / ".agentfactory" / "credentials.json"
DEFAULT_API_URL = "https://content-api.panaversity.org"
DEFAULT_SSO_URL = "https://sso.panaversity.org"
CLIENT_ID = "learn-skill-cli-client"


def _load_token() -> str:
    """Load auth token from credentials file.

    Prefers id_token (JWT) over access_token (opaque) because downstream
    services like progress-api validate JWTs locally via JWKS, whereas
    opaque tokens require a round-trip to SSO's userinfo endpoint.
    """
    if not CREDENTIALS_PATH.exists():
        print(
            "ERROR: Not authenticated.\n"
            "Run: python3 scripts/auth.py",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        creds = json.loads(CREDENTIALS_PATH.read_text())
    except (json.JSONDecodeError, OSError) as e:
        print(f"ERROR: Cannot read credentials: {e}", file=sys.stderr)
        sys.exit(1)

    # Prefer id_token (JWT) — validates locally at both content-api and progress-api
    token = creds.get("id_token") or creds.get("access_token")
    if not token:
        print(
            "ERROR: No token in credentials.\n"
            "Run: python3 scripts/auth.py",
            file=sys.stderr,
        )
        sys.exit(1)

    return token


def _base_url() -> str:
    return os.environ.get("CONTENT_API_URL", DEFAULT_API_URL).rstrip("/")


def _sso_url() -> str:
    return os.environ.get("PANAVERSITY_SSO_URL", DEFAULT_SSO_URL).rstrip("/")


def _try_refresh() -> str | None:
    """Attempt to refresh the access token using the stored refresh_token.

    Returns the new access_token on success, None on failure.
    """
    if not CREDENTIALS_PATH.exists():
        return None

    try:
        creds = json.loads(CREDENTIALS_PATH.read_text())
    except (json.JSONDecodeError, OSError):
        return None

    refresh_token = creds.get("refresh_token")
    if not refresh_token:
        return None

    body = urlencode({
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": CLIENT_ID,
    }).encode()

    req = Request(
        f"{_sso_url()}/api/auth/oauth2/token",
        data=body,
        method="POST",
    )
    req.add_header("Content-Type", "application/x-www-form-urlencoded")

    try:
        with urlopen(req, timeout=15) as resp:
            new_tokens = json.loads(resp.read())
    except Exception:
        return None

    new_access = new_tokens.get("access_token")
    if not new_access:
        return None

    # Save updated tokens
    creds["access_token"] = new_access
    if new_tokens.get("refresh_token"):
        creds["refresh_token"] = new_tokens["refresh_token"]
    if new_tokens.get("id_token"):
        creds["id_token"] = new_tokens["id_token"]

    try:
        CREDENTIALS_PATH.write_text(json.dumps(creds, indent=2))
        CREDENTIALS_PATH.chmod(stat.S_IRUSR | stat.S_IWUSR)  # 600
    except OSError:
        pass  # token works even if save fails

    return new_access


def _api_get(path: str, params: dict | None = None) -> dict:
    """Authenticated GET to Content API. Auto-refreshes token on 401."""
    url = f"{_base_url()}{path}"
    if params:
        url += "?" + urlencode(params)

    token = _load_token()
    for attempt in range(2):
        req = Request(url)
        req.add_header("Authorization", f"Bearer {token}")
        req.add_header("Accept", "application/json")

        try:
            with urlopen(req, timeout=30) as resp:
                return json.loads(resp.read())
        except HTTPError as e:
            if e.code == 401 and attempt == 0:
                new_token = _try_refresh()
                if new_token:
                    token = new_token
                    continue  # retry with refreshed token
            _handle_http_error(e)
        except OSError as e:
            print(f"ERROR: Connection failed: {e}", file=sys.stderr)
            sys.exit(1)
    return {}  # unreachable


def _api_post(path: str, data: dict) -> dict:
    """Authenticated POST to Content API. Auto-refreshes token on 401."""
    url = f"{_base_url()}{path}"
    body = json.dumps(data).encode()

    token = _load_token()
    for attempt in range(2):
        req = Request(url, data=body, method="POST")
        req.add_header("Authorization", f"Bearer {token}")
        req.add_header("Content-Type", "application/json")
        req.add_header("Accept", "application/json")

        try:
            with urlopen(req, timeout=30) as resp:
                return json.loads(resp.read())
        except HTTPError as e:
            if e.code == 401 and attempt == 0:
                new_token = _try_refresh()
                if new_token:
                    token = new_token
                    continue  # retry with refreshed token
            _handle_http_error(e)
        except OSError as e:
            print(f"ERROR: Connection failed: {e}", file=sys.stderr)
            sys.exit(1)
    return {}  # unreachable


def _handle_http_error(e: HTTPError):
    """Handle HTTP errors with actionable messages."""
    if e.code == 401:
        print(
            "ERROR: Token expired or invalid.\n"
            "Run: python3 scripts/auth.py",
            file=sys.stderr,
        )
        sys.exit(1)
    elif e.code == 402:
        body = _safe_json(e)
        msg = body.get("detail", "Insufficient credits")
        print(f"ERROR: Payment required — {msg}", file=sys.stderr)
        sys.exit(1)
    elif e.code == 403:
        body = _safe_json(e)
        msg = body.get("detail", "Access denied")
        print(f"ERROR: Forbidden — {msg}", file=sys.stderr)
        sys.exit(1)
    elif e.code == 404:
        print("ERROR: Not found. Check part/chapter/lesson slugs.", file=sys.stderr)
        sys.exit(1)
    elif e.code == 429:
        print("ERROR: Rate limited. Wait a moment and try again.", file=sys.stderr)
        sys.exit(1)
    elif e.code == 503:
        body = _safe_json(e)
        msg = body.get("detail", "Service unavailable")
        print(f"ERROR: Service unavailable — {msg}", file=sys.stderr)
        sys.exit(1)
    else:
        body_text = e.read().decode(errors="replace")
        print(f"ERROR: HTTP {e.code}: {body_text}", file=sys.stderr)
        sys.exit(1)


def _safe_json(e: HTTPError) -> dict:
    """Try to parse error body as JSON, return empty dict on failure."""
    try:
        return json.loads(e.read())
    except Exception:
        return {}


# ── Commands ──────────────────────────────────────────────────────────────


def cmd_health():
    """Check API health (no auth required)."""
    url = f"{_base_url()}/health"
    try:
        with urlopen(Request(url), timeout=10) as resp:
            data = json.loads(resp.read())
            print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"ERROR: Health check failed: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_tree():
    """Fetch book tree structure."""
    data = _api_get("/api/v1/content/tree")
    print(json.dumps(data, indent=2))


def cmd_lesson(part: str, chapter: str, lesson: str):
    """Fetch a single lesson."""
    data = _api_get(
        "/api/v1/content/lesson",
        {"part": part, "chapter": chapter, "lesson": lesson},
    )
    print(json.dumps(data, indent=2))


def cmd_complete(chapter: str, lesson: str, duration: int = 0):
    """Mark a lesson complete."""
    data = _api_post(
        "/api/v1/content/complete",
        {
            "chapter_slug": chapter,
            "lesson_slug": lesson,
            "active_duration_secs": duration,
            "source": "skill",
        },
    )
    print(json.dumps(data, indent=2))


def cmd_progress():
    """Fetch user's learning progress."""
    data = _api_get("/api/v1/content/progress")
    print(json.dumps(data, indent=2))


# ── Auth commands (agent-driven, non-blocking) ───────────────────────────

DEVICE_PENDING_PATH = Path.home() / ".agentfactory" / "device-pending.json"


def cmd_auth_start():
    """Start device auth flow. Non-blocking — returns immediately with user code.

    Saves device_code to ~/.agentfactory/device-pending.json for polling.
    Prints JSON: {user_code, verification_uri, interval, expires_in}
    """
    sso = _sso_url()
    data = json.dumps({
        "client_id": CLIENT_ID,
        "scope": "openid profile email",
    }).encode()
    req = Request(f"{sso}/api/auth/device/code", data=data, method="POST")
    req.add_header("Content-Type", "application/json")

    try:
        with urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read())
    except HTTPError as e:
        print(json.dumps({
            "status": "error",
            "error": f"Failed to start device flow: {e.code}",
        }))
        sys.exit(1)
    except OSError as e:
        print(json.dumps({
            "status": "error",
            "error": f"Connection failed: {e}",
        }))
        sys.exit(1)

    # Save pending state for auth-poll
    pending = {
        "device_code": result["device_code"],
        "interval": result.get("interval", 5),
        "sso_url": sso,
    }
    DEVICE_PENDING_PATH.parent.mkdir(parents=True, exist_ok=True)
    DEVICE_PENDING_PATH.write_text(json.dumps(pending))
    DEVICE_PENDING_PATH.chmod(0o600)

    # Return info for the agent to show the user
    print(json.dumps({
        "status": "started",
        "user_code": result["user_code"],
        "verification_uri": result.get("verification_uri", f"{sso}/device"),
        "interval": result.get("interval", 5),
        "expires_in": result.get("expires_in", 600),
    }))


def cmd_auth_poll():
    """Poll once for device auth completion. Non-blocking.

    Prints JSON: {status: "pending"|"complete"|"expired"|"denied"|"error"}
    On "complete", credentials are saved to ~/.agentfactory/credentials.json.
    """
    if not DEVICE_PENDING_PATH.exists():
        print(json.dumps({
            "status": "error",
            "error": "No pending auth. Run auth-start first.",
        }))
        sys.exit(1)

    try:
        pending = json.loads(DEVICE_PENDING_PATH.read_text())
    except (json.JSONDecodeError, OSError):
        print(json.dumps({
            "status": "error",
            "error": "Cannot read pending auth state.",
        }))
        sys.exit(1)

    sso = pending["sso_url"]
    poll_data = json.dumps({
        "client_id": CLIENT_ID,
        "device_code": pending["device_code"],
        "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
    }).encode()
    req = Request(f"{sso}/api/auth/device/token", data=poll_data, method="POST")
    req.add_header("Content-Type", "application/json")

    try:
        with urlopen(req, timeout=15) as resp:
            tokens = json.loads(resp.read())

        # Success — save credentials
        CREDENTIALS_PATH.parent.mkdir(parents=True, exist_ok=True)
        CREDENTIALS_PATH.write_text(json.dumps(tokens, indent=2))
        CREDENTIALS_PATH.chmod(0o600)

        # Clean up pending file
        DEVICE_PENDING_PATH.unlink(missing_ok=True)

        print(json.dumps({"status": "complete"}))

    except HTTPError as e:
        try:
            body = json.loads(e.read())
        except Exception:
            body = {}
        error = body.get("error", "")

        if error == "authorization_pending":
            print(json.dumps({"status": "pending"}))
        elif error == "slow_down":
            # Update interval in pending file
            pending["interval"] = pending.get("interval", 5) + 5
            DEVICE_PENDING_PATH.write_text(json.dumps(pending))
            print(json.dumps({
                "status": "pending",
                "interval": pending["interval"],
            }))
        elif error == "expired_token":
            DEVICE_PENDING_PATH.unlink(missing_ok=True)
            print(json.dumps({"status": "expired"}))
        elif error == "access_denied":
            DEVICE_PENDING_PATH.unlink(missing_ok=True)
            print(json.dumps({"status": "denied"}))
        else:
            print(json.dumps({
                "status": "error",
                "error": body.get("error_description", str(body)),
            }))
    except OSError as e:
        print(json.dumps({
            "status": "error",
            "error": f"Connection failed: {e}",
        }))


# ── Entry point ───────────────────────────────────────────────────────────

USAGE = """\
Usage: api.py <command> [args]

Commands:
  health                                    Check API health
  tree                                      Browse book structure
  lesson <part> <chapter> <lesson>          Read a lesson
  complete <chapter> <lesson> [duration]    Mark lesson complete
  progress                                  View learning progress
  auth-start                                Start device auth (non-blocking)
  auth-poll                                 Poll auth status (non-blocking)

Environment:
  CONTENT_API_URL     API base URL (default: https://content-api.panaversity.org)
  PANAVERSITY_SSO_URL SSO base URL (default: https://sso.panaversity.org)
"""


def main():
    if len(sys.argv) < 2:
        print(USAGE)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "health":
        cmd_health()

    elif cmd == "tree":
        cmd_tree()

    elif cmd == "lesson":
        if len(sys.argv) != 5:
            print(
                "Usage: api.py lesson <part> <chapter> <lesson>",
                file=sys.stderr,
            )
            sys.exit(1)
        cmd_lesson(sys.argv[2], sys.argv[3], sys.argv[4])

    elif cmd == "complete":
        if len(sys.argv) < 4:
            print(
                "Usage: api.py complete <chapter> <lesson> [duration_secs]",
                file=sys.stderr,
            )
            sys.exit(1)
        duration = int(sys.argv[4]) if len(sys.argv) > 4 else 0
        cmd_complete(sys.argv[2], sys.argv[3], duration)

    elif cmd == "progress":
        cmd_progress()

    elif cmd == "auth-start":
        cmd_auth_start()

    elif cmd == "auth-poll":
        cmd_auth_poll()

    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        print(USAGE)
        sys.exit(1)


if __name__ == "__main__":
    main()
