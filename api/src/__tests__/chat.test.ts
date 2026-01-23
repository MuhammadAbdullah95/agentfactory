/**
 * Chat Handler Tests (Mock-First)
 *
 * Tests the chat handler with mocked dependencies
 */

import { describe, it, expect, beforeEach } from 'vitest';
import { handleChat, ChatHandlerDependencies } from '../handlers/chat';
import { RateLimiter } from '../services/rate-limiter';
import { LessonLoader } from '../services/lesson-loader';
import { MockAIProvider } from '../services/ai-provider';
import type { ChatRequest, ChatResponse, ErrorResponse, LessonContext } from '../types';

// =============================================================================
// Mock Lesson Loader
// =============================================================================

class MockLessonLoader {
  private lessons: Map<string, LessonContext> = new Map();
  private shouldFail: boolean = false;

  setLesson(path: string, lesson: LessonContext): void {
    this.lessons.set(path, lesson);
  }

  setShouldFail(fail: boolean): void {
    this.shouldFail = fail;
  }

  async load(urlPath: string): Promise<LessonContext> {
    if (this.shouldFail) {
      throw new Error('Mock failure');
    }

    const lesson = this.lessons.get(urlPath);
    if (!lesson) {
      const { StudyModeError } = await import('../types');
      throw new StudyModeError('LESSON_NOT_FOUND', `Lesson not found: ${urlPath}`);
    }

    return lesson;
  }
}

// =============================================================================
// Test Fixtures
// =============================================================================

const mockLesson: LessonContext = {
  path: '/docs/01-foundations/01-intro',
  title: 'Introduction to Agent Factory',
  content: '# Introduction\n\nThis is the introduction lesson about building AI agents.',
  chapterNumber: 1,
  lessonNumber: 1,
};

const validRequest: ChatRequest = {
  lessonPath: '/docs/01-foundations/01-intro',
  userMessage: 'What is this lesson about?',
  conversationHistory: [],
  mode: 'teach',
};

// =============================================================================
// Tests
// =============================================================================

describe('handleChat', () => {
  let rateLimiter: RateLimiter;
  let lessonLoader: MockLessonLoader;
  let aiProvider: MockAIProvider;
  let deps: ChatHandlerDependencies;

  beforeEach(() => {
    rateLimiter = new RateLimiter({ maxRequests: 60, windowMs: 3600000 });
    lessonLoader = new MockLessonLoader();
    lessonLoader.setLesson(mockLesson.path, mockLesson);
    aiProvider = new MockAIProvider();

    deps = {
      rateLimiter,
      lessonLoader: lessonLoader as unknown as LessonLoader,
      aiProvider,
    };
  });

  describe('successful requests', () => {
    it('should return 200 with AI response for valid teach mode request', async () => {
      const result = await handleChat(validRequest, '127.0.0.1', deps);

      expect(result.status).toBe(200);
      const body = result.body as ChatResponse;
      expect(body.assistantMessage).toBeDefined();
      expect(body.metadata.model).toBe('mock-model');
      expect(body.metadata.tokensUsed).toBeGreaterThan(0);
      expect(body.metadata.processingTimeMs).toBeGreaterThanOrEqual(0);
    });

    it('should return 200 with AI response for valid ask mode request', async () => {
      const askRequest = { ...validRequest, mode: 'ask' as const };
      const result = await handleChat(askRequest, '127.0.0.1', deps);

      expect(result.status).toBe(200);
      const body = result.body as ChatResponse;
      expect(body.assistantMessage).toBeDefined();
    });

    it('should include lesson context in AI response', async () => {
      aiProvider.setDefaultResponse('This response references the lesson.');
      const result = await handleChat(validRequest, '127.0.0.1', deps);

      expect(result.status).toBe(200);
      const body = result.body as ChatResponse;
      expect(body.assistantMessage).toContain(mockLesson.title);
    });

    it('should preserve conversation history', async () => {
      const requestWithHistory: ChatRequest = {
        ...validRequest,
        conversationHistory: [
          { role: 'user', content: 'Previous question', timestamp: '2026-01-23T10:00:00Z' },
          { role: 'assistant', content: 'Previous answer', timestamp: '2026-01-23T10:00:05Z' },
        ],
      };

      const result = await handleChat(requestWithHistory, '127.0.0.1', deps);
      expect(result.status).toBe(200);
    });
  });

  describe('validation errors', () => {
    it('should return 400 for missing lessonPath', async () => {
      const invalid = { ...validRequest, lessonPath: '' };
      const result = await handleChat(invalid, '127.0.0.1', deps);

      expect(result.status).toBe(400);
      const body = result.body as ErrorResponse;
      expect(body.error.code).toBe('VALIDATION_ERROR');
    });

    it('should return 400 for missing userMessage', async () => {
      const invalid = { ...validRequest, userMessage: '' };
      const result = await handleChat(invalid, '127.0.0.1', deps);

      expect(result.status).toBe(400);
    });

    it('should return 400 for invalid mode', async () => {
      const invalid = { ...validRequest, mode: 'invalid' };
      const result = await handleChat(invalid, '127.0.0.1', deps);

      expect(result.status).toBe(400);
    });

    it('should return 400 for message exceeding max length', async () => {
      const invalid = { ...validRequest, userMessage: 'a'.repeat(5001) };
      const result = await handleChat(invalid, '127.0.0.1', deps);

      expect(result.status).toBe(400);
    });

    it('should return 400 for non-object body', async () => {
      const result = await handleChat('invalid', '127.0.0.1', deps);
      expect(result.status).toBe(400);
    });

    it('should return 400 for null body', async () => {
      const result = await handleChat(null, '127.0.0.1', deps);
      expect(result.status).toBe(400);
    });
  });

  describe('rate limiting', () => {
    it('should return 429 when rate limit exceeded', async () => {
      // Exhaust rate limit
      const strictLimiter = new RateLimiter({ maxRequests: 1, windowMs: 3600000 });
      const strictDeps = { ...deps, rateLimiter: strictLimiter };

      // First request should succeed
      await handleChat(validRequest, '127.0.0.1', strictDeps);

      // Second request should be rate limited
      const result = await handleChat(validRequest, '127.0.0.1', strictDeps);

      expect(result.status).toBe(429);
      const body = result.body as ErrorResponse;
      expect(body.error.code).toBe('RATE_LIMITED');
      expect(result.headers?.['Retry-After']).toBeDefined();
    });

    it('should allow requests from different IPs', async () => {
      const strictLimiter = new RateLimiter({ maxRequests: 1, windowMs: 3600000 });
      const strictDeps = { ...deps, rateLimiter: strictLimiter };

      // First IP
      await handleChat(validRequest, '192.168.1.1', strictDeps);

      // Different IP should not be rate limited
      const result = await handleChat(validRequest, '192.168.1.2', strictDeps);
      expect(result.status).toBe(200);
    });
  });

  describe('lesson loading errors', () => {
    it('should return 404 when lesson not found', async () => {
      const notFoundRequest = { ...validRequest, lessonPath: '/docs/nonexistent' };
      const result = await handleChat(notFoundRequest, '127.0.0.1', deps);

      expect(result.status).toBe(404);
      const body = result.body as ErrorResponse;
      expect(body.error.code).toBe('LESSON_NOT_FOUND');
    });
  });

  describe('mode-specific behavior', () => {
    it('should use teach mode prompt for teach requests', async () => {
      const teachRequest = { ...validRequest, mode: 'teach' as const };
      const result = await handleChat(teachRequest, '127.0.0.1', deps);

      expect(result.status).toBe(200);
      const body = result.body as ChatResponse;
      // Mock provider includes lesson title in response
      expect(body.assistantMessage).toContain(mockLesson.title);
    });

    it('should use ask mode prompt for ask requests', async () => {
      const askRequest = { ...validRequest, mode: 'ask' as const };
      const result = await handleChat(askRequest, '127.0.0.1', deps);

      expect(result.status).toBe(200);
      const body = result.body as ChatResponse;
      expect(body.assistantMessage).toContain(mockLesson.title);
    });
  });
});
