/**
 * Chat Handler
 * Platform-agnostic handler for /api/chat endpoint
 */

import type {
  ChatRequest,
  ChatResponse,
  ErrorResponse,
  Message,
} from '../types';
import {
  isValidChatRequest,
  createErrorResponse,
  StudyModeError,
} from '../types';
import { RateLimiter, getRateLimiter } from '../services/rate-limiter';
import { LessonLoader, createLessonLoader } from '../services/lesson-loader';
import { AIProvider, createAIProviderFromEnv } from '../services/ai-provider';

// =============================================================================
// Types
// =============================================================================

export interface ChatHandlerDependencies {
  rateLimiter?: RateLimiter;
  lessonLoader?: LessonLoader;
  aiProvider?: AIProvider;
}

export interface ChatHandlerResult {
  status: number;
  body: ChatResponse | ErrorResponse;
  headers?: Record<string, string>;
}

// =============================================================================
// Logging (structured, no message content)
// =============================================================================

interface LogEntry {
  timestamp: string;
  event: string;
  ip?: string;
  lessonPath?: string;
  mode?: string;
  model?: string;
  tokensUsed?: number;
  processingTimeMs?: number;
  errorCode?: string;
}

function log(entry: LogEntry): void {
  // Structured logging - can be parsed by log aggregators
  console.log(JSON.stringify(entry));
}

// =============================================================================
// Handler
// =============================================================================

/**
 * Platform-agnostic chat handler
 *
 * @param body - Parsed request body
 * @param clientIp - Client IP address for rate limiting
 * @param deps - Injectable dependencies for testing
 */
export async function handleChat(
  body: unknown,
  clientIp: string,
  deps: ChatHandlerDependencies = {}
): Promise<ChatHandlerResult> {
  const startTime = Date.now();

  // Use provided dependencies or defaults
  const rateLimiter = deps.rateLimiter ?? getRateLimiter();
  const lessonLoader = deps.lessonLoader ?? createLessonLoader();
  const aiProvider = deps.aiProvider ?? createAIProviderFromEnv();

  // 1. Rate limit check
  const rateLimit = rateLimiter.check(clientIp);
  if (!rateLimit.allowed) {
    log({
      timestamp: new Date().toISOString(),
      event: 'rate_limited',
      ip: clientIp,
    });

    return {
      status: 429,
      body: createErrorResponse('RATE_LIMITED', 'Rate limit exceeded. Please try again later.'),
      headers: {
        'Retry-After': String(Math.ceil((rateLimit.resetAt - Date.now()) / 1000)),
      },
    };
  }

  // 2. Validate request
  if (!isValidChatRequest(body)) {
    log({
      timestamp: new Date().toISOString(),
      event: 'validation_error',
      ip: clientIp,
    });

    return {
      status: 400,
      body: createErrorResponse('VALIDATION_ERROR', 'Invalid request. Check lessonPath, userMessage, and mode.'),
    };
  }

  const request: ChatRequest = body;

  try {
    // 3. Try to load lesson content
    let lessonContext;
    let isGeneralMode = false;

    try {
      lessonContext = await lessonLoader.load(request.lessonPath);
    } catch (loadError) {
      // Content not found - use general mode with guidance
      isGeneralMode = true;
      lessonContext = {
        path: request.lessonPath,
        title: 'AgentFactory Book',
        content: `You are on a chapter or part index page. The user is browsing the AgentFactory book.

To provide specific, book-based answers, please guide the user to:
1. Navigate to a specific lesson page in the sidebar
2. Then use the Study Mode to get detailed explanations

For now, you can:
- Help them understand the book structure
- Suggest which chapter/lesson might cover their topic
- Give general guidance about AI agents, cloud native development, or the topics covered in this book

Book Parts:
- Part 1: General Agents Foundations
- Part 2: Applied General Agent Workflows
- Part 3: SDD-RI Fundamentals
- Part 4: Coding for Problem Solving
- Part 5: Building Custom Agents
- Part 6: AI Cloud Native Development`,
        chapterNumber: undefined,
        lessonNumber: undefined,
      };
    }

    // 4. Call AI provider
    const aiResponse = await aiProvider.complete({
      lessonContext,
      userMessage: request.userMessage,
      conversationHistory: request.conversationHistory ?? [],
      mode: request.mode,
    });

    const processingTimeMs = Date.now() - startTime;

    // 5. Log success (no message content!)
    log({
      timestamp: new Date().toISOString(),
      event: isGeneralMode ? 'chat_general_mode' : 'chat_success',
      ip: clientIp,
      lessonPath: request.lessonPath,
      mode: request.mode,
      model: aiResponse.model,
      tokensUsed: aiResponse.tokensUsed,
      processingTimeMs,
    });

    // 6. Return response
    const response: ChatResponse = {
      assistantMessage: aiResponse.content,
      metadata: {
        model: aiResponse.model,
        tokensUsed: aiResponse.tokensUsed,
        processingTimeMs,
      },
    };

    return {
      status: 200,
      body: response,
    };

  } catch (error) {
    const processingTimeMs = Date.now() - startTime;

    if (error instanceof StudyModeError) {
      log({
        timestamp: new Date().toISOString(),
        event: 'error',
        ip: clientIp,
        lessonPath: request.lessonPath,
        mode: request.mode,
        errorCode: error.code,
        processingTimeMs,
      });

      const statusMap: Record<string, number> = {
        LESSON_NOT_FOUND: 404,
        AI_UNAVAILABLE: 503,
        VALIDATION_ERROR: 400,
        RATE_LIMITED: 429,
        INTERNAL_ERROR: 500,
      };

      return {
        status: statusMap[error.code] ?? 500,
        body: error.toResponse(),
      };
    }

    // Unexpected error
    log({
      timestamp: new Date().toISOString(),
      event: 'internal_error',
      ip: clientIp,
      lessonPath: request.lessonPath,
      mode: request.mode,
      errorCode: 'INTERNAL_ERROR',
      processingTimeMs,
    });

    return {
      status: 500,
      body: createErrorResponse('INTERNAL_ERROR', 'An unexpected error occurred.'),
    };
  }
}

// =============================================================================
// Exports for testing
// =============================================================================

export { log as _log };
