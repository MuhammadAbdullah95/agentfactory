# PanaversityFS

MCP server for educational content management with multi-backend storage support.

## Features

- **12 MCP Tools**: Content, summaries, assets, search, bulk operations
- **3 Storage Backends**: Local filesystem, Cloudflare R2, Supabase
- **52 Tests**: Unit, integration, e2e, edge cases (100% passing)

## Quick Start

```bash
# Install
cd panaversity-fs && uv sync

# Configure
export PANAVERSITY_STORAGE_BACKEND=fs
export PANAVERSITY_STORAGE_ROOT=/tmp/panaversity-test

# Test
uv run pytest tests/ -q
# Expected: 52 passed
```

## MCP Tools

| Category | Tools |
|----------|-------|
| Content | `read_content`, `write_content`, `delete_content` |
| Summaries | `read_summary`, `write_summary`, `delete_summary` |
| Assets | `upload_asset`, `get_asset`, `list_assets` |
| Search | `glob_search`, `grep_search` |
| Registry | `list_books` |
| Bulk | `get_book_archive` |

## Project Structure

```
panaversity-fs/
├── src/panaversity_fs/
│   ├── server.py      # MCP server entry point
│   ├── config.py      # Backend configuration
│   ├── models.py      # Pydantic models
│   ├── storage.py     # OpenDAL abstraction
│   └── tools/         # 14 MCP tool implementations
├── tests/
│   ├── unit/          # 18 component tests
│   ├── integration/   # 15 workflow tests
│   ├── e2e/           # 12 end-to-end tests
│   └── edge_cases/    # 10 error handling tests
└── docs/
    └── SETUP.md       # Backend setup guide
```

## Storage Backends

### Local Filesystem (Default)
```bash
export PANAVERSITY_STORAGE_BACKEND=fs
export PANAVERSITY_STORAGE_ROOT=/tmp/panaversity-data
```

### Cloudflare R2
```bash
export PANAVERSITY_STORAGE_BACKEND=s3
export PANAVERSITY_S3_BUCKET=your-bucket
export PANAVERSITY_S3_ENDPOINT=https://xxx.r2.cloudflarestorage.com
export PANAVERSITY_S3_ACCESS_KEY_ID=your-key
export PANAVERSITY_S3_SECRET_ACCESS_KEY=your-secret
export PANAVERSITY_S3_REGION=auto
```

### Supabase
```bash
export PANAVERSITY_STORAGE_BACKEND=supabase
export PANAVERSITY_SUPABASE_URL=https://xxx.supabase.co
export PANAVERSITY_SUPABASE_ANON_KEY=your-key
export PANAVERSITY_SUPABASE_SERVICE_ROLE_KEY=your-service-key
export PANAVERSITY_SUPABASE_BUCKET=panaversity-books
```

See [docs/SETUP.md](docs/SETUP.md) for detailed setup instructions.

## Running Tests

```bash
# All tests
uv run pytest tests/ -v

# By category
uv run pytest tests/unit/ -v
uv run pytest tests/integration/ -v
uv run pytest tests/e2e/ -v
uv run pytest tests/edge_cases/ -v
```

## Architecture

- **FastMCP**: Python MCP framework
- **OpenDAL**: Unified storage abstraction
- **Pydantic v2**: Request/response validation
- **pytest-asyncio**: Async test support

## License

MIT
