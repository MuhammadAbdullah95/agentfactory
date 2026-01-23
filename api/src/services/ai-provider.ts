/**
 * AI Provider Adapter
 * Provider-agnostic interface for OpenAI and Anthropic
 */

import type { AIProviderConfig, AIProviderResponse, Message, LessonContext, ChatMode } from '../types';
import { StudyModeError } from '../types';
import { buildTeachModePrompt } from '../prompts/teach-mode';
import { buildAskModePrompt } from '../prompts/ask-mode';

// =============================================================================
// Types
// =============================================================================

export interface AICompletionRequest {
  lessonContext: LessonContext;
  userMessage: string;
  conversationHistory: Message[];
  mode: ChatMode;
}

export interface AIProvider {
  complete(request: AICompletionRequest): Promise<AIProviderResponse>;
}

// =============================================================================
// Mock Provider (for testing)
// =============================================================================

export class MockAIProvider implements AIProvider {
  private responses: Map<string, string> = new Map();
  private defaultResponse: string = 'This is a mock AI response for testing.';

  setResponse(keyword: string, response: string): void {
    this.responses.set(keyword.toLowerCase(), response);
  }

  setDefaultResponse(response: string): void {
    this.defaultResponse = response;
  }

  async complete(request: AICompletionRequest): Promise<AIProviderResponse> {
    // Check for keyword matches in user message
    const userMessageLower = request.userMessage.toLowerCase();
    for (const [keyword, response] of this.responses) {
      if (userMessageLower.includes(keyword)) {
        return {
          content: response,
          model: 'mock-model',
          tokensUsed: response.length,
        };
      }
    }

    // Generate context-aware mock response
    const modePrefix = request.mode === 'teach'
      ? `Let me explain the concept from "${request.lessonContext.title}".`
      : `Based on the lesson "${request.lessonContext.title}":`;

    const response = `${modePrefix} ${this.defaultResponse}`;

    return {
      content: response,
      model: 'mock-model',
      tokensUsed: response.length,
    };
  }
}

// =============================================================================
// OpenAI Provider
// =============================================================================

export class OpenAIProvider implements AIProvider {
  private apiKey: string;
  private model: string;

  constructor(config: { apiKey: string; model?: string }) {
    this.apiKey = config.apiKey;
    this.model = config.model || 'gpt-4-turbo-preview';
  }

  async complete(request: AICompletionRequest): Promise<AIProviderResponse> {
    const systemPrompt = request.mode === 'teach'
      ? buildTeachModePrompt(request.lessonContext, request.conversationHistory)
      : buildAskModePrompt(request.lessonContext, request.conversationHistory);

    const messages = [
      { role: 'system' as const, content: systemPrompt },
      ...request.conversationHistory.map(m => ({
        role: m.role as 'user' | 'assistant',
        content: m.content,
      })),
      { role: 'user' as const, content: request.userMessage },
    ];

    try {
      const response = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.apiKey}`,
        },
        body: JSON.stringify({
          model: this.model,
          messages,
          max_tokens: 1024,
          temperature: 0.7,
        }),
      });

      if (!response.ok) {
        const error = await response.text();
        throw new Error(`OpenAI API error: ${response.status} ${error}`);
      }

      const data = await response.json();
      const choice = data.choices?.[0];

      if (!choice?.message?.content) {
        throw new Error('Invalid OpenAI response format');
      }

      return {
        content: choice.message.content,
        model: this.model,
        tokensUsed: data.usage?.total_tokens || 0,
      };
    } catch (error) {
      if (error instanceof Error && error.message.includes('OpenAI API error')) {
        throw new StudyModeError('AI_UNAVAILABLE', error.message);
      }
      throw new StudyModeError('AI_UNAVAILABLE', 'Failed to connect to OpenAI');
    }
  }
}

// =============================================================================
// Anthropic Provider
// =============================================================================

export class AnthropicProvider implements AIProvider {
  private apiKey: string;
  private model: string;

  constructor(config: { apiKey: string; model?: string }) {
    this.apiKey = config.apiKey;
    this.model = config.model || 'claude-3-opus-20240229';
  }

  async complete(request: AICompletionRequest): Promise<AIProviderResponse> {
    const systemPrompt = request.mode === 'teach'
      ? buildTeachModePrompt(request.lessonContext, request.conversationHistory)
      : buildAskModePrompt(request.lessonContext, request.conversationHistory);

    const messages = [
      ...request.conversationHistory.map(m => ({
        role: m.role as 'user' | 'assistant',
        content: m.content,
      })),
      { role: 'user' as const, content: request.userMessage },
    ];

    try {
      const response = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': this.apiKey,
          'anthropic-version': '2023-06-01',
        },
        body: JSON.stringify({
          model: this.model,
          max_tokens: 1024,
          system: systemPrompt,
          messages,
        }),
      });

      if (!response.ok) {
        const error = await response.text();
        throw new Error(`Anthropic API error: ${response.status} ${error}`);
      }

      const data = await response.json();
      const content = data.content?.[0]?.text;

      if (!content) {
        throw new Error('Invalid Anthropic response format');
      }

      return {
        content,
        model: this.model,
        tokensUsed: (data.usage?.input_tokens || 0) + (data.usage?.output_tokens || 0),
      };
    } catch (error) {
      if (error instanceof Error && error.message.includes('Anthropic API error')) {
        throw new StudyModeError('AI_UNAVAILABLE', error.message);
      }
      throw new StudyModeError('AI_UNAVAILABLE', 'Failed to connect to Anthropic');
    }
  }
}

// =============================================================================
// Factory
// =============================================================================

export function createAIProvider(config?: AIProviderConfig): AIProvider {
  // If no config, return mock provider (for testing)
  if (!config) {
    return new MockAIProvider();
  }

  switch (config.provider) {
    case 'openai':
      return new OpenAIProvider({
        apiKey: config.apiKey,
        model: config.model,
      });
    case 'anthropic':
      return new AnthropicProvider({
        apiKey: config.apiKey,
        model: config.model,
      });
    default:
      throw new Error(`Unknown AI provider: ${config.provider}`);
  }
}

/**
 * Create provider from environment variables
 */
export function createAIProviderFromEnv(): AIProvider {
  const provider = process.env.AI_PROVIDER || 'anthropic';
  const openaiKey = process.env.OPENAI_API_KEY;
  const anthropicKey = process.env.ANTHROPIC_API_KEY;

  if (provider === 'openai' && openaiKey) {
    return new OpenAIProvider({ apiKey: openaiKey });
  }

  if (provider === 'anthropic' && anthropicKey) {
    return new AnthropicProvider({ apiKey: anthropicKey });
  }

  // Fall back to mock provider if no keys configured
  console.warn('No AI provider API keys configured, using mock provider');
  return new MockAIProvider();
}

// =============================================================================
// Convenience Factory Functions
// =============================================================================

export function createMockProvider(): AIProvider & { name: string } {
  const provider = new MockAIProvider();
  return Object.assign(provider, { name: 'mock' });
}

export function createOpenAIProvider(apiKey: string, model?: string): AIProvider & { name: string } {
  const provider = new OpenAIProvider({ apiKey, model });
  return Object.assign(provider, { name: `openai/${model || 'gpt-4o-mini'}` });
}

export function createAnthropicProvider(apiKey: string, model?: string): AIProvider & { name: string } {
  const provider = new AnthropicProvider({ apiKey, model });
  return Object.assign(provider, { name: `anthropic/${model || 'claude-3-haiku'}` });
}
