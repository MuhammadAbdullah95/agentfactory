/**
 * Lesson content loader
 * Reads lesson markdown from filesystem based on URL path
 */

import * as fs from 'fs';
import * as path from 'path';
import type { LessonContext } from '../types';
import { StudyModeError } from '../types';

export interface LessonLoaderConfig {
  docsRoot: string; // Absolute path to docs directory
}

/**
 * Convert URL path to filesystem path
 * Example: "/docs/01-foundations/03-principles/01-intro" -> "01-foundations/03-principles/01-intro.md"
 */
export function urlPathToFilePath(urlPath: string): string {
  // Remove /docs prefix if present
  let cleanPath = urlPath.replace(/^\/docs\/?/, '');

  // Remove trailing slash
  cleanPath = cleanPath.replace(/\/$/, '');

  // The path might be a directory (index.md) or a specific file
  // We'll try both: path.md first, then path/index.md
  return cleanPath;
}

/**
 * Extract title from markdown frontmatter or first heading
 */
export function extractTitle(content: string): string {
  // Try frontmatter title first
  const frontmatterMatch = content.match(/^---\s*\n[\s\S]*?title:\s*["']?([^"'\n]+)["']?\s*\n[\s\S]*?---/);
  if (frontmatterMatch) {
    return frontmatterMatch[1].trim();
  }

  // Fall back to first H1 heading
  const headingMatch = content.match(/^#\s+(.+)$/m);
  if (headingMatch) {
    return headingMatch[1].trim();
  }

  return 'Untitled Lesson';
}

/**
 * Extract chapter and lesson numbers from path
 * Example: "01-foundations/03-principles/01-intro" -> { chapter: 3, lesson: 1 }
 */
export function extractNumbers(urlPath: string): { chapterNumber?: number; lessonNumber?: number } {
  const parts = urlPath.split('/').filter(Boolean);

  // Find parts that start with numbers
  const numberParts = parts
    .map(p => {
      const match = p.match(/^(\d+)-/);
      return match ? parseInt(match[1], 10) : null;
    })
    .filter((n): n is number => n !== null);

  if (numberParts.length >= 2) {
    return {
      chapterNumber: numberParts[numberParts.length - 2],
      lessonNumber: numberParts[numberParts.length - 1],
    };
  }

  if (numberParts.length === 1) {
    return { lessonNumber: numberParts[0] };
  }

  return {};
}

/**
 * Truncate content to fit within context window limits
 * Keeps frontmatter and beginning of content
 */
export function truncateContent(content: string, maxLength: number = 50000): string {
  if (content.length <= maxLength) {
    return content;
  }

  // Find a good break point (end of paragraph)
  const truncated = content.slice(0, maxLength);
  const lastParagraph = truncated.lastIndexOf('\n\n');

  if (lastParagraph > maxLength * 0.8) {
    return truncated.slice(0, lastParagraph) + '\n\n[Content truncated for length]';
  }

  return truncated + '\n\n[Content truncated for length]';
}

export class LessonLoader {
  private config: LessonLoaderConfig;

  constructor(config: LessonLoaderConfig) {
    this.config = config;
  }

  /**
   * Find directory matching a path segment (handles numbered prefixes)
   * e.g., "Building-Custom-Agents" matches "05-Building-Custom-Agents"
   */
  private async findMatchingDir(basePath: string, segment: string): Promise<string | null> {
    try {
      const entries = await fs.promises.readdir(basePath);
      // First try exact match
      if (entries.includes(segment)) {
        return segment;
      }
      // Then try with number prefix pattern (e.g., "05-Building-Custom-Agents")
      const match = entries.find(entry => {
        // Match "NN-segment" pattern
        const pattern = new RegExp(`^\\d+-${segment}$`, 'i');
        return pattern.test(entry);
      });
      return match || null;
    } catch {
      return null;
    }
  }

  /**
   * Resolve URL path to actual filesystem path (handles numbered prefixes)
   */
  private async resolvePathWithPrefixes(urlPath: string): Promise<string> {
    const segments = urlPath.split('/').filter(Boolean);
    let currentPath = this.config.docsRoot;
    const resolvedSegments: string[] = [];

    for (const segment of segments) {
      const match = await this.findMatchingDir(currentPath, segment);
      if (match) {
        resolvedSegments.push(match);
        currentPath = path.join(currentPath, match);
      } else {
        // Keep original segment if no match found
        resolvedSegments.push(segment);
        currentPath = path.join(currentPath, segment);
      }
    }

    return resolvedSegments.join('/');
  }

  /**
   * Load summaries from all chapters within a Part directory
   * Returns concatenated summary content for AI context
   */
  private async loadPartChapterSummaries(partDir: string): Promise<string> {
    try {
      const entries = await fs.promises.readdir(partDir, { withFileTypes: true });
      const chapterDirs = entries
        .filter(e => e.isDirectory() && /^\d+-/.test(e.name))
        .map(e => e.name)
        .sort();

      if (chapterDirs.length === 0) {
        return '';
      }

      const allSummaries: string[] = [];
      for (const chapterName of chapterDirs) {
        const chapterPath = path.join(partDir, chapterName);
        // Extract chapter number and name
        const chapterMatch = chapterName.match(/^(\d+)-(.+)/);
        const chapterLabel = chapterMatch
          ? `Chapter ${parseInt(chapterMatch[1], 10)}: ${chapterMatch[2].replace(/-/g, ' ')}`
          : chapterName;

        const chapterSummaries = await this.loadChapterSummaries(chapterPath);
        if (chapterSummaries) {
          allSummaries.push(`\n=== ${chapterLabel.toUpperCase()} ===\n${chapterSummaries}`);
        }
      }

      if (allSummaries.length > 0) {
        return '\n\n=== PART CONTENT SUMMARIES ===\nThe following summaries cover all chapters and lessons in this part:\n' + allSummaries.join('\n');
      }
      return '';
    } catch {
      return '';
    }
  }

  /**
   * Load all lesson summaries from a chapter directory
   * Returns concatenated summary content for AI context
   */
  private async loadChapterSummaries(chapterDir: string): Promise<string> {
    try {
      const files = await fs.promises.readdir(chapterDir);
      const summaryFiles = files
        .filter(f => f.endsWith('.summary.md'))
        .sort(); // Sort to maintain lesson order

      if (summaryFiles.length === 0) {
        return '';
      }

      const summaries: string[] = [];
      for (const file of summaryFiles) {
        try {
          const content = await fs.promises.readFile(path.join(chapterDir, file), 'utf-8');
          // Extract lesson name from filename (e.g., "03-agents-as-tools.summary.md" -> "Lesson 3")
          const lessonMatch = file.match(/^(\d+)-/);
          const lessonNum = lessonMatch ? `Lesson ${parseInt(lessonMatch[1], 10)}` : file.replace('.summary.md', '');
          summaries.push(`\n--- ${lessonNum} Summary ---\n${content}`);
        } catch {
          // Skip files that can't be read
        }
      }

      if (summaries.length > 0) {
        return '\n\n=== CHAPTER LESSON SUMMARIES ===\nThe following summaries cover all lessons in this chapter:\n' + summaries.join('\n');
      }
      return '';
    } catch {
      return '';
    }
  }

  /**
   * Load full content from a single lesson file (truncated for context)
   */
  private async loadLessonContent(filePath: string, maxChars: number = 3000): Promise<string> {
    try {
      const content = await fs.promises.readFile(filePath, 'utf-8');
      // Remove frontmatter for cleaner content
      const withoutFrontmatter = content.replace(/^---[\s\S]*?---\n*/, '');
      // Truncate if too long
      if (withoutFrontmatter.length > maxChars) {
        return withoutFrontmatter.slice(0, maxChars) + '\n[...truncated]';
      }
      return withoutFrontmatter;
    } catch {
      return '';
    }
  }

  /**
   * Load all lesson content from a chapter directory
   */
  private async loadChapterFullContent(chapterDir: string): Promise<string> {
    try {
      const files = await fs.promises.readdir(chapterDir);
      const lessonFiles = files
        .filter(f => f.endsWith('.md') && !f.endsWith('.summary.md') && f !== 'README.md')
        .sort();

      if (lessonFiles.length === 0) {
        return '';
      }

      const lessons: string[] = [];
      for (const file of lessonFiles) {
        const content = await this.loadLessonContent(path.join(chapterDir, file));
        if (content) {
          const lessonMatch = file.match(/^(\d+)-(.+)\.md$/);
          const lessonLabel = lessonMatch
            ? `Lesson ${parseInt(lessonMatch[1], 10)}: ${lessonMatch[2].replace(/-/g, ' ')}`
            : file.replace('.md', '');
          lessons.push(`\n--- ${lessonLabel} ---\n${content}`);
        }
      }

      return lessons.join('\n');
    } catch {
      return '';
    }
  }

  /**
   * Load all content from chapters within a Part directory
   */
  private async loadPartFullContent(partDir: string): Promise<string> {
    try {
      const entries = await fs.promises.readdir(partDir, { withFileTypes: true });
      const chapterDirs = entries
        .filter(e => e.isDirectory() && /^\d+-/.test(e.name))
        .map(e => e.name)
        .sort();

      if (chapterDirs.length === 0) {
        return '';
      }

      const allChapters: string[] = [];
      for (const chapterName of chapterDirs) {
        const chapterPath = path.join(partDir, chapterName);
        const chapterMatch = chapterName.match(/^(\d+)-(.+)/);
        const chapterLabel = chapterMatch
          ? `Chapter ${parseInt(chapterMatch[1], 10)}: ${chapterMatch[2].replace(/-/g, ' ')}`
          : chapterName;

        const chapterContent = await this.loadChapterFullContent(chapterPath);
        if (chapterContent) {
          allChapters.push(`\n=== ${chapterLabel.toUpperCase()} ===\n${chapterContent}`);
        }
      }

      return allChapters.join('\n');
    } catch {
      return '';
    }
  }

  /**
   * Load full content from ALL Parts in the entire book
   * Used for minimal pages (like thesis) that need full book context
   */
  private async loadAllBookSummaries(): Promise<string> {
    try {
      const entries = await fs.promises.readdir(this.config.docsRoot, { withFileTypes: true });
      const partDirs = entries
        .filter(e => e.isDirectory() && /^\d+-/.test(e.name))
        .map(e => e.name)
        .sort();

      if (partDirs.length === 0) {
        return '';
      }

      const allPartContent: string[] = [];
      for (const partName of partDirs) {
        const partPath = path.join(this.config.docsRoot, partName);
        const partMatch = partName.match(/^(\d+)-(.+)/);
        const partLabel = partMatch
          ? `Part ${parseInt(partMatch[1], 10)}: ${partMatch[2].replace(/-/g, ' ')}`
          : partName;

        const partContent = await this.loadPartFullContent(partPath);
        if (partContent) {
          allPartContent.push(`\n\n========== ${partLabel.toUpperCase()} ==========\n${partContent}`);
        }
      }

      if (allPartContent.length > 0) {
        return '\n\n========== COMPLETE BOOK CONTENT ==========\nThe following content covers ALL parts, chapters, and lessons in the AgentFactory book:\n' + allPartContent.join('\n');
      }
      return '';
    } catch {
      return '';
    }
  }

  /**
   * Load lesson content from filesystem
   * Works with lessons, chapters, parts, and any page with markdown content
   * For chapter README pages, also loads all lesson summaries for context
   */
  async load(urlPath: string): Promise<LessonContext> {
    const relativePath = urlPathToFilePath(urlPath);

    // First, try to resolve path with numbered prefixes
    const resolvedPath = await this.resolvePathWithPrefixes(relativePath);

    // Try different file paths (order matters - most specific first)
    const candidates = [
      // Resolved path variants (with number prefixes)
      path.join(this.config.docsRoot, `${resolvedPath}.md`),
      path.join(this.config.docsRoot, `${resolvedPath}.mdx`),
      path.join(this.config.docsRoot, resolvedPath, 'index.md'),
      path.join(this.config.docsRoot, resolvedPath, 'index.mdx'),
      path.join(this.config.docsRoot, resolvedPath, 'README.md'),
      path.join(this.config.docsRoot, resolvedPath, 'README.mdx'),
      // Original path variants (fallback)
      path.join(this.config.docsRoot, `${relativePath}.md`),
      path.join(this.config.docsRoot, `${relativePath}.mdx`),
      path.join(this.config.docsRoot, relativePath, 'index.md'),
      path.join(this.config.docsRoot, relativePath, 'index.mdx'),
      path.join(this.config.docsRoot, relativePath, 'README.md'),
      path.join(this.config.docsRoot, relativePath, 'README.mdx'),
      // Root level README for parts
      path.join(this.config.docsRoot, resolvedPath.split('/')[0], 'README.md'),
    ];

    let content: string | null = null;
    let foundFilePath: string | null = null;

    for (const candidate of candidates) {
      try {
        content = await fs.promises.readFile(candidate, 'utf-8');
        foundFilePath = candidate;
        break;
      } catch {
        // Try next candidate
      }
    }

    if (!content || !foundFilePath) {
      // Try to find ANY markdown file in the resolved directory as fallback
      try {
        const dirPath = path.join(this.config.docsRoot, resolvedPath);
        const files = await fs.promises.readdir(dirPath);
        const mdFile = files.find(f => f.endsWith('.md') && !f.includes('.summary.'));
        if (mdFile) {
          content = await fs.promises.readFile(path.join(dirPath, mdFile), 'utf-8');
          foundFilePath = path.join(dirPath, mdFile);
        }
      } catch {
        // Directory doesn't exist or can't be read
      }
    }

    if (!content || !foundFilePath) {
      throw new StudyModeError(
        'LESSON_NOT_FOUND',
        `Could not load content for: ${urlPath}`
      );
    }

    // If this is a README, load additional context
    let additionalContent = '';
    if (foundFilePath.endsWith('README.md') || foundFilePath.endsWith('README.mdx')) {
      const dir = path.dirname(foundFilePath);

      // Check if this is a Part-level README (has chapter subdirectories) or Chapter-level
      const entries = await fs.promises.readdir(dir, { withFileTypes: true });
      const hasChapterDirs = entries.some(e => e.isDirectory() && /^\d+-/.test(e.name));

      if (hasChapterDirs) {
        // This is a Part-level README - load summaries from all chapters
        additionalContent = await this.loadPartChapterSummaries(dir);
      } else {
        // This is a Chapter-level README - load lesson summaries
        additionalContent = await this.loadChapterSummaries(dir);
      }
    }

    // If content is too short (< 1000 chars), it's likely a minimal page
    // Load ALL book summaries for full context
    const contentTextOnly = content.replace(/<[^>]*>/g, '').replace(/\{[^}]*\}/g, '').trim();
    if (contentTextOnly.length < 1000 && additionalContent.length === 0) {
      // Load summaries from all Parts in the book
      additionalContent = await this.loadAllBookSummaries();
    }

    const title = extractTitle(content);
    const { chapterNumber, lessonNumber } = extractNumbers(urlPath);
    const fullContent = content + additionalContent;
    const truncatedContent = truncateContent(fullContent);

    return {
      path: urlPath,
      title,
      content: truncatedContent,
      chapterNumber,
      lessonNumber,
    };
  }
}

// Factory function for creating loader with default config
export function createLessonLoader(docsRoot?: string): LessonLoader {
  const root = docsRoot || path.resolve(process.cwd(), 'apps/learn-app/docs');
  return new LessonLoader({ docsRoot: root });
}
