/**
 * useStudyModeAPI Hook
 *
 * Handles API calls to the study mode backend
 * Works with StudyModeContext for state management
 */

import { useCallback } from 'react';
import { useStudyMode, type Message, type ChatMode } from '../../contexts/StudyModeContext';

// =============================================================================
// Types
// =============================================================================

interface ChatRequest {
  lessonPath: string;
  userMessage: string;
  conversationHistory: Message[];
  mode: ChatMode;
}

interface ChatResponse {
  assistantMessage: string;
  metadata: {
    model: string;
    tokensUsed: number;
    processingTimeMs: number;
  };
}

interface ErrorResponse {
  error: {
    code: string;
    message: string;
  };
}

// =============================================================================
// API Configuration
// =============================================================================

// API base URL - can be configured via window variable or defaults to API server
const API_BASE_URL = typeof window !== 'undefined'
  ? (window as unknown as { __STUDY_MODE_API_URL__?: string }).__STUDY_MODE_API_URL__ || 'http://localhost:3001/api'
  : 'http://localhost:3001/api';

// =============================================================================
// Hook
// =============================================================================

export function useStudyModeAPI() {
  const {
    mode,
    getCurrentConversation,
    addMessage,
    setLoading,
    setError,
  } = useStudyMode();

  /**
   * Send a message to the AI and get a response
   */
  const sendMessage = useCallback(async (lessonPath: string, userMessage: string): Promise<void> => {
    // Get current conversation history
    const conversation = getCurrentConversation(lessonPath);

    // Create user message
    const userMsg: Message = {
      role: 'user',
      content: userMessage,
      timestamp: new Date().toISOString(),
    };

    // Add user message to conversation immediately
    addMessage(lessonPath, userMsg);

    // Prepare request
    const request: ChatRequest = {
      lessonPath,
      userMessage,
      conversationHistory: conversation.messages,
      mode,
    };

    setLoading(true);
    setError(null);

    try {
      const response = await fetch(`${API_BASE_URL}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(request),
      });

      if (!response.ok) {
        const errorData = await response.json() as ErrorResponse;
        throw new Error(errorData.error?.message || `Request failed: ${response.status}`);
      }

      const data = await response.json() as ChatResponse;

      // Add assistant message to conversation
      const assistantMsg: Message = {
        role: 'assistant',
        content: data.assistantMessage,
        timestamp: new Date().toISOString(),
      };

      addMessage(lessonPath, assistantMsg);
      setLoading(false);

    } catch (error) {
      const errorMessage = error instanceof Error
        ? error.message
        : 'An unexpected error occurred. Please try again.';

      setError(errorMessage);
      setLoading(false);
    }
  }, [mode, getCurrentConversation, addMessage, setLoading, setError]);

  return {
    sendMessage,
  };
}
