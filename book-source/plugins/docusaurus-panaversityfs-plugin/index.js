/**
 * Docusaurus PanaversityFS Plugin
 *
 * Fetches educational content from PanaversityFS MCP server via HTTP
 * and writes it to the docs/ folder before Docusaurus processes it.
 *
 * Features:
 * - Fetch all book content at build time using read_content (scope=book)
 * - Write content to docs/ folder for Docusaurus to process
 * - Preserves directory structure from server (content/ -> docs/)
 * - Cleans docs/ folder before writing (when enabled)
 *
 * @param {Object} context - Docusaurus context
 * @param {Object} options - Plugin options
 */
const fs = require('fs');
const path = require('path');
const MCPHttpClient = require('./mcp-http-client');

module.exports = function panaversityFSPlugin(context, options) {
  const {
    bookId = 'ai-native-dev',
    enabled = false, // Disabled by default
    serverUrl = process.env.PANAVERSITY_SERVER_URL || 'http://localhost:8000/mcp',
    docsDir = 'docs', // Output directory relative to siteDir
    cleanDocsDir = true, // Clean docs/ before writing
  } = options;

  const siteDir = context.siteDir;
  const docsPath = path.join(siteDir, docsDir);

  return {
    name: 'docusaurus-panaversityfs-plugin',

    async loadContent() {
      console.log('[PanaversityFS] Plugin starting...');
      console.log(`[PanaversityFS] Book ID: ${bookId}`);
      console.log(`[PanaversityFS] Enabled: ${enabled}`);
      console.log(`[PanaversityFS] Server URL: ${serverUrl}`);
      console.log(`[PanaversityFS] Docs Path: ${docsPath}`);

      if (!enabled) {
        console.log('[PanaversityFS] Plugin disabled, using existing docs/ folder');
        return null;
      }

      // Connect to PanaversityFS MCP server via HTTP
      try {
        const client = new MCPHttpClient({ serverUrl, bookId });

        // Check server availability
        console.log('[PanaversityFS] Checking server availability...');
        const available = await client.ping();
        if (!available) {
          throw new Error(`Server not available at ${serverUrl}`);
        }
        console.log('[PanaversityFS] Server is available');

        // Fetch all content using scope=book (single request, all files)
        console.log('[PanaversityFS] Fetching all book content...');
        const allContent = await client.readBookContent(bookId);
        console.log(`[PanaversityFS] Received ${allContent.length} files from server`);

        // Clean docs/ directory if enabled
        if (cleanDocsDir && fs.existsSync(docsPath)) {
          console.log('[PanaversityFS] Cleaning docs/ directory...');
          fs.rmSync(docsPath, { recursive: true, force: true });
        }

        // Create docs/ directory
        fs.mkdirSync(docsPath, { recursive: true });

        // Write each file to docs/
        let writtenCount = 0;
        for (const file of allContent) {
          // Skip non-markdown files
          if (!file.path?.endsWith('.md')) {
            continue;
          }

          // Transform path: content/01-Part/01-Chapter/lesson.md -> docs/01-Part/01-Chapter/lesson.md
          const relativePath = file.path.replace(/^content\//, '');
          const outputPath = path.join(docsPath, relativePath);
          const outputDir = path.dirname(outputPath);

          // Create directory structure
          fs.mkdirSync(outputDir, { recursive: true });

          // Write the file
          fs.writeFileSync(outputPath, file.content || '', 'utf-8');
          writtenCount++;
        }

        console.log(`[PanaversityFS] Written ${writtenCount} files to ${docsPath}`);

        // Return summary for contentLoaded hook
        return {
          totalFiles: allContent.length,
          writtenFiles: writtenCount,
          source: 'panaversityfs-http',
          serverUrl,
          bookId,
          timestamp: new Date().toISOString(),
        };
      } catch (error) {
        console.error('[PanaversityFS] Error fetching content:', error.message);

        // Check if docs/ exists - if not, this is a fatal error
        if (!fs.existsSync(docsPath)) {
          throw new Error(
            `PanaversityFS failed to fetch content and no docs/ folder exists. ` +
              `Either disable the plugin or ensure the server is running at ${serverUrl}`
          );
        }

        // docs/ exists, warn and continue with existing content
        console.warn('[PanaversityFS] Using existing docs/ folder as fallback');
        return {
          totalFiles: 0,
          writtenFiles: 0,
          source: 'fallback-existing',
          error: error.message,
          timestamp: new Date().toISOString(),
        };
      }
    },

    async contentLoaded({ content, actions }) {
      if (!content || !enabled) {
        return;
      }

      const { createData } = actions;

      // Store build metadata
      await createData('panaversityfs-build.json', JSON.stringify(content, null, 2));

      console.log('[PanaversityFS] Build metadata saved');
      console.log(`[PanaversityFS] Source: ${content.source}`);
      console.log(`[PanaversityFS] Files written: ${content.writtenFiles}`);
    },
  };
};
