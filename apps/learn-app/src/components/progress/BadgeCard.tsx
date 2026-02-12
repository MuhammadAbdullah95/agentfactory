import React from "react";
import styles from "./BadgeCard.module.css";

interface BadgeCardProps {
  name: string;
  icon: string;
  earnedAt?: string;
}

function formatDate(iso: string): string {
  try {
    return new Intl.DateTimeFormat("en", {
      month: "short",
      day: "numeric",
    }).format(new Date(iso));
  } catch {
    return "";
  }
}

export default function BadgeCard({ name, icon, earnedAt }: BadgeCardProps) {
  const earned = !!earnedAt;

  return (
    <div className={`${styles.card} ${!earned ? styles.locked : ""}`}>
      <div className={styles.icon}>{icon}</div>
      <div className={styles.name}>{name}</div>
      {earned && <div className={styles.date}>{formatDate(earnedAt)}</div>}
    </div>
  );
}
