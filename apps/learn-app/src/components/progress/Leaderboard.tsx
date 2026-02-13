import React, { useEffect, useState } from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Link from "@docusaurus/Link";
import { useAuth } from "@/contexts/AuthContext";
import { getLeaderboard } from "@/lib/progress-api";
import type {
  LeaderboardEntry,
  LeaderboardResponse,
} from "@/lib/progress-types";
import { BADGE_DEFINITIONS } from "@/lib/progress-types";
import { cn } from "@/lib/utils";
import { Card, CardContent } from "@/components/ui/card";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
} from "@/components/ui/dialog";
import { BadgeCard } from "@/components/progress/BadgeCard";
import {
  Zap,
  Trophy,
  Medal,
  Crown,
  Award,
  Lock,
  LogIn,
  Loader2,
} from "lucide-react";
import "@/components/progress/gamification.css";
import styles from "./Leaderboard.module.css";

/* ───────────────────── Helpers ───────────────────── */

function getInitials(name: string): string {
  return name
    .split(" ")
    .map((w) => w[0])
    .join("")
    .slice(0, 2)
    .toUpperCase();
}

function ordinal(n: number): string {
  const s = ["th", "st", "nd", "rd"];
  const v = n % 100;
  return n + (s[(v - 20) % 10] || s[v] || s[0]);
}

/* ───────────────────── Badge Modal ───────────────────── */

interface BadgeModalProps {
  isOpen: boolean;
  onClose: () => void;
  displayName: string;
  badgeIds: string[];
}

function BadgeModal({
  isOpen,
  onClose,
  displayName,
  badgeIds,
}: BadgeModalProps) {
  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="max-w-md sm:max-w-lg max-h-[80vh] overflow-y-auto">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2">
            <Award className="w-5 h-5 text-primary" />
            {displayName}&apos;s Badges
          </DialogTitle>
          <DialogDescription>
            {badgeIds.length} badge{badgeIds.length !== 1 ? "s" : ""} earned
          </DialogDescription>
        </DialogHeader>

        <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 mt-4">
          {badgeIds.map((id) => (
            <BadgeCard
              key={id}
              badgeId={id}
              isEarned={true}
              size="md"
              showDescription={true}
            />
          ))}
        </div>

        {badgeIds.length === 0 && (
          <div className="flex flex-col items-center py-8 text-muted-foreground">
            <Award className="w-12 h-12 mb-2 opacity-50" />
            <p>No badges earned yet</p>
          </div>
        )}
      </DialogContent>
    </Dialog>
  );
}

/* ───────────────────── Rank Badge ───────────────────── */

function RankBadge({ rank }: { rank: number }) {
  if (rank === 1) {
    return (
      <div className="w-7 h-7 sm:w-8 sm:h-8 flex items-center justify-center rank-badge-gold text-white font-bold text-sm allow-rounded rounded-full shrink-0">
        <Crown className="w-4 h-4 sm:w-5 sm:h-5" fill="currentColor" />
      </div>
    );
  }
  if (rank === 2) {
    return (
      <div className="w-7 h-7 sm:w-8 sm:h-8 flex items-center justify-center rank-badge-silver text-white font-bold text-sm allow-rounded rounded-full shrink-0">
        <Medal className="w-4 h-4 sm:w-5 sm:h-5" />
      </div>
    );
  }
  if (rank === 3) {
    return (
      <div className="w-7 h-7 sm:w-8 sm:h-8 flex items-center justify-center rank-badge-bronze text-white font-bold text-sm allow-rounded rounded-full shrink-0">
        <Medal className="w-4 h-4 sm:w-5 sm:h-5" />
      </div>
    );
  }
  return (
    <div className="w-7 h-7 sm:w-8 sm:h-8 flex items-center justify-center font-semibold text-muted-foreground text-xs sm:text-sm shrink-0">
      #{rank}
    </div>
  );
}

/* ───────────────────── Badge Button ───────────────────── */

function BadgeButton({
  entry,
  onBadgeClick,
}: {
  entry: LeaderboardEntry;
  onBadgeClick: (entry: LeaderboardEntry) => void;
}) {
  return (
    <button
      onClick={() => onBadgeClick(entry)}
      className={cn(
        "flex items-center gap-1 text-xs mt-1 px-2 py-0.5 rounded-full allow-rounded transition-colors",
        entry.badge_ids.length > 0
          ? "bg-amber-100 dark:bg-amber-900/30 text-amber-700 dark:text-amber-400 hover:bg-amber-200 dark:hover:bg-amber-900/50 cursor-pointer"
          : "bg-muted/50 text-muted-foreground cursor-default",
      )}
      disabled={entry.badge_ids.length === 0}
      title={entry.badge_ids.length > 0 ? "View badges" : "No badges yet"}
    >
      <Award
        className="w-3.5 h-3.5"
        fill={entry.badge_ids.length > 0 ? "currentColor" : "none"}
      />
      <span className="font-medium">{entry.badge_ids.length}</span>
    </button>
  );
}

/* ───────────────────── Top 3 Podium ───────────────────── */

function TopThreePodium({
  entries,
  currentUserId,
  onBadgeClick,
}: {
  entries: LeaderboardEntry[];
  currentUserId?: string;
  onBadgeClick: (entry: LeaderboardEntry) => void;
}) {
  const first = entries.find((e) => e.rank === 1);
  const second = entries.find((e) => e.rank === 2);
  const third = entries.find((e) => e.rank === 3);

  if (!first) return null;

  return (
    <div className="flex items-end justify-center gap-1 sm:gap-4 py-4 sm:py-8 px-2 sm:px-4 bg-gradient-to-b from-card to-background border-b border-border">
      {/* Second Place */}
      {second && (
        <div className="flex flex-col items-center min-w-0">
          <Avatar className="w-10 h-10 sm:w-16 sm:h-16 border-2 border-[oklch(0.75_0.02_260)] mb-1 sm:mb-2 allow-rounded">
            <AvatarImage src={second.avatar_url ?? undefined} />
            <AvatarFallback className="bg-[oklch(0.75_0.02_260)] text-white font-bold text-xs sm:text-base">
              {getInitials(second.display_name)}
            </AvatarFallback>
          </Avatar>
          <div className="w-16 sm:w-24 h-12 sm:h-20 flex flex-col items-center justify-center rank-badge-silver">
            <span className="text-white font-bold text-base sm:text-lg">2</span>
            <span className="text-white/80 text-[10px] sm:text-xs">
              {second.total_xp.toLocaleString()}
            </span>
          </div>
          <p className="text-xs sm:text-sm font-medium mt-1 sm:mt-2 truncate max-w-16 sm:max-w-24 text-center">
            {second.display_name}
            {second.user_id === currentUserId && (
              <span className={styles.youTag}>you</span>
            )}
          </p>
          <div className="hidden sm:block">
            <BadgeButton entry={second} onBadgeClick={onBadgeClick} />
          </div>
        </div>
      )}

      {/* First Place */}
      <div className="flex flex-col items-center -mt-2 sm:-mt-4 min-w-0">
        <Crown
          className="w-6 h-6 sm:w-8 sm:h-8 text-[oklch(0.77_0.16_70)] mb-0.5 sm:mb-1"
          fill="currentColor"
        />
        <Avatar className="w-14 h-14 sm:w-24 sm:h-24 border-2 sm:border-4 border-[oklch(0.77_0.16_70)] mb-1 sm:mb-2 allow-rounded">
          <AvatarImage src={first.avatar_url ?? undefined} />
          <AvatarFallback className="bg-[oklch(0.77_0.16_70)] text-white font-bold text-sm sm:text-xl">
            {getInitials(first.display_name)}
          </AvatarFallback>
        </Avatar>
        <div className="w-20 sm:w-28 h-14 sm:h-24 flex flex-col items-center justify-center rank-badge-gold">
          <span className="text-white font-bold text-xl sm:text-2xl">1</span>
          <span className="text-white/90 text-xs sm:text-sm">
            {first.total_xp.toLocaleString()}
          </span>
        </div>
        <p className="text-sm sm:text-base font-semibold mt-1 sm:mt-2 truncate max-w-20 sm:max-w-28 text-center">
          {first.display_name}
          {first.user_id === currentUserId && (
            <span className={styles.youTag}>you</span>
          )}
        </p>
        <div className="hidden sm:block">
          <BadgeButton entry={first} onBadgeClick={onBadgeClick} />
        </div>
      </div>

      {/* Third Place */}
      {third && (
        <div className="flex flex-col items-center min-w-0">
          <Avatar className="w-9 h-9 sm:w-14 sm:h-14 border-2 border-[oklch(0.6_0.1_50)] mb-1 sm:mb-2 allow-rounded">
            <AvatarImage src={third.avatar_url ?? undefined} />
            <AvatarFallback className="bg-[oklch(0.6_0.1_50)] text-white font-bold text-xs sm:text-base">
              {getInitials(third.display_name)}
            </AvatarFallback>
          </Avatar>
          <div className="w-14 sm:w-20 h-10 sm:h-16 flex flex-col items-center justify-center rank-badge-bronze">
            <span className="text-white font-bold text-sm sm:text-base">3</span>
            <span className="text-white/80 text-[10px] sm:text-xs">
              {third.total_xp.toLocaleString()}
            </span>
          </div>
          <p className="text-xs sm:text-sm font-medium mt-1 sm:mt-2 truncate max-w-14 sm:max-w-20 text-center">
            {third.display_name}
            {third.user_id === currentUserId && (
              <span className={styles.youTag}>you</span>
            )}
          </p>
          <div className="hidden sm:block">
            <BadgeButton entry={third} onBadgeClick={onBadgeClick} />
          </div>
        </div>
      )}
    </div>
  );
}

/* ───────────────────── Leaderboard Row ───────────────────── */

function LeaderboardRow({
  entry,
  isMe,
  animationDelay = 0,
  onBadgeClick,
}: {
  entry: LeaderboardEntry;
  isMe: boolean;
  animationDelay?: number;
  onBadgeClick: (entry: LeaderboardEntry) => void;
}) {
  const isTopThree = entry.rank <= 3;

  return (
    <div
      className={cn(
        "flex items-center gap-2 sm:gap-4 px-2 sm:px-4 py-2 sm:py-3 transition-colors",
        "hover:bg-accent/50",
        isMe && "your-rank-highlight border-l-4 border-l-primary",
        isTopThree && "bg-card",
      )}
      style={{ animationDelay: `${animationDelay}ms` }}
    >
      {/* Rank */}
      <RankBadge rank={entry.rank} />

      {/* Avatar — smaller on mobile */}
      <Avatar
        className={cn(
          "w-8 h-8 sm:w-10 sm:h-10 allow-rounded",
          isTopThree && "border-2",
          entry.rank === 1 && "border-[oklch(0.77_0.16_70)]",
          entry.rank === 2 && "border-[oklch(0.75_0.02_260)]",
          entry.rank === 3 && "border-[oklch(0.6_0.1_50)]",
        )}
      >
        <AvatarImage src={entry.avatar_url ?? undefined} />
        <AvatarFallback
          className={cn(
            "text-xs sm:text-sm font-semibold",
            isTopThree
              ? "bg-primary text-primary-foreground"
              : "bg-muted text-muted-foreground",
          )}
        >
          {getInitials(entry.display_name)}
        </AvatarFallback>
      </Avatar>

      {/* Name & Badge count */}
      <div className="flex-1 min-w-0">
        <p
          className={cn(
            "text-sm sm:text-base font-medium truncate",
            isMe ? "text-primary" : "text-foreground",
          )}
        >
          {entry.display_name}
          {isMe && (
            <span className="ml-1 sm:ml-2 text-[10px] sm:text-xs text-primary">
              (You)
            </span>
          )}
        </p>
        <button
          onClick={() => onBadgeClick(entry)}
          className={cn(
            "hidden sm:flex items-center gap-1.5 text-xs transition-colors",
            entry.badge_ids.length > 0
              ? "text-amber-600 dark:text-amber-400 hover:text-amber-700 dark:hover:text-amber-300 cursor-pointer"
              : "text-muted-foreground cursor-default",
          )}
          disabled={entry.badge_ids.length === 0}
          title={entry.badge_ids.length > 0 ? "View badges" : "No badges yet"}
        >
          <Award
            className="w-3.5 h-3.5"
            fill={entry.badge_ids.length > 0 ? "currentColor" : "none"}
          />
          <span className="font-medium">{entry.badge_ids.length}</span>
        </button>
      </div>

      {/* XP */}
      <div className="flex items-center gap-1">
        <Zap
          className={cn(
            "w-3.5 h-3.5 sm:w-4 sm:h-4",
            isTopThree
              ? "text-[oklch(0.72_0.18_142)]"
              : "text-[oklch(0.68_0.16_142)]",
          )}
          fill="currentColor"
        />
        <span
          className={cn(
            "font-semibold tabular-nums",
            isTopThree ? "text-sm sm:text-lg" : "text-xs sm:text-sm",
          )}
        >
          {entry.total_xp.toLocaleString()}
        </span>
      </div>
    </div>
  );
}

/* ───────────────────── Main ───────────────────── */

export default function Leaderboard() {
  const { siteConfig } = useDocusaurusContext();
  const progressApiUrl =
    (siteConfig.customFields?.progressApiUrl as string) ||
    "http://localhost:8002";
  const { session } = useAuth();
  const currentUserId = session?.user?.id;

  const [data, setData] = useState<LeaderboardResponse | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Badge modal
  const [badgeModalOpen, setBadgeModalOpen] = useState(false);
  const [selectedEntry, setSelectedEntry] = useState<LeaderboardEntry | null>(
    null,
  );

  const fetchLeaderboard = () => {
    setIsLoading(true);
    setError(null);
    getLeaderboard(progressApiUrl)
      .then((res) => {
        setData(res);
      })
      .catch((err) => {
        console.error("[Leaderboard] Failed to load:", err);
        setError(err.message || "Failed to load leaderboard");
      })
      .finally(() => {
        setIsLoading(false);
      });
  };

  useEffect(() => {
    fetchLeaderboard();
  }, [progressApiUrl]);

  const handleBadgeClick = (entry: LeaderboardEntry) => {
    if (entry.badge_ids.length > 0) {
      setSelectedEntry(entry);
      setBadgeModalOpen(true);
    }
  };

  /* Loading */
  if (isLoading) {
    return (
      <div className="max-w-screen-xl mx-auto px-4 py-12">
        <div className="flex flex-col items-center py-12">
          <Loader2 className="w-8 h-8 text-primary animate-spin mb-4" />
          <p className="text-muted-foreground">Loading leaderboard...</p>
        </div>
      </div>
    );
  }

  /* Error */
  if (error) {
    return (
      <div className="max-w-screen-xl mx-auto px-4 py-12">
        <Card>
          <CardContent className="flex flex-col items-center py-12">
            <Trophy className="w-12 h-12 text-muted-foreground mb-4" />
            <p className="text-muted-foreground text-center mb-4">
              Could not load leaderboard.
              <br />
              <span className="text-xs">{error}</span>
            </p>
            <Button size="sm" variant="outline" onClick={fetchLeaderboard}>
              Try Again
            </Button>
          </CardContent>
        </Card>
      </div>
    );
  }

  const entries = data?.entries ?? [];

  /* Empty */
  if (entries.length === 0) {
    return (
      <div className="max-w-screen-xl mx-auto px-4 py-12">
        <Card>
          <CardContent className="flex flex-col items-center py-12">
            <Trophy className="w-12 h-12 text-muted-foreground mb-4" />
            <p className="text-muted-foreground text-center">
              No learners on the leaderboard yet.
              <br />
              Complete quizzes to be the first!
            </p>
          </CardContent>
        </Card>
      </div>
    );
  }

  const top3 = entries.filter((e) => e.rank <= 3);
  const rest = entries.filter((e) => e.rank > 3);
  const myEntry = entries.find((e) => e.user_id === currentUserId);

  return (
    <div className="max-w-screen-xl mx-auto px-2 sm:px-4 py-4 sm:py-8">
      {/* Header */}
      <div className="flex items-center justify-between mb-4 sm:mb-6">
        <div className="flex items-center gap-2 sm:gap-3">
          <Trophy className="w-6 h-6 sm:w-8 sm:h-8 text-primary" />
          <div>
            <h1 className="text-xl sm:text-2xl font-bold text-foreground m-0">
              Leaderboard
            </h1>
            <p className="text-xs sm:text-sm text-muted-foreground m-0">
              Top {Math.min(entries.length, 100)} of {data?.total_users ?? 0}{" "}
              learners
            </p>
          </div>
        </div>
        <Button size="sm" asChild className="hidden sm:inline-flex">
          <Link to="/progress">Your Progress</Link>
        </Button>
      </div>

      <Card className="overflow-hidden">
        {/* Top 3 Podium */}
        {top3.length > 0 && (
          <TopThreePodium
            entries={top3}
            currentUserId={currentUserId}
            onBadgeClick={handleBadgeClick}
          />
        )}

        {/* Your Rank Section */}
        {!currentUserId ? (
          /* Sign-in prompt for non-logged-in users */
          <div className="border-b border-border bg-muted/20">
            <div className="flex items-center justify-between px-3 sm:px-4 py-2.5 sm:py-3">
              <span className="text-xs sm:text-sm text-muted-foreground">
                Sign in to track your rank
              </span>
              <Button size="sm" className="gap-1.5 shrink-0" asChild>
                <Link to="/">
                  <LogIn className="w-3.5 h-3.5" />
                  Sign In
                </Link>
              </Button>
            </div>
          </div>
        ) : myEntry ? (
          /* Logged-in user's rank */
          <div className="border-b border-border">
            <div className="px-3 sm:px-4 py-2 text-xs font-medium text-primary uppercase tracking-wider flex items-center gap-2">
              <Trophy className="w-3 h-3" />
              Your Rank
            </div>
            <div className="flex items-center gap-2 sm:gap-4 px-2 sm:px-4 py-2 sm:py-3 your-rank-highlight border-l-4 border-l-primary">
              <div className="w-8 h-8 flex items-center justify-center font-bold text-primary text-base sm:text-lg shrink-0">
                {myEntry.rank}
              </div>
              <Avatar className="w-8 h-8 sm:w-10 sm:h-10 allow-rounded shrink-0">
                <AvatarImage src={myEntry.avatar_url ?? undefined} />
                <AvatarFallback className="bg-primary text-primary-foreground text-xs sm:text-sm font-semibold">
                  {getInitials(myEntry.display_name)}
                </AvatarFallback>
              </Avatar>
              <div className="flex-1 min-w-0">
                <p className="text-sm sm:text-base font-medium text-primary m-0 truncate">
                  {myEntry.display_name}{" "}
                  <span className="text-[10px] sm:text-xs">(You)</span>
                </p>
                <button
                  onClick={() => handleBadgeClick(myEntry)}
                  className={cn(
                    "hidden sm:flex items-center gap-1.5 text-xs transition-colors",
                    myEntry.badge_ids.length > 0
                      ? "text-amber-600 dark:text-amber-400 hover:text-amber-700 cursor-pointer"
                      : "text-muted-foreground cursor-default",
                  )}
                  disabled={myEntry.badge_ids.length === 0}
                >
                  <Award
                    className="w-3.5 h-3.5"
                    fill={
                      myEntry.badge_ids.length > 0 ? "currentColor" : "none"
                    }
                  />
                  <span className="font-medium">
                    {myEntry.badge_ids.length} badge
                    {myEntry.badge_ids.length !== 1 ? "s" : ""}
                  </span>
                </button>
              </div>
              <div className="flex items-center gap-1">
                <Zap
                  className="w-3.5 h-3.5 sm:w-4 sm:h-4 text-[oklch(0.68_0.16_142)]"
                  fill="currentColor"
                />
                <span className="text-xs sm:text-sm font-semibold tabular-nums">
                  {myEntry.total_xp.toLocaleString()}
                </span>
              </div>
            </div>
          </div>
        ) : currentUserId ? (
          /* Logged-in but not ranked */
          <div className="border-b border-border">
            <div className="px-3 sm:px-4 py-2 text-xs font-medium text-primary uppercase tracking-wider flex items-center gap-2">
              <Trophy className="w-3 h-3" />
              Your Rank
            </div>
            <div className="flex items-center gap-2 sm:gap-4 px-3 sm:px-4 py-2 sm:py-3">
              <div className="w-8 h-8 flex items-center justify-center shrink-0">
                <span className="text-muted-foreground">—</span>
              </div>
              <div className="flex-1 min-w-0">
                <p className="text-xs sm:text-sm text-muted-foreground italic m-0">
                  Complete a quiz to join the leaderboard
                </p>
              </div>
            </div>
          </div>
        ) : null}

        {/* Leaderboard List (rank 4+) */}
        <div className="divide-y divide-border/50">
          {rest.map((entry, index) => (
            <LeaderboardRow
              key={entry.user_id}
              entry={entry}
              isMe={entry.user_id === currentUserId}
              animationDelay={index * 30}
              onBadgeClick={handleBadgeClick}
            />
          ))}
        </div>
      </Card>

      {/* Badge Modal */}
      {selectedEntry && (
        <BadgeModal
          isOpen={badgeModalOpen}
          onClose={() => setBadgeModalOpen(false)}
          displayName={selectedEntry.display_name}
          badgeIds={selectedEntry.badge_ids}
        />
      )}
    </div>
  );
}
