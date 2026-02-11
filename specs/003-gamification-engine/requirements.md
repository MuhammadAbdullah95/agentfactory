# 003 — Gamification Engine: Business Requirements

> **Status**: Draft — Defining business requirements
> **Origin**: Strategic prioritization session (Feb 2026)
> **Key Insight**: The 6 interactive teaching modes are the _data generators_. Gamification is the _data surfacer_. They are one system.

---

## 1. Problem Statement

Agent Factory has a **complete teaching platform** — SSO, content, AI tutoring (Teach/Ask), quizzes, personalization — but **no feedback loop** telling learners how they're progressing. Quiz scores vanish on page refresh. Study sessions leave no trace. There's no reason to come back tomorrow.

**The gap**: Rich interaction data is generated every session but never surfaces back to the learner.

## 2. The Unified Engine Model

The user's framing — and the core architectural insight:

```
┌─────────────────────────────────────────────────────────┐
│                    LEARNER SURFACE                       │
│   XP Counter │ Badges │ Streaks │ Progress │ Leaderboard │
└──────────────────────────┬──────────────────────────────┘
                           │ surfaces
┌──────────────────────────▼──────────────────────────────┐
│                  PROGRESS STORE                          │
│   quiz_attempts │ user_progress │ user_badges            │
│   study_sessions │ mastery_signals │ streaks              │
└──────────────────────────┬──────────────────────────────┘
                           │ aggregates
┌──────────────────────────▼──────────────────────────────┐
│               INTERACTIVE MODE ENGINE                    │
│                                                          │
│  LIVE TODAY:          FUTURE MODES:                       │
│  ├── Teach Mode       ├── Socratic Mode (pilot 3-6mo)   │
│  ├── Ask Mode         ├── Coach Mode                     │
│  └── Quiz Mode        ├── Mentor Mode                    │
│                       ├── Simulator Mode                 │
│                       └── Manager Mode                   │
│                                                          │
│  Each mode produces mastery signals:                     │
│  conversations, scores, highlights, completions          │
└─────────────────────────────────────────────────────────┘
```

**This is NOT "build gamification, then build interactive modes."**
It's: **every mode that comes online automatically feeds the engagement surface.**

---

## 3. Current State Inventory

### What's Live and Producing Data

| Component                   | Status      | Data Produced                                                | Persisted?                   |
| --------------------------- | ----------- | ------------------------------------------------------------ | ---------------------------- |
| **Teach Mode** (GPT-5-nano) | Live        | Conversation threads, message count, timestamps, lesson path | Yes (PostgreSQL via ChatKit) |
| **Ask Mode** (DeepSeek)     | Live        | Highlighted text, question type, lesson context              | Yes (PostgreSQL via ChatKit) |
| **Quiz UI**                 | Live        | Score %, per-question results, explanations                  | **No** (React state only)    |
| **Personalization**         | Live (3/mo) | Generated content, interest tag, grade level                 | Yes (R2 + DB)                |
| **Token Metering**          | Live        | Token usage per request, model, cost                         | Yes (token-metering-api)     |
| **GA4 Analytics**           | Live        | Scroll depth, time on page, quiz events                      | Yes (Google Analytics)       |
| **Reading Progress**        | Live        | Scroll % indicator                                           | **No** (visual only)         |

### What Was Built Then Removed (PR #680 history)

The learn-app branch previously contained full gamification UI:

- `ProgressContext.tsx`, `ProgressDashboard.tsx`, `XPCounter.tsx`
- `BadgeCard.tsx`, `BadgeUnlockModal.tsx`, `Leaderboard.tsx`
- `progress-api.ts`, `progress-types.ts`
- Pages: `/progress`, `/leaderboard`

**All removed from current branch.** The TypeScript types and design documents remain in PR #680.

### What's Designed But Not Built

| Component                         | Source               | Readiness            |
| --------------------------------- | -------------------- | -------------------- |
| XP formula (diminishing returns)  | PR #680 PRD          | Ready to implement   |
| 14 badge definitions              | PR #680 types        | Ready to implement   |
| Content-addressed progress schema | PR #680 decision doc | Ready, needs review  |
| Progress API endpoints (5)        | PR #680 PRD          | Spec'd, not coded    |
| Backend service (`progress-api`)  | PR #680 PRD          | Architecture defined |

---

## 4. Business Requirements

### BR-1: Quiz Score Persistence

**Requirement**: When a learner completes a quiz, the score MUST be persisted to a backend store and associated with their user account.

**Rationale**: This is the prerequisite for everything else. Without persisted scores, XP, badges, progress, and leaderboards are impossible.

**Acceptance Criteria**:

- Quiz score survives page refresh
- Score includes: user_id, chapter_id, score_percentage, attempt_number, timestamp
- Multiple attempts tracked with diminishing XP returns (PR #680 formula)
- Best score per chapter is queryable

**Data Source**: Quiz component (`Quiz.tsx`) already calculates scores — needs API call on submit.

---

### BR-2: XP System with Diminishing Returns

**Requirement**: Each quiz submission earns XP using a fair formula that rewards first attempts and diminishing returns on reattempts.

**Rationale**: Prevents XP farming while still rewarding improvement. Creates meaningful differentiation on leaderboard.

**Formula** (from PR #680, validated):

```
Attempt 1: XP = score_percentage (e.g., 85% → 85 XP)
Attempt 2: XP = improvement × 0.5
Attempt 3: XP = improvement × 0.25
Attempt 4+: XP = improvement × 0.10
No improvement = 0 XP
```

**Acceptance Criteria**:

- 100 XP base per quiz, scaled by percentage
- Improvement-only XP on reattempts (never exceeds first-attempt potential)
- XP is immutable once earned (never removed, even if curriculum changes)

---

### BR-3: Streak Tracking

**Requirement**: Track consecutive days of learning activity to encourage daily engagement.

**Rationale**: Streaks are the highest-ROI gamification mechanic. Duolingo's entire retention model is built on streaks.

**What Counts as Activity** (must define):

- Completing a quiz (any score)
- Completing a Teach mode session (minimum N turns?)
- Using Ask mode on a lesson?
- Reading a lesson to 100% scroll depth?

**Open Question**: What's the minimum bar for "active day"? Too low = meaningless. Too high = punishing.

**Acceptance Criteria**:

- Current streak (consecutive days) tracked
- Longest streak (all-time) tracked
- Streak badges at 3, 7, 30 days
- Grace period? (e.g., miss one day, streak preserved if resumed next day)

---

### BR-4: Badge System

**Requirement**: Award achievement badges for meaningful learning milestones.

**Rationale**: Badges mark mastery moments. They're the "yearbook" of a learner's journey. They provide collection motivation beyond XP.

**14 Badges Defined** (from PR #680):

| Category        | Badges                           | Trigger                    |
| --------------- | -------------------------------- | -------------------------- |
| Milestone       | First Steps                      | First quiz completed       |
| Achievement     | Perfect Score                    | 100% on any quiz           |
| Achievement     | Ace                              | 100% on first attempt      |
| Streak          | On Fire, Week Warrior, Dedicated | 3, 7, 30-day streaks       |
| Part Completion | Foundations through Cloud Native | All quizzes in Part 1-6    |
| Capstone        | Agent Factory Graduate           | All quizzes in entire book |
| Ranking         | Elite                            | Top 100 on leaderboard     |

**Acceptance Criteria**:

- Badges awarded atomically with quiz submission (returned in response)
- Badge unlock notification shown to user
- Badge gallery viewable on profile/dashboard
- Badges never revoked

**Future Extension**: As new modes come online, new badge categories emerge:

- "Socratic Scholar" — complete 10 Socratic sessions
- "Quick Learner" — master a concept in <5 Teach turns
- "Deep Diver" — use Ask mode 50+ times across lessons

---

### BR-5: Progress Dashboard

**Requirement**: A dedicated page showing the learner's journey across the entire book.

**Rationale**: Progress visibility is the core motivation loop. Learners need to see how far they've come and what's ahead.

**Dashboard Sections**:

1. **Stat Cards**: Total XP, Global Rank, Current Streak, Perfect Scores
2. **Chapter Progress**: Per-chapter best score, XP earned, attempt count, visual progress bar
3. **Badge Gallery**: Earned badges with dates, locked badges shown as targets
4. **Activity History**: Recent quiz completions, study sessions

**Acceptance Criteria**:

- Page loads in <2s (denormalized summary table)
- Shows progress against ACTIVE curriculum (soft-deleted chapters excluded from %)
- XP animation when dashboard loads after earning new XP
- Mobile responsive

---

### BR-6: Leaderboard

**Requirement**: Global leaderboard ranking learners by total XP.

**Rationale**: Social comparison drives engagement. Seeing yourself climb motivates continued effort. Creates community around the book.

**Design**:

- Top 100 displayed
- Current user's rank always shown (even if not in top 100)
- Display: rank, name, avatar, XP, badge count
- Top 3 get special styling

**Acceptance Criteria**:

- Leaderboard updates within 1 hour of quiz submission (materialized view)
- Privacy: users can opt out of leaderboard (display "Anonymous Learner")
- No personal information leaked (just display name + avatar)

---

### BR-7: Content-Addressed Progress Architecture

**Requirement**: Progress tracking must survive curriculum changes (lessons added, removed, reordered).

**Rationale**: The book is actively evolving. Chapters get added, restructured, archived. Earned progress must never be lost.

**Design Principles** (from PR #680 decision doc):

1. **Separate content catalog from progress** — Parts/chapters table vs. user_progress table
2. **Soft deletes only** — `archived_at` timestamp, never hard delete
3. **Completion % against active chapters** — Archived chapters don't count toward "% complete"
4. **XP is immutable** — Once earned, XP persists even if source chapter is archived
5. **UUID references** — Progress links to chapter UUID, not slug (survives renames)

**Acceptance Criteria**:

- Adding a chapter: new chapter appears at 0%, total possible increases
- Removing a chapter: soft delete, earned XP preserved, completion % recalculated
- Moving a chapter: progress follows (linked by UUID)

---

### BR-8: Study Session Tracking (Engine Foundation)

**Requirement**: Track learning sessions across ALL interactive modes, not just quizzes.

**Rationale**: This is the **engine requirement** — what makes gamification a unified system rather than just "quiz scores + badges." Every mode produces mastery evidence. The system must capture it.

**Session Signals by Mode**:

| Mode      | Signal                         | Mastery Evidence                              |
| --------- | ------------------------------ | --------------------------------------------- |
| **Teach** | Thread completion (N turns)    | Engaged with material, correctness trajectory |
| **Teach** | Restatement quality            | Deep comprehension (student explains back)    |
| **Ask**   | Highlight frequency per lesson | Comprehension gaps identified                 |
| **Ask**   | Question type distribution     | Surface vs. deep understanding                |
| **Quiz**  | Score + attempt count          | Direct mastery measurement                    |
| **Quiz**  | Per-question performance       | Concept-level strengths/weaknesses            |

**MVP Scope**: Quiz persistence is the MVP. Teach/Ask session tracking is Phase 2. But the schema and API must be designed to accommodate all modes from day one.

**Acceptance Criteria**:

- `study_sessions` table captures: user_id, lesson_path, mode (teach/ask/quiz), started_at, completed_at, metadata (JSONB)
- Quiz submissions are a specific type of study session
- Teach mode threads can be linked to study sessions (thread_id reference)
- Schema extensible for future modes without migration

---

## 5. Mode-to-Gamification Signal Map

This is the **engine specification** — how each interactive mode feeds the gamification surface.

### Phase 1: Quiz-Only (MVP)

```
Quiz Score → XP Calculation → User Progress → Dashboard
                            → Badge Check → Badge Award
                            → Streak Update → Streak Badge Check
                            → Leaderboard Update
```

**Data flow**: `Quiz.tsx` → `POST /api/v1/quiz/submit` → XP + badges in response → ProgressContext update → UI animation

### Phase 2: Teach + Ask Integration

```
Teach Session Complete → Study Session Record → Activity Day (streak)
                                              → "Study Bug" badge (10 sessions)
                                              → "Deep Thinker" badge (50+ turns total)

Ask Mode Usage → Study Session Record → Activity Day (streak)
                                      → Content quality signal (lessons with high Ask usage)
```

**New signals**: Session count, total conversation turns, highlight density per lesson

### Phase 3: New Modes Online

```
Socratic Mode → Mastery Score (evaluated by grader) → XP
             → "Socratic Scholar" badge

Coach Mode → Practice Problem Score → XP
           → "Problem Solver" badge

Mentor Mode → Project Milestone → XP
            → "Builder" badge
```

**Key design principle**: The XP formula and badge system must be **mode-agnostic**. A `submit_mastery_signal(user_id, mode, lesson_id, score, metadata)` endpoint that any mode can call.

---

## 5A. The Five Core Data Signals

These are the **platform-wide engagement signals** — collected everywhere, surfaced selectively. The system collects ALL data but only reveals what drives engagement.

### Signal 1: Chapter-End Quiz Completion

**What**: Did the learner complete the quiz at the end of each chapter?
**Why it matters**: This is the **primary mastery gate**. A completed quiz = verifiable evidence of chapter comprehension.
**Current state**: Quiz UI exists and works. Scores are NOT persisted.

| Data Point           | Source                   | Persisted?       |
| -------------------- | ------------------------ | ---------------- |
| Quiz started         | Quiz.tsx `onStart`       | No (GA4 only)    |
| Score percentage     | Quiz.tsx `onComplete`    | No (React state) |
| Per-question results | Quiz.tsx answer tracking | No               |
| Attempt number       | Not tracked              | No               |
| Time to complete     | Not tracked              | No               |

**Action**: BR-1 covers this. First signal to wire up.

### Signal 2: Lesson-by-Lesson Progress

**What**: Has the learner gone through each individual lesson in a chapter?
**Why it matters**: A learner who reads 3 of 10 lessons then aces the quiz vs. one who reads all 10 — both passed, but their learning journeys are different. Lesson-level progress shows depth of engagement.
**Current state**: `ReadingProgress` component shows scroll depth as a visual indicator. GA4 tracks scroll milestones (25%, 50%, 75%, 100%). Neither is persisted to our backend.

| Data Point                        | Source                     | Persisted?       |
| --------------------------------- | -------------------------- | ---------------- |
| Lesson page visit                 | Router/Analytics           | GA4 only         |
| Scroll depth (%)                  | ReadingProgress component  | No (visual only) |
| Scroll milestones (25/50/75/100%) | GA4 AnalyticsTracker       | GA4 only         |
| Time on lesson page               | GA4 AnalyticsTracker (>5s) | GA4 only         |
| Lesson "completed"                | Not defined                | No               |

**What "completed" means** (needs decision):

- Option A: Scrolled to 100% depth (easy to fake, scroll and leave)
- Option B: Spent >= 2 minutes AND scrolled to 75%+ (better signal)
- Option C: Opened the lesson page at all (too loose)
- Option D: Completed a Teach/Ask session on that lesson (strongest signal, but not all learners use AI modes)

**Recommendation**: Option B as default, with Option D as "verified completion" (gold star).

### Signal 3: AI Mode Usage Frequency

**What**: Which AI mode did the learner use, how many times, on which lessons?
**Why it matters**: Mode usage reveals learning style AND engagement depth. A learner who uses Teach mode on every lesson is deeply engaged. A learner who only uses Ask mode for quick lookups has a different pattern. This data feeds both gamification (XP/badges) and content quality signals (lessons with high Ask usage may be confusing).
**Current state**: Every Teach/Ask session creates a `thread` in PostgreSQL with `lesson_path` and `mode` metadata. This data EXISTS but is not surfaced.

| Data Point                | Source                                        | Persisted?      |
| ------------------------- | --------------------------------------------- | --------------- |
| Mode selected (Teach/Ask) | study-mode-api threads.data.mode              | Yes             |
| Session count per lesson  | study-mode-api threads (group by lesson_path) | Yes (queryable) |
| Message count per session | study-mode-api items (count per thread)       | Yes (queryable) |
| Total sessions per user   | study-mode-api threads (group by user_id)     | Yes (queryable) |

**This is the richest signal we already have but never surface.** A simple query on the study-mode-api database gives us: sessions per user, sessions per lesson, messages per session, mode distribution.

### Signal 4: Tokens Burned (Credit Consumption)

**What**: How many AI tokens has the learner consumed across all interactions?
**Why it matters**: Tokens = effort. A learner who burns 50,000 tokens in a month is deeply engaged with the AI features. This is a proxy for "active learning time with AI" and also ties to business metrics (cost per learner).
**Current state**: Token metering API tracks every request. Credits system records consumption per user.

| Data Point                        | Source                             | Persisted? |
| --------------------------------- | ---------------------------------- | ---------- |
| Tokens per request (input/output) | token-metering-api usage_details   | Yes        |
| Credits consumed per request      | token-metering-api balance changes | Yes        |
| Total credits burned per user     | token-metering-api user balance    | Yes        |
| Model used per request            | token-metering-api model field     | Yes        |

**Note**: This data is already collected and billed. Surfacing it as "AI Learning Credits Used" in the dashboard is a presentation decision, not an engineering one.

### Signal 5: Active Engagement Time

**What**: How much time has the learner spent actively engaged with any part of the platform?
**Why it matters**: Time-on-task is the strongest predictor of learning outcomes. But not all time is equal — 10 minutes actively chatting with Teach mode > 10 minutes with the page open in a background tab.
**Current state**: GA4 tracks time-on-page (fires after 5 seconds). Study-mode-api has timestamps on all messages. No unified "engagement time" metric exists.

| Data Point               | Source                                     | Persisted?      |
| ------------------------ | ------------------------------------------ | --------------- |
| Page view duration       | GA4 AnalyticsTracker                       | GA4 only        |
| Teach session duration   | threads.created_at to last item.created_at | Yes (derivable) |
| Ask interaction duration | Single request/response (brief)            | Minimal         |
| Quiz time-to-complete    | Not tracked                                | No              |
| Personalization session  | agentfactory-api request timestamp         | Yes             |

**Engagement time calculation**: Sum of (Teach session durations) + (Quiz completion times) + (lesson page active time where scroll depth > 25%). Background tabs and idle time excluded.

### Signal Summary: Collect Everything, Surface Selectively

```
COLLECTED (backend, analytics):          SURFACED (learner dashboard):
├── Every lesson page visit              ├── Chapters completed (quiz-gated)
├── Scroll depth per lesson              ├── Total XP earned
├── Every AI mode session                ├── Current streak
├── Every message in every thread        ├── Badges earned
├── Every quiz score & answer            ├── Global rank
├── Every token consumed                 ├── "Time Learning" stat
├── Every personalization request        └── Chapter progress bars
├── Time stamps on everything
└── Mode selection patterns
```

The learner sees a **clean, motivating surface**. The platform team sees the **full signal** for content quality, learner health, and business metrics.

---

## 5B. XP Economics: Base, Bonus, and Accumulation

### How XP Maps to Badges

Badges are NOT earned from XP thresholds. They're earned from **specific achievements**. This is intentional — XP measures volume, badges measure milestones. A learner with 5,000 XP and 3 badges has different behavior than one with 3,000 XP and 8 badges.

```
XP = Quantitative measure of total effort
Badges = Qualitative markers of specific achievements
Leaderboard = XP-ranked (effort competition)
Badge Gallery = Achievement collection (milestone motivation)
```

### Base XP Sources

| Activity                       | XP Earned            | Frequency                     |
| ------------------------------ | -------------------- | ----------------------------- |
| Quiz completion (1st attempt)  | 0-100 XP (= score %) | Per chapter quiz              |
| Quiz improvement (2nd attempt) | improvement × 0.5    | Per reattempt                 |
| Quiz improvement (3rd attempt) | improvement × 0.25   | Per reattempt                 |
| Teach mode session (5+ turns)  | 10 XP                | Per session, max 3/day/lesson |
| Ask mode usage (per lesson)    | 5 XP                 | Per unique lesson, once       |
| Lesson completion (verified)   | 5 XP                 | Per lesson, once              |

### Bonus XP (Engagement Multipliers)

Inspired by Duolingo's data: limited-time XP boosts led to 50% surge in activity, and streaks increased commitment by 60%.

| Bonus Type              | Multiplier | Trigger                                  | Duration                              |
| ----------------------- | ---------- | ---------------------------------------- | ------------------------------------- |
| **Streak Bonus**        | 1.5x       | Active streak >= 7 days                  | Applies to all XP while streak active |
| **Perfect Score Bonus** | +25 XP     | 100% on first attempt                    | One-time per quiz                     |
| **First-of-Day Bonus**  | +10 XP     | First activity of the day                | Once per day                          |
| **Chapter Sweep Bonus** | +50 XP     | Complete ALL lessons + quiz in a chapter | One-time per chapter                  |
| **Weekend Challenge**   | 2x         | Platform event (bi-weekly)               | 48 hours                              |

### XP to Real Value

XP has no monetary value. But it has **social value** (leaderboard rank) and **recognition value** (profile display). Future extensions could include:

- XP thresholds for certification eligibility
- XP-gated content (advanced chapters)
- XP milestones that unlock cosmetic profile features

### Anti-Gaming Rules

- Max 3 Teach sessions per lesson per day count toward XP (prevents session farming)
- Ask mode XP: once per unique lesson (prevents highlight spam)
- Quiz reattempt XP: diminishing returns (prevents retake farming)
- No XP for page views alone (prevents passive accumulation)

---

## 5C. Industry Badge Standards: Google, GitHub, Duolingo

### Google Developer Badges

Google's system structures badges by **technology domain** (Web, Android, ML, Cloud) with escalating difficulty. Key patterns:

- **Tiered progression**: Each domain has multiple badges from beginner to advanced
- **Verifiable**: Tied to completed learning paths, codelabs, or certifications
- **Shareable**: Displayed on Google Developer Profile, shareable to LinkedIn
- **Arcade Points**: Google Cloud uses a points system exchangeable for swag
- **Skills Challenge**: Leaderboard-based competitions at events
- **450+ badges available** across the ecosystem

**Applicable to Agent Factory**: Our Parts (1-6) naturally map to Google's domain tiers. Part completion badges are already in the design. We should add **lesson-level micro-badges** within each part.

### GitHub Achievements

GitHub awards badges automatically based on platform activity. Key patterns:

- **Tiered badges**: Bronze → Silver → Gold (e.g., Starstruck: 16 → 128 → 512 stars)
- **Activity-based**: Earned by doing, not by studying (merge PRs, answer discussions, sponsor)
- **Surprise element**: Some badges feel like "easter eggs" (YOLO = merge without review)
- **Profile display**: Badges shown on GitHub profile, visible to all

**Applicable to Agent Factory**: We should add **tiered versions** of our badges:

| Badge                  | Bronze         | Silver            | Gold                |
| ---------------------- | -------------- | ----------------- | ------------------- |
| On Fire (streak)       | 3 days         | 7 days            | 30 days             |
| Perfect Score          | 1 perfect quiz | 5 perfect quizzes | All quizzes perfect |
| Deep Diver (Ask mode)  | 10 lessons     | 50 lessons        | All lessons         |
| Study Bug (Teach mode) | 10 sessions    | 50 sessions       | 100 sessions        |

### Duolingo's Engagement Engine

Duolingo's data-driven approach shows:

- Streaks increase commitment by **60%**
- XP leaderboards drive **40% more engagement**
- Badges boost completion rates by **30%**
- Users who hit 7-day streak are **3.6x more likely** to stay engaged
- Streak Freeze (grace period) reduced churn by **21%**
- Limited-time XP boosts → **50% activity surge**

**Key mechanics**:

- **Streak Freeze**: Miss one day, streak preserved (purchasable with gems)
- **Double XP events**: Time-limited engagement spikes
- **Leagues**: Weekly XP competition groups (Bronze → Diamond)
- **Gems currency**: Earned by completing lessons, spent on powerups

**Applicable to Agent Factory**: We should adopt:

1. Streak Freeze (1 free/week, or earned through high quiz scores)
2. Bonus XP events (Weekend Challenges)
3. The "First-of-Day" bonus (Duolingo does this, huge retention signal)
4. Tiered badges (matches GitHub's model, adds collection depth)

### Badge Design Principles (Synthesized)

| Principle                  | Source            | Our Application                           |
| -------------------------- | ----------------- | ----------------------------------------- |
| **Tiered progression**     | Google, GitHub    | Bronze/Silver/Gold versions of key badges |
| **Activity-based earning** | GitHub            | Badges from doing, not just scoring       |
| **Shareable credentials**  | Google            | Profile page with public badge display    |
| **Surprise/delight**       | GitHub (YOLO)     | Hidden badges for unexpected achievements |
| **Grace period**           | Duolingo (Freeze) | 1 streak freeze per week                  |
| **Time-limited events**    | Duolingo (2x XP)  | Weekend/monthly bonus XP challenges       |

### Updated Badge Count: 14 → 25+

Original 14 badges + tiered expansions + new categories:

**Existing (14)**: First Steps, Perfect Score, Ace, On Fire (3/7/30), Part 1-6 Complete, Graduate, Elite

**Proposed Additions**:

- **Tiered streaks** already covered (3 tiers exist)
- **Study Bug** (Bronze: 10, Silver: 50, Gold: 100 Teach sessions)
- **Deep Diver** (Bronze: 10, Silver: 50, Gold: all lessons via Ask)
- **Token Burner** (50k, 200k, 1M tokens consumed — "dedication" badge)
- **Speed Demon** (Complete a quiz in <3 minutes with 90%+)
- **Night Owl** (Study sessions after midnight, 5 times)
- **Weekend Warrior** (Complete activities on 4 consecutive weekends)
- **Comeback Kid** (Return after 30+ day absence and complete a quiz)
- **Hidden**: "YOLO" equivalent — complete all chapter quizzes in a single day

---

## 5D. xAPI Learning Analytics Backbone (LearnMCP Integration)

### What is xAPI?

xAPI (Experience API) is the **industry standard** for recording learning experiences across any platform. Unlike SCORM (which only tracks course completion inside an LMS), xAPI can capture:

- Formal learning (quizzes, courses)
- Informal learning (reading, conversations, practice)
- Real-world activities (projects, simulations)
- Cross-platform experiences (mobile, web, API)

Every learning event becomes an **xAPI statement**: `Actor → Verb → Object → Result → Context`

### Why xAPI Matters for Agent Factory

Our platform generates learning data from **6 different sources** (Teach, Ask, Quiz, Personalization, Reading, Token usage). Without a standard, each source stores data differently. xAPI gives us:

1. **Unified data model**: Every interaction → same statement format
2. **Interoperability**: Data portable to any xAPI-compliant analytics tool
3. **Compliance**: FERPA/GDPR alignment (xAPI has built-in privacy patterns)
4. **Future-proofing**: New modes (Socratic, Coach) automatically fit the model
5. **Accreditation path**: xAPI is the standard for verifiable credentials in education

### LearnMCP-xAPI: Direct Integration

[LearnMCP-xAPI](https://davidlms.github.io/learnmcp-xapi/) is an open-source MCP server that bridges AI agents with xAPI Learning Record Stores. It provides:

- **Statement Recording**: Convert learning events to xAPI statements
- **Progress Retrieval**: Query filtered learning histories
- **Vocabulary Management**: Standardized learning verbs
- **LRS Plugins**: SQLite (dev), Ralph LRS (production), Veracity Learning (cloud)
- **Privacy**: UUID-based actor identification (no PII in statements)

### How It Fits Our Architecture

```
┌─────────────────────────────────────────────────┐
│              LEARNER SURFACE                     │
│  XP │ Badges │ Streaks │ Progress │ Leaderboard  │
└───────────────────────┬─────────────────────────┘
                        │ reads from
┌───────────────────────▼─────────────────────────┐
│           PROGRESS API (gamification)            │
│  quiz_attempts │ user_progress │ user_badges      │
└───────────────────────┬─────────────────────────┘
                        │ consumes from
┌───────────────────────▼─────────────────────────┐
│        xAPI LEARNING RECORD STORE (LRS)          │
│  Every learning event as xAPI statement          │
│  Actor → Verb → Object → Result → Context        │
└───────────────────────┬─────────────────────────┘
                        │ receives from
┌───────────────────────▼─────────────────────────┐
│           LearnMCP-xAPI (MCP Server)             │
│  Statement Recording │ Progress Retrieval        │
└───┬───────┬───────┬───────┬───────┬─────────────┘
    │       │       │       │       │
  Teach   Ask    Quiz  Personal. Reading
  Mode    Mode   Submit  API     Progress
```

### xAPI Statements for Agent Factory

| Activity                      | xAPI Verb      | Object                      | Result                    |
| ----------------------------- | -------------- | --------------------------- | ------------------------- |
| Start lesson                  | `experienced`  | `lesson/{path}`             | —                         |
| Complete lesson (scroll 100%) | `completed`    | `lesson/{path}`             | duration                  |
| Start quiz                    | `attempted`    | `quiz/{chapter-id}`         | —                         |
| Submit quiz                   | `scored`       | `quiz/{chapter-id}`         | score: 85%, XP: 85        |
| Start Teach session           | `interacted`   | `teach-session/{thread-id}` | —                         |
| Complete Teach session        | `completed`    | `teach-session/{thread-id}` | turns: 12, duration: 8min |
| Use Ask mode                  | `asked`        | `ask/{lesson-path}`         | highlighted_text          |
| Earn badge                    | `earned`       | `badge/{badge-id}`          | badge metadata            |
| Reach streak milestone        | `progressed`   | `streak/{user-id}`          | streak_days: 7            |
| Use personalization           | `personalized` | `lesson/{path}`             | interest_tag              |

### Implementation Decision (OQ-7)

**Should xAPI be Phase 1 or Phase 2?**

- **Phase 1 (with MVP)**: Design the progress-api to emit xAPI statements from day one. Even with a SQLite LRS for development. This ensures the data model is right.
- **Phase 2 (later)**: Build gamification first with custom schema, migrate to xAPI later. Faster to ship but creates migration debt.

**Recommendation**: Phase 1.5 — Ship the gamification MVP with our custom schema (Phase 1), but design the schema to be **xAPI-aligned** so migration is trivial. Add LearnMCP-xAPI integration in Phase 2 alongside Teach/Ask session tracking.

---

## 6. Open Questions

### OQ-1: Separate Service or Extend Existing?

PR #680 proposes a new `apps/progress-api/` service. But we already have:

- `agentfactory-api` (personalization, preferences) — same auth, same DB needs
- `study-mode-api` (ChatKit, threads) — produces the raw data
- `token-metering-api` (credits) — tracks usage

**Options**:

- **(A) New service** (`progress-api`): Clean separation, independent scaling, clear ownership
- **(B) Extend `agentfactory-api`**: Already has auth, DB, rate limiting. Add progress routes alongside personalization
- **(C) Extend `study-mode-api`**: Closest to the data source. But mixes concerns

**Recommendation**: Option A (new service) for clean ownership, but reuse auth patterns from agentfactory-api.

### OQ-2: What Counts as an "Active Day" for Streaks?

- Option A: Any quiz completion (strict, high signal)
- Option B: Any quiz OR Teach session >=5 turns (medium)
- Option C: Any authenticated page view of a lesson (loose)

### OQ-3: Real-time XP or Batch?

- Real-time: XP shown immediately after quiz → better UX, more complex
- Batch: XP calculated hourly → simpler, but delayed feedback kills motivation

**Recommendation**: Real-time for quiz XP (synchronous response). Batch for Teach/Ask session XP (background job).

### OQ-4: Leaderboard Scope

- Global (all users) — largest pool, most competitive
- Per-cohort (users who started same month) — fairer for newcomers
- Per-organization — for enterprise/team use

### OQ-5: Privacy and GDPR

- Can users opt out of leaderboard?
- Is progress data exportable?
- What's the data retention policy?

### OQ-6: Personalization XP

The personalization feature (3 lessons/month, agentfactory-api) generates content. Should using personalization count as a study activity for streaks? Should it grant XP?

### OQ-7: xAPI Integration Timing

Should we design the progress-api with xAPI-aligned schema from day one, or build custom first and migrate later? See Section 5D for full analysis.

### OQ-8: Lesson Completion Definition

What constitutes "completing" a lesson? See Signal 2 in Section 5A for options. This affects lesson-level progress bars, chapter completion %, and XP for lesson completion.

### OQ-9: Tiered Badges — How Many Tiers?

Google and GitHub use 2-4 tiers. Do we want Bronze/Silver/Gold (3 tiers) or add a 4th "Platinum" tier? More tiers = more collection motivation but also more complexity. See Section 5C.

---

## 7. Vision Document Alignment

The AI-Native Interactive Book Platform architecture document defines a **4-level mastery model** and **6 assessment methods**. Here's how gamification maps to them:

### Mastery Levels → XP Thresholds (Future)

| Vision Level | Description               | Gamification Signal                               |
| ------------ | ------------------------- | ------------------------------------------------- |
| Basic        | Conceptual awareness      | Lesson completion + low quiz score                |
| Functional   | Independent execution     | Quiz 70%+ on first attempt                        |
| Advanced     | System design             | Part completion + Mentor mode artifacts           |
| Expert       | Optimization & innovation | All chapters complete + high XP + all Gold badges |

### Assessment Methods → XP Sources

| Vision Method            | Implementation              | XP Source                     |
| ------------------------ | --------------------------- | ----------------------------- |
| Teach-back scoring       | Teach mode + Feynman grader | Phase 3 (post-hoc evaluation) |
| Artifact validation      | Spec validator (future)     | Phase 4                       |
| Simulation performance   | Simulator mode (future)     | Phase 4                       |
| Socratic reasoning depth | Socratic mode (future)      | Phase 3                       |
| Quiz scoring             | Quiz.tsx (live today)       | **Phase 1 (MVP)**             |
| Session engagement       | Teach/Ask thread data       | Phase 2                       |

### UserState (Vision Doc) → Our Schema

The vision doc defines:

```
UserState {
  skills[]           → user_badges + concept mastery (future)
  mastery_scores     → quiz_attempts + user_progress
  artifacts[]        → artifact_store (Phase 4)
  current_section    → lesson page visit tracking
  learning_plan      → Manager mode output (future)
}
```

Our gamification schema captures `mastery_scores` and `current_section` in Phase 1, `skills[]` via badges in Phase 2, and the rest grows with new modes.

---

## 8. Implementation Phases (Updated)

### Phase 1: Foundation (MVP) — Estimated 2-3 weeks

**Goal**: Quiz scores persist, XP works, basic dashboard exists.

| Task                              | Description                                               |
| --------------------------------- | --------------------------------------------------------- |
| Progress API service scaffold     | FastAPI app with auth, DB, health check                   |
| Database schema                   | quiz_attempts, user_progress, user_badges, study_sessions |
| Quiz submit endpoint              | `POST /api/v1/quiz/submit` with XP calculation            |
| Progress endpoint                 | `GET /api/v1/progress` with full user summary             |
| Frontend: wire Quiz.tsx           | Add API call on quiz completion                           |
| Frontend: restore ProgressContext | From PR #680, connect to real API                         |
| Frontend: XP notification         | Toast/modal showing XP earned + new badges                |
| Frontend: Progress dashboard      | Restore from PR #680, connect to real API                 |

### Phase 2: Social + Retention — Estimated 1-2 weeks

| Task                           | Description                                      |
| ------------------------------ | ------------------------------------------------ |
| Streak calculation             | Daily activity tracking, grace period logic      |
| Leaderboard endpoint           | `GET /api/v1/leaderboard` with materialized view |
| Frontend: Leaderboard page     | Restore from PR #680                             |
| Frontend: XP counter in navbar | Always-visible motivation                        |
| Badge unlock animations        | Satisfying unlock moments                        |

### Phase 3: Engine Integration + xAPI — Estimated 2-3 weeks

| Task                           | Description                                               |
| ------------------------------ | --------------------------------------------------------- |
| Study session tracking         | Record Teach/Ask sessions as activity                     |
| Teach mode session → streak    | Count completed Teach sessions as active day              |
| Ask mode analytics             | Aggregate highlight patterns per lesson                   |
| Content quality signals        | Surface lessons with high Ask usage to content team       |
| Mode-agnostic mastery endpoint | `POST /api/v1/mastery` for any mode                       |
| Lesson-level progress          | Track page visits, scroll depth, time per lesson          |
| xAPI statement emitter         | Emit xAPI statements from progress-api to LRS             |
| LearnMCP-xAPI integration      | Connect MCP server for AI agent access to learning data   |
| Token usage dashboard          | Surface "AI Credits Used" from token-metering-api         |
| Engagement time calculation    | Derive active time from thread timestamps + page duration |
| Bonus XP engine                | Streak multiplier, first-of-day, perfect score bonuses    |
| Tiered badge system            | Bronze/Silver/Gold versions of activity badges            |

### Phase 4: Advanced — Future

| Task                      | Description                                               |
| ------------------------- | --------------------------------------------------------- |
| Socratic mode integration | Mastery scoring via OpenAI Evals graders                  |
| Concept-level progress    | Track mastery per concept, not just per chapter           |
| Spaced repetition         | Return to weakest concepts after N days                   |
| Adaptive difficulty       | Adjust quiz difficulty based on mastery level             |
| Achievement sharing       | Share badges to social media (Google Developer style)     |
| Weekend Challenge events  | Bi-weekly 2x XP events to spike engagement                |
| Streak Freeze mechanic    | 1 free streak freeze per week (Duolingo pattern)          |
| Hidden badges             | Surprise badges for unusual behaviors (GitHub YOLO style) |
| Certification integration | XP thresholds as prerequisite for certification exams     |

---

## 8. Success Metrics

| Metric                       | Baseline (now)        | Target (3 months post-launch) |
| ---------------------------- | --------------------- | ----------------------------- |
| Quiz completion rate         | Unknown (no tracking) | Measurable + 20% from Month 1 |
| 7-day return rate            | Unknown               | 30%+                          |
| Quiz retake rate             | Unknown               | 15%+ (users improving scores) |
| Average quizzes per user     | Unknown               | 5+ per month                  |
| Leaderboard page views       | 0                     | 500+ unique/month             |
| Streak maintenance (7+ days) | 0                     | 10% of active users           |

---

## 9. Dependency Map

```
                        ┌──────────────┐
                        │     SSO      │
                        │ (JWT tokens) │
                        └──────┬───────┘
                               │ auth
    ┌──────────────────────────┼──────────────────────────┐
    │                          │                          │
┌───▼────────────┐   ┌────────▼────────┐   ┌─────────────▼──┐
│ study-mode-api │   │  progress-api   │   │agentfactory-api│
│ (Teach/Ask)    │   │  (NEW)          │   │(Personalize)   │
│                │   │                 │   │                │
│ threads ───────┼──►│ sessions        │   │                │
│ messages       │   │ quiz scores     │   │                │
└────────────────┘   │ XP/badges       │   └────────────────┘
                     │ leaderboard     │
┌────────────────┐   │                 │
│token-metering  │   │                 │
│(credits/usage) ├──►│ token dashboard │
└────────────────┘   └───────┬─────────┘
                             │ emits xAPI statements
                     ┌───────▼─────────┐
                     │  xAPI LRS       │
                     │  (Phase 3)      │
                     │  LearnMCP-xAPI  │
                     └───────┬─────────┘
                             │
                     ┌───────▼─────────┐
                     │   learn-app     │
                     │   (frontend)    │
                     │                 │
                     │ Quiz.tsx        │
                     │ Dashboard       │
                     │ Leaderboard     │
                     │ Badge Gallery   │
                     │ XP Counter      │
                     └─────────────────┘
```

---

## 10. Risk Assessment

| Risk                                   | Impact                | Mitigation                                                      |
| -------------------------------------- | --------------------- | --------------------------------------------------------------- |
| XP farming (bot accounts)              | Leaderboard integrity | Rate limit quiz attempts, require auth, CAPTCHAs if needed      |
| Curriculum restructure breaks progress | User trust            | Content-addressed architecture (UUIDs, soft deletes)            |
| Backend not ready when frontend ships  | Dead UI               | Mock data fallback already exists in PR #680                    |
| Over-gamification cheapens learning    | Brand damage          | Keep it scholarly — no flashy animations, Polar Night aesthetic |
| Streak pressure causes burnout         | User churn            | Grace period (1 day), no public streak display                  |
| Privacy concerns (leaderboard)         | GDPR/trust            | Opt-out mechanism, anonymous display option                     |

---

## Appendix A: PR #680 Assessment — Should We Use It as Starter?

PR #680 (`feat/user-progress`, 6 commits, 4656 additions) was built by a contributor. It contains frontend gamification UI with mock data. Implementation would start fresh from `main` — PR #680 is **reference material**, not a merge candidate.

### What PR #680 Contains

| Artifact                                         | Lines | Quality                                    | Usable?                                                        |
| ------------------------------------------------ | ----- | ------------------------------------------ | -------------------------------------------------------------- |
| `progress-types.ts` (types + 14 badge defs)      | ~120  | Solid TypeScript, well-structured          | Yes — adopt types                                              |
| `progress-api.ts` (API client + mock data)       | ~405  | Full CRUD client + generous mocks          | Partially — API contract useful, mock data needs review        |
| `ProgressContext.tsx` (provider + hooks)         | ~255  | `useMockData` toggle, XP animation state   | Partially — pattern good, auth integration needs audit         |
| `ProgressDashboard.tsx` (full dashboard)         | ~400  | StatCards, badges, chapter progress        | Review — UI design decisions not validated against Polar Night |
| `BadgeCard.tsx` / `BadgeUnlockModal.tsx`         | ~200  | Badge display + unlock animation           | Review — new dependency (dialog component)                     |
| `XPCounter.tsx` (navbar widget)                  | ~80   | Always-visible XP counter                  | Review — modifies Navbar swizzle                               |
| `Leaderboard.tsx` (full page)                    | ~200  | Rankings table with current user highlight | Review — design decisions                                      |
| `QuizXPModal.tsx` (post-quiz modal)              | ~100  | XP earned + new badges overlay             | Review                                                         |
| `gamification.css`                               | ~300  | Styling for all components                 | Review against Polar Night theme                               |
| `decision-progress.md` (architecture)            | ~200  | Content-addressed progress, soft deletes   | Yes — strong architecture thinking                             |
| `gamified-progress-feat-prd.md` (PRD)            | ~300  | XP formula, badges, schema, API spec       | Yes — requirements are solid                                   |
| `.claude/handoffs/` + `.claude/logs/` (11 files) | ~500  | Session artifacts                          | No — should not be in repo                                     |
| `package.json` changes                           | —     | New dependencies added                     | Audit — what was added and why                                 |

### Questions to Raise About Using PR #680

**1. Code Quality & Review Status**

- Was this code reviewed by anyone before the PR was opened?
- The PR has merge conflicts with main — how stale is it?
- 11 `.claude/` session artifact files committed — suggests no `.gitignore` hygiene

**2. Design Decisions Made Without Requirements**

- Badge definitions (14 badges) — were these validated against any learning science or business goals? Or are they a first draft?
- XP formula (diminishing returns) — the math is sound, but the specific multipliers (0.5, 0.25, 0.10) — are these tuned or arbitrary?
- `useMockData` toggle — good pattern, but mock data is hardcoded (1234 XP, rank #42, 5-day streak). Does this represent realistic user behavior?

**3. Architecture Gaps**

- No backend exists. The API client (`progress-api.ts`) defines endpoints that don't exist yet. If the frontend ships first, learners see a dead UI.
- `ProgressContext` uses `localStorage.getItem("ainative_access_token")` — but our auth flow uses `ainative_id_token` (JWT) not access_token (opaque). This would fail in production.
- No rate limiting on quiz submissions — a user could submit unlimited scores
- No xAPI consideration — data model is custom, not standards-aligned

**4. Scope Alignment with Business Requirements**

- PR #680 only covers **quiz-based gamification**. Our requirements (Section 5A) define 5 data signals including Teach/Ask mode usage, token consumption, and engagement time. PR #680 doesn't address any of these.
- No lesson-level progress tracking (Signal 2)
- No AI mode usage tracking (Signal 3)
- No bonus XP mechanics (Section 5B)
- No tiered badges (Section 5C)
- No xAPI integration (Section 5D)

**5. Dependencies Introduced**

- What new npm packages were added in `package.json`? (UI dialog, tooltip components)
- Are these compatible with our Docusaurus setup?
- Do they introduce bundle size concerns?

### Recommendation

**Use PR #680 as reference, not as code to merge.**

| What to adopt                          | What to rebuild                                           | What to discard                                 |
| -------------------------------------- | --------------------------------------------------------- | ----------------------------------------------- |
| Type definitions (`progress-types.ts`) | All UI components (align to Polar Night, add new signals) | `.claude/` artifacts                            |
| XP formula (validate multipliers)      | API client (fix auth token, add new endpoints)            | Mock data (rebuild with realistic scenarios)    |
| Content-addressed architecture concept | ProgressContext (fix auth, add 5 signals)                 | `package.json` dep changes (audit first)        |
| PRD document as requirements input     | Backend service (build from scratch)                      | Navbar swizzle changes (review against current) |

The contributor should:

1. Start a **new branch from main**
2. Reference PR #680's PRD and architecture docs
3. Follow **this spec** (`specs/003-gamification-engine/requirements.md`) as the source of truth
4. Build backend first (progress-api), then wire frontend
5. Close PR #680 with a comment linking to the new implementation

## Appendix B: Study Mode API Signals Available Today

**Already persisted** (can be queried for gamification):

- `threads.lesson_path` — which lesson was studied
- `threads.created_at` — when study started
- `items.created_at` — per-message timestamps
- `threads.data.mode` — "teach" or "ask"
- `items.data.role` — user vs assistant turn count

**Available but not captured**:

- Teach mode correctness (needs post-hoc evaluation)
- Ask mode highlighted text (in metadata, not aggregated)
- Session completion signal (no explicit "I'm done studying" event)
- Concept-level tagging (messages aren't tagged to specific concepts)
