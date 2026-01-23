/**
 * Interactive Study Mode API
 * Main entry point
 */

// Types
export * from './types';

// Handlers
export { handleChat } from './handlers/chat';
export type { ChatHandlerDependencies, ChatHandlerResult } from './handlers/chat';

// Services
export { RateLimiter, getRateLimiter, resetRateLimiter } from './services/rate-limiter';
export { LessonLoader, createLessonLoader } from './services/lesson-loader';
export {
  MockAIProvider,
  OpenAIProvider,
  AnthropicProvider,
  createAIProvider,
  createAIProviderFromEnv,
} from './services/ai-provider';
export type { AIProvider, AICompletionRequest } from './services/ai-provider';

// Prompts
export { buildTeachModePrompt } from './prompts/teach-mode';
export { buildAskModePrompt } from './prompts/ask-mode';

// Server
export { startServer } from './server';

// Auto-start server when run directly
import { startServer } from './server';
import { config } from 'dotenv';

// Load environment variables
config();

// Start the server
startServer();
