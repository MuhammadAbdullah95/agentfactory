# Token Metering API (v5)

Freemium token tracking and metering service for the Agent Factory platform.

## v5 Architecture: Balance-Only Model

The v5 release simplifies the metering system to a **single balance-based model**:

- **No trial tracking** - Users start with `STARTER_TOKENS` (50,000)
- **Single balance field** - Source of truth for available tokens
- **365-day inactivity expiry** - Balance expires after 1 year of inactivity
- **Redis sorted set reservations** - Atomic reservation handling with O(1) operations

## Features

- **Pre-request balance checks** with reservation pattern (<5ms target)
- **Post-request token deductions** with idempotency via request_id
- **Administrative operations** (grant, topup)
- **Balance caching** with Redis read-through cache
- **Rate limiting** on admin endpoints (20 req/min via Redis)
- **Redis-first architecture** with PostgreSQL system of record
- **Prometheus metrics** for observability

## Quick Start

### Prerequisites

- Python 3.12+
- PostgreSQL 16+
- Redis 7+
- uv (recommended) or pip

### Local Development

```bash
# Install dependencies
cd apps/token-metering-api
uv sync

# Start dependencies with Docker
docker-compose up -d postgres redis

# Copy environment file
cp .env.example .env

# Start the server
uv run uvicorn token_metering_api.main:app --reload --port 8001

# Or via Nx
pnpm nx serve token-metering-api
```

### Environment Variables

See `.env.example` for all configuration options.

Key variables:
| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | Required |
| `REDIS_URL` | Redis connection string | Optional (fail-open) |
| `SSO_URL` | SSO service for JWT verification | Required for prod |
| `TOKEN_AUDIENCE` | JWT audience for validation | `token-metering-api` |
| `DEV_MODE` | Bypass authentication for development | `false` |
| `STARTER_TOKENS` | Initial tokens for new users | `50000` |
| `INACTIVITY_EXPIRY_DAYS` | Days before balance expires | `365` |
| `MARKUP_PERCENT` | Cost markup percentage | `20.0` |
| `FAIL_OPEN` | Allow requests when Redis unavailable | `true` |

## API Endpoints

### Metering (Core)

| Endpoint                   | Method | Description                             |
| -------------------------- | ------ | --------------------------------------- |
| `/api/v1/metering/check`   | POST   | Pre-request balance check (reserve)     |
| `/api/v1/metering/deduct`  | POST   | Post-request token deduction (finalize) |
| `/api/v1/metering/release` | POST   | Cancel reservation                      |

### Balance

| Endpoint                    | Method | Description                         |
| --------------------------- | ------ | ----------------------------------- |
| `/api/v1/balance`           | GET    | Get current user's balance          |
| `/api/v1/balance/{user_id}` | GET    | Get specific user's balance (admin) |
| `/api/v1/transactions`      | GET    | Get transaction history             |
| `/api/v1/allocations`       | GET    | Get allocation history              |

### Admin

| Endpoint              | Method | Description                  |
| --------------------- | ------ | ---------------------------- |
| `/api/v1/admin/grant` | POST   | Grant tokens (institutional) |
| `/api/v1/admin/topup` | POST   | Add tokens (paid)            |

### Health & Metrics

| Endpoint   | Method | Description        |
| ---------- | ------ | ------------------ |
| `/health`  | GET    | Health check       |
| `/metrics` | GET    | Prometheus metrics |

## Reservation Pattern

The metering service uses a reservation pattern to prevent overcharging:

```
1. PRE-CHECK (reserve)
   POST /api/v1/metering/check
   → Atomically reserve estimated_tokens in Redis ZSET
   → Return reservation_id + allowed status

2. LLM CALL (external)
   → Get actual input/output tokens

3a. SUCCESS: FINALIZE
    POST /api/v1/metering/deduct
    → Deduct actual tokens from balance
    → Remove reservation from ZSET
    → Idempotent via request_id

3b. FAILURE: RELEASE
    POST /api/v1/metering/release
    → Remove reservation from ZSET
    → No balance change
```

## Error Codes

| Code                             | HTTP | Description                           |
| -------------------------------- | ---- | ------------------------------------- |
| `INSUFFICIENT_BALANCE`           | 402  | Balance too low for request           |
| `ACCOUNT_SUSPENDED`              | 403  | Account suspended by admin            |
| `USER_MISMATCH`                  | 403  | Request user_id doesn't match JWT     |
| `REQUEST_ID_CONFLICT`            | 409  | Same request_id with different params |
| `ESTIMATED_TOKENS_EXCEEDS_LIMIT` | 402  | Request exceeds model's max_tokens    |

## Testing

```bash
# Run tests
pnpm nx test token-metering-api

# Run tests with coverage
pnpm nx test-coverage token-metering-api

# Run directly with pytest
uv run pytest tests/ -v

# Run with coverage report
uv run pytest tests/ --cov=src/token_metering_api --cov-report=term-missing
```

### Test Coverage

Current coverage: **79%** (265 tests)

| Category              | Tests |
| --------------------- | ----- |
| Core metering service | 22    |
| E2E user journeys     | 34    |
| Edge cases            | 24    |
| v5 balance model      | 47    |
| Caching               | 20    |
| Redis integration     | 29    |
| Authentication        | 27    |
| API endpoints         | 17    |
| Security              | 13    |
| Concurrency           | 10    |
| Spec compliance       | 11    |
| Account service       | 9     |
| Balance endpoints     | 9     |
| Health                | 2     |

## Architecture

```
token-metering-api/
├── src/token_metering_api/
│   ├── core/              # Infrastructure
│   │   ├── auth.py        # JWT validation, dev mode
│   │   ├── cache.py       # Redis read-through cache
│   │   ├── database.py    # PostgreSQL async engine
│   │   ├── rate_limit.py  # slowapi rate limiting
│   │   └── redis.py       # Redis connection, Lua scripts
│   ├── models/            # SQLModel data models
│   │   ├── account.py     # TokenAccount (balance, expiry)
│   │   ├── allocation.py  # TokenAllocation (audit)
│   │   ├── pricing.py     # Model pricing config
│   │   └── transaction.py # TokenTransaction (usage log)
│   ├── routes/            # FastAPI endpoints
│   │   ├── admin.py       # Grant, topup endpoints
│   │   ├── balance.py     # Balance, transactions
│   │   ├── metering.py    # Check, deduct, release
│   │   └── schemas.py     # Request/response models
│   ├── services/          # Business logic
│   │   ├── account.py     # Account creation, cache
│   │   ├── admin.py       # Admin operations
│   │   ├── balance.py     # Balance queries
│   │   ├── metering.py    # Core metering logic
│   │   └── types.py       # TypedDict definitions
│   └── scripts/           # Redis Lua scripts
│       ├── reserve.lua    # Atomic reservation
│       ├── finalize.lua   # Complete reservation
│       └── release.lua    # Cancel reservation
├── tests/                 # 265 tests
├── docker-compose.yaml    # Local development
└── Dockerfile             # Production container
```

## Security

- **JWT authentication** with audience verification
- **Rate limiting** on admin endpoints via slowapi (per-user, Redis-backed)
- **Admin role enforcement** for privileged endpoints
- **Dev mode safety** - blocked in production environment
- **Token limits** on admin operations (max 100M per grant)

## CI/CD

Tests run automatically via `nx affected` on:

- Pull requests to main
- Pushes to main

The CI workflow runs lint, test, and build for affected projects only.

## Related Documentation

- [Specification](../../specs/001-freemium-tracker/spec.md)
- [Data Model](../../specs/001-freemium-tracker/data-model.md)
- [OpenAPI Contract](../../specs/001-freemium-tracker/contracts/openapi.yaml)
- [Quickstart Guide](../../specs/001-freemium-tracker/quickstart.md)
