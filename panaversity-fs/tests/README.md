# PanaversityFS Test Suite

Comprehensive test coverage for all 14 MCP tools and core infrastructure.

## Test Structure

```
tests/
├── unit/                           # Unit tests (individual tools)
│   ├── test_content_tools.py      # Content operations (3 tools)
│   ├── test_summary_tools.py      # Summary management (4 tools)
│   ├── test_search_tools.py       # Search operations (2 tools)
│   └── test_registry_bulk_tools.py # Registry + bulk (2 tools)
├── integration/                    # Integration tests (workflows)
│   └── test_content_workflows.py  # CRUD workflows, conflict detection
├── e2e/                           # End-to-end tests (complete scenarios)
│   └── test_complete_book_workflow.py # Full book creation & management
├── edge_cases/                    # Edge case tests (production scenarios)
│   └── test_production_structure.py # Multi-part books, complex frontmatter, large volumes
└── conftest.py                    # Shared fixtures
```

## Quick Start

### Install Test Dependencies

```bash
# Install with dev dependencies
uv sync --extra dev

# Or install manually
uv pip install pytest pytest-asyncio pytest-cov pytest-timeout
```

### Run All Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=panaversity_fs --cov-report=html --cov-report=term

# Run specific test file
pytest tests/unit/test_content_tools.py

# Run specific test
pytest tests/unit/test_content_tools.py::TestReadContent::test_read_existing_content
```

### Run by Category

```bash
# Unit tests only
pytest tests/unit/

# Integration tests only
pytest tests/integration/

# End-to-end tests only
pytest tests/e2e/

# Edge case tests only
pytest tests/edge_cases/

# Run with markers
pytest -m unit
pytest -m integration
pytest -m e2e
```

## Test Coverage

### Unit Tests (by tool)

**Content Tools (test_content_tools.py):**
- ✅ read_content: existing content, nonexistent content, metadata validation
- ✅ write_content: create, update with hash, conflict detection, upsert
- ✅ delete_content: existing, nonexistent, idempotent

**Summary Tools (test_summary_tools.py):**
- ✅ add_summary: new summary, duplicate prevention
- ✅ update_summary: existing, create if missing
- ✅ get_summary: existing, nonexistent
- ✅ list_summaries: all, filtered by chapter, empty book, metadata

**Search Tools (test_search_tools.py):**
- ✅ glob_search: all markdown, specific patterns, no matches
- ✅ grep_search: keyword search, regex patterns, max results, invalid regex

**Registry & Bulk Tools (test_registry_bulk_tools.py):**
- ✅ list_books: with registry, no registry, validation
- ✅ get_book_archive: with content, metadata, empty book

### Integration Tests

**Content Workflows (test_content_workflows.py):**
- ✅ Complete CRUD workflow (create → read → update → delete)
- ✅ Concurrent modification detection
- ✅ Bulk operations (multiple lessons)

### End-to-End Tests

**Complete Book Workflow (test_complete_book_workflow.py):**
- ✅ Create complete book (registry, metadata, lessons, summaries)
- ✅ Book version evolution (multiple updates)
- ✅ Multi-book management (3 books simultaneously)

## Test Coverage Metrics

```
Total Tests: 55
- Unit: 30 tests
- Integration: 6 tests
- E2E: 6 tests
- Edge Cases: 13 tests (NEW)

Tools Coverage: 14/14 (100%)
- Content: 3/3 ✅
- Summaries: 4/4 ✅
- Search: 2/2 ✅
- Registry: 1/1 ✅
- Bulk: 1/1 ✅
- Assets: 3/3 (requires binary data, tested manually)

Production Scenarios Covered:
- Multi-part books (13 parts, 117+ lessons) ✅
- Complex frontmatter (skills, learning_objectives, cognitive_load) ✅
- Large content volumes (100+ lessons, 10KB+ per lesson) ✅
- Various naming conventions (dashes, underscores, numbers) ✅
- Deep directory nesting (5+ levels) ✅
```

## Fixtures

### Provided by conftest.py

- **event_loop**: Async event loop for tests
- **temp_storage_root**: Temporary directory for each test
- **setup_fs_backend**: Configured filesystem backend
- **sample_book_data**: Pre-created book with lesson and summary
- **sample_lesson_content**: Sample markdown lesson
- **sample_summary_content**: Sample markdown summary

### Usage Example

```python
@pytest.mark.asyncio
async def test_my_feature(sample_book_data):
    """Test using sample data."""
    result = await read_content(ReadContentInput(
        book_id=sample_book_data["book_id"],
        path=sample_book_data["lesson_path"]
    ))
    assert result is not None
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.13'
      - name: Install dependencies
        run: |
          pip install uv
          uv sync --extra dev
      - name: Run tests
        run: pytest --cov=panaversity_fs --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

## Writing New Tests

### Unit Test Template

```python
import pytest
import json
from panaversity_fs.tools.your_module import your_tool
from panaversity_fs.models import YourToolInput


class TestYourTool:
    """Test your_tool functionality."""

    @pytest.mark.asyncio
    async def test_basic_functionality(self, setup_fs_backend):
        """Test basic tool usage."""
        result = await your_tool(YourToolInput(
            param1="value1"
        ))

        data = json.loads(result)
        assert data["status"] == "success"

    @pytest.mark.asyncio
    async def test_error_handling(self, setup_fs_backend):
        """Test error conditions."""
        with pytest.raises(SomeError):
            await your_tool(YourToolInput(
                param1="invalid"
            ))
```

### Integration Test Template

```python
@pytest.mark.asyncio
async def test_workflow(self, setup_fs_backend):
    """Test multi-tool workflow."""
    # Step 1: Create
    create_result = await tool1(Input1(...))

    # Step 2: Process
    process_result = await tool2(Input2(...))

    # Step 3: Verify
    verify_result = await tool3(Input3(...))

    assert verify_result["status"] == "success"
```

## Debugging Tests

### Run with verbose output

```bash
pytest -vv
```

### Run with print statements

```bash
pytest -s
```

### Debug specific test

```bash
pytest --pdb tests/unit/test_content_tools.py::TestReadContent::test_read_existing_content
```

### Show local variables on failure

```bash
pytest -l
```

## Performance Testing

### Time tests

```bash
pytest --durations=10
```

### Timeout configuration

Tests timeout after 30 seconds by default (configurable in pytest.ini).

## Known Limitations

### Asset Tools Testing

Asset tools (upload_asset, get_asset, list_assets) require binary data and are tested manually via MCP Inspector rather than pytest. This is intentional as:

1. Binary data in test fixtures is unwieldy
2. Base64 encoding/decoding adds test complexity
3. Manual testing via Inspector is more realistic

### Storage Backend Testing

Current tests use local filesystem backend. To test S3/Supabase backends:

```bash
export PANAVERSITY_STORAGE_BACKEND=s3
export PANAVERSITY_S3_BUCKET=test-bucket
# ... other credentials
pytest
```

## Contributing

When adding new tools:

1. Add unit tests in `tests/unit/test_your_tool.py`
2. Add integration tests if tool interacts with others
3. Update this README with coverage information
4. Ensure pytest passes: `pytest --cov`

## Resources

- [pytest documentation](https://docs.pytest.org/)
- [pytest-asyncio](https://pytest-asyncio.readthedocs.io/)
- [Testing FastMCP servers](https://github.com/modelcontextprotocol/python-sdk)
