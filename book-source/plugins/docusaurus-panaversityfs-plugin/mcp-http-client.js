/**
 * MCP HTTP Client for Docusaurus Plugin
 *
 * Communicates with PanaversityFS MCP server via Streamable HTTP transport.
 * Does NOT spawn a server process - expects server to be running externally.
 */

class MCPHttpClient {
  constructor(config = {}) {
    this.serverUrl = config.serverUrl || 'http://localhost:8000/mcp';
    this.bookId = config.bookId || 'ai-native-dev';
    this.messageId = 0;
  }

  /**
   * Call an MCP tool via HTTP POST
   * @param {string} toolName - Name of the tool to call
   * @param {Object} params - Tool parameters (wrapped in params object)
   * @returns {Promise<Object>} Tool result
   */
  async callTool(toolName, params = {}) {
    const messageId = ++this.messageId;

    const request = {
      jsonrpc: '2.0',
      id: messageId,
      method: 'tools/call',
      params: {
        name: toolName,
        arguments: { params },  // Server expects params wrapper (Pydantic model)
      },
    };

    console.log(`[MCP HTTP] Calling ${toolName}...`);

    const response = await fetch(this.serverUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
      body: JSON.stringify(request),
    });

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status} ${response.statusText}`);
    }

    const result = await response.json();

    if (result.error) {
      throw new Error(result.error.message || 'Tool call failed');
    }

    // Extract content from MCP response format
    if (result.result?.content?.[0]?.text) {
      return JSON.parse(result.result.content[0].text);
    }

    return result.result;
  }

  /**
   * List all books from server
   * @param {Object} options - List options
   * @returns {Promise<Array>} Array of book entries
   */
  async listBooks(options = {}) {
    return this.callTool('list_books', options);
  }

  /**
   * Read all content from a book using scope=book
   * @param {string} bookId - Book identifier
   * @returns {Promise<Array>} Array of content objects with path, content, file_size, etc.
   */
  async readBookContent(bookId) {
    return this.callTool('read_content', {
      book_id: bookId || this.bookId,
      scope: 'book',
    });
  }

  /**
   * Read a single file from the book
   * @param {string} bookId - Book identifier
   * @param {string} path - File path relative to book root
   * @returns {Promise<Object>} Content object with content, metadata, etc.
   */
  async readContent(bookId, path) {
    return this.callTool('read_content', {
      book_id: bookId || this.bookId,
      path: path,
      scope: 'file',
    });
  }

  /**
   * Search for files matching glob pattern
   * @param {string} bookId - Book identifier
   * @param {string} pattern - Glob pattern (e.g., '**\/*.md')
   * @returns {Promise<Array>} Array of matching file paths
   */
  async globSearch(bookId, pattern) {
    return this.callTool('glob_search', {
      book_id: bookId || this.bookId,
      pattern: pattern || '**/*.md',
    });
  }

  /**
   * Get book archive download URL
   * @param {string} bookId - Book identifier
   * @param {string} scope - Archive scope: 'content', 'assets', or 'all'
   * @returns {Promise<Object>} Archive URL and metadata
   */
  async getBookArchive(bookId, scope = 'content') {
    return this.callTool('get_book_archive', {
      book_id: bookId || this.bookId,
      scope: scope,
    });
  }

  /**
   * Check if server is available
   * @returns {Promise<boolean>} True if server responds
   */
  async ping() {
    try {
      const response = await fetch(this.serverUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
        body: JSON.stringify({
          jsonrpc: '2.0',
          id: 0,
          method: 'tools/list',
          params: {},
        }),
      });
      return response.ok;
    } catch {
      return false;
    }
  }
}

module.exports = MCPHttpClient;
