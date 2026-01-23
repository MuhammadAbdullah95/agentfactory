/**
 * IP-based rate limiter
 * Platform-agnostic, in-memory implementation
 *
 * Limit: 60 requests per hour per IP address
 */

export interface RateLimitConfig {
  maxRequests: number;
  windowMs: number;
}

export interface RateLimitResult {
  allowed: boolean;
  remaining: number;
  resetAt: number; // Unix timestamp (ms)
}

interface RateLimitEntry {
  count: number;
  windowStart: number;
}

const DEFAULT_CONFIG: RateLimitConfig = {
  maxRequests: 60,
  windowMs: 60 * 60 * 1000, // 1 hour in milliseconds
};

/**
 * In-memory rate limiter
 * Note: In a distributed environment, consider using Redis or similar
 */
export class RateLimiter {
  private entries: Map<string, RateLimitEntry> = new Map();
  private config: RateLimitConfig;

  constructor(config: Partial<RateLimitConfig> = {}) {
    this.config = { ...DEFAULT_CONFIG, ...config };
  }

  /**
   * Check if a request from the given IP is allowed
   */
  check(ip: string): RateLimitResult {
    const now = Date.now();
    const entry = this.entries.get(ip);

    // No existing entry or window expired - allow and start new window
    if (!entry || now - entry.windowStart >= this.config.windowMs) {
      this.entries.set(ip, { count: 1, windowStart: now });
      return {
        allowed: true,
        remaining: this.config.maxRequests - 1,
        resetAt: now + this.config.windowMs,
      };
    }

    // Within window - check count
    if (entry.count >= this.config.maxRequests) {
      return {
        allowed: false,
        remaining: 0,
        resetAt: entry.windowStart + this.config.windowMs,
      };
    }

    // Increment and allow
    entry.count++;
    return {
      allowed: true,
      remaining: this.config.maxRequests - entry.count,
      resetAt: entry.windowStart + this.config.windowMs,
    };
  }

  /**
   * Get current status for an IP without incrementing
   */
  status(ip: string): RateLimitResult {
    const now = Date.now();
    const entry = this.entries.get(ip);

    if (!entry || now - entry.windowStart >= this.config.windowMs) {
      return {
        allowed: true,
        remaining: this.config.maxRequests,
        resetAt: now + this.config.windowMs,
      };
    }

    return {
      allowed: entry.count < this.config.maxRequests,
      remaining: Math.max(0, this.config.maxRequests - entry.count),
      resetAt: entry.windowStart + this.config.windowMs,
    };
  }

  /**
   * Clear expired entries (call periodically to prevent memory leaks)
   */
  cleanup(): void {
    const now = Date.now();
    for (const [ip, entry] of this.entries) {
      if (now - entry.windowStart >= this.config.windowMs) {
        this.entries.delete(ip);
      }
    }
  }

  /**
   * Reset rate limit for an IP (for testing or admin purposes)
   */
  reset(ip: string): void {
    this.entries.delete(ip);
  }

  /**
   * Clear all entries (for testing)
   */
  clear(): void {
    this.entries.clear();
  }
}

// Singleton instance for use across requests
let defaultInstance: RateLimiter | null = null;

export function getRateLimiter(): RateLimiter {
  if (!defaultInstance) {
    defaultInstance = new RateLimiter();
  }
  return defaultInstance;
}

// For testing - allows resetting the singleton
export function resetRateLimiter(): void {
  defaultInstance = null;
}
