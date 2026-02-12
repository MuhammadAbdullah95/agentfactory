import React, { useEffect, useState } from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { useAuth } from "@/contexts/AuthContext";
import { getLeaderboard } from "@/lib/progress-api";
import type {
  LeaderboardEntry,
  LeaderboardResponse,
} from "@/lib/progress-types";
import "@/components/progress/gamification.css";
import styles from "./Leaderboard.module.css";

function rankClass(rank: number): string {
  if (rank === 1) return styles.gold;
  if (rank === 2) return styles.silver;
  if (rank === 3) return styles.bronze;
  return "";
}

function initials(name: string): string {
  return name
    .split(" ")
    .map((w) => w[0])
    .join("")
    .slice(0, 2)
    .toUpperCase();
}

export default function Leaderboard() {
  const { siteConfig } = useDocusaurusContext();
  const progressApiUrl =
    (siteConfig.customFields?.progressApiUrl as string) ||
    "http://localhost:8002";
  const { session } = useAuth();
  const currentUserId = session?.user?.id;

  const [entries, setEntries] = useState<LeaderboardEntry[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    let cancelled = false;
    setIsLoading(true);
    getLeaderboard(progressApiUrl)
      .then((data) => {
        if (!cancelled) setEntries(data.entries);
      })
      .catch(() => {
        // Non-critical
      })
      .finally(() => {
        if (!cancelled) setIsLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [progressApiUrl]);

  if (isLoading) {
    return (
      <div className={styles.container}>
        <h1 className={styles.heading}>Leaderboard</h1>
        <p className={styles.loading}>Loading leaderboard...</p>
      </div>
    );
  }

  if (entries.length === 0) {
    return (
      <div className={styles.container}>
        <h1 className={styles.heading}>Leaderboard</h1>
        <p className={styles.empty}>
          No one on the leaderboard yet. Be the first to earn XP!
        </p>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <h1 className={styles.heading}>Leaderboard</h1>
      <table className={styles.table}>
        <thead>
          <tr>
            <th>Rank</th>
            <th>Learner</th>
            <th>XP</th>
            <th>Badges</th>
          </tr>
        </thead>
        <tbody>
          {entries.map((entry) => {
            const isMe = entry.user_id === currentUserId;
            return (
              <tr
                key={entry.user_id}
                className={`${styles.row} ${isMe ? styles.currentUser : ""}`}
              >
                <td className={`${styles.rankCell} ${rankClass(entry.rank)}`}>
                  {entry.rank}
                </td>
                <td>
                  <div className={styles.nameCell}>
                    {entry.avatar_url ? (
                      <img
                        src={entry.avatar_url}
                        alt=""
                        className={styles.avatar}
                      />
                    ) : (
                      <div className={styles.avatarPlaceholder}>
                        {initials(entry.display_name)}
                      </div>
                    )}
                    <span>
                      {entry.display_name}
                      {isMe ? " (you)" : ""}
                    </span>
                  </div>
                </td>
                <td className={styles.xpCell}>{entry.total_xp}</td>
                <td className={styles.badgeCount}>{entry.badge_count}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
