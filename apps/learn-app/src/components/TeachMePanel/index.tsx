/**
 * TeachMePanel Component - Official OpenAI ChatKit Integration
 *
 * Uses @openai/chatkit-react for the chat UI with Shadcn Sheet for the panel.
 * Connected to our self-hosted ChatKit server for book-grounded responses.
 *
 * Features:
 * - Socratic Teaching Mode (teach) - explains step-by-step, asks checking questions
 * - Quick Ask Mode (ask) - direct answers via text selection
 * - Text selection "Ask" button for quick questions
 *
 * Reference: https://github.com/openai/openai-chatkit-starter-app
 */

import React, { useState, useMemo, useCallback, useEffect, useRef } from "react";
import { ChatKit, useChatKit } from "@openai/chatkit-react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { useStudyMode } from "../../contexts/StudyModeContext";
import { useAuth } from "../../contexts/AuthContext";
import { Sheet, SheetContent, SheetClose } from "@/components/ui/sheet";
import { X } from "lucide-react";
import styles from "./styles.module.css";

// Fallback user ID for anonymous users (not logged in)
function getAnonymousUserId(): string {
  if (typeof window === "undefined") return "anonymous";

  let userId = localStorage.getItem("study_mode_user_id");
  if (!userId) {
    userId = `anon_${Math.random().toString(36).substring(2, 15)}`;
    localStorage.setItem("study_mode_user_id", userId);
  }
  return userId;
}

// Chat mode type
type ChatMode = "teach" | "ask";

// Build URL with lesson path, user info, and mode
function getChatKitUrl(
  apiBase: string,
  lessonPath: string,
  userId: string,
  mode: ChatMode = "teach",
  userName?: string,
): string {
  const params = new URLSearchParams();
  params.set("mode", mode);
  params.set("user_id", userId);
  if (userName) {
    params.set("user_name", userName);
  }
  if (lessonPath) {
    params.set("lesson_path", lessonPath);
  }
  return `${apiBase}/chatkit?${params.toString()}`;
}

interface TeachMePanelProps {
  lessonPath: string;
}

/**
 * Inner ChatKit wrapper with user context
 */
function ChatKitWrapper({
  lessonPath,
  lessonTitle,
  apiBase,
  domainKey,
  mode = "teach",
  initialMessage,
  onSendMessage,
  onInitialMessageSent,
  hideFirstUserMessage = false,
}: {
  lessonPath: string;
  lessonTitle: string;
  apiBase: string;
  domainKey: string;
  mode?: ChatMode;
  initialMessage?: string;
  onSendMessage?: (sendFn: (text: string) => Promise<void>) => void;
  onInitialMessageSent?: () => void;
  hideFirstUserMessage?: boolean;
}) {
  const { session } = useAuth();

  // Use authenticated user ID if available, otherwise anonymous
  const userId = useMemo(() => {
    if (session?.user?.id) {
      return session.user.id;
    }
    return getAnonymousUserId();
  }, [session?.user?.id]);

  // Get user's display name from auth context
  const userName = useMemo(() => {
    if (session?.user?.name) {
      return session.user.name;
    }
    if (session?.user?.email) {
      return session.user.email.split("@")[0];
    }
    return undefined;
  }, [session?.user?.name, session?.user?.email]);

  const apiUrl = useMemo(
    () => getChatKitUrl(apiBase, lessonPath, userId, mode, userName),
    [apiBase, lessonPath, userId, mode, userName],
  );

  // Custom fetch that injects Authorization header with JWT token
  // Must use ID token (JWT format) not access token (may be opaque)
  const authenticatedFetch = useCallback(
    async (input: RequestInfo | URL, options?: RequestInit) => {
      // Priority: ID token from localStorage (JWT format required by backend)
      const token = localStorage.getItem("ainative_id_token");

      // Debug logging - ALWAYS log to see what's happening
      console.log("[TeachMePanel] ===== authenticatedFetch called =====");
      console.log("[TeachMePanel] ainative_id_token:", token ? "EXISTS" : "NULL/MISSING");
      console.log("[TeachMePanel] ainative_access_token:", localStorage.getItem("ainative_access_token") ? "EXISTS" : "NULL/MISSING");
      if (token) {
        console.log("[TeachMePanel] Token preview:", token.substring(0, 50) + "...");
        console.log("[TeachMePanel] Token parts (should be 3):", token.split(".").length);
      } else {
        console.log("[TeachMePanel] WARNING: No ID token found! User may not be logged in properly.");
      }
      console.log("[TeachMePanel] Options headers from ChatKit:", options?.headers);

      const response = await fetch(input, {
        ...options,
        headers: {
          ...options?.headers,
          ...(token ? { Authorization: `Bearer ${token}` } : {}),
          "X-User-ID": userId,
          ...(userName ? { "X-User-Name": userName } : {}),
        },
      });

      console.log("[TeachMePanel] Response status:", response.status);
      return response;
    },
    [userId, userName],
  );

  const { control, sendUserMessage } = useChatKit({
    api: {
      url: apiUrl,
      domainKey,
      fetch: authenticatedFetch,
    },
    composer: {
      placeholder:
        mode === "teach"
          ? "Ask me anything about this lesson..."
          : "Ask a quick question...",
      attachments: { enabled: false },
    },
    startScreen: {
      greeting:
        mode === "teach"
          ? `Let's explore ${lessonTitle}`
          : `Quick answers about ${lessonTitle}`,
      prompts:
        mode === "teach"
          ? [
              {
                icon: "circle-question",
                label: "What should I understand?",
                prompt:
                  "What are the key things I should understand from this lesson? Ask me questions to check my understanding.",
              },
              {
                icon: "lightbulb",
                label: "Walk me through it",
                prompt:
                  "Walk me through the main concept step by step. Pause to ask if I understand before moving on.",
              },
              {
                icon: "circle-question",
                label: "Help me think about this",
                prompt:
                  "Help me think through this topic. What questions should I be asking myself?",
              },
              {
                icon: "lightbulb",
                label: "Quiz me",
                prompt:
                  "Quiz me on this topic to test my understanding. Ask one question at a time.",
              },
            ]
          : [
              {
                icon: "circle-question",
                label: "Quick summary",
                prompt: "Give me a quick summary in 2-3 sentences",
              },
              {
                icon: "lightbulb",
                label: "Define this",
                prompt: "Define this concept briefly",
              },
            ],
    },
  });

  // Expose sendUserMessage to parent for Ask button
  useEffect(() => {
    if (onSendMessage && sendUserMessage) {
      onSendMessage(async (text: string) => {
        await sendUserMessage({ text, newThread: false });
      });
    }
  }, [onSendMessage, sendUserMessage]);

  // Send initial message if provided (for Ask feature or auto-start teach mode)
  // Calls onInitialMessageSent callback to clear the message after sending
  useEffect(() => {
    if (initialMessage && sendUserMessage) {
      sendUserMessage({ text: initialMessage, newThread: true }).then(() => {
        if (onInitialMessageSent) {
          onInitialMessageSent();
        }
      });
    }
  }, [initialMessage, sendUserMessage, onInitialMessageSent]);

  // Ref for MutationObserver to hide first user message
  const wrapperRef = useRef<HTMLDivElement>(null);

  // Use MutationObserver to hide the first user message (works with shadow DOM)
  useEffect(() => {
    if (!hideFirstUserMessage || !wrapperRef.current) return;

    const hideFirstUserMsg = (container: Element | ShadowRoot) => {
      // Debug: log what we're searching in
      console.log('[TeachMePanel] Searching for user messages in:', container);

      // Try multiple selectors for ChatKit user messages
      const selectors = [
        '[data-role="user"]',
        '[data-message-role="user"]',
        '[class*="user"]',
        '[class*="User"]',
        '[class*="human"]',
        '[class*="Human"]',
        '.oai-user-message',
        'div[style*="flex-end"]', // User messages often aligned right
      ];

      for (const selector of selectors) {
        try {
          const userMessages = container.querySelectorAll(selector);
          console.log(`[TeachMePanel] Selector "${selector}" found ${userMessages.length} elements`);

          if (userMessages.length > 0) {
            const firstUserMsg = userMessages[0] as HTMLElement;
            // Check if this contains "Teach me!" text
            if (firstUserMsg.textContent?.includes('Teach me!')) {
              console.log('[TeachMePanel] Found "Teach me!" message, hiding it:', firstUserMsg);
              firstUserMsg.style.display = 'none';
              firstUserMsg.style.visibility = 'hidden';
              firstUserMsg.style.height = '0';
              firstUserMsg.style.overflow = 'hidden';
              return true;
            }
          }
        } catch (e) {
          // Some selectors might fail in shadow DOM
        }
      }

      // Also try finding by text content directly
      const allElements = container.querySelectorAll('*');
      for (const el of allElements) {
        if (el.textContent === 'Teach me!' || el.textContent?.trim() === 'Teach me!') {
          console.log('[TeachMePanel] Found exact "Teach me!" text in:', el);
          // Hide the message container (go up a few levels)
          let parent = el.parentElement;
          for (let i = 0; i < 5 && parent; i++) {
            if (parent.children.length <= 2) {
              (parent as HTMLElement).style.display = 'none';
              console.log('[TeachMePanel] Hidden parent:', parent);
              return true;
            }
            parent = parent.parentElement;
          }
        }
      }

      return false;
    };

    // Check shadow DOM recursively
    const checkShadowDOM = (element: Element): boolean => {
      if (element.shadowRoot) {
        console.log('[TeachMePanel] Found shadow root on:', element.tagName);
        if (hideFirstUserMsg(element.shadowRoot)) return true;

        // Observe shadow root for changes too
        const shadowObserver = new MutationObserver(() => {
          hideFirstUserMsg(element.shadowRoot!);
        });
        shadowObserver.observe(element.shadowRoot, { childList: true, subtree: true });

        for (const child of element.shadowRoot.querySelectorAll('*')) {
          if (checkShadowDOM(child)) return true;
        }
      }
      for (const child of element.children) {
        if (checkShadowDOM(child)) return true;
      }
      return false;
    };

    // Run checks with delay to ensure ChatKit has rendered
    const runChecks = () => {
      if (wrapperRef.current) {
        console.log('[TeachMePanel] Running hide checks...');
        hideFirstUserMsg(wrapperRef.current);
        checkShadowDOM(wrapperRef.current);
      }
    };

    // Initial check after short delay
    setTimeout(runChecks, 100);
    setTimeout(runChecks, 500);
    setTimeout(runChecks, 1000);
    setTimeout(runChecks, 2000);

    // Observe for changes
    const observer = new MutationObserver(() => {
      runChecks();
    });

    observer.observe(wrapperRef.current, {
      childList: true,
      subtree: true,
      attributes: true,
    });

    return () => observer.disconnect();
  }, [hideFirstUserMessage]);

  return (
    <div
      ref={wrapperRef}
      className={`${styles.chatWrapper} ${hideFirstUserMessage ? styles.hideFirstUser : ''}`}
    >
      <ChatKit control={control} className={styles.chatKit} />
    </div>
  );
}

export function TeachMePanel({ lessonPath }: TeachMePanelProps) {
  const { siteConfig } = useDocusaurusContext();
  const { isOpen, closePanel, openPanel } = useStudyMode();
  const { session } = useAuth();
  const [chatKey, setChatKey] = useState(0);
  const [mode, setMode] = useState<ChatMode>("teach");
  const [initialMessage, setInitialMessage] = useState<string | undefined>();

  // Text selection state for Ask feature
  const [selectedText, setSelectedText] = useState("");
  const [selectionPosition, setSelectionPosition] = useState<{
    x: number;
    y: number;
  } | null>(null);

  // Auth check - only show for logged-in users
  const isLoggedIn = !!session?.user;

  // Get Study Mode API URL from Docusaurus config
  const studyModeApiUrl =
    (siteConfig.customFields?.studyModeApiUrl as string) ||
    "http://localhost:8000";

  // Get ChatKit domain key from config (register at OpenAI for production)
  const chatkitDomainKey =
    (siteConfig.customFields?.chatkitDomainKey as string)?.trim() ||
    "domain_pk_localhost_dev";

  // Extract lesson title for personalized greeting
  const lessonTitle = useMemo(() => {
    const parts = lessonPath.split("/");
    const lastPart = parts[parts.length - 1] || "this lesson";
    // Convert kebab-case to title case, remove numeric prefixes
    return lastPart
      .replace(/^\d+-/, "")
      .replace(/-/g, " ")
      .replace(/\b\w/g, (c) => c.toUpperCase());
  }, [lessonPath]);

  // Track if we've auto-started teach mode for this chat session
  const [hasAutoStarted, setHasAutoStarted] = useState(false);

  // Auto-start Socratic conversation when panel opens in teach mode
  // The agent will text first with a greeting and initial question
  useEffect(() => {
    if (isOpen && mode === "teach" && !initialMessage && !hasAutoStarted) {
      // Short natural message - AI will respond with Socratic greeting
      setInitialMessage("Teach me!");
      setHasAutoStarted(true);
    }
  }, [isOpen, mode, initialMessage, hasAutoStarted, lessonTitle]);

  // Reset auto-start flag when chat key changes (new chat) or mode changes
  useEffect(() => {
    setHasAutoStarted(false);
  }, [chatKey]);

  // Handle text selection for Ask feature
  const handleSelection = useCallback(() => {
    const selection = window.getSelection();
    if (!selection || selection.rangeCount === 0) {
      setSelectedText("");
      setSelectionPosition(null);
      return;
    }

    const text = selection.toString().trim();
    if (text.length > 0 && text.length < 500) {
      // Limit selection length
      setSelectedText(text);
      const range = selection.getRangeAt(0);
      const rect = range.getBoundingClientRect();
      // Position button above selection
      setSelectionPosition({
        x: rect.left + rect.width / 2,
        y: rect.top - 10 + window.scrollY,
      });
    } else {
      setSelectedText("");
      setSelectionPosition(null);
    }
  }, []);

  // Listen for text selection
  useEffect(() => {
    document.addEventListener("selectionchange", handleSelection);
    document.addEventListener("mouseup", handleSelection);
    return () => {
      document.removeEventListener("selectionchange", handleSelection);
      document.removeEventListener("mouseup", handleSelection);
    };
  }, [handleSelection]);

  // Handle Ask button click - opens panel in ask mode with selected text
  const handleAskSelectedText = useCallback(() => {
    if (!selectedText) return;

    const question = `Can you explain this from "${lessonTitle}":\n\n"${selectedText}"`;
    setMode("ask");
    setInitialMessage(question);
    setChatKey((prev) => prev + 1); // Reset chat with new message
    openPanel(); // Open the panel

    // Clear selection
    setSelectedText("");
    setSelectionPosition(null);
    window.getSelection()?.removeAllRanges();
  }, [selectedText, lessonTitle, openPanel]);

  return (
    <>
      {/* Floating Ask button appears when text is selected (logged-in only) */}
      {isLoggedIn && selectedText && selectionPosition && !isOpen && (
        <div
          className={styles.askButton}
          style={{
            position: "absolute",
            left: `${selectionPosition.x}px`,
            top: `${selectionPosition.y}px`,
            transform: "translateX(-50%) translateY(-100%)",
            zIndex: 9999,
          }}
          onClick={handleAskSelectedText}
        >
          <span>Ask</span>
        </div>
      )}

      <Sheet
        open={isLoggedIn && isOpen}
        onOpenChange={(open) => {
          if (!open) {
            closePanel();
            // Clear initialMessage when panel closes to prevent re-sending on next open
            setInitialMessage(undefined);
            // Reset to teach mode as default
            setMode("teach");
          }
        }}
      >
        <SheetContent
          side="right"
          className="w-full sm:max-w-md md:max-w-lg p-0 flex flex-col"
          hideCloseButton
        >
          {/* Mobile close button - top left corner */}
          <SheetClose className={styles.mobileCloseButton}>
            <X className="h-5 w-5" />
            <span className="sr-only">Close</span>
          </SheetClose>

          {/* ChatKit Component - no header, full height */}
          <div className={styles.chatContainer}>
            <ChatKitWrapper
              key={`${lessonPath}-${chatKey}-${mode}`}
              lessonPath={lessonPath}
              lessonTitle={lessonTitle}
              apiBase={studyModeApiUrl}
              domainKey={chatkitDomainKey}
              mode={mode}
              initialMessage={initialMessage}
              onInitialMessageSent={() => setInitialMessage(undefined)}
              hideFirstUserMessage={hasAutoStarted && mode === "teach"}
            />
          </div>
        </SheetContent>
      </Sheet>
    </>
  );
}

export default TeachMePanel;
