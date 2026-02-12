import React, { useState, useCallback } from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { useAuth } from "@/contexts/AuthContext";
import { useProgress } from "@/contexts/ProgressContext";
import { updatePreferences } from "@/lib/progress-api";
import type { BadgeEarned } from "@/lib/progress-types";
import "@/components/progress/gamification.css";
import styles from "./ProgressDashboard.module.css";

/** All 14 Phase-1 badge definitions (mirrors backend BADGE_DEFINITIONS). */
const ALL_BADGES: Array<{
  id: string;
  name: string;
  description: string;
  icon: string;
}> = [
  { id: "first-steps", name: "First Steps", description: "Complete your first quiz", icon: "1" },
  { id: "perfect-score", name: "Perfect Score", description: "Score 100% on any quiz", icon: "100" },
  { id: "ace", name: "Ace", description: "Score 100% on your first attempt", icon: "A+" },
  { id: "on-fire", name: "On Fire", description: "3-day learning streak", icon: "3d" },
  { id: "week-warrior", name: "Week Warrior", description: "7-day learning streak", icon: "7d" },
  { id: "dedicated", name: "Dedicated", description: "30-day learning streak", icon: "30" },
  { id: "foundations-complete", name: "Foundations Complete", description: "All quizzes in Part 1", icon: "P1" },
  { id: "workflows-complete", name: "Workflows Complete", description: "All quizzes in Part 2", icon: "P2" },
  { id: "sdd-complete", name: "SDD Complete", description: "All quizzes in Part 3", icon: "P3" },
  { id: "coding-complete", name: "Coding Complete", description: "All quizzes in Part 4", icon: "P4" },
  { id: "deployment-complete", name: "Deployment Complete", description: "All quizzes in Part 5", icon: "P5" },
  { id: "cloud-native-complete", name: "Cloud Native Complete", description: "All quizzes in Part 6", icon: "P6" },
  { id: "agent-factory-graduate", name: "Agent Factory Graduate", description: "Complete all quizzes", icon: "Grad" },
  { id: "elite", name: "Elite", description: "Reach the top 100", icon: "Top" },
];

function formatDate(iso: string): string {
  try {
    return new Intl.DateTimeFormat("en", {
      month: "short",
      day: "numeric",
      year: "numeric",
    }).format(new Date(iso));
  } catch {
    return iso;
  }
}

export default function ProgressDashboard() {
  const { session } = useAuth();
  const { progress, isLoading } = useProgress();
  const { siteConfig } = useDocusaurusContext();
  const progressApiUrl =
    (siteConfig.customFields?.progressApiUrl as string) ||
    "http://localhost:8002";

  const [showOnLeaderboard, setShowOnLeaderboard] = useState(true);
  const [togglingPref, setTogglingPref] = useState(false);

  const handleToggleLeaderboard = useCallback(async () => {
    const newValue = !showOnLeaderboard;
    setTogglingPref(true);
    try {
      await updatePreferences(progressApiUrl, {
        show_on_leaderboard: newValue,
      });
      setShowOnLeaderboard(newValue);
    } catch {
      // Non-critical
    } finally {
      setTogglingPref(false);
    }
  }, [showOnLeaderboard, progressApiUrl]);

  if (!session?.user) {
    return (
      <div className={styles.container}>
        <p className={styles.loginPrompt}>
          Sign in to view your learning progress.
        </p>
      </div>
    );
  }

  if (isLoading && !progress) {
    return (
      <div className={styles.container}>
        <p className={styles.loginPrompt}>Loading your progress...</p>
      </div>
    );
  }

  const stats = progress?.stats;
  const earnedMap = new Map<string, BadgeEarned>(
    (progress?.badges ?? []).map((b) => [b.id, b]),
  );

  return (
    <div className={styles.container}>
      <h1 className={styles.heading}>My Progress</h1>

      {/* Stat cards */}
      <div className={styles.stats}>
        <div className={styles.statCard}>
          <span className={`${styles.statValue} ${styles.xpValue}`}>
            {stats?.total_xp ?? 0}
          </span>
          <span className={styles.statLabel}>Total XP</span>
        </div>
        <div className={styles.statCard}>
          <span className={`${styles.statValue} ${styles.rankValue}`}>
            {stats?.rank ?? "--"}
          </span>
          <span className={styles.statLabel}>Rank</span>
        </div>
        <div className={styles.statCard}>
          <span className={`${styles.statValue} ${styles.streakValue}`}>
            {stats?.current_streak ?? 0}
          </span>
          <span className={styles.statLabel}>Current Streak</span>
        </div>
        <div className={styles.statCard}>
          <span className={`${styles.statValue} ${styles.perfectValue}`}>
            {stats?.perfect_scores ?? 0}
          </span>
          <span className={styles.statLabel}>Perfect Scores</span>
        </div>
      </div>

      {/* Chapter progress */}
      <div className={styles.section}>
        <h2 className={styles.sectionTitle}>Chapter Progress</h2>
        {(progress?.chapters?.length ?? 0) === 0 ? (
          <p className={styles.empty}>
            No chapter activity yet. Take a quiz to get started!
          </p>
        ) : (
          <div className={styles.chapterList}>
            {progress!.chapters.map((ch) => (
              <div key={ch.slug} className={styles.chapterCard}>
                <div className={styles.chapterInfo}>
                  <div className={styles.chapterTitle}>{ch.title || ch.slug}</div>
                  <div className={styles.chapterMeta}>
                    <span>Best: {ch.best_score}%</span>
                    <span>{ch.xp_earned} XP</span>
                    <span>{ch.attempts} attempt{ch.attempts !== 1 ? "s" : ""}</span>
                    <span>{ch.lessons_completed.length} lesson{ch.lessons_completed.length !== 1 ? "s" : ""}</span>
                  </div>
                </div>
                <div className={styles.progressBar}>
                  <div
                    className={styles.progressFill}
                    style={{ width: `${Math.min(ch.best_score, 100)}%` }}
                  />
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Badge gallery */}
      <div className={styles.section}>
        <h2 className={styles.sectionTitle}>Badges</h2>
        <div className={styles.badgeGrid}>
          {ALL_BADGES.map((def) => {
            const earned = earnedMap.get(def.id);
            return (
              <div
                key={def.id}
                className={`${styles.badgeCard} ${!earned ? styles.badgeLocked : ""}`}
              >
                <div className={styles.badgeIcon}>{def.icon}</div>
                <div className={styles.badgeName}>{def.name}</div>
                <div className={styles.badgeDesc}>{def.description}</div>
                {earned && (
                  <div className={styles.badgeDate}>
                    Earned {formatDate(earned.earned_at)}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      {/* Privacy preferences */}
      <div className={styles.section}>
        <h2 className={styles.sectionTitle}>Preferences</h2>
        <label className={styles.toggleRow}>
          <input
            type="checkbox"
            checked={showOnLeaderboard}
            onChange={handleToggleLeaderboard}
            disabled={togglingPref}
            className={styles.toggleInput}
          />
          <span className={styles.toggleLabel}>
            Show me on the leaderboard
          </span>
        </label>
      </div>
    </div>
  );
}
