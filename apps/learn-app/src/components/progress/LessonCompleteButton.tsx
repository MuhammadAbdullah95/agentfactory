import React, { useState, useCallback } from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { useLessonTimer } from "@/hooks/useLessonTimer";
import { useProgress } from "@/contexts/ProgressContext";
import { completeLesson } from "@/lib/progress-api";
import styles from "./LessonCompleteButton.module.css";

interface LessonCompleteButtonProps {
  chapterSlug: string;
  lessonSlug: string;
}

function formatTime(seconds: number): string {
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return `${m}:${s.toString().padStart(2, "0")}`;
}

export default function LessonCompleteButton({
  chapterSlug,
  lessonSlug,
}: LessonCompleteButtonProps) {
  const { siteConfig } = useDocusaurusContext();
  const progressApiUrl =
    (siteConfig.customFields?.progressApiUrl as string) ||
    "http://localhost:8002";

  const { isLessonCompleted, refreshProgress } = useProgress();
  const alreadyCompleted = isLessonCompleted(chapterSlug, lessonSlug);

  const activeSeconds = useLessonTimer();
  const [justCompleted, setJustCompleted] = useState(false);
  const [submitting, setSubmitting] = useState(false);

  const completed = alreadyCompleted || justCompleted;

  const handleComplete = useCallback(async () => {
    if (completed || submitting) return;
    setSubmitting(true);
    try {
      await completeLesson(progressApiUrl, {
        chapter_slug: chapterSlug,
        lesson_slug: lessonSlug,
        active_duration_secs: activeSeconds,
      });
      setJustCompleted(true);
      // Refresh progress context so dashboard and other components update
      refreshProgress();
    } catch {
      // Progress is an enhancement -- never break the lesson experience
    } finally {
      setSubmitting(false);
    }
  }, [
    completed,
    submitting,
    progressApiUrl,
    chapterSlug,
    lessonSlug,
    activeSeconds,
    refreshProgress,
  ]);

  return (
    <div className={styles.container}>
      <button
        className={`${styles.button} ${completed ? styles.completed : ""}`}
        onClick={handleComplete}
        disabled={completed || submitting}
      >
        {completed ? "Completed" : submitting ? "Saving..." : "Mark as Complete"}
      </button>
      <span className={styles.timer}>
        Active time: {formatTime(activeSeconds)}
      </span>
    </div>
  );
}
