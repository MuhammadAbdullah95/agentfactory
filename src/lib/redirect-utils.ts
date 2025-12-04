/**
 * Redirect URL Validation Utilities
 * 
 * Validates redirect URLs against trusted client origins to prevent open redirect attacks.
 * Uses the TRUSTED_CLIENTS configuration to derive allowed origins.
 */

import { TRUSTED_CLIENTS } from "./trusted-clients";

/**
 * Extract unique origins from trusted client redirect URLs
 * @returns Array of trusted origins (e.g., ["https://example.com", "http://localhost:3000"])
 */
export function getTrustedOrigins(): string[] {
  const origins = new Set<string>();
  
  // Add SSO server's own origin (same-origin redirects are always safe)
  // In client-side: use window.location.origin
  // In server-side: this will be skipped, but server-side doesn't need same-origin check
  if (typeof window !== 'undefined') {
    origins.add(window.location.origin);
  }
  
  // Extract origins from all trusted client redirect URLs
  for (const client of TRUSTED_CLIENTS) {
    for (const redirectUrl of client.redirectUrls) {
      try {
        const url = new URL(redirectUrl);
        origins.add(url.origin);
      } catch (error) {
        // Skip invalid URLs - only log in development
        if (process.env.NODE_ENV === 'development') {
          console.warn(`Invalid redirect URL in trusted clients: ${redirectUrl}`);
        }
      }
    }
  }
  
  return Array.from(origins);
}

/**
 * Validate if a redirect URL is safe to use
 * @param url - The redirect URL to validate
 * @returns true if the URL is safe, false otherwise
 */
export function isValidRedirectUrl(url: string): boolean {
  // Reject empty or whitespace-only URLs
  if (!url || url.trim().length === 0) {
    return false;
  }
  
  // Allow relative URLs (same origin)
  if (url.startsWith('/')) {
    return true;
  }
  
  // Reject URLs that don't start with http:// or https://
  if (!url.startsWith('http://') && !url.startsWith('https://')) {
    return false;
  }
  
  try {
    // Parse the URL to get its origin
    const parsedUrl = new URL(url);
    const trustedOrigins = getTrustedOrigins();
    
    // Check if the origin is in the trusted list
    return trustedOrigins.includes(parsedUrl.origin);
  } catch (error) {
    // Invalid URL format - only log in development
    if (process.env.NODE_ENV === 'development') {
      console.warn(`Invalid redirect URL format: ${url}`, error);
    }
    return false;
  }
}
