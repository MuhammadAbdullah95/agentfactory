#!/usr/bin/env python3
"""Migration script: book-source → Supabase Storage.

This script uploads content from the Docusaurus book-source structure
directly to Supabase Storage (not local filesystem).

Source structure (book-source/):
    docs/
        {NN-Part}/
            README.md
            {NN-Chapter}/
                README.md
                {NN-lesson}.md
    static/
        img/
        slides/

Target structure (Supabase bucket):
    books/{book-id}/
        content/                    # Maps to docs/
            {NN-Part}/
                README.md
                {NN-Chapter}/
                    README.md
                    {NN-lesson}.md
        static/                     # Maps to static/
            images/                 # Renamed from img/
            slides/

Environment variables:
    PANAVERSITY_SUPABASE_URL       - Supabase project URL
    PANAVERSITY_SUPABASE_SERVICE_ROLE_KEY - Service role key (NOT anon key)
    PANAVERSITY_SUPABASE_BUCKET    - Storage bucket name

Usage:
    # First, ensure correct Supabase key format in .env:
    # PANAVERSITY_SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

    # Dry run (preview changes)
    uv run python scripts/migrate_to_supabase.py --dry-run

    # Migrate content only
    uv run python scripts/migrate_to_supabase.py --content-only

    # Migrate assets only
    uv run python scripts/migrate_to_supabase.py --assets-only

    # Full migration with URL rewriting (recommended)
    uv run python scripts/migrate_to_supabase.py --rewrite-urls

    # With verbose output
    uv run python scripts/migrate_to_supabase.py --verbose

    # Resume from a specific path (for large migrations)
    uv run python scripts/migrate_to_supabase.py --resume-from "03-Markdown"
"""

import argparse
import mimetypes
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

# Load .env file
load_dotenv()


@dataclass
class MigrationStats:
    """Track migration statistics."""
    content_uploaded: int = 0
    content_skipped: int = 0
    content_failed: int = 0
    assets_uploaded: int = 0
    assets_skipped: int = 0
    assets_failed: int = 0
    urls_rewritten: int = 0
    bytes_uploaded: int = 0
    errors: list = field(default_factory=list)

    def summary(self) -> str:
        mb = self.bytes_uploaded / (1024 * 1024)
        return f"""
Migration Summary
=================
Content:
  Uploaded: {self.content_uploaded}
  Skipped:  {self.content_skipped}
  Failed:   {self.content_failed}

Assets:
  Uploaded: {self.assets_uploaded}
  Skipped:  {self.assets_skipped}
  Failed:   {self.assets_failed}

URLs Rewritten: {self.urls_rewritten}
Total Size: {mb:.2f} MB
Errors: {len(self.errors)}
"""


@dataclass
class MigrationConfig:
    """Migration configuration."""
    source_dir: Path
    book_id: str
    supabase_url: str
    supabase_key: str
    supabase_bucket: str
    dry_run: bool = False
    content_only: bool = False
    assets_only: bool = False
    rewrite_urls: bool = False
    verbose: bool = False
    resume_from: Optional[str] = None

    @property
    def docs_path(self) -> Path:
        return self.source_dir / "docs"

    @property
    def static_path(self) -> Path:
        return self.source_dir / "static"

    @property
    def cdn_base_url(self) -> str:
        """Supabase public URL for assets."""
        return f"{self.supabase_url}/storage/v1/object/public/{self.supabase_bucket}"


class SupabaseMigrator:
    """Migrate book-source to Supabase Storage."""

    def __init__(self, config: MigrationConfig):
        self.config = config
        self.stats = MigrationStats()
        self.client = None
        self.resumed = not bool(config.resume_from)

        # Directory mapping (img → images for ADR-0018 compliance)
        self.dir_mapping = {
            "img": "images"
        }

    def connect(self):
        """Initialize Supabase client."""
        if self.config.dry_run:
            print("[DRY RUN] Would connect to Supabase")
            return

        try:
            from supabase import create_client
            self.client = create_client(
                self.config.supabase_url,
                self.config.supabase_key
            )
            print(f"✓ Connected to Supabase: {self.config.supabase_url}")
        except ImportError:
            print("ERROR: supabase package not installed")
            print("Run: uv add supabase")
            sys.exit(1)
        except Exception as e:
            print(f"ERROR: Failed to connect to Supabase: {e}")
            sys.exit(1)

    def should_skip(self, path: Path) -> bool:
        """Check if file should be skipped."""
        # Skip hidden files/dirs
        if any(part.startswith('.') for part in path.parts):
            return True
        # Skip node_modules
        if 'node_modules' in path.parts:
            return True
        return False

    def check_resume(self, path: Path) -> bool:
        """Check if we should process this file (resume logic)."""
        if self.resumed:
            return True
        if self.config.resume_from and self.config.resume_from in str(path):
            self.resumed = True
            print(f"Resuming from: {path}")
            return True
        return False

    def get_storage_path(self, local_path: Path, content_type: str) -> str:
        """Convert local path to Supabase storage path.

        Args:
            local_path: Local file path
            content_type: 'content' or 'static'

        Returns:
            Storage path like 'books/ai-native-dev/content/...'
        """
        if content_type == "content":
            rel_path = local_path.relative_to(self.config.docs_path)
            return f"books/{self.config.book_id}/content/{rel_path}"
        elif content_type == "static":
            rel_path = local_path.relative_to(self.config.static_path)
            # Apply directory mapping (img → images)
            parts = list(rel_path.parts)
            if parts and parts[0] in self.dir_mapping:
                parts[0] = self.dir_mapping[parts[0]]
            mapped_path = Path(*parts)
            return f"books/{self.config.book_id}/static/{mapped_path}"
        else:
            raise ValueError(f"Unknown content type: {content_type}")

    def rewrite_image_urls(self, content: str) -> tuple[str, int]:
        """Rewrite local image URLs to Supabase CDN URLs.

        Transforms these patterns:
        - /img/part-1/... → {cdn}/books/{book_id}/static/images/part-1/...
        - /slides/... → {cdn}/books/{book_id}/static/slides/...
        - ./images/... → {cdn}/books/{book_id}/static/images/...

        Skips external URLs (http://, https://).

        Returns:
            Tuple of (modified content, number of URLs rewritten)
        """
        count = 0
        cdn_base = self.config.cdn_base_url

        def replace_url(match):
            nonlocal count
            alt_text = match.group(1)
            url = match.group(2)

            # Skip external URLs
            if url.startswith('http://') or url.startswith('https://'):
                return match.group(0)

            # Handle different path patterns
            new_url = None

            # Pattern 1: /img/... → static/images/...
            if url.startswith('/img/'):
                rel_path = url[5:]  # Remove '/img/'
                new_url = f"{cdn_base}/books/{self.config.book_id}/static/images/{rel_path}"

            # Pattern 2: /slides/... → static/slides/...
            elif url.startswith('/slides/'):
                rel_path = url[8:]  # Remove '/slides/'
                new_url = f"{cdn_base}/books/{self.config.book_id}/static/slides/{rel_path}"

            # Pattern 3: ./images/... or ./img/... (relative)
            elif url.startswith('./images/') or url.startswith('./img/'):
                rel_path = url.split('/', 2)[-1] if '/' in url else url
                new_url = f"{cdn_base}/books/{self.config.book_id}/static/images/{rel_path}"

            # Pattern 4: Plain filename (screenshot.png)
            elif '/' not in url and url.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')):
                new_url = f"{cdn_base}/books/{self.config.book_id}/static/images/{url}"

            if new_url:
                count += 1
                return f"![{alt_text}]({new_url})"

            # Return unchanged if pattern not recognized
            return match.group(0)

        # Match markdown image syntax: ![alt](url)
        pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        new_content = re.sub(pattern, replace_url, content)

        return new_content, count

    def upload_file(self, local_path: Path, storage_path: str, content_type: str) -> bool:
        """Upload a single file to Supabase Storage.

        Args:
            local_path: Local file path
            storage_path: Target path in Supabase storage
            content_type: MIME type hint ('text/markdown' or auto-detect)

        Returns:
            True if successful, False otherwise
        """
        if self.config.dry_run:
            size = local_path.stat().st_size
            size_str = f"{size / 1024:.1f} KB" if size < 1024 * 1024 else f"{size / (1024*1024):.2f} MB"
            print(f"  [DRY RUN] {storage_path} ({size_str})")
            self.stats.bytes_uploaded += size
            return True

        try:
            content = local_path.read_bytes()

            # Determine MIME type
            if content_type == "text/markdown":
                mime_type = "text/markdown"
            else:
                mime_type, _ = mimetypes.guess_type(str(local_path))
                mime_type = mime_type or "application/octet-stream"

            # Upload to Supabase with upsert
            result = self.client.storage.from_(self.config.supabase_bucket).upload(
                storage_path,
                content,
                file_options={"content-type": mime_type, "upsert": "true"}
            )

            size = len(content)
            self.stats.bytes_uploaded += size

            if self.config.verbose:
                size_str = f"{size / 1024:.1f} KB" if size < 1024 * 1024 else f"{size / (1024*1024):.2f} MB"
                print(f"  ✓ {storage_path} ({size_str})")

            return True

        except Exception as e:
            self.stats.errors.append(f"{storage_path}: {e}")
            if self.config.verbose:
                print(f"  ✗ {storage_path}: {e}")
            return False

    def upload_content_with_rewrite(self, local_path: Path, storage_path: str) -> bool:
        """Upload markdown content, optionally rewriting image URLs.

        Args:
            local_path: Local markdown file path
            storage_path: Target path in Supabase storage

        Returns:
            True if successful, False otherwise
        """
        try:
            # Read content as text
            content = local_path.read_text(encoding='utf-8')

            # Apply URL rewriting if enabled
            if self.config.rewrite_urls:
                content, url_count = self.rewrite_image_urls(content)
                self.stats.urls_rewritten += url_count
                if url_count > 0 and self.config.verbose:
                    print(f"    Rewrote {url_count} URLs in {local_path.name}")

            if self.config.dry_run:
                size = len(content.encode('utf-8'))
                size_str = f"{size / 1024:.1f} KB" if size < 1024 * 1024 else f"{size / (1024*1024):.2f} MB"
                print(f"  [DRY RUN] {storage_path} ({size_str})")
                self.stats.bytes_uploaded += size
                return True

            # Upload to Supabase
            content_bytes = content.encode('utf-8')
            result = self.client.storage.from_(self.config.supabase_bucket).upload(
                storage_path,
                content_bytes,
                file_options={"content-type": "text/markdown", "upsert": "true"}
            )

            size = len(content_bytes)
            self.stats.bytes_uploaded += size

            if self.config.verbose:
                size_str = f"{size / 1024:.1f} KB" if size < 1024 * 1024 else f"{size / (1024*1024):.2f} MB"
                print(f"  ✓ {storage_path} ({size_str})")

            return True

        except Exception as e:
            self.stats.errors.append(f"{storage_path}: {e}")
            if self.config.verbose:
                print(f"  ✗ {storage_path}: {e}")
            return False

    def migrate_content(self):
        """Migrate all markdown content from docs/."""
        print("\n=== Migrating Content ===")
        if self.config.rewrite_urls:
            print("  URL rewriting: ENABLED")

        if not self.config.docs_path.exists():
            print(f"  ⚠ Source docs directory not found: {self.config.docs_path}")
            return

        # Find all markdown files
        md_files = list(self.config.docs_path.rglob("*.md"))
        mdx_files = list(self.config.docs_path.rglob("*.mdx"))
        all_files = sorted(md_files + mdx_files)

        total = len(all_files)
        print(f"  Found {total} markdown files")

        for i, md_file in enumerate(all_files):
            if self.should_skip(md_file):
                continue

            if not self.check_resume(md_file):
                self.stats.content_skipped += 1
                continue

            storage_path = self.get_storage_path(md_file, "content")

            if not self.config.verbose:
                # Progress indicator
                print(f"\r  Uploading: {i+1}/{total}", end="", flush=True)

            # Use upload_content_with_rewrite for markdown files (handles URL rewriting)
            if self.upload_content_with_rewrite(md_file, storage_path):
                self.stats.content_uploaded += 1
            else:
                self.stats.content_failed += 1

        if not self.config.verbose:
            print()  # Newline after progress

        print(f"  ✓ Uploaded: {self.stats.content_uploaded}")
        if self.stats.content_failed:
            print(f"  ✗ Failed: {self.stats.content_failed}")
        if self.config.rewrite_urls and self.stats.urls_rewritten > 0:
            print(f"  ↻ URLs rewritten: {self.stats.urls_rewritten}")

    def migrate_assets(self):
        """Migrate all static assets from static/."""
        print("\n=== Migrating Assets ===")

        if not self.config.static_path.exists():
            print(f"  ⚠ Source static directory not found: {self.config.static_path}")
            return

        # Asset file extensions to include
        asset_extensions = {
            '.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.ico',
            '.pdf', '.pptx', '.ppt',
            '.mp4', '.webm', '.mov',
            '.mp3', '.wav', '.ogg'
        }

        # Find all asset files
        all_files = []
        for ext in asset_extensions:
            all_files.extend(self.config.static_path.rglob(f"*{ext}"))
        all_files = sorted(all_files)

        total = len(all_files)
        print(f"  Found {total} asset files")

        for i, asset_file in enumerate(all_files):
            if self.should_skip(asset_file):
                continue

            if not self.check_resume(asset_file):
                self.stats.assets_skipped += 1
                continue

            storage_path = self.get_storage_path(asset_file, "static")

            if not self.config.verbose:
                # Progress indicator
                print(f"\r  Uploading: {i+1}/{total}", end="", flush=True)

            if self.upload_file(asset_file, storage_path, "auto"):
                self.stats.assets_uploaded += 1
            else:
                self.stats.assets_failed += 1

        if not self.config.verbose:
            print()  # Newline after progress

        print(f"  ✓ Uploaded: {self.stats.assets_uploaded}")
        if self.stats.assets_failed:
            print(f"  ✗ Failed: {self.stats.assets_failed}")

    def run(self):
        """Run the migration."""
        print(f"""
{'='*60}
Supabase Migration (ADR-0018)
{'='*60}
Source:      {self.config.source_dir}
Target:      {self.config.supabase_bucket}/books/{self.config.book_id}/
Mode:        {'DRY RUN' if self.config.dry_run else 'LIVE'}
Content:     {'Yes' if not self.config.assets_only else 'No'}
Assets:      {'Yes' if not self.config.content_only else 'No'}
Rewrite URLs: {'Yes' if self.config.rewrite_urls else 'No'}
Resume:      {self.config.resume_from or 'From beginning'}
{'='*60}
""")

        self.connect()

        if not self.config.assets_only:
            self.migrate_content()

        if not self.config.content_only:
            self.migrate_assets()

        print(self.stats.summary())

        if self.stats.errors:
            print("\nErrors (first 10):")
            for error in self.stats.errors[:10]:
                print(f"  - {error}")
            if len(self.stats.errors) > 10:
                print(f"  ... and {len(self.stats.errors) - 10} more")

        # Print CDN URL info
        if not self.config.dry_run:
            print(f"""
Next Steps
==========
1. Update your .env to use Supabase CDN URL:
   PANAVERSITY_CDN_BASE_URL={self.config.cdn_base_url}

2. Access content via:
   {self.config.cdn_base_url}/books/{self.config.book_id}/content/...

3. Access assets via:
   {self.config.cdn_base_url}/books/{self.config.book_id}/static/images/...
   {self.config.cdn_base_url}/books/{self.config.book_id}/static/slides/...
""")

        return self.stats


def main():
    parser = argparse.ArgumentParser(
        description="Migrate book-source to Supabase Storage",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument(
        "--source",
        type=Path,
        default=Path(__file__).parent.parent.parent / "book-source",
        help="Source book-source directory (default: ../book-source)"
    )

    parser.add_argument(
        "--book-id",
        type=str,
        default="ai-native-dev",
        help="Book identifier (default: ai-native-dev)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without uploading"
    )

    parser.add_argument(
        "--content-only",
        action="store_true",
        help="Only upload markdown content (skip assets)"
    )

    parser.add_argument(
        "--assets-only",
        action="store_true",
        help="Only upload assets (skip content)"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed output"
    )

    parser.add_argument(
        "--resume-from",
        type=str,
        help="Resume from files containing this string"
    )

    parser.add_argument(
        "--rewrite-urls",
        action="store_true",
        help="Rewrite local image URLs (/img/...) to Supabase CDN URLs"
    )

    args = parser.parse_args()

    # Validate source exists
    if not args.source.exists():
        print(f"ERROR: Source directory not found: {args.source}")
        sys.exit(1)

    # Load Supabase config from environment
    supabase_url = os.getenv("PANAVERSITY_SUPABASE_URL", "")
    supabase_key = os.getenv("PANAVERSITY_SUPABASE_SERVICE_ROLE_KEY", "")
    supabase_bucket = os.getenv("PANAVERSITY_SUPABASE_BUCKET", "panaversity-books")

    # Validate config (unless dry run)
    if not args.dry_run:
        if not supabase_url:
            print("ERROR: PANAVERSITY_SUPABASE_URL not set")
            sys.exit(1)
        if not supabase_key:
            print("ERROR: PANAVERSITY_SUPABASE_SERVICE_ROLE_KEY not set")
            sys.exit(1)
        if not supabase_key.startswith("eyJ"):
            print("ERROR: PANAVERSITY_SUPABASE_SERVICE_ROLE_KEY appears invalid")
            print("       Service role key should start with 'eyJ' (JWT format)")
            print("       Get it from: Supabase Dashboard → Project Settings → API")
            sys.exit(1)

    config = MigrationConfig(
        source_dir=args.source,
        book_id=args.book_id,
        supabase_url=supabase_url,
        supabase_key=supabase_key,
        supabase_bucket=supabase_bucket,
        dry_run=args.dry_run,
        content_only=args.content_only,
        assets_only=args.assets_only,
        rewrite_urls=args.rewrite_urls,
        verbose=args.verbose,
        resume_from=args.resume_from,
    )

    migrator = SupabaseMigrator(config)
    stats = migrator.run()

    # Exit with error if there were failures
    if stats.content_failed or stats.assets_failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
