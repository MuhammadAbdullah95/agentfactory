/**
 * DocItem/Content Theme Swizzle (Wrap)
 *
 * Wraps the original DocItem/Content component with LessonContent
 * to provide tabbed interface for Full Lesson and AI Summary views.
 *
 * The summary is read from global data (populated by docusaurus-summaries-plugin)
 * which scans for .summary.md files at build time.
 */

import React, { useState, useEffect, useRef, useCallback } from "react";
import Content from "@theme-original/DocItem/Content";
import type ContentType from "@theme/DocItem/Content";
import type { WrapperProps } from "@docusaurus/types";
import { useDoc } from "@docusaurus/plugin-content-docs/client";
import { usePluginData } from "@docusaurus/useGlobalData";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import LessonContent from "../../../components/LessonContent";
import ReactMarkdown from "react-markdown";
import ReadingProgress from "@/components/ReadingProgress";
import DocPageActions from "@/components/DocPageActions";
import { useStudyMode } from "@/contexts/StudyModeContext";
import { useAuth } from "@/contexts/AuthContext";
import { TeachMePanel } from "@/components/TeachMePanel";
import { getOAuthAuthorizationUrl } from "@/lib/auth-client";

type Props = WrapperProps<typeof ContentType>;

/**
 * Reading Time Component - calculates from content
 */
function ReadingTime() {
  const [readingTime, setReadingTime] = useState<number | null>(null);

  useEffect(() => {
    // Calculate reading time from article content
    const article = document.querySelector("article");
    if (article) {
      const text = article.textContent || "";
      const words = text.trim().split(/\s+/).length;
      const minutes = Math.ceil(words / 200); // 200 words per minute
      setReadingTime(minutes);
    }
  }, []);

  if (!readingTime) return null;

  return (
    <div className="reading-time">
      <svg
        width="14"
        height="14"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <circle cx="12" cy="12" r="10" />
        <polyline points="12 6 12 12 16 14" />
      </svg>
      <span>{readingTime} min read</span>
    </div>
  );
}

function formatLastUpdated(timestamp: number, locale: string) {
  try {
    return new Intl.DateTimeFormat(locale, {
      year: "numeric",
      month: "short",
      day: "2-digit",
    }).format(new Date(timestamp));
  } catch {
    return new Date(timestamp).toDateString();
  }
}

function getHistoryUrl(editUrl?: string): string | null {
  if (!editUrl) return null;
  try {
    const url = new URL(editUrl);
    if (!url.hostname.includes("github.com")) return null;
    url.pathname = url.pathname.replace("/edit/", "/commits/");
    return url.toString();
  } catch {
    return null;
  }
}

/**
 * Back to Top Button Component
 * Only shows when user scrolls UP (not always visible after scrolling down)
 */
function BackToTopButton() {
  const [visible, setVisible] = useState(false);
  const lastScrollY = useRef(0);

  useEffect(() => {
    const handleScroll = () => {
      const currentScrollY = window.scrollY;

      // Show only when:
      // 1. User has scrolled down at least 400px AND
      // 2. User is scrolling UP (current position < last position)
      const isScrollingUp = currentScrollY < lastScrollY.current;
      const hasScrolledEnough = currentScrollY > 400;

      setVisible(isScrollingUp && hasScrolledEnough);
      lastScrollY.current = currentScrollY;
    };

    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  if (!visible) return null;

  return (
    <button
      onClick={scrollToTop}
      className="back-to-top-button"
      title="Back to top"
      aria-label="Scroll back to top"
    >
      <svg
        width="20"
        height="20"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <path d="M18 15l-6-6-6 6" />
      </svg>
    </button>
  );
}

interface SummariesPluginData {
  summaries: Record<string, string>;
}

/**
 * Teach Me Floating Button - visible to all users
 * Redirects to login if not authenticated, opens panel if authenticated
 */
function TeachMeFloatingButton({
  isLoggedIn,
  openPanel,
  handleLoginRedirect,
}: {
  isLoggedIn: boolean;
  openPanel: () => void;
  handleLoginRedirect: () => void;
}) {
  return (
    <button
      onClick={isLoggedIn ? openPanel : handleLoginRedirect}
      className="study-mode-float"
      title={isLoggedIn ? "Teach Me" : "Sign in for Teach Me"}
      aria-label={isLoggedIn ? "Open Teach Me" : "Sign in for Teach Me Access"}
    >
      <svg
        width="20"
        height="20"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" />
        <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" />
      </svg>
    </button>
  );
}

/**
 * Ask Floating Button - opens panel directly in ask mode
 * Redirects to login if not authenticated
 */
function AskFloatingButton({
  isLoggedIn,
  openPanelInAskMode,
  handleLoginRedirect,
}: {
  isLoggedIn: boolean;
  openPanelInAskMode: () => void;
  handleLoginRedirect: () => void;
}) {
  return (
    <button
      onClick={isLoggedIn ? openPanelInAskMode : handleLoginRedirect}
      className="ask-mode-float"
      title={isLoggedIn ? "Ask a Question" : "Sign in to ask questions"}
      aria-label={isLoggedIn ? "Open Ask Mode" : "Sign in for Ask Mode Access"}
    >
      <svg
        width="20"
        height="20"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <circle cx="12" cy="12" r="10" />
        <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" />
        <line x1="12" y1="17" x2="12.01" y2="17" />
      </svg>
    </button>
  );
}

export default function ContentWrapper(props: Props): React.ReactElement {
  const doc = useDoc();

  // Persist zen mode in localStorage
  const [zenMode, setZenMode] = React.useState(() => {
    if (typeof window !== "undefined") {
      return localStorage.getItem("zenMode") === "true";
    }
    return false;
  });

  React.useEffect(() => {
    if (zenMode) {
      document.body.classList.add("zen-mode");
      localStorage.setItem("zenMode", "true");
    } else {
      document.body.classList.remove("zen-mode");
      localStorage.setItem("zenMode", "false");
    }
  }, [zenMode]);

  // Apply zen mode on mount (for SSR hydration)
  React.useEffect(() => {
    if (localStorage.getItem("zenMode") === "true") {
      document.body.classList.add("zen-mode");
    }
  }, []);

  // Get summaries from global data (populated by docusaurus-summaries-plugin)
  let summaries: Record<string, string> = {};
  try {
    const pluginData = usePluginData("docusaurus-summaries-plugin") as
      | SummariesPluginData
      | undefined;
    summaries = pluginData?.summaries || {};
  } catch {
    // Plugin might not be loaded yet or doesn't exist
    summaries = {};
  }

  // Get the doc's source path to look up its summary
  // The sourceDirName is like "01-Introducing-AI-Driven-Development/01-ai-development-revolution"
  // The slug is the doc ID
  // The summary key is stored as relative path without .summary.md
  // e.g., "01-Introducing-AI-Driven-Development/01-ai-development-revolution/08-traditional-cs-education-gaps"

  // Build the lookup key from doc metadata
  const metadata = doc.metadata;
  const sourceDirName = metadata.sourceDirName || "";
  const slug = metadata.slug || "";

  // The source path in doc metadata points to the markdown file
  // We need to construct the summary lookup key
  // Doc ID format example: "01-Introducing-AI-Driven-Development/01-ai-development-revolution/08-traditional-cs-education-gaps"
  const docId = metadata.id;

  // Debug log in development
  if (typeof window !== "undefined" && process.env.NODE_ENV === "development") {
    console.log("[DocItem/Content] Doc ID:", docId);
    console.log("[DocItem/Content] Source dir:", sourceDirName);
    console.log("[DocItem/Content] Slug:", slug);
    console.log(
      "[DocItem/Content] Available summaries:",
      Object.keys(summaries),
    );
  }

  // Look up summary by doc ID (the key format matches how plugin stores them)
  const summary = summaries[docId];

  // Get lesson path for TeachMePanel
  // Use metadata.source for the actual file path with numeric prefixes
  // Format: @site/docs/01-Part/02-Chapter/03-lesson.md -> 01-Part/02-Chapter/03-lesson
  const rawSource = (metadata as { source?: string }).source || "";
  const lessonPath = rawSource
    .replace(/^@site\/docs\//, "")
    .replace(/\.(md|mdx)$/, "");

  // Study mode controls
  const { isOpen: isStudyModeOpen, openPanel, setMode } = useStudyMode();

  // Callback to open panel in ask mode
  const openPanelInAskMode = React.useCallback(() => {
    setMode("ask");
    openPanel();
  }, [setMode, openPanel]);
  const { session } = useAuth();
  const isLoggedIn = !!session?.user;

  // Auth config for login redirect
  const { siteConfig } = useDocusaurusContext();
  const authUrl = siteConfig.customFields?.authUrl as string | undefined;
  const oauthClientId = siteConfig.customFields?.oauthClientId as
    | string
    | undefined;
  const locale = siteConfig.i18n?.currentLocale || "en";

  const lastUpdatedAt = metadata.lastUpdatedAt;
  const editUrl = metadata.editUrl;
  const historyUrl = getHistoryUrl(editUrl);
  // Only show real git dates, not simulated dev dates (year 2018 is Docusaurus's fake date)
  const isRealDate =
    lastUpdatedAt && new Date(lastUpdatedAt).getFullYear() > 2020;
  const showUpdateMeta = Boolean(isRealDate || historyUrl);

  /**
   * Redirect to login page with return URL (for non-logged-in users)
   */
  const handleLoginRedirect = useCallback(async () => {
    try {
      const returnUrl = window.location.href;
      localStorage.setItem("auth_return_url", returnUrl);
      const loginUrl = await getOAuthAuthorizationUrl(undefined, {
        authUrl,
        clientId: oauthClientId,
      });
      window.location.href = loginUrl;
    } catch (err) {
      console.error("Failed to redirect to login:", err);
    }
  }, [authUrl, oauthClientId]);

  // Determine if this is a content page vs category landing page
  // - Lessons have 3+ path segments: part/chapter/lesson
  // - Special root pages (thesis, preface) have 1 segment but ARE content pages
  // - Parts have 1 segment (category landing - no panel)
  // - Chapters have 2 segments (category landing - no panel)
  const pathSegments = docId.split("/").filter(Boolean);
  const specialRootPages = ["thesis", "preface"];
  const isSpecialRootPage =
    pathSegments.length === 1 && specialRootPages.includes(pathSegments[0]);
  const isLeafPage = pathSegments.length >= 3 || isSpecialRootPage;

  // If no summary, just render original content
  if (!summary) {
    return (
      <>
        <ReadingProgress />
        <div className="doc-content-header">
          <ReadingTime />
          <DocPageActions />
        </div>
        {showUpdateMeta && (
          <div className="doc-update-meta">
            {isRealDate && (
              <div className="doc-update-meta__item">
                Updated {formatLastUpdated(lastUpdatedAt, locale)}
              </div>
            )}
            {historyUrl && (
              <div className="doc-update-meta__links">
                <a
                  href={historyUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Version history
                </a>
              </div>
            )}
          </div>
        )}
        {/* Floating action buttons - hidden when study mode panel is open */}
        {!isStudyModeOpen && (
          <div className="floating-actions">
            <BackToTopButton />
            <TeachMeFloatingButton
              isLoggedIn={isLoggedIn}
              openPanel={openPanel}
              handleLoginRedirect={handleLoginRedirect}
            />
            <AskFloatingButton
              isLoggedIn={isLoggedIn}
              openPanelInAskMode={openPanelInAskMode}
              handleLoginRedirect={handleLoginRedirect}
            />
            <button
              onClick={() => setZenMode(!zenMode)}
              className="zen-mode-toggle"
              title={zenMode ? "Exit Focus Mode" : "Focus Mode"}
              aria-label={zenMode ? "Exit Focus Mode" : "Enter Focus Mode"}
            >
              {zenMode ? (
                // Exit: Grid/sidebar icon
                <svg
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <rect x="3" y="3" width="7" height="7"></rect>
                  <rect x="14" y="3" width="7" height="7"></rect>
                  <rect x="14" y="14" width="7" height="7"></rect>
                  <rect x="3" y="14" width="7" height="7"></rect>
                </svg>
              ) : (
                // Enter: Focus/center icon
                <svg
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <circle cx="12" cy="12" r="3"></circle>
                  <path d="M3 12h4m10 0h4M12 3v4m0 10v4"></path>
                </svg>
              )}
            </button>
          </div>
        )}
        <Content {...props} />
        {<TeachMePanel lessonPath={lessonPath} />}
      </>
    );
  }

  // Render summary as markdown
  // Calculate reading time
  // Assuming 200 words per minute
  // We need to get the text content. Since we don't have direct access to the raw markdown here easily without parsing,
  // we can use a rough estimate based on the rendered content or just skip it if it's too complex to get right now.
  // Actually, Docusaurus usually provides reading time in metadata if configured, but let's check.
  // doc.metadata.readingTime is available if the readingTime option is enabled in preset.
  // Let's check if we can access it.

  // For now, let's just use the progress bar and zoom as the main features.
  // If we want reading time, we should enable it in docusaurus.config.ts first.

  const summaryElement = <ReactMarkdown>{summary}</ReactMarkdown>;

  return (
    <>
      <ReadingProgress />
      <div className="doc-content-header">
        <ReadingTime />
        <DocPageActions />
      </div>
      {showUpdateMeta && (
        <div className="doc-update-meta">
          {isRealDate && (
            <div className="doc-update-meta__item">
              Updated {formatLastUpdated(lastUpdatedAt, locale)}
            </div>
          )}
          {historyUrl && (
            <div className="doc-update-meta__links">
              <a href={historyUrl} target="_blank" rel="noopener noreferrer">
                Version history
              </a>
            </div>
          )}
        </div>
      )}
      {/* Floating action buttons - hidden when study mode panel is open */}
      {!isStudyModeOpen && (
        <div className="floating-actions">
          <BackToTopButton />
          <TeachMeFloatingButton
            isLoggedIn={isLoggedIn}
            openPanel={openPanel}
            handleLoginRedirect={handleLoginRedirect}
          />
          <AskFloatingButton
            isLoggedIn={isLoggedIn}
            openPanelInAskMode={openPanelInAskMode}
            handleLoginRedirect={handleLoginRedirect}
          />
          <button
            onClick={() => setZenMode(!zenMode)}
            className="zen-mode-toggle"
            title={zenMode ? "Exit Focus Mode" : "Focus Mode"}
            aria-label={zenMode ? "Exit Focus Mode" : "Enter Focus Mode"}
          >
            {zenMode ? (
              // Exit: Grid/sidebar icon
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <rect x="3" y="3" width="7" height="7"></rect>
                <rect x="14" y="3" width="7" height="7"></rect>
                <rect x="14" y="14" width="7" height="7"></rect>
                <rect x="3" y="14" width="7" height="7"></rect>
              </svg>
            ) : (
              // Enter: Focus/center icon
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <circle cx="12" cy="12" r="3"></circle>
                <path d="M3 12h4m10 0h4M12 3v4m0 10v4"></path>
              </svg>
            )}
          </button>
        </div>
      )}
      <LessonContent summaryElement={summaryElement}>
        <Content {...props} />
        {/* TODO: ASK ME ENALBE AFTER BACKEND DEP */}
      </LessonContent>
      {<TeachMePanel lessonPath={lessonPath} />}
    </>
  );
}
