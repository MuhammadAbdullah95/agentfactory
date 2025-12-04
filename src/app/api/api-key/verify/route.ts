import { NextRequest, NextResponse } from "next/server";
import { auth } from "@/lib/auth";

/**
 * POST /api/api-key/verify
 *
 * Verify an API key for M2M authentication.
 * This endpoint is used by external services (FastAPI, NestJS, etc.)
 * to validate API keys before processing requests.
 *
 * Request body:
 * {
 *   "key": "pana_xxx..." // The full API key to verify
 * }
 *
 * Response (success):
 * {
 *   "valid": true,
 *   "key": {
 *     "id": "...",
 *     "name": "...",
 *     "userId": "...",
 *     "enabled": true,
 *     "expiresAt": "..." | null,
 *     "metadata": {...} | null
 *   }
 * }
 *
 * Response (failure):
 * {
 *   "valid": false,
 *   "error": {
 *     "code": "INVALID_API_KEY" | "EXPIRED_API_KEY" | "DISABLED_API_KEY",
 *     "message": "..."
 *   }
 * }
 */
export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { key } = body;

    if (!key || typeof key !== "string") {
      return NextResponse.json(
        {
          valid: false,
          error: {
            code: "MISSING_KEY",
            message: "API key is required in request body",
          },
        },
        { status: 400 }
      );
    }

    // Use Better Auth's server-side verification
    const result = await auth.api.verifyApiKey({
      body: { key },
    });

    if (result.valid) {
      return NextResponse.json({
        valid: true,
        key: {
          id: result.key?.id,
          name: result.key?.name,
          userId: result.key?.userId,
          enabled: result.key?.enabled,
          expiresAt: result.key?.expiresAt,
          metadata: result.key?.metadata,
        },
      });
    } else {
      return NextResponse.json(
        {
          valid: false,
          error: result.error || {
            code: "INVALID_API_KEY",
            message: "API key is invalid",
          },
        },
        { status: 401 }
      );
    }
  } catch (error: unknown) {
    console.error("[API Key Verify] Error:", error);

    const message = error instanceof Error ? error.message : "Internal server error";

    return NextResponse.json(
      {
        valid: false,
        error: {
          code: "INTERNAL_ERROR",
          message,
        },
      },
      { status: 500 }
    );
  }
}

// Handle CORS preflight
export async function OPTIONS() {
  return new NextResponse(null, {
    status: 204,
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    },
  });
}
