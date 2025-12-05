import { auth } from "@/lib/auth";
import { TRUSTED_CLIENTS } from "@/lib/trusted-clients";
import { cookies } from "next/headers";
import { NextRequest, NextResponse } from "next/server";

/**
 * Allowed post-logout redirect origins
 * Derived from trusted clients + SSO's own origin
 * Security: Prevents open redirect attacks (CWE-601)
 */
function getAllowedPostLogoutOrigins(): string[] {
  const origins = new Set<string>();

  // Add SSO's own origin
  const ssoUrl = process.env.BETTER_AUTH_URL || "http://localhost:3001";
  try {
    origins.add(new URL(ssoUrl).origin);
  } catch {
    // Invalid URL, skip
  }

  // Add all trusted client redirect URL origins
  for (const client of TRUSTED_CLIENTS) {
    for (const redirectUrl of client.redirectUrls) {
      try {
        origins.add(new URL(redirectUrl).origin);
      } catch {
        // Invalid URL, skip
      }
    }
  }

  // Add allowed CORS origins
  const allowedOrigins = process.env.ALLOWED_ORIGINS?.split(",") || [];
  for (const origin of allowedOrigins) {
    const trimmed = origin.trim();
    if (trimmed && trimmed.startsWith("http")) {
      try {
        origins.add(new URL(trimmed).origin);
      } catch {
        // Invalid URL, skip
      }
    }
  }

  return Array.from(origins);
}

/**
 * Validate post_logout_redirect_uri against allowed origins
 * Security: Prevents open redirect attacks
 */
function isValidPostLogoutUri(uri: string): boolean {
  try {
    const parsedUri = new URL(uri);
    const allowedOrigins = getAllowedPostLogoutOrigins();

    // Check if origin matches any allowed origin
    return allowedOrigins.includes(parsedUri.origin);
  } catch {
    return false;
  }
}

/**
 * OIDC RP-Initiated Logout Endpoint
 * Handles session termination and optionally redirects to post-logout URI
 *
 * Spec: https://openid.net/specs/openid-connect-rpinitiated-1_0.html
 *
 * Security:
 * - Validates post_logout_redirect_uri against allowed origins
 * - Prevents open redirect attacks (CWE-601)
 * - Clears session cookies securely
 */
async function handleEndSession(request: NextRequest) {
  const url = new URL(request.url);

  // Get query parameters
  const idTokenHint = url.searchParams.get("id_token_hint");
  const postLogoutRedirectUri = url.searchParams.get("post_logout_redirect_uri");
  const state = url.searchParams.get("state");
  const clientId = url.searchParams.get("client_id");

  // Validate post_logout_redirect_uri if provided
  if (postLogoutRedirectUri && !isValidPostLogoutUri(postLogoutRedirectUri)) {
    console.warn("[EndSession] Rejected invalid post_logout_redirect_uri:", postLogoutRedirectUri);
    return NextResponse.json(
      { error: "invalid_request", error_description: "Invalid post_logout_redirect_uri" },
      { status: 400 }
    );
  }

  try {
    // Clear session using Better Auth's sign-out
    // This removes the session from the database and clears cookies
    const cookieStore = await cookies();

    // Get all cookies to forward to Better Auth
    const cookieHeader = cookieStore.getAll()
      .map(c => `${c.name}=${c.value}`)
      .join("; ");

    // Call Better Auth's sign-out endpoint internally
    await auth.api.signOut({
      headers: {
        cookie: cookieHeader,
      },
    });

    // Build redirect response (URI already validated above)
    if (postLogoutRedirectUri) {
      const redirectUrl = new URL(postLogoutRedirectUri);
      if (state) {
        redirectUrl.searchParams.set("state", state);
      }

      const response = NextResponse.redirect(redirectUrl.toString(), 302);

      // Clear auth cookies explicitly
      const cookieNames = ["robolearn.session_token", "robolearn.session_data"];
      for (const name of cookieNames) {
        response.cookies.set(name, "", {
          expires: new Date(0),
          path: "/",
          httpOnly: true,
          secure: process.env.NODE_ENV === "production",
          sameSite: "lax",
        });
      }

      return response;
    }

    // No redirect URI - return success JSON
    return NextResponse.json(
      { success: true, message: "Session terminated" },
      { status: 200 }
    );
  } catch (error) {
    console.error("[EndSession] Error:", error);

    // On error, still redirect if valid URI was provided
    if (postLogoutRedirectUri) {
      const redirectUrl = new URL(postLogoutRedirectUri);
      if (state) {
        redirectUrl.searchParams.set("state", state);
      }
      return NextResponse.redirect(redirectUrl.toString(), 302);
    }

    return NextResponse.json(
      { success: false, error: "Failed to end session" },
      { status: 500 }
    );
  }
}

export async function GET(request: NextRequest) {
  return handleEndSession(request);
}

export async function POST(request: NextRequest) {
  return handleEndSession(request);
}
