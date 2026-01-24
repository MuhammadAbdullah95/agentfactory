/**
 * TeachMePanel Component
 *
 * Main slide-out chat panel for Interactive Study Mode
 * Uses @chatscope/chat-ui-kit-react for polished chat UI
 * Renders markdown content to match book styling
 */

import React, { useCallback, useEffect, useRef, useMemo } from 'react';
import {
  MainContainer,
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
  TypingIndicator,
  Avatar,
  ConversationHeader,
} from '@chatscope/chat-ui-kit-react';
import '@chatscope/chat-ui-kit-styles/dist/default/styles.min.css';
import ReactMarkdown from 'react-markdown';

import { useStudyMode } from '../../contexts/StudyModeContext';
import { useStudyModeAPI } from './useStudyModeAPI';
import { ModeToggle } from './ModeToggle';
import styles from './styles.module.css';

/**
 * Render markdown content with book-matching styles
 */
function MarkdownContent({ content }: { content: string }) {
  return (
    <div className={styles.markdownContent}>
      <ReactMarkdown
        components={{
          // Custom renderers to match book styling
          p: ({ children }) => <p className={styles.mdParagraph}>{children}</p>,
          strong: ({ children }) => <strong className={styles.mdBold}>{children}</strong>,
          em: ({ children }) => <em className={styles.mdItalic}>{children}</em>,
          ul: ({ children }) => <ul className={styles.mdList}>{children}</ul>,
          ol: ({ children }) => <ol className={styles.mdOrderedList}>{children}</ol>,
          li: ({ children }) => <li className={styles.mdListItem}>{children}</li>,
          h3: ({ children }) => <h3 className={styles.mdHeading}>{children}</h3>,
          h4: ({ children }) => <h4 className={styles.mdSubheading}>{children}</h4>,
          code: ({ children }) => <code className={styles.mdCode}>{children}</code>,
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}

/**
 * Parse message content to extract clickable topics/questions
 * Returns { mainContent: string, clickables: [], label: string }
 */
function parseMessageForClickables(content: string): {
  mainContent: string;
  clickables: { text: string; type: 'topic' | 'question' }[];
  label: string;
} {
  const clickables: { text: string; type: 'topic' | 'question' }[] = [];
  let mainContent = content;
  let label = '';

  // Pattern for "Think about this:" (Teach mode Socratic questions)
  const socraticMatch = content.match(/🤔\s*\*\*Think about this:\*\*:?\s*([\s\S]*?)(?=\n\n|$)/i);
  if (socraticMatch) {
    label = '🤔 Think about this:';
    const socraticSection = socraticMatch[1];
    // Extract bullet points (• or -)
    const bulletPoints = socraticSection.match(/[•\-]\s*([^\n]+)/g);
    if (bulletPoints) {
      bulletPoints.forEach(bp => {
        const text = bp.replace(/^[•\-]\s*/, '').trim();
        if (text) {
          clickables.push({ text, type: 'topic' });
        }
      });
    }
    // Remove the Socratic section from main content
    mainContent = content.replace(/🤔\s*\*\*Think about this:\*\*:?\s*[\s\S]*?(?=\n\n|$)/i, '').trim();
  }

  // Pattern for "Let me check:" (Teach mode opening Socratic question)
  const checkMatch = content.match(/🤔\s*\*\*Let me check:\*\*:?\s*([\s\S]*?)(?=\n\n|$)/i);
  if (checkMatch && clickables.length === 0) {
    label = '🤔 Let me check:';
    const checkSection = checkMatch[1];
    // Extract bullet points or single question
    const bulletPoints = checkSection.match(/[•\-]\s*([^\n]+)/g);
    if (bulletPoints) {
      bulletPoints.forEach(bp => {
        const text = bp.replace(/^[•\-]\s*/, '').trim();
        if (text) {
          clickables.push({ text, type: 'topic' });
        }
      });
    } else {
      // Single question without bullets
      const singleQuestion = checkSection.trim();
      if (singleQuestion) {
        clickables.push({ text: singleQuestion, type: 'topic' });
      }
    }
    // Remove the check section from main content
    mainContent = content.replace(/🤔\s*\*\*Let me check:\*\*:?\s*[\s\S]*?(?=\n\n|$)/i, '').trim();
  }

  // Pattern for "Do you also want to know about?" (Teach mode topics - legacy)
  const topicsMatch = content.match(/🤔\s*\*\*Do you also want to know about\?\*\*:?\s*([\s\S]*?)(?=\n\n|$)/i);
  if (topicsMatch && clickables.length === 0) {
    label = '🤔 Do you also want to know about?';
    const topicsSection = topicsMatch[1];
    // Extract bullet points (• or -)
    const bulletPoints = topicsSection.match(/[•\-]\s*([^\n]+)/g);
    if (bulletPoints) {
      bulletPoints.forEach(bp => {
        const text = bp.replace(/^[•\-]\s*/, '').trim();
        if (text) {
          clickables.push({ text, type: 'topic' });
        }
      });
    }
    // Remove the topics section from main content
    mainContent = content.replace(/🤔\s*\*\*Do you also want to know about\?\*\*:?\s*[\s\S]*?(?=\n\n|$)/i, '').trim();
  }

  // Pattern for "What would you like to know?" (Ask mode questions) - handles with or without bold
  const questionsMatch = content.match(/❓\s*\*{0,2}What would you like to know\??\*{0,2}:?\s*([\s\S]*?)(?=\n\n|$)/i);
  if (questionsMatch && clickables.length === 0) {
    label = '❓ What would you like to know?';
    const questionsSection = questionsMatch[1];
    // Extract numbered items (1. 2. 3.)
    const numberedItems = questionsSection.match(/\d+\.\s*([^\n]+)/g);
    if (numberedItems) {
      numberedItems.forEach(item => {
        const text = item.replace(/^\d+\.\s*/, '').trim();
        if (text && !text.startsWith('[')) {  // Skip template placeholders
          clickables.push({ text, type: 'question' });
        }
      });
    }
    // Also try bullet points if no numbered items found
    if (clickables.length === 0) {
      const bulletPoints = questionsSection.match(/[•\-]\s*([^\n]+)/g);
      if (bulletPoints) {
        bulletPoints.forEach(bp => {
          const text = bp.replace(/^[•\-]\s*/, '').trim();
          if (text && !text.startsWith('[')) {
            clickables.push({ text, type: 'question' });
          }
        });
      }
    }
    // Remove the questions section from main content
    mainContent = mainContent.replace(/❓\s*\*{0,2}What would you like to know\??\*{0,2}:?\s*[\s\S]*?(?=\n\n|$)/i, '').trim();
  }

  // Pattern for "What else would you like to know?" (Ask mode follow-up)
  const followUpMatch = content.match(/🤔\s*\*{0,2}What else would you like to know\??\*{0,2}:?\s*([\s\S]*?)(?=\n\n|$)/i);
  if (followUpMatch && clickables.length === 0) {
    label = '🤔 What else would you like to know?';
    const followUpSection = followUpMatch[1];
    const bulletPoints = followUpSection.match(/[•\-]\s*([^\n]+)/g);
    if (bulletPoints) {
      bulletPoints.forEach(bp => {
        const text = bp.replace(/^[•\-]\s*/, '').trim();
        if (text && !text.startsWith('[')) {
          clickables.push({ text, type: 'question' });
        }
      });
    }
    mainContent = mainContent.replace(/🤔\s*\*{0,2}What else would you like to know\??\*{0,2}:?\s*[\s\S]*?(?=\n\n|$)/i, '').trim();
  }

  // Also support old formats for backward compatibility
  if (clickables.length === 0) {
    // Old topic format
    const oldTopicsMatch = content.match(/📚\s*\*\*Related topics[^*]*\*\*:?\s*([\s\S]*?)(?=\n\n|$)/i);
    if (oldTopicsMatch) {
      label = '🤔 Do you also want to know about?';
      const topicsSection = oldTopicsMatch[1];
      const bulletPoints = topicsSection.match(/[•\-]\s*([^\n]+)/g);
      if (bulletPoints) {
        bulletPoints.forEach(bp => {
          const text = bp.replace(/^[•\-]\s*/, '').trim();
          if (text) clickables.push({ text, type: 'topic' });
        });
      }
      mainContent = content.replace(/📚\s*\*\*Related topics[^*]*\*\*:?\s*[\s\S]*?(?=\n\n|$)/i, '').trim();
    }

    // Old question format
    const oldQuestionsMatch = content.match(/💡\s*\*\*Questions[^*]*\*\*:?\s*([\s\S]*?)(?=\n\n|$)/i);
    if (oldQuestionsMatch) {
      label = '❓ What would you like to know?';
      const questionsSection = oldQuestionsMatch[1];
      const numberedItems = questionsSection.match(/\d+\.\s*([^\n]+)/g);
      if (numberedItems) {
        numberedItems.forEach(item => {
          const text = item.replace(/^\d+\.\s*/, '').trim();
          if (text) clickables.push({ text, type: 'question' });
        });
      }
      mainContent = mainContent.replace(/💡\s*\*\*Questions[^*]*\*\*:?\s*[\s\S]*?(?=\n\n|$)/i, '').trim();
    }
  }

  return { mainContent, clickables, label };
}

interface TeachMePanelProps {
  /** Current lesson path for context */
  lessonPath: string;
}

export function TeachMePanel({ lessonPath }: TeachMePanelProps) {
  const {
    isOpen,
    mode,
    isLoading,
    error,
    closePanel,
    setMode,
    getCurrentConversation,
    clearConversation,
    setError,
  } = useStudyMode();

  const { sendMessage } = useStudyModeAPI();

  // Get current conversation for this lesson + mode (separate conversations per mode)
  const conversationKey = `${lessonPath}:${mode}`;
  const conversation = getCurrentConversation(conversationKey);

  // Ref for message list container to control scrolling
  const messageListRef = useRef<HTMLDivElement>(null);
  const prevMessageCountRef = useRef(0);

  // Handle sending messages (use conversationKey for mode-specific storage)
  const handleSend = useCallback((text: string) => {
    if (text.trim()) {
      sendMessage(lessonPath, text.trim(), `${lessonPath}:${mode}`);
    }
  }, [lessonPath, mode, sendMessage]);

  // Handle clearing conversation (clears current mode's conversation only)
  const handleClear = useCallback(() => {
    clearConversation(`${lessonPath}:${mode}`);
  }, [lessonPath, mode, clearConversation]);

  // Track previous mode to detect changes
  const prevModeRef = useRef(mode);

  // Scroll to show the start of new AI response (not the end)
  useEffect(() => {
    const currentCount = conversation.messages.length;
    const prevCount = prevMessageCountRef.current;

    // Check if a new assistant message was added
    if (currentCount > prevCount && currentCount > 0) {
      const lastMessage = conversation.messages[currentCount - 1];
      if (lastMessage.role === 'assistant') {
        // Scroll to show the START of the new AI message (not the end)
        const scrollToStart = () => {
          const scrollWrapper = document.querySelector('.cs-message-list__scroll-wrapper');
          const messages = document.querySelectorAll('.cs-message');
          const lastMessageEl = messages[messages.length - 1] as HTMLElement;

          if (scrollWrapper && lastMessageEl) {
            // Scroll to position the message at the top with padding
            const targetScroll = lastMessageEl.offsetTop - 10;
            scrollWrapper.scrollTop = targetScroll;
          }
        };

        // Run multiple times to override ChatScope's auto-scroll
        setTimeout(scrollToStart, 50);
        setTimeout(scrollToStart, 150);
        setTimeout(scrollToStart, 300);
      }
    }

    prevMessageCountRef.current = currentCount;
  }, [conversation.messages]);

  // Handle mode change - auto-send initial message
  const handleModeChange = useCallback((newMode: 'teach' | 'ask') => {
    setMode(newMode);
    // DON'T clear conversation - keep separate conversations per mode

    // Only auto-send initial message if that mode has no conversation yet
    const newConversationKey = `${lessonPath}:${newMode}`;
    const existingConversation = getCurrentConversation(newConversationKey);

    if (existingConversation.messages.length === 0) {
      setTimeout(() => {
        if (newMode === 'ask') {
          sendMessage(lessonPath, 'show suggestions', newConversationKey);
        } else if (newMode === 'teach') {
          sendMessage(lessonPath, 'teach me', newConversationKey);
        }
      }, 100);
    }
  }, [setMode, lessonPath, sendMessage, getCurrentConversation]);

  // Handle escape key to close panel
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isOpen) {
        closePanel();
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, closePanel]);

  // Prevent body scroll when panel is open on mobile
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => {
      document.body.style.overflow = '';
    };
  }, [isOpen]);

  // Clear error after 5 seconds
  useEffect(() => {
    if (error) {
      const timer = setTimeout(() => setError(null), 5000);
      return () => clearTimeout(timer);
    }
  }, [error, setError]);

  // Get placeholder text based on mode
  const placeholder = mode === 'teach'
    ? 'Say "teach me" or ask for an explanation...'
    : 'Ask any question about this lesson...';

  return (
    <>
      {/* Overlay for mobile */}
      <div
        className={`${styles.overlay} ${isOpen ? styles.overlayVisible : ''}`}
        onClick={closePanel}
        aria-hidden="true"
      />

      {/* Main panel */}
      <aside
        className={`${styles.panel} ${isOpen ? styles.panelOpen : ''}`}
        role="complementary"
        aria-label="Study Mode Chat Panel"
        aria-hidden={!isOpen}
      >
        {/* Custom Header with Mode Toggle */}
        <div className={styles.chatKitHeader}>
          <div className={styles.headerTop}>
            <div className={styles.titleSection}>
              <h2 className={styles.title}>Study Mode</h2>
              {mode === 'teach' && (
                <span className={styles.methodBadge}>
                  Teaching by Socratic Method (OpenAI Study Mode & Google Extended Learning)
                </span>
              )}
            </div>
            <div className={styles.headerActions}>
              <button
                className={styles.iconButton}
                onClick={handleClear}
                aria-label="Start new conversation"
                title="New Chat"
              >
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M12 5v14M5 12h14" />
                </svg>
              </button>
              <button
                className={styles.iconButton}
                onClick={closePanel}
                aria-label="Close panel"
              >
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <line x1="18" y1="6" x2="6" y2="18" />
                  <line x1="6" y1="6" x2="18" y2="18" />
                </svg>
              </button>
            </div>
          </div>
          <ModeToggle mode={mode} onModeChange={handleModeChange} />
        </div>

        {/* Error display */}
        {error && (
          <div className={styles.error} role="alert">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="12" cy="12" r="10" />
              <line x1="12" y1="8" x2="12" y2="12" />
              <line x1="12" y1="16" x2="12.01" y2="16" />
            </svg>
            {error}
          </div>
        )}

        {/* Mode indicator bar */}
        <div className={`${styles.modeIndicator} ${mode === 'teach' ? styles.modeTeach : styles.modeAsk}`}>
          {mode === 'teach' ? (
            <>
              <span className={styles.modeIcon}>📚</span>
              <span>Socratic Teaching - AI guides you with questions</span>
            </>
          ) : (
            <>
              <span className={styles.modeIcon}>⚡</span>
              <span>Quick Answers - Direct responses only</span>
            </>
          )}
        </div>

        {/* ChatScope Chat Container */}
        <div className={styles.chatKitContainer}>
          <MainContainer>
            <ChatContainer>
              <MessageList
                autoScrollToBottom={false}
                autoScrollToBottomOnMount={false}
                typingIndicator={
                  isLoading ? (
                    <TypingIndicator content="AI Tutor is thinking..." />
                  ) : null
                }
              >
                {conversation.messages.length === 0 && !isLoading ? (
                  <MessageList.Content className={styles.emptyStateWrapper}>
                    <div className={styles.emptyState}>
                      <div className={styles.emptyIcon}>
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                          {mode === 'teach' ? (
                            <><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" /><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" /></>
                          ) : (
                            <><circle cx="12" cy="12" r="10" /><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" /><line x1="12" y1="17" x2="12.01" y2="17" /></>
                          )}
                        </svg>
                      </div>
                      <h3 className={styles.emptyTitle}>
                        {mode === 'teach' ? 'Ready to Learn' : 'Ask Questions'}
                      </h3>
                      <p className={styles.emptyText}>
                        {mode === 'teach'
                          ? 'Click the Teach button to get a guided explanation of this lesson from the book.'
                          : 'Click the Ask button to see suggested questions from this lesson.'}
                      </p>
                    </div>
                  </MessageList.Content>
                ) : (
                  conversation.messages.map((msg, index) => {
                    // Parse assistant messages for clickable topics/questions
                    const parsed = msg.role === 'assistant'
                      ? parseMessageForClickables(msg.content)
                      : { mainContent: msg.content, clickables: [], label: '' };

                    return (
                      <React.Fragment key={`${msg.timestamp}-${index}`}>
                        <Message
                          model={{
                            sentTime: msg.timestamp,
                            sender: msg.role === 'user' ? 'You' : 'AI Tutor',
                            direction: msg.role === 'user' ? 'outgoing' : 'incoming',
                            position: 'single',
                          }}
                        >
                          {msg.role === 'assistant' && (
                            <Avatar
                              name="AI Tutor"
                              src=""
                              size="sm"
                            >
                              <div className={styles.aiAvatar}>
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                  <path d="M12 2a10 10 0 1 0 10 10H12V2z" />
                                  <path d="M12 2a10 10 0 0 1 10 10" />
                                  <circle cx="12" cy="12" r="3" />
                                </svg>
                              </div>
                            </Avatar>
                          )}
                          {/* Render markdown for assistant, plain text for user */}
                          <Message.CustomContent>
                            {msg.role === 'assistant' ? (
                              <MarkdownContent content={parsed.mainContent} />
                            ) : (
                              <div className={styles.userMessage}>{parsed.mainContent}</div>
                            )}
                          </Message.CustomContent>
                        </Message>

                        {/* Render clickable topics/questions as buttons */}
                        {parsed.clickables.length > 0 && (
                          <div className={styles.clickableButtonsWrapper}>
                            <div className={styles.clickableButtonsLabel}>
                              {parsed.label || (parsed.clickables[0].type === 'topic'
                                ? '🤔 Do you also want to know about?'
                                : '❓ What would you like to know?')}
                            </div>
                            <div className={styles.clickableButtons}>
                              {parsed.clickables.map((item, i) => (
                                <button
                                  key={i}
                                  className={`${styles.clickableButton} ${
                                    item.type === 'topic' ? styles.topicButton : styles.questionButton
                                  }`}
                                  onClick={() => handleSend(item.text)}
                                  disabled={isLoading}
                                >
                                  <span className={styles.buttonIcon}>
                                    {item.type === 'topic' ? '→' : '?'}
                                  </span>
                                  {item.text}
                                </button>
                              ))}
                            </div>
                          </div>
                        )}
                      </React.Fragment>
                    );
                  })
                )}
              </MessageList>
              <MessageInput
                placeholder={placeholder}
                onSend={handleSend}
                disabled={isLoading}
                attachButton={false}
                sendButton={true}
              />
            </ChatContainer>
          </MainContainer>
        </div>
      </aside>
    </>
  );
}

// Also export sub-components for potential standalone use
export { ModeToggle } from './ModeToggle';
export { ChatMessages } from './ChatMessages';
export { ChatInput } from './ChatInput';
export { useStudyModeAPI } from './useStudyModeAPI';
