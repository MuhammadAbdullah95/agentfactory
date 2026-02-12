import React, { useState, useCallback } from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Quiz, { QuizProps } from "@/components/quiz/Quiz";
import ContentGate from "@/components/ContentGate";
import QuizXPNotification from "@/components/progress/QuizXPNotification";
import { submitQuizScore } from "@/lib/progress-api";
import { useProgress } from "@/contexts/ProgressContext";
import type { QuizSubmitResponse } from "@/lib/progress-types";

interface GatedQuizProps extends QuizProps {
  /** Override the default gate title */
  gateTitle?: string;
  /** Override the default gate description */
  gateDescription?: string;
}

/**
 * GatedQuiz - A Quiz component wrapped with authentication gate
 *
 * Users must be signed in to access the quiz.
 * When not authenticated, shows a preview with sign-in prompt.
 * On completion, submits score to the progress API and shows XP notification.
 */
export function GatedQuiz({
  gateTitle,
  gateDescription,
  ...quizProps
}: GatedQuizProps) {
  const { siteConfig } = useDocusaurusContext();
  const progressApiUrl =
    (siteConfig.customFields?.progressApiUrl as string) ||
    "http://localhost:8002";

  const { refreshProgress } = useProgress();
  const [xpData, setXpData] = useState<QuizSubmitResponse | null>(null);

  const handleComplete = useCallback(
    async (result: {
      score_pct: number;
      questions_correct: number;
      questions_total: number;
    }) => {
      try {
        const pathSegments = window.location.pathname.split("/");
        const docsIndex = pathSegments.indexOf("docs");
        const chapterSlug =
          docsIndex >= 0
            ? pathSegments.slice(docsIndex + 1, -1).join("/")
            : window.location.pathname;

        const response = await submitQuizScore(progressApiUrl, {
          chapter_slug: chapterSlug,
          score_pct: result.score_pct,
          questions_correct: result.questions_correct,
          questions_total: result.questions_total,
        });
        setXpData(response);
        refreshProgress();
      } catch {
        // Progress is an enhancement — never break the quiz experience
      }
    },
    [progressApiUrl, refreshProgress],
  );

  return (
    <>
      <ContentGate
        type="quiz"
        title={gateTitle}
        description={gateDescription}
      >
        <Quiz {...quizProps} onComplete={handleComplete} />
      </ContentGate>
      {xpData && (
        <QuizXPNotification
          xpEarned={xpData.xp_earned}
          badges={xpData.new_badges}
          onDismiss={() => setXpData(null)}
        />
      )}
    </>
  );
}

export default GatedQuiz;
