/**
 * Lesson content loader with tiered retrieval
 *
 * Content Loading Priority (strict order):
 * - Tier 1: Current page - FULL content (always)
 * - Tier 2: Explicitly referenced pages - FULL content (if user mentions topic)
 * - Tier 3: Same chapter/part - Summaries
 * - Tier 4: Other book pages - Indexed snippets (on-demand)
 */

import * as fs from 'fs';
import * as path from 'path';
import type { LessonContext } from '../types';
import { StudyModeError } from '../types';

export interface LessonLoaderConfig {
  docsRoot: string; // Absolute path to docs directory
}

export type StudyMode = 'teach' | 'ask';

export interface TieredLoadResult {
  tier1: string;           // Current page (full)
  tier2: string;           // Explicitly referenced content (full)
  tier3: string;           // Same chapter/part summaries
  tier4: string;           // Other book snippets (on-demand)
  referencedTopics: string[]; // Topics detected in user message
}

/**
 * Topic patterns to detect in user messages
 * Maps common terms to their page slugs
 */
interface TopicMatch {
  pattern: RegExp;
  pageSlug: string;
  label: string;
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
  private topicIndex: Map<string, string> = new Map(); // slug -> full path
  private indexBuilt = false;

  constructor(config: LessonLoaderConfig) {
    this.config = config;
  }

  /**
   * Build an index of all topics/pages in the book for Tier 2/4 lookup
   * Run once lazily on first need
   */
  private async buildTopicIndex(): Promise<void> {
    if (this.indexBuilt) return;

    try {
      const parts = await fs.promises.readdir(this.config.docsRoot, { withFileTypes: true });
      for (const part of parts.filter(p => p.isDirectory() && /^\d+-/.test(p.name))) {
        const partPath = path.join(this.config.docsRoot, part.name);
        const chapters = await fs.promises.readdir(partPath, { withFileTypes: true });

        for (const chapter of chapters.filter(c => c.isDirectory() && /^\d+-/.test(c.name))) {
          const chapterPath = path.join(partPath, chapter.name);
          const files = await fs.promises.readdir(chapterPath);

          for (const file of files.filter(f => f.endsWith('.md') && !f.endsWith('.summary.md'))) {
            // Extract slug from filename (e.g., "03-openai-agents-sdk.md" -> "openai-agents-sdk")
            const slugMatch = file.match(/^\d+-(.+)\.md$/);
            const slug = slugMatch ? slugMatch[1] : file.replace('.md', '');

            // Also extract from chapter name
            const chapterSlugMatch = chapter.name.match(/^\d+-(.+)/);
            const chapterSlug = chapterSlugMatch ? chapterSlugMatch[1] : chapter.name;

            // Index by both file slug and keywords
            this.topicIndex.set(slug.toLowerCase(), path.join(chapterPath, file));
            this.topicIndex.set(chapterSlug.toLowerCase(), path.join(chapterPath, 'README.md'));

            // Also index common word variations
            const words = slug.split('-').filter(w => w.length > 3);
            for (const word of words) {
              if (!this.topicIndex.has(word)) {
                this.topicIndex.set(word, path.join(chapterPath, file));
              }
            }
          }
        }
      }
      this.indexBuilt = true;
    } catch {
      // Index build failed, will operate without Tier 2/4
    }
  }

  /**
   * Detect topic references in user message
   * Returns page slugs that match topics mentioned
   */
  private async detectTopicReferences(userMessage: string): Promise<string[]> {
    await this.buildTopicIndex();

    const message = userMessage.toLowerCase();
    const matchedPaths: string[] = [];

    // Check each indexed topic against the message
    for (const [topic, pagePath] of this.topicIndex.entries()) {
      // Only match if it's a meaningful word (not too short)
      if (topic.length > 4 && message.includes(topic)) {
        if (!matchedPaths.includes(pagePath)) {
          matchedPaths.push(pagePath);
        }
      }
    }

    // Limit to top 3 matches to control context size
    return matchedPaths.slice(0, 3);
  }

  /**
   * Load full content from explicitly referenced pages (Tier 2)
   */
  private async loadReferencedContent(pagePaths: string[], currentPagePath: string): Promise<string> {
    if (pagePaths.length === 0) return '';

    const contents: string[] = [];
    for (const pagePath of pagePaths) {
      // Skip if this is the current page
      if (pagePath.includes(currentPagePath)) continue;

      try {
        const content = await fs.promises.readFile(pagePath, 'utf-8');
        const withoutFrontmatter = content.replace(/^---[\s\S]*?---\n*/, '');

        // Extract page slug for labeling
        const fileName = path.basename(pagePath, '.md');
        const slugMatch = fileName.match(/^\d+-(.+)/);
        const slug = slugMatch ? slugMatch[1] : fileName;

        // Truncate each page to fit context (5000 chars each)
        const truncated = withoutFrontmatter.length > 5000
          ? withoutFrontmatter.slice(0, 5000) + '\n[...truncated]'
          : withoutFrontmatter;

        contents.push(`\n--- From: ${slug} ---\n${truncated}`);
      } catch {
        // Skip files that can't be read
      }
    }

    if (contents.length > 0) {
      return '\n\n=== REFERENCED CONTENT (from topics you mentioned) ===\n' + contents.join('\n');
    }
    return '';
  }

  /**
   * Load book-wide summaries for Tier 4 (on-demand, limited)
   * Only used when Tier 1-3 don't have the answer
   */
  private async loadBookSnippets(userMessage: string): Promise<string> {
    // Only load summaries from all chapters (not full content)
    // This is a fallback - keep it lightweight
    try {
      const parts = await fs.promises.readdir(this.config.docsRoot, { withFileTypes: true });
      const partDirs = parts
        .filter(p => p.isDirectory() && /^\d+-/.test(p.name))
        .map(p => p.name)
        .sort();

      const snippets: string[] = [];
      let totalSize = 0;
      const maxSize = 15000; // Limit total Tier 4 content

      for (const partName of partDirs) {
        if (totalSize >= maxSize) break;

        const partPath = path.join(this.config.docsRoot, partName);
        const partSummaries = await this.loadPartChapterSummaries(partPath);

        if (partSummaries) {
          const partMatch = partName.match(/^(\d+)-(.+)/);
          const partLabel = partMatch ? partMatch[2].replace(/-/g, ' ') : partName;

          snippets.push(`\n--- ${partLabel} ---\n${partSummaries.slice(0, 3000)}`);
          totalSize += partSummaries.length;
        }
      }

      if (snippets.length > 0) {
        return '\n\n=== BOOK-WIDE CONTEXT (summaries) ===\n' + snippets.join('\n');
      }
      return '';
    } catch {
      return '';
    }
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
   * Load Tier 1 content (current page - always FULL)
   */
  private async loadTier1Content(urlPath: string): Promise<{ content: string; filePath: string; title: string }> {
    const relativePath = urlPathToFilePath(urlPath);
    const resolvedPath = await this.resolvePathWithPrefixes(relativePath);

    const candidates = [
      path.join(this.config.docsRoot, `${resolvedPath}.md`),
      path.join(this.config.docsRoot, `${resolvedPath}.mdx`),
      path.join(this.config.docsRoot, resolvedPath, 'index.md'),
      path.join(this.config.docsRoot, resolvedPath, 'index.mdx'),
      path.join(this.config.docsRoot, resolvedPath, 'README.md'),
      path.join(this.config.docsRoot, resolvedPath, 'README.mdx'),
      path.join(this.config.docsRoot, `${relativePath}.md`),
      path.join(this.config.docsRoot, `${relativePath}.mdx`),
      path.join(this.config.docsRoot, relativePath, 'index.md'),
      path.join(this.config.docsRoot, relativePath, 'index.mdx'),
      path.join(this.config.docsRoot, relativePath, 'README.md'),
      path.join(this.config.docsRoot, relativePath, 'README.mdx'),
      path.join(this.config.docsRoot, resolvedPath.split('/')[0], 'README.md'),
    ];

    for (const candidate of candidates) {
      try {
        const content = await fs.promises.readFile(candidate, 'utf-8');
        return { content, filePath: candidate, title: extractTitle(content) };
      } catch {
        // Try next
      }
    }

    // Fallback: find any markdown in directory
    try {
      const dirPath = path.join(this.config.docsRoot, resolvedPath);
      const files = await fs.promises.readdir(dirPath);
      const mdFile = files.find(f => f.endsWith('.md') && !f.includes('.summary.'));
      if (mdFile) {
        const content = await fs.promises.readFile(path.join(dirPath, mdFile), 'utf-8');
        return { content, filePath: path.join(dirPath, mdFile), title: extractTitle(content) };
      }
    } catch {
      // Directory doesn't exist
    }

    throw new StudyModeError('LESSON_NOT_FOUND', `Could not load content for: ${urlPath}`);
  }

  /**
   * Load Tier 3 content (same chapter/part summaries)
   */
  private async loadTier3Content(filePath: string): Promise<string> {
    if (filePath.endsWith('README.md') || filePath.endsWith('README.mdx')) {
      const dir = path.dirname(filePath);
      const entries = await fs.promises.readdir(dir, { withFileTypes: true });
      const hasChapterDirs = entries.some(e => e.isDirectory() && /^\d+-/.test(e.name));

      if (hasChapterDirs) {
        return await this.loadPartChapterSummaries(dir);
      } else {
        return await this.loadChapterSummaries(dir);
      }
    }

    // For lesson pages, load sibling lesson summaries
    const chapterDir = path.dirname(filePath);
    return await this.loadChapterSummaries(chapterDir);
  }

  /**
   * Main load method with tiered retrieval
   *
   * @param urlPath - Current page URL path
   * @param userMessage - User's question (for topic detection)
   * @param mode - 'teach' or 'ask' (affects loading strategy)
   */
  async loadWithContext(
    urlPath: string,
    userMessage: string = '',
    mode: StudyMode = 'ask'
  ): Promise<LessonContext> {
    // Tier 1: Current page (always FULL)
    const { content: tier1Content, filePath, title } = await this.loadTier1Content(urlPath);

    // Tier 3: Same chapter/part summaries (lightweight, always load)
    const tier3Content = await this.loadTier3Content(filePath);

    // Tier 2: Referenced content (only if user mentions topics)
    let tier2Content = '';
    if (userMessage && mode === 'ask') {
      // Only do Tier 2 for Ask mode (full book search)
      const referencedPaths = await this.detectTopicReferences(userMessage);
      tier2Content = await this.loadReferencedContent(referencedPaths, urlPath);
    }

    // Tier 4: Book-wide snippets (only for minimal pages or Ask mode with no results)
    let tier4Content = '';
    const contentTextOnly = tier1Content.replace(/<[^>]*>/g, '').replace(/\{[^}]*\}/g, '').trim();
    const isMinimalPage = contentTextOnly.length < 1000 && tier3Content.length === 0;

    if (isMinimalPage || (mode === 'ask' && tier2Content.length === 0 && tier3Content.length < 500)) {
      tier4Content = await this.loadBookSnippets(userMessage);
    }

    // Combine all tiers with clear labels
    const { chapterNumber, lessonNumber } = extractNumbers(urlPath);
    let fullContent = tier1Content;

    if (tier2Content) {
      fullContent += tier2Content;
    }
    if (tier3Content) {
      fullContent += tier3Content;
    }
    if (tier4Content) {
      fullContent += tier4Content;
    }

    return {
      path: urlPath,
      title,
      content: truncateContent(fullContent),
      chapterNumber,
      lessonNumber,
    };
  }

  /**
   * Simple load method (backwards compatible)
   * For basic loading without tiered retrieval
   */
  async load(urlPath: string): Promise<LessonContext> {
    return this.loadWithContext(urlPath, '', 'teach');
  }
}

// Factory function for creating loader with default config
export function createLessonLoader(docsRoot?: string): LessonLoader {
  const root = docsRoot || path.resolve(process.cwd(), 'apps/learn-app/docs');
  return new LessonLoader({ docsRoot: root });
}
