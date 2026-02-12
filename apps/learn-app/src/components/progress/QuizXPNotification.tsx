import React, { useEffect, useState } from "react";
import type { BadgeEarned } from "@/lib/progress-types";
import styles from "./QuizXPNotification.module.css";

interface QuizXPNotificationProps {
  xpEarned: number;
  badges: BadgeEarned[];
  onDismiss: () => void;
}

export default function QuizXPNotification({
  xpEarned,
  badges,
  onDismiss,
}: QuizXPNotificationProps) {
  const [hiding, setHiding] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setHiding(true);
      // Wait for the slide-out animation to finish before removing
      setTimeout(onDismiss, 300);
    }, 5000);
    return () => clearTimeout(timer);
  }, [onDismiss]);

  return (
    <div className={`${styles.notification} ${hiding ? styles.hiding : ""}`}>
      <p className={styles.xpAmount}>+{xpEarned} XP</p>
      {badges.length > 0 && (
        <ul className={styles.badgeList}>
          {badges.map((b) => (
            <li key={b.id} className={styles.badge}>
              {b.name}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
