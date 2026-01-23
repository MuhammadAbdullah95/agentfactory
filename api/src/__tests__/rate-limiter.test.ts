/**
 * Rate Limiter Tests
 */

import { describe, it, expect, beforeEach, vi } from 'vitest';
import { RateLimiter } from '../services/rate-limiter';

describe('RateLimiter', () => {
  let limiter: RateLimiter;

  beforeEach(() => {
    limiter = new RateLimiter({ maxRequests: 3, windowMs: 1000 });
  });

  describe('check', () => {
    it('should allow requests under the limit', () => {
      const result1 = limiter.check('127.0.0.1');
      expect(result1.allowed).toBe(true);
      expect(result1.remaining).toBe(2);

      const result2 = limiter.check('127.0.0.1');
      expect(result2.allowed).toBe(true);
      expect(result2.remaining).toBe(1);

      const result3 = limiter.check('127.0.0.1');
      expect(result3.allowed).toBe(true);
      expect(result3.remaining).toBe(0);
    });

    it('should block requests over the limit', () => {
      limiter.check('127.0.0.1');
      limiter.check('127.0.0.1');
      limiter.check('127.0.0.1');

      const result = limiter.check('127.0.0.1');
      expect(result.allowed).toBe(false);
      expect(result.remaining).toBe(0);
    });

    it('should track different IPs separately', () => {
      limiter.check('192.168.1.1');
      limiter.check('192.168.1.1');
      limiter.check('192.168.1.1');

      // First IP should be blocked
      const blocked = limiter.check('192.168.1.1');
      expect(blocked.allowed).toBe(false);

      // Different IP should not be blocked
      const allowed = limiter.check('192.168.1.2');
      expect(allowed.allowed).toBe(true);
      expect(allowed.remaining).toBe(2);
    });

    it('should reset after window expires', async () => {
      const shortLimiter = new RateLimiter({ maxRequests: 1, windowMs: 50 });

      shortLimiter.check('127.0.0.1');
      const blocked = shortLimiter.check('127.0.0.1');
      expect(blocked.allowed).toBe(false);

      // Wait for window to expire
      await new Promise(resolve => setTimeout(resolve, 60));

      const allowed = shortLimiter.check('127.0.0.1');
      expect(allowed.allowed).toBe(true);
    });

    it('should return correct resetAt timestamp', () => {
      const now = Date.now();
      const result = limiter.check('127.0.0.1');

      // resetAt should be ~1 second from now (1000ms window)
      expect(result.resetAt).toBeGreaterThanOrEqual(now + 900);
      expect(result.resetAt).toBeLessThanOrEqual(now + 1100);
    });
  });

  describe('status', () => {
    it('should return current status without incrementing', () => {
      const check1 = limiter.check('127.0.0.1');
      expect(check1.remaining).toBe(2);

      const status = limiter.status('127.0.0.1');
      expect(status.remaining).toBe(2); // Still 2, not incremented

      const check2 = limiter.check('127.0.0.1');
      expect(check2.remaining).toBe(1); // Now decremented
    });

    it('should return full quota for unknown IP', () => {
      const status = limiter.status('unknown-ip');
      expect(status.allowed).toBe(true);
      expect(status.remaining).toBe(3);
    });
  });

  describe('reset', () => {
    it('should reset limit for specific IP', () => {
      limiter.check('127.0.0.1');
      limiter.check('127.0.0.1');
      limiter.check('127.0.0.1');

      const blocked = limiter.check('127.0.0.1');
      expect(blocked.allowed).toBe(false);

      limiter.reset('127.0.0.1');

      const allowed = limiter.check('127.0.0.1');
      expect(allowed.allowed).toBe(true);
      expect(allowed.remaining).toBe(2);
    });
  });

  describe('cleanup', () => {
    it('should remove expired entries', async () => {
      const shortLimiter = new RateLimiter({ maxRequests: 1, windowMs: 50 });

      shortLimiter.check('192.168.1.1');
      shortLimiter.check('192.168.1.2');

      // Wait for window to expire
      await new Promise(resolve => setTimeout(resolve, 60));

      shortLimiter.cleanup();

      // Both should have fresh limits
      const result1 = shortLimiter.check('192.168.1.1');
      const result2 = shortLimiter.check('192.168.1.2');

      expect(result1.allowed).toBe(true);
      expect(result2.allowed).toBe(true);
    });
  });

  describe('clear', () => {
    it('should clear all entries', () => {
      limiter.check('192.168.1.1');
      limiter.check('192.168.1.2');
      limiter.check('192.168.1.3');

      limiter.clear();

      // All should have fresh limits
      expect(limiter.status('192.168.1.1').remaining).toBe(3);
      expect(limiter.status('192.168.1.2').remaining).toBe(3);
      expect(limiter.status('192.168.1.3').remaining).toBe(3);
    });
  });
});
