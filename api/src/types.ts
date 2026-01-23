/**
 * TypeScript interfaces for Interactive Study Mode API
 * Generated from api/openapi.yaml (single source of truth)
 */

// =============================================================================
// Request/Response Types
// =============================================================================

/**
 * Chat Mode - Determines AI behavior
 *
 * TEACH MODE ('teach'):
 * - AI Role: Proactive tutor who explains concepts
 * - Behavior: Gives guided explanations from book content
 * - Response Format: Explanation + "Related topics you might explore: ..."
 * - Source: ONLY from lesson content (book), never invented
 * - Use When: User wants to learn/understand the lesson
 *
 * ASK MODE ('ask'):
 * - AI Role: Reactive assistant who answers questions
 * - Behavior: Answers only what is asked, concisely
 * - Response Format: Direct answer OR suggested questions (on first message)
 * - Source: ONLY from lesson content (book), never invented
 * - Use When: User has specific questions about the lesson
 */
export type ChatMode = 'teach' | 'ask';

export interface Message {
  role: 'user' | 'assistant';
  content: string;
  timestamp: string; // ISO 8601
}

export interface ChatRequest {
  lessonPath: string;
  userMessage: string;
  conversationHistory?: Message[];
  mode: ChatMode;
}

export interface ResponseMetadata {
  model: string;
  tokensUsed: number;
  processingTimeMs: number;
}

export interface ChatResponse {
  assistantMessage: string;
  metadata: ResponseMetadata;
}

// =============================================================================
// Error Types
// =============================================================================

export type ErrorCode =
  | 'VALIDATION_ERROR'
  | 'RATE_LIMITED'
  | 'LESSON_NOT_FOUND'
  | 'AI_UNAVAILABLE'
  | 'INTERNAL_ERROR';

export interface ErrorResponse {
  error: {
    code: ErrorCode;
    message: string;
  };
}

// =============================================================================
// Internal Types (not exposed in API)
// =============================================================================

export interface LessonContext {
  path: string;
  title: string;
  content: string;
  chapterNumber?: number;
  lessonNumber?: number;
}

export interface AIProviderConfig {
  provider: 'openai' | 'anthropic';
  apiKey: string;
  model?: string;
}

export interface AIProviderResponse {
  content: string;
  model: string;
  tokensUsed: number;
}

// =============================================================================
// Validation
// =============================================================================

export const VALIDATION_LIMITS = {
  LESSON_PATH_MAX: 500,
  USER_MESSAGE_MIN: 1,
  USER_MESSAGE_MAX: 5000,
  CONVERSATION_HISTORY_MAX: 50,
} as const;

export function isValidChatRequest(req: unknown): req is ChatRequest {
  if (!req || typeof req !== 'object') return false;

  const r = req as Record<string, unknown>;

  // Required fields
  if (typeof r.lessonPath !== 'string' || r.lessonPath.length === 0) return false;
  if (r.lessonPath.length > VALIDATION_LIMITS.LESSON_PATH_MAX) return false;

  if (typeof r.userMessage !== 'string') return false;
  if (r.userMessage.length < VALIDATION_LIMITS.USER_MESSAGE_MIN) return false;
  if (r.userMessage.length > VALIDATION_LIMITS.USER_MESSAGE_MAX) return false;

  if (r.mode !== 'teach' && r.mode !== 'ask') return false;

  // Optional conversationHistory
  if (r.conversationHistory !== undefined) {
    if (!Array.isArray(r.conversationHistory)) return false;
    if (r.conversationHistory.length > VALIDATION_LIMITS.CONVERSATION_HISTORY_MAX) return false;

    for (const msg of r.conversationHistory) {
      if (!isValidMessage(msg)) return false;
    }
  }

  return true;
}

export function isValidMessage(msg: unknown): msg is Message {
  if (!msg || typeof msg !== 'object') return false;

  const m = msg as Record<string, unknown>;

  if (m.role !== 'user' && m.role !== 'assistant') return false;
  if (typeof m.content !== 'string') return false;
  if (typeof m.timestamp !== 'string') return false;

  return true;
}

// =============================================================================
// Error Helpers
// =============================================================================

export function createErrorResponse(code: ErrorCode, message: string): ErrorResponse {
  return {
    error: { code, message }
  };
}

export class StudyModeError extends Error {
  constructor(
    public readonly code: ErrorCode,
    message: string
  ) {
    super(message);
    this.name = 'StudyModeError';
  }

  toResponse(): ErrorResponse {
    return createErrorResponse(this.code, this.message);
  }
}
