---
sidebar_position: 11
title: "Chapter 14: Ten Axioms Quiz"
proficiency_level: B1
layer: 2
estimated_time: "30 mins"
chapter_type: Concept
running_example_id: ten-axioms-quiz
---

# Chapter 14: Ten Axioms of Agentic Development Quiz

Test your understanding of the ten axioms that govern effective agentic software development: Shell as Orchestrator, Knowledge is Markdown, Programs Over Scripts, Composition Over Monoliths, Types Are Guardrails, Data is Relational, Tests Are the Specification, Version Control is Memory, Verification is a Pipeline, and Observability Extends Verification.

<Quiz
  title="Chapter 14: Ten Axioms of Agentic Development Assessment"
  questions={[
    {
      question: "A developer has a workflow that fetches data from an API, transforms it with jq, filters results with grep, and writes output to a file. They wrote all of this as a single 80-line bash script with nested if-else blocks for error handling and retry logic. What should they do?",
      options: [
        "Keep it as a bash script since shell is the orchestrator for all work",
        "Rewrite the entire workflow in Python since bash is only for simple commands",
        "Keep the shell as the orchestrator (pipe/coordinate) but extract the retry logic and complex transformations into a proper program",
        "Split it into 80 separate one-line scripts for maximum composability"
      ],
      correctOption: 2,
      explanation: "Axiom I (Shell as Orchestrator) distinguishes between the shell's role as coordinator and programs' role as computational engines. The shell excels at piping data between programs, but when logic grows complex (nested conditionals, retry mechanisms, state management), that logic has crossed the complexity threshold and belongs in a proper program. The shell should still orchestrate (call the program, pipe its output), but the computation itself should be a typed, tested program. Option A ignores the complexity threshold. Option B overcorrects—the shell is still the right orchestrator. Option D is absurd fragmentation.",
      source: "Lesson 01: Shell as Orchestrator"
    },
    {
      question: "An AI agent needs to coordinate: (1) run linting, (2) run tests, (3) build a Docker image, (4) push to registry. A developer writes this as a Python script that uses subprocess.run() for each step. What architectural problem does this introduce?",
      options: [
        "Python is too slow for orchestration tasks",
        "The developer replaced the shell (natural orchestrator) with a program, hiding coordination logic inside compiled code that's harder to inspect and modify",
        "subprocess.run() is deprecated and should not be used",
        "Docker commands cannot be run from Python scripts"
      ],
      correctOption: 1,
      explanation: "Axiom I states that the shell is the natural orchestration layer—it coordinates programs. By wrapping shell orchestration inside Python (using subprocess.run), the developer hides the coordination logic inside a program, making it harder to read, modify, and debug. A Makefile or shell script would express this coordination more transparently: each step is visible, the flow is obvious, and any developer can understand or modify it without Python knowledge. The shell coordinates; programs compute. When your 'program' is just calling other programs in sequence, it should be shell orchestration instead.",
      source: "Lesson 01: Shell as Orchestrator"
    },
    {
      question: "A team stores their project decisions in a Notion database, API documentation in Confluence, and coding standards in a Google Doc. Their AI agent struggles to access this context effectively. What axiom are they violating?",
      options: [
        "Shell as Orchestrator—they should use bash to access these tools",
        "Knowledge is Markdown—persistent knowledge should be in version-controlled markdown files that AI can directly read",
        "Version Control is Memory—they should commit their Notion pages to git",
        "Observability Extends Verification—they need better monitoring of their docs"
      ],
      correctOption: 1,
      explanation: "Axiom II (Knowledge is Markdown) states that all persistent knowledge should live in markdown files because markdown is human-readable, version-controllable, AI-parseable, and tool-agnostic. Notion, Confluence, and Google Docs are proprietary silos that require API authentication, special tooling, and network access for AI to read. Markdown files (CLAUDE.md, ADRs, README.md) sit in the repository where any AI agent can read them directly with standard file access. Option C is wrong because you can't meaningfully 'commit Notion pages' without converting them to markdown first. The fundamental issue is format choice, not storage location.",
      source: "Lesson 02: Knowledge is Markdown"
    },
    {
      question: "A developer creates a DECISIONS.md file to track architectural choices but writes entries like: 'We picked PostgreSQL because it seemed good.' Three months later, nobody remembers the actual reasoning. What aspect of the 'Knowledge is Markdown' axiom did they miss?",
      options: [
        "They should have used a database instead of markdown for decisions",
        "They captured the decision but not the reasoning—markdown knowledge must be complete enough to reconstruct context without the original authors",
        "They should have stored the decision in multiple markdown files for redundancy",
        "They should have used a wiki instead of a markdown file"
      ],
      correctOption: 1,
      explanation: "Axiom II requires that markdown knowledge be self-contained and complete. 'Seemed good' provides no reconstructible context—future developers (or AI agents) cannot understand the trade-offs, alternatives considered, or constraints that drove the choice. Proper markdown knowledge includes: the problem, options considered, decision made, and reasoning. An ADR format captures all this. The axiom isn't just 'use markdown files'—it's 'encode knowledge completely in markdown so it persists beyond the original author's memory.' Options A and D miss the point entirely—the problem is content quality, not format or storage choice.",
      source: "Lesson 02: Knowledge is Markdown"
    },
    {
      question: "A team has a 200-line bash script that parses CSV files, validates email formats with regex, handles database connections, and sends HTTP requests with retry logic. It works but has no tests and fails silently on edge cases. Which axiom guides the fix?",
      options: [
        "Shell as Orchestrator—rewrite the shell to orchestrate better",
        "Programs Over Scripts—this script should become a proper program with types, tests, error handling, and CI integration",
        "Composition Over Monoliths—just split it into smaller bash scripts",
        "Tests Are the Specification—add tests to the bash script"
      ],
      correctOption: 1,
      explanation: "Axiom III (Programs Over Scripts) states that production work requires proper programs with the full discipline stack: types (pyright), linting (ruff), testing (pytest), dependency management (uv), and CI integration. A 200-line bash script doing CSV parsing, email validation, database connections, and HTTP requests is well past the complexity threshold—it needs type safety for data structures, proper error handling, testable functions, and CI to catch regressions. Option C (splitting into smaller scripts) still lacks types and tests. Option D (testing bash) is impractical for complex logic. The script must graduate to a proper program.",
      source: "Lesson 03: Programs Over Scripts"
    },
    {
      question: "A junior developer asks: 'Why do I need uv, pyright, ruff, AND pytest? Can't I just write Python and run it?' What is the best response based on the axioms?",
      options: [
        "You're right—for small projects, just running Python is fine since tools add unnecessary complexity",
        "Each tool in the discipline stack catches different error categories: uv manages dependencies reproducibly, pyright catches type errors before runtime, ruff enforces style consistency, and pytest verifies behavior—together they prevent entire classes of bugs that 'just running Python' would miss",
        "You only need pytest since testing is the most important part",
        "You only need pyright since type checking catches all bugs"
      ],
      correctOption: 1,
      explanation: "Axiom III defines the Python discipline stack as a layered defense system where each tool serves a distinct purpose: uv ensures reproducible environments (no 'works on my machine'), pyright catches type errors at analysis time (wrong argument types, missing attributes), ruff enforces consistent style (readability, common mistakes), and pytest verifies behavior (correct outputs for given inputs). Removing any layer leaves a gap—without types, you get runtime AttributeError; without tests, you get undetected logic bugs; without dependency management, you get environment drift. 'Just running Python' works for exploration but fails for production. The discipline stack is what makes programs reliable.",
      source: "Lesson 03: Programs Over Scripts"
    },
    {
      question: "A developer builds a TaskManager class that handles: database connections, input validation, business logic, email notifications, logging, and error reporting. When they need to change the email provider, they must modify and retest the entire class. What axiom addresses this?",
      options: [
        "Types Are Guardrails—they need better type annotations",
        "Tests Are the Specification—they need more tests",
        "Composition Over Monoliths—the class should be decomposed into focused, composable units with clear interfaces",
        "Shell as Orchestrator—they should use bash to coordinate the components"
      ],
      correctOption: 2,
      explanation: "Axiom IV (Composition Over Monoliths) prescribes building from composable, focused units rather than monolithic blocks. The TaskManager class violates this by combining six unrelated responsibilities into one unit. Following the Unix philosophy and dependency injection, each concern should be a separate component: a Validator, a Repository (database), a Notifier (email), a Logger—each with a focused interface. Changing the email provider then requires modifying only the Notifier, not the entire system. This is the Single Responsibility Principle applied architecturally: each unit does one thing, and composition assembles them into a system.",
      source: "Lesson 04: Composition Over Monoliths"
    },
    {
      question: "A team debates between building one large FastAPI application with all endpoints versus multiple small services. Following Axiom IV, which approach is correct?",
      options: [
        "Always use microservices—monoliths are always wrong",
        "Always use a monolith—microservices add unnecessary complexity",
        "Start with a well-structured monolith using composable internal modules, then extract services only when specific boundaries prove necessary",
        "The number of services doesn't matter as long as you have tests"
      ],
      correctOption: 2,
      explanation: "Axiom IV (Composition Over Monoliths) doesn't mean 'always use microservices'—it means build from composable units with clear interfaces. A well-structured monolith with internal modules (separate routers, services, repositories) IS composition. The key is focused interfaces and dependency injection, not deployment boundaries. You can have a monolithic deployment with composable internal architecture. Extract to separate services only when you have clear evidence: different scaling needs, different team ownership, or different deployment cadences. Option A is dogmatic. Option B ignores composition. Option D misses the architectural point entirely.",
      source: "Lesson 04: Composition Over Monoliths"
    },
    {
      question: "A developer writes a function `def process_data(data)` that accepts any input—dictionaries, lists, strings, None—and attempts to handle each case with isinstance() checks throughout. The function frequently crashes in production with unexpected input types. Which axiom provides the solution?",
      options: [
        "Tests Are the Specification—add more tests for edge cases",
        "Types Are Guardrails—define explicit types so invalid inputs are caught before runtime",
        "Observability Extends Verification—add logging to see what types arrive",
        "Verification is a Pipeline—add CI checks for the function"
      ],
      correctOption: 1,
      explanation: "Axiom V (Types Are Guardrails) states that type systems prevent errors at compile/analysis time rather than runtime. Instead of accepting 'any' and checking types dynamically, the function should declare its expected input: `def process_data(data: list[TaskRecord]) -> ProcessingResult`. With the three-layer type stack (hints for documentation, Pyright for static analysis, Pydantic for runtime validation), invalid inputs are caught before they cause production crashes. Pyright would flag callers passing wrong types during development. Pydantic would validate external data at system boundaries. The isinstance() pattern is a symptom of missing type discipline.",
      source: "Lesson 05: Types Are Guardrails"
    },
    {
      question: "A team uses Pydantic models for their API request/response types but doesn't run Pyright in their CI pipeline. They catch some type errors from Pydantic at runtime but miss others that only surface in rare code paths. What layer of the type stack are they missing?",
      options: [
        "They need better Pydantic validators to catch all runtime errors",
        "They're missing the static analysis layer (Pyright) which catches type mismatches across ALL code paths without needing to execute them",
        "They need to replace Pydantic with dataclasses for better performance",
        "They need to add more unit tests to cover rare code paths"
      ],
      correctOption: 1,
      explanation: "Axiom V defines a three-layer type stack: type hints (documentation), Pyright (static analysis), and Pydantic (runtime validation). Pydantic validates data at boundaries (API requests, external input) but only when that code path executes. Pyright analyzes ALL code paths statically—it finds type mismatches in error handlers, rare branches, and untested paths without running the code. The team has layer 1 (hints via Pydantic models) and layer 3 (runtime validation) but is missing layer 2 (static analysis). Adding Pyright to CI would catch the type errors in rare paths that Pydantic never sees because those paths haven't been triggered yet.",
      source: "Lesson 05: Types Are Guardrails"
    },
    {
      question: "A developer stores their application's task records as JSON files in a directory: one file per task, with fields like status, assignee, due_date, and priority. They need to answer: 'Show all high-priority tasks assigned to Alice that are overdue.' This query requires reading every file and filtering in Python. What axiom suggests a better approach?",
      options: [
        "Knowledge is Markdown—store tasks in markdown files instead",
        "Data is Relational—structured data with query needs belongs in a relational database where SQL handles filtering, joining, and indexing",
        "Composition Over Monoliths—split each field into its own file",
        "Shell as Orchestrator—use grep and find to query the JSON files"
      ],
      correctOption: 1,
      explanation: "Axiom VI (Data is Relational) states that SQL is the default for structured data. Task records have defined fields, relationships (assignee belongs to a users table), and query patterns (filter by priority, date, assignee). A relational database handles this naturally: `SELECT * FROM tasks WHERE priority = 'high' AND assignee = 'Alice' AND due_date < NOW()`. With JSON files, every query requires reading all files, parsing JSON, and filtering in application code—no indexes, no joins, no query optimization. SQLite provides this capability with zero server setup. The axiom isn't anti-JSON; it's pro-SQL for data that has structure and query needs.",
      source: "Lesson 06: Data is Relational"
    },
    {
      question: "A team is building a new feature and debates between SQLite and PostgreSQL for their database. The application currently runs on a single server with fewer than 10,000 records and no concurrent write requirements. Which does Axiom VI recommend?",
      options: [
        "PostgreSQL—always use the most powerful database available",
        "SQLite—it's a file-based database perfect for single-server apps with modest data volumes, requiring zero infrastructure",
        "MongoDB—document databases are more flexible than relational ones",
        "Neither—store data in CSV files for simplicity"
      ],
      correctOption: 1,
      explanation: "Axiom VI provides clear guidance on SQLite vs PostgreSQL: SQLite is ideal for single-server applications with modest data volumes and no concurrent write pressure. It requires zero infrastructure (no database server, no connection management, no separate deployment)—it's just a file. PostgreSQL becomes necessary when you need concurrent writes from multiple processes, advanced features (JSONB, full-text search), or when data exceeds what a single file handles efficiently. For fewer than 10,000 records on a single server, SQLite is the right choice—simpler deployment, simpler backup (copy the file), and zero operational overhead. Option A over-engineers. Options C and D violate the 'Data is Relational' axiom.",
      source: "Lesson 06: Data is Relational"
    },
    {
      question: "A developer asks AI to 'implement a user registration system.' The AI generates code that handles email/password signup. Later, the developer discovers it doesn't validate email format, hash passwords properly, or handle duplicate registrations. How should they have approached this using Axiom VII?",
      options: [
        "Write a more detailed natural language specification for the AI",
        "Write failing tests first that define all expected behaviors (email validation, password hashing, duplicate handling), then give the AI those tests as the specification to implement against",
        "Ask the AI to also write the tests along with the implementation",
        "Review the AI's code more carefully before accepting it"
      ],
      correctOption: 1,
      explanation: "Axiom VII (Tests Are the Specification) prescribes Test-Driven Generation (TDG): write tests FIRST that define correct behavior, then prompt AI to generate implementation that passes those tests. Tests like `test_rejects_invalid_email()`, `test_hashes_password_with_bcrypt()`, and `test_returns_error_on_duplicate_email()` unambiguously specify requirements. The AI can then implement against concrete, verifiable specifications rather than interpreting vague prose. Option A still suffers from natural language ambiguity. Option C (AI writes its own tests) creates circular validation—the AI defines its own success criteria. Option D catches problems after the fact rather than preventing them. TDG makes the test permanent and the implementation disposable.",
      source: "Lesson 07: Tests Are the Specification"
    },
    {
      question: "A team practices TDD but their tests look like: `assert user_service._hash_password('abc') == 'a9993e364...'`. When they switch from SHA-256 to bcrypt, all tests break even though the system behavior is correct. What TDG anti-pattern are they committing?",
      options: [
        "They're testing too many edge cases",
        "They're coupling tests to implementation details (specific hash values) rather than specifying behavior (password is properly hashed and verifiable)",
        "They should remove password hashing tests entirely since hashing is an implementation detail",
        "They should test the hash function in isolation rather than through the service"
      ],
      correctOption: 1,
      explanation: "Axiom VII warns against implementation coupling—tests should specify WHAT (behavior) not HOW (implementation). Testing that a specific hash value is produced ties the test to a specific algorithm. A behavior-specifying test would be: `assert verify_password('abc', user.hashed_password) == True` and `assert user.hashed_password != 'abc'`. These tests pass regardless of whether you use SHA-256, bcrypt, or argon2—they specify the behavior (passwords are hashed, hashed passwords are verifiable) without coupling to implementation. Option C goes too far—password hashing IS a behavior worth testing. Option D doesn't fix the coupling problem. The test should remain valid across multiple correct implementations.",
      source: "Lesson 07: Tests Are the Specification"
    },
    {
      question: "A developer working with an AI agent makes changes across 15 files and creates one commit message: 'Updated stuff.' The next day, they need to understand what changed and why, but the commit provides no useful information. Which axiom did they violate?",
      options: [
        "Knowledge is Markdown—they should have written a changelog in markdown",
        "Version Control is Memory—git commits should be atomic (one logical change) with conventional messages that explain the 'why', forming a searchable project memory",
        "Observability Extends Verification—they need better logging",
        "Tests Are the Specification—they should have written tests first"
      ],
      correctOption: 1,
      explanation: "Axiom VIII (Version Control is Memory) states that git serves as the persistent memory layer for all project work. This requires atomic commits (one logical change per commit, not 15 files of mixed changes) with conventional messages (feat:, fix:, refactor: prefixes) that explain reasoning. 'Updated stuff' provides zero memory—you can't search it, can't understand it, can't revert part of it. Proper practice: `feat(auth): add email validation to prevent invalid registrations`. Each commit is a discrete, understandable unit of change that future developers (and AI agents) can reason about. The AI collaboration protocol also requires this—AI reads commit history to understand project evolution.",
      source: "Lesson 08: Version Control is Memory"
    },
    {
      question: "A developer collaborates with an AI agent but works entirely on the main branch. After an hour of AI-generated changes, they realize the approach is wrong and want to start over. They've already committed 12 times to main. What version control practice would have prevented this problem?",
      options: [
        "Never let AI commit directly—always review changes manually first",
        "Use feature branches for AI collaboration so the main branch remains clean, enabling easy abandonment of failed approaches via branch deletion",
        "Commit less frequently so there are fewer commits to revert",
        "Use git stash instead of commits to save work in progress"
      ],
      correctOption: 1,
      explanation: "Axiom VIII prescribes using feature branches as the AI collaboration protocol. Working on main means bad commits pollute your primary branch and require complex reverts (git revert for each commit, or dangerous git reset). Feature branches provide isolation: if the approach fails, delete the branch—main is untouched. This enables fearless experimentation with AI because the cost of failure is zero (just delete the branch). Option A slows collaboration unnecessarily. Option C loses work protection. Option D doesn't provide the same history and isolation benefits as branches. The principle: branches make AI collaboration reversible and safe.",
      source: "Lesson 08: Version Control is Memory"
    },
    {
      question: "A team runs tests locally and deploys when they pass. One developer forgets to run the linter before pushing, introducing style violations. Another developer's tests pass locally because they have a dependency installed globally that isn't in requirements.txt. What axiom addresses these failures?",
      options: [
        "Programs Over Scripts—they need better scripts for their tools",
        "Types Are Guardrails—they need stricter type checking",
        "Verification is a Pipeline—automated CI/CD should run ALL checks in a clean environment, enforcing that nothing reaches production without passing the full verification pipeline",
        "Tests Are the Specification—they need more comprehensive tests"
      ],
      correctOption: 2,
      explanation: "Axiom IX (Verification is a Pipeline) states: 'If it's not in CI, it's not enforced.' Relying on developers to remember to run linting locally is a process, not a pipeline—processes are forgotten, skipped, or done inconsistently. A CI pipeline (GitHub Actions) runs all checks automatically in a clean environment: linting, type checking, tests, and builds. The clean environment catches the global dependency issue because CI has no pre-installed extras. The six-level verification pyramid (format, lint, types, unit tests, integration tests, E2E) ensures nothing is missed. Option A, B, and D address specific checks but miss the systemic issue: without automation, any check can be skipped.",
      source: "Lesson 09: Verification is a Pipeline"
    },
    {
      question: "A developer adds a new check to their CI pipeline: a security scanner that takes 45 minutes to run. Now every pull request takes an hour to get feedback. Developers start ignoring CI results because they're too slow. How should this be resolved according to Axiom IX?",
      options: [
        "Remove the security scanner since it slows down development",
        "Structure the pipeline into fast feedback tiers: quick checks (lint, types, unit tests) run first and fail fast, while slower checks (security scan, E2E tests) run in parallel or as a separate required stage",
        "Make the security scanner optional so developers can skip it",
        "Run CI only on the main branch, not on pull requests"
      ],
      correctOption: 1,
      explanation: "Axiom IX describes the six-level verification pyramid where faster, cheaper checks run first (format in seconds, lint in seconds, types in minutes) and slower, more expensive checks run later (integration tests, E2E, security scans). This provides fast feedback for common issues while still enforcing comprehensive verification. The key insight is 'fail fast'—if linting fails in 10 seconds, there's no need to wait 45 minutes for the security scan. Option A removes important verification. Option C makes security optional (defeats the purpose). Option D means broken code reaches main before being caught. The pipeline should be structured, not gutted.",
      source: "Lesson 09: Verification is a Pipeline"
    },
    {
      question: "A team's application passes all CI tests and deploys successfully. Two hours later, users report that API response times have increased from 200ms to 5 seconds. The team has no way to detect or diagnose this because they only verify at deployment time. What axiom addresses this gap?",
      options: [
        "Tests Are the Specification—they need performance tests in CI",
        "Verification is a Pipeline—they need a better CI pipeline",
        "Observability Extends Verification—they need runtime monitoring (metrics, logs, traces) that extends verification beyond deployment into production behavior",
        "Types Are Guardrails—they need better type checking to prevent slow code"
      ],
      correctOption: 2,
      explanation: "Axiom X (Observability Extends Verification) states that runtime monitoring extends pre-deployment verification into production. CI catches bugs in code but cannot predict production behavior under real load, real data, and real network conditions. Observability provides three pillars: logs (what happened—structured events), metrics (aggregated measurements—response time P95), and traces (request journey through services). With Prometheus metrics, the team would have seen response time spike immediately. With structured logs (structlog), they could diagnose the cause. Option A helps but CI load differs from production load. Option B is pre-deployment only. Option D is irrelevant to performance monitoring.",
      source: "Lesson 10: Observability Extends Verification"
    },
    {
      question: "A developer adds print() statements throughout their code to debug a production issue. They find the problem, remove most print statements (missing a few), and deploy. Later, the remaining print statements flood the log files with unstructured noise, making it impossible to find real errors. What observability practice does Axiom X recommend instead?",
      options: [
        "Use a debugger instead of print statements for all debugging",
        "Use structured logging (structlog) with log levels, consistent fields, and machine-parseable format so logs are queryable, filterable, and don't pollute production with debug noise",
        "Write all output to a separate debug file that's never checked in production",
        "Remove all logging entirely to keep logs clean"
      ],
      correctOption: 1,
      explanation: "Axiom X prescribes structured logging (structlog) over ad-hoc print statements. Structured logs have: levels (DEBUG, INFO, WARNING, ERROR) so debug output is suppressed in production; consistent fields (timestamp, request_id, user_id) for correlation; and machine-parseable format (JSON) for querying. Instead of `print(f'user {uid} failed')`, use `logger.error('login_failed', user_id=uid, reason=reason)`. This enables filtering (show only ERRORs), searching (find all events for user X), and alerting (notify on error rate spike). Print statements lack all of these capabilities and persist accidentally. The three pillars (logs, metrics, traces) work together for complete observability.",
      source: "Lesson 10: Observability Extends Verification"
    }
  ]}
/>

## Answer Key

| Question | Correct Answer | Axiom Tested |
|----------|---------------|--------------|
| 1 | C | Axiom I: Shell as Orchestrator |
| 2 | B | Axiom I: Shell as Orchestrator |
| 3 | B | Axiom II: Knowledge is Markdown |
| 4 | B | Axiom II: Knowledge is Markdown |
| 5 | B | Axiom III: Programs Over Scripts |
| 6 | B | Axiom III: Programs Over Scripts |
| 7 | C | Axiom IV: Composition Over Monoliths |
| 8 | C | Axiom IV: Composition Over Monoliths |
| 9 | B | Axiom V: Types Are Guardrails |
| 10 | B | Axiom V: Types Are Guardrails |
| 11 | B | Axiom VI: Data is Relational |
| 12 | B | Axiom VI: Data is Relational |
| 13 | B | Axiom VII: Tests Are the Specification |
| 14 | B | Axiom VII: Tests Are the Specification |
| 15 | B | Axiom VIII: Version Control is Memory |
| 16 | B | Axiom VIII: Version Control is Memory |
| 17 | C | Axiom IX: Verification is a Pipeline |
| 18 | B | Axiom IX: Verification is a Pipeline |
| 19 | C | Axiom X: Observability Extends Verification |
| 20 | B | Axiom X: Observability Extends Verification |

## Scoring Guide

| Score | Proficiency Level | Interpretation |
|-------|------------------|----------------|
| 18-20 | B2 (Advanced) | Strong understanding of all ten axioms and their practical application |
| 14-17 | B1 (Intermediate) | Good understanding with some gaps in applying axioms to real scenarios |
| 10-13 | A2 (Elementary) | Basic understanding of axioms but needs more practice with application |
| 0-9 | A1 (Beginner) | Review the lessons and work through the "Try With AI" exercises |

## Next Steps

Based on your performance, focus on:

- **Axioms I-III (Foundation Layer)**: If you missed questions 1-6, review the lessons on shell orchestration, markdown knowledge, and the program discipline stack. These axioms establish the base tools and practices for all agentic work.
- **Axioms IV-VI (Architecture Layer)**: If you missed questions 7-12, study composition patterns, the three-layer type stack, and relational data modeling. These axioms govern how you structure code and data.
- **Axioms VII-VIII (Workflow Layer)**: If you missed questions 13-16, focus on Test-Driven Generation and git as memory. These axioms define how you collaborate with AI agents effectively.
- **Axioms IX-X (Verification Layer)**: If you missed questions 17-20, study CI/CD pipelines and observability practices. These axioms ensure your code is verified both before and after deployment.

Remember: The ten axioms build upon each other—shell orchestrates programs (I, III), programs are composed (IV) with types (V) and relational data (VI), tested via TDG (VII), tracked in git (VIII), verified in CI (IX), and monitored in production (X). Master each layer before advancing to the next.
