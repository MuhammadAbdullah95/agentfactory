/**
 * Docusaurus PanaversityFS Plugin
 *
 * Fetches educational content from PanaversityFS MCP server instead of local filesystem.
 *
 * Features:
 * - Fetch content from PanaversityFS at build time
 * - Cache content locally for fast builds
 * - Support multiple storage backends (local/R2/Supabase)
 * - Preserve frontmatter and metadata
 *
 * @param {Object} context - Docusaurus context
 * @param {Object} options - Plugin options
 */
const MCPClient = require('./mcp-client');

module.exports = function panaversityFSPlugin(context, options) {
  const {
    bookId = 'ai-native-software-development',
    enabled = false, // Disabled by default (POC)
    useMockData = true, // Use mock data for POC
    cacheDir = '.docusaurus/panaversityfs-cache',
    serverPath = '../../panaversity-fs',
    storageBackend = process.env.PANAVERSITY_STORAGE_BACKEND || 'fs',
    storageRoot = process.env.PANAVERSITY_STORAGE_ROOT || '/tmp/panaversity-test',
  } = options;

  let mcpClient = null;

  return {
    name: 'docusaurus-panaversityfs-plugin',

    async loadContent() {
      console.log('[PanaversityFS] Loading content...');
      console.log(`[PanaversityFS] Book ID: ${bookId}`);
      console.log(`[PanaversityFS] Enabled: ${enabled}`);
      console.log(`[PanaversityFS] Mock Data: ${useMockData}`);

      if (!enabled) {
        console.log('[PanaversityFS] Plugin disabled, skipping content loading');
        return null;
      }

      if (useMockData) {
        // POC: Return mock data to test plugin integration
        console.log('[PanaversityFS] Using mock data for POC');
        return {
          lessons: [
            {
              id: 'chapter-02-lesson-01',
              path: '/docs/01-Introducing-AI-Driven-Development/02-ai-turning-point/01-the-inflection-point',
              title: 'The Inflection Point',
              content: '# The Inflection Point\n\nThis is mock content from PanaversityFS plugin.\n\n**Status**: Plugin working! Ready to connect to real MCP server.',
              frontmatter: {
                title: 'The Inflection Point',
                chapter: 2,
                lesson: 1,
              },
            },
          ],
          summary: {
            totalLessons: 1,
            source: 'mock-data',
            timestamp: new Date().toISOString(),
          },
        };
      }

      // Connect to PanaversityFS MCP server
      try {
        console.log('[PanaversityFS] Connecting to MCP server...');
        mcpClient = new MCPClient({
          serverPath,
          storageBackend,
          storageRoot,
        });

        await mcpClient.start();
        console.log('[PanaversityFS] MCP server connected successfully');

        // Fetch all lesson files
        console.log('[PanaversityFS] Searching for lessons...');
        const paths = await mcpClient.globSearch(bookId, '**/*.md');
        console.log(`[PanaversityFS] Found ${paths.length} files`);

        // Read content for each lesson
        const lessons = [];
        for (const path of paths) {
          // Skip README files for now
          if (path.includes('README.md')) {
            continue;
          }

          console.log(`[PanaversityFS] Reading: ${path}`);
          const contentData = await mcpClient.readContent(bookId, path);

          // Extract lesson ID from path (e.g., "02-ai-turning-point/01-the-inflection-point.md")
          const parts = path.split('/');
          const filename = parts[parts.length - 1].replace('.md', '');
          const chapterDir = parts[parts.length - 2];

          lessons.push({
            id: `${chapterDir}-${filename}`,
            path: `/docs/${path.replace('.md', '')}`,
            title: contentData.metadata?.title || filename,
            content: contentData.content,
            frontmatter: contentData.metadata || {},
            sha256: contentData.sha256,
          });
        }

        console.log(`[PanaversityFS] Loaded ${lessons.length} lessons from MCP server`);

        // Stop MCP server
        await mcpClient.stop();
        mcpClient = null;

        return {
          lessons,
          summary: {
            totalLessons: lessons.length,
            source: 'panaversityfs-mcp',
            storageBackend,
            timestamp: new Date().toISOString(),
          },
        };
      } catch (error) {
        console.error('[PanaversityFS] Error connecting to MCP server:', error);

        // Cleanup on error
        if (mcpClient) {
          try {
            await mcpClient.stop();
          } catch (stopError) {
            console.error('[PanaversityFS] Error stopping MCP server:', stopError);
          }
          mcpClient = null;
        }

        // Fall back to mock data on error
        console.log('[PanaversityFS] Falling back to mock data due to error');
        return {
          lessons: [],
          summary: {
            totalLessons: 0,
            source: 'error-fallback',
            error: error.message,
            timestamp: new Date().toISOString(),
          },
        };
      }
    },

    async contentLoaded({ content, actions }) {
      if (!content || !enabled) {
        return;
      }

      console.log(`[PanaversityFS] Content loaded: ${content.lessons.length} lessons`);

      const { createData, addRoute } = actions;

      // Create routes for each lesson
      for (const lesson of content.lessons) {
        const lessonData = await createData(
          `panaversityfs-${lesson.id}.json`,
          JSON.stringify(lesson)
        );

        // Note: In full implementation, this would integrate with Docusaurus docs
        // For POC, we just log that we'd create routes
        console.log(`[PanaversityFS] Would create route: ${lesson.path}`);
      }

      // Store summary data
      const summaryData = await createData(
        'panaversityfs-summary.json',
        JSON.stringify(content.summary)
      );

      console.log('[PanaversityFS] Content loaded successfully');
    },

    getPathsToWatch() {
      // Watch cache directory for changes
      return [cacheDir];
    },

    // Removed getThemePath() - not needed for this plugin
  };
};
