export interface QuizSubmitRequest {
  chapter_slug: string;
  score_pct: number;
  questions_correct: number;
  questions_total: number;
  duration_secs?: number;
}

export interface BadgeEarned {
  id: string;
  name: string;
  earned_at: string;
}

export interface StreakInfo {
  current: number;
  longest: number;
}

export interface QuizSubmitResponse {
  xp_earned: number;
  total_xp: number;
  attempt_number: number;
  best_score: number;
  new_badges: BadgeEarned[];
  streak: StreakInfo;
}

export interface LessonCompleteRequest {
  chapter_slug: string;
  lesson_slug: string;
  active_duration_secs?: number;
}

export interface LessonCompleteResponse {
  completed: boolean;
  active_duration_secs: number;
  streak: StreakInfo;
  already_completed: boolean;
}

export interface ProgressResponse {
  user: { display_name: string; avatar_url: string | null };
  stats: {
    total_xp: number;
    rank: number | null;
    current_streak: number;
    longest_streak: number;
    quizzes_completed: number;
    perfect_scores: number;
    lessons_completed: number;
    badge_count: number;
  };
  badges: BadgeEarned[];
  chapters: Array<{
    slug: string;
    title: string;
    best_score: number;
    attempts: number;
    xp_earned: number;
    lessons_completed: Array<{
      lesson_slug: string;
      active_duration_secs: number;
      completed_at: string;
    }>;
  }>;
}

export interface LeaderboardEntry {
  rank: number;
  user_id: string;
  display_name: string;
  avatar_url: string | null;
  total_xp: number;
  badge_count: number;
}

export interface LeaderboardResponse {
  entries: LeaderboardEntry[];
  current_user_rank: number | null;
  total_users: number;
}
