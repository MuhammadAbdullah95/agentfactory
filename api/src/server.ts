/**
 * Study Mode API Server
 *
 * Standalone HTTP server for development and production.
 * Can also be imported for serverless deployment.
 */

import { createServer, IncomingMessage, ServerResponse } from 'http';
import { handleChat } from './handlers/chat';
import {
  createOpenAIProvider,
  createAnthropicProvider,
  createMockProvider,
  type AIProvider,
} from './services/ai-provider';
import { createLessonLoader, LessonLoader } from './services/lesson-loader';
import { RateLimiter } from './services/rate-limiter';

// =============================================================================
// Configuration
// =============================================================================

interface ServerConfig {
  port: number;
  aiProvider: AIProvider & { name?: string };
  lessonLoader: LessonLoader;
  rateLimiter: RateLimiter;
}

function loadConfig(): ServerConfig {
  const provider = process.env.AI_PROVIDER || 'mock';
  const contentPath = process.env.CONTENT_BASE_PATH || '../apps/learn-app/docs';
  const rateLimit = parseInt(process.env.RATE_LIMIT_REQUESTS_PER_HOUR || '60', 10);
  const port = parseInt(process.env.PORT || '3001', 10);

  // Create AI provider based on configuration
  let aiProvider: AIProvider & { name?: string };
  switch (provider) {
    case 'openai':
      if (!process.env.OPENAI_API_KEY) {
        console.warn('OPENAI_API_KEY not set, falling back to mock provider');
        aiProvider = createMockProvider();
      } else {
        aiProvider = createOpenAIProvider(
          process.env.OPENAI_API_KEY,
          process.env.OPENAI_MODEL || 'gpt-4o-mini'
        );
      }
      break;
    case 'anthropic':
      if (!process.env.ANTHROPIC_API_KEY) {
        console.warn('ANTHROPIC_API_KEY not set, falling back to mock provider');
        aiProvider = createMockProvider();
      } else {
        aiProvider = createAnthropicProvider(
          process.env.ANTHROPIC_API_KEY,
          process.env.ANTHROPIC_MODEL || 'claude-3-haiku-20240307'
        );
      }
      break;
    default:
      aiProvider = createMockProvider();
  }

  return {
    port,
    aiProvider,
    lessonLoader: createLessonLoader(contentPath),
    rateLimiter: new RateLimiter({ maxRequests: rateLimit }),
  };
}

// =============================================================================
// Request Handler
// =============================================================================

function getClientIP(req: IncomingMessage): string {
  // Check common proxy headers
  const forwarded = req.headers['x-forwarded-for'];
  if (forwarded) {
    const ips = Array.isArray(forwarded) ? forwarded[0] : forwarded;
    return ips.split(',')[0].trim();
  }

  const realIP = req.headers['x-real-ip'];
  if (realIP) {
    return Array.isArray(realIP) ? realIP[0] : realIP;
  }

  return req.socket.remoteAddress || '127.0.0.1';
}

function parseBody(req: IncomingMessage): Promise<unknown> {
  return new Promise((resolve, reject) => {
    let body = '';
    req.on('data', (chunk) => {
      body += chunk.toString();
      // Limit body size to 1MB
      if (body.length > 1024 * 1024) {
        reject(new Error('Body too large'));
      }
    });
    req.on('end', () => {
      try {
        resolve(body ? JSON.parse(body) : null);
      } catch {
        reject(new Error('Invalid JSON'));
      }
    });
    req.on('error', reject);
  });
}

function sendJSON(res: ServerResponse, status: number, data: unknown): void {
  res.writeHead(status, {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
  });
  res.end(JSON.stringify(data));
}

function createRequestHandler(config: ServerConfig) {
  return async (req: IncomingMessage, res: ServerResponse): Promise<void> => {
    const url = new URL(req.url || '/', `http://${req.headers.host}`);

    // CORS preflight
    if (req.method === 'OPTIONS') {
      res.writeHead(204, {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
      });
      res.end();
      return;
    }

    // Health check
    if (url.pathname === '/api/health' && req.method === 'GET') {
      sendJSON(res, 200, { status: 'ok', timestamp: new Date().toISOString() });
      return;
    }

    // Chat endpoint
    if (url.pathname === '/api/chat' && req.method === 'POST') {
      try {
        const body = await parseBody(req);
        const clientIP = getClientIP(req);

        const result = await handleChat(body, clientIP, {
          aiProvider: config.aiProvider,
          lessonLoader: config.lessonLoader,
          rateLimiter: config.rateLimiter,
        });

        sendJSON(res, result.status, result.body);
      } catch (error) {
        console.error('Request error:', error);
        sendJSON(res, 500, {
          error: {
            code: 'INTERNAL_ERROR',
            message: 'An unexpected error occurred',
          },
        });
      }
      return;
    }

    // 404 for unknown routes
    sendJSON(res, 404, {
      error: {
        code: 'NOT_FOUND',
        message: 'Endpoint not found',
      },
    });
  };
}

// =============================================================================
// Server Startup
// =============================================================================

export function startServer(): void {
  const config = loadConfig();
  const handler = createRequestHandler(config);
  const server = createServer(handler);

  server.listen(config.port, () => {
    console.log(`
╔═══════════════════════════════════════════════════════════════╗
║         Interactive Study Mode API Server                     ║
╠═══════════════════════════════════════════════════════════════╣
║  URL:      http://localhost:${config.port}                          ║
║  Provider: ${(config.aiProvider as { name?: string }).name || 'unknown'}                                       ║
║  Docs:     http://localhost:${config.port}/api/health                ║
╚═══════════════════════════════════════════════════════════════╝
    `);
  });
}

// Export for serverless use
export { loadConfig, createRequestHandler };
