import { auth } from "@/lib/auth";
import { cookies } from "next/headers";
import { NextRequest, NextResponse } from "next/server";

/**
 * OIDC RP-Initiated Logout Endpoint
 * Handles session termination and optionally redirects to post-logout URI
 *
 * Spec: https://openid.net/specs/openid-connect-rpinitiated-1_0.html
 */
async function handleEndSession(request: NextRequest) {
  const url = new URL(request.url);

  // Get query parameters
  const idTokenHint = url.searchParams.get("id_token_hint");
  const postLogoutRedirectUri = url.searchParams.get("post_logout_redirect_uri");
  const state = url.searchParams.get("state");
  const clientId = url.searchParams.get("client_id");

  try {
    // Clear session using Better Auth's sign-out
    // This removes the session from the database and clears cookies
    const cookieStore = await cookies();

    // Get all cookies to forward to Better Auth
    const cookieHeader = cookieStore.getAll()
      .map(c => `${c.name}=${c.value}`)
      .join("; ");

    // Call Better Auth's sign-out endpoint internally
    const signOutResponse = await auth.api.signOut({
      headers: {
        cookie: cookieHeader,
      },
    });

    // Build redirect response
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

    // Even on error, try to redirect if URI provided
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
