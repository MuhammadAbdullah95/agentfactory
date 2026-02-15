### Core Concept

Neon is a serverless PostgreSQL database that makes your application persistent, scalable, and accessible from anywhere. Moving from in-memory SQLite to Neon means your data survives restarts, handles multiple users, and auto-scales -- with zero server management.

### Key Mental Models

- **Environment variables as the security boundary**: Database credentials live in `.env` files, never in code. `.env` goes in `.gitignore` immediately. If credentials reach a Git repository, attackers will find them -- bots scan public repos constantly.
- **Connection pooling as connection reuse**: Instead of opening a new database connection for every query (slow, hits limits), a pool keeps connections warm and reuses them. `pool_pre_ping=True` is critical for Neon because it auto-pauses idle databases, killing stale connections.

### Critical Patterns

- Connection string anatomy: `postgresql+psycopg2://user:password@host/dbname?sslmode=require`
- Secure credential flow: `.env` file with `DATABASE_URL`, `load_dotenv()`, `os.getenv("DATABASE_URL")`, `.env` in `.gitignore`
- Production engine configuration: `pool_size=5`, `max_overflow=10`, `pool_pre_ping=True`, `pool_recycle=3600`
- Connection verification: `conn.execute(text("SELECT 1"))` before deploying models

### Common Mistakes

- Hardcoding the connection string in Python code -- one accidental git push exposes your database to the world
- Forgetting `pool_pre_ping=True` -- Neon pauses after 5 minutes idle, and stale connections fail silently
- Not checking that `.env` is actually in `.gitignore` before committing (verify with `git status`)

### Connections

- **Builds on**: In-memory SQLite from Lessons 2-5 (same SQLAlchemy code, different engine URL)
- **Leads to**: Hybrid SQL + bash verification patterns (Lesson 7), then integrating everything in the capstone (Lesson 8)
