/**
 * TeachMePanel Integration Tests
 *
 * Tests the complete flow from UI interaction to API communication
 */

import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { TeachMePanel } from '../index';
import { StudyModeProvider } from '../../../contexts/StudyModeContext';

// Mock fetch for API calls
const mockFetch = jest.fn();
global.fetch = mockFetch;

// Test wrapper with provider
function TestWrapper({ children }: { children: React.ReactNode }) {
  return <StudyModeProvider>{children}</StudyModeProvider>;
}

describe('TeachMePanel', () => {
  beforeEach(() => {
    mockFetch.mockReset();
    sessionStorage.clear();
  });

  describe('rendering', () => {
    it('renders panel in closed state by default', () => {
      render(
        <TestWrapper>
          <TeachMePanel lessonPath="/docs/test-lesson" />
        </TestWrapper>
      );

      const panel = screen.getByRole('complementary');
      expect(panel).toHaveAttribute('aria-hidden', 'true');
    });

    it('renders mode toggle with Teach and Ask buttons', () => {
      render(
        <TestWrapper>
          <TeachMePanel lessonPath="/docs/test-lesson" />
        </TestWrapper>
      );

      expect(screen.getByRole('tab', { name: /teach/i })).toBeInTheDocument();
      expect(screen.getByRole('tab', { name: /ask/i })).toBeInTheDocument();
    });

    it('renders empty state when no messages', () => {
      render(
        <TestWrapper>
          <TeachMePanel lessonPath="/docs/test-lesson" />
        </TestWrapper>
      );

      expect(screen.getByText(/start learning/i)).toBeInTheDocument();
    });
  });

  describe('mode toggle', () => {
    it('switches between teach and ask modes', async () => {
      const user = userEvent.setup();

      render(
        <TestWrapper>
          <TeachMePanel lessonPath="/docs/test-lesson" />
        </TestWrapper>
      );

      const teachTab = screen.getByRole('tab', { name: /teach/i });
      const askTab = screen.getByRole('tab', { name: /ask/i });

      // Default is teach mode
      expect(teachTab).toHaveAttribute('aria-selected', 'true');
      expect(askTab).toHaveAttribute('aria-selected', 'false');

      // Switch to ask mode
      await user.click(askTab);
      expect(teachTab).toHaveAttribute('aria-selected', 'false');
      expect(askTab).toHaveAttribute('aria-selected', 'true');
    });
  });

  describe('message input', () => {
    it('enables send button when text is entered', async () => {
      const user = userEvent.setup();

      render(
        <TestWrapper>
          <TeachMePanel lessonPath="/docs/test-lesson" />
        </TestWrapper>
      );

      const input = screen.getByRole('textbox');
      const sendButton = screen.getByRole('button', { name: /send/i });

      // Initially disabled
      expect(sendButton).toBeDisabled();

      // Type message
      await user.type(input, 'Hello AI');
      expect(sendButton).not.toBeDisabled();
    });

    it('clears input after sending message', async () => {
      const user = userEvent.setup();

      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: () =>
          Promise.resolve({
            assistantMessage: 'Hello! How can I help?',
            metadata: { model: 'test', tokensUsed: 10, processingTimeMs: 100 },
          }),
      });

      render(
        <TestWrapper>
          <TeachMePanel lessonPath="/docs/test-lesson" />
        </TestWrapper>
      );

      const input = screen.getByRole('textbox');
      await user.type(input, 'Hello AI');
      await user.keyboard('{Enter}');

      expect(input).toHaveValue('');
    });
  });

  describe('API integration', () => {
    it('sends correct request payload for teach mode', async () => {
      const user = userEvent.setup();

      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: () =>
          Promise.resolve({
            assistantMessage: 'Let me teach you...',
            metadata: { model: 'test', tokensUsed: 50, processingTimeMs: 200 },
          }),
      });

      render(
        <TestWrapper>
          <TeachMePanel lessonPath="/docs/test-lesson" />
        </TestWrapper>
      );

      const input = screen.getByRole('textbox');
      await user.type(input, 'Teach me about AI agents');
      await user.keyboard('{Enter}');

      await waitFor(() => {
        expect(mockFetch).toHaveBeenCalledWith(
          '/api/chat',
          expect.objectContaining({
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: expect.stringContaining('"mode":"teach"'),
          })
        );
      });
    });

    it('sends correct request payload for ask mode', async () => {
      const user = userEvent.setup();

      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: () =>
          Promise.resolve({
            assistantMessage: 'The answer is...',
            metadata: { model: 'test', tokensUsed: 30, processingTimeMs: 150 },
          }),
      });

      render(
        <TestWrapper>
          <TeachMePanel lessonPath="/docs/test-lesson" />
        </TestWrapper>
      );

      // Switch to ask mode
      const askTab = screen.getByRole('tab', { name: /ask/i });
      await user.click(askTab);

      const input = screen.getByRole('textbox');
      await user.type(input, 'What is an AI agent?');
      await user.keyboard('{Enter}');

      await waitFor(() => {
        expect(mockFetch).toHaveBeenCalledWith(
          '/api/chat',
          expect.objectContaining({
            body: expect.stringContaining('"mode":"ask"'),
          })
        );
      });
    });

    it('displays assistant response after successful API call', async () => {
      const user = userEvent.setup();

      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: () =>
          Promise.resolve({
            assistantMessage: 'Here is my response about AI agents.',
            metadata: { model: 'gpt-4', tokensUsed: 100, processingTimeMs: 500 },
          }),
      });

      render(
        <TestWrapper>
          <TeachMePanel lessonPath="/docs/test-lesson" />
        </TestWrapper>
      );

      const input = screen.getByRole('textbox');
      await user.type(input, 'Tell me about agents');
      await user.keyboard('{Enter}');

      await waitFor(() => {
        expect(
          screen.getByText('Here is my response about AI agents.')
        ).toBeInTheDocument();
      });
    });

    it('displays error message on API failure', async () => {
      const user = userEvent.setup();

      mockFetch.mockResolvedValueOnce({
        ok: false,
        status: 429,
        json: () =>
          Promise.resolve({
            error: { code: 'RATE_LIMITED', message: 'Too many requests' },
          }),
      });

      render(
        <TestWrapper>
          <TeachMePanel lessonPath="/docs/test-lesson" />
        </TestWrapper>
      );

      const input = screen.getByRole('textbox');
      await user.type(input, 'Hello');
      await user.keyboard('{Enter}');

      await waitFor(() => {
        expect(screen.getByRole('alert')).toHaveTextContent('Too many requests');
      });
    });
  });

  describe('conversation persistence', () => {
    it('maintains separate conversations per lesson', async () => {
      const user = userEvent.setup();

      mockFetch.mockResolvedValue({
        ok: true,
        json: () =>
          Promise.resolve({
            assistantMessage: 'Response',
            metadata: { model: 'test', tokensUsed: 10, processingTimeMs: 100 },
          }),
      });

      const { rerender } = render(
        <TestWrapper>
          <TeachMePanel lessonPath="/docs/lesson-1" />
        </TestWrapper>
      );

      const input = screen.getByRole('textbox');
      await user.type(input, 'Question for lesson 1');
      await user.keyboard('{Enter}');

      await waitFor(() => {
        expect(screen.getByText('Question for lesson 1')).toBeInTheDocument();
      });

      // Switch to different lesson
      rerender(
        <TestWrapper>
          <TeachMePanel lessonPath="/docs/lesson-2" />
        </TestWrapper>
      );

      // Should show empty state for new lesson
      expect(screen.getByText(/start learning/i)).toBeInTheDocument();
      expect(screen.queryByText('Question for lesson 1')).not.toBeInTheDocument();
    });
  });

  describe('accessibility', () => {
    it('has correct ARIA attributes on panel', () => {
      render(
        <TestWrapper>
          <TeachMePanel lessonPath="/docs/test-lesson" />
        </TestWrapper>
      );

      const panel = screen.getByRole('complementary');
      expect(panel).toHaveAttribute('aria-label', 'Study Mode Chat Panel');
    });

    it('has accessible labels on buttons', () => {
      render(
        <TestWrapper>
          <TeachMePanel lessonPath="/docs/test-lesson" />
        </TestWrapper>
      );

      expect(
        screen.getByRole('button', { name: /close panel/i })
      ).toBeInTheDocument();
      expect(
        screen.getByRole('button', { name: /start new conversation/i })
      ).toBeInTheDocument();
      expect(
        screen.getByRole('button', { name: /send message/i })
      ).toBeInTheDocument();
    });

    it('has accessible input label', () => {
      render(
        <TestWrapper>
          <TeachMePanel lessonPath="/docs/test-lesson" />
        </TestWrapper>
      );

      expect(
        screen.getByRole('textbox', { name: /chat message input/i })
      ).toBeInTheDocument();
    });
  });
});
