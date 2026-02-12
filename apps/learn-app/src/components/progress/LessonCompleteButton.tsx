import React, { useState, useCallback } from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { useLessonTimer } from "@/hooks/useLessonTimer";
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

  const activeSeconds = useLessonTimer();
  const [completed, setCompleted] = useState(false);
  const [submitting, setSubmitting] = useState(false);

  const handleComplete = useCallback(async () => {
    if (completed || submitting) return;
    setSubmitting(true);
    try {
      await completeLesson(progressApiUrl, {
        chapter_slug: chapterSlug,
        lesson_slug: lessonSlug,
        active_duration_secs: activeSeconds,
      });
      setCompleted(true);
    } catch {
      // Progress is an enhancement — never break the lesson experience
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
