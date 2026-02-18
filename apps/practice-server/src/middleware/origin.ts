import type { IncomingMessage } from "node:http";

export const ORIGIN_RE = /^https?:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/;

/**
 * CORS origin callback for Hono cors() middleware.
 * Returns the origin if it matches localhost, undefined otherwise.
 * Shared between main server setup and tests to avoid drift.
 */
export function corsOrigin(origin: string): string | undefined {
  if (!origin) return origin;
  return ORIGIN_RE.test(origin) ? origin : undefined;
}

/**
 * Validate that a WebSocket upgrade request comes from a trusted origin.
 */
export function isValidOrigin(req: IncomingMessage): boolean {
  const origin = req.headers.origin || "";
  // Allow requests with no origin (e.g., curl, wscat)
  if (!origin) return true;
  return ORIGIN_RE.test(origin);
}
