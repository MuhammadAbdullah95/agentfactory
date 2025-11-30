/**
 * Translator Module
 * 
 * Gemini API integration for translation.
 */

const { GoogleGenerativeAI } = require('@google/generative-ai');

/**
 * Initialize Gemini client with configurable temperature
 * Lower temperature (0.1-0.3) = more deterministic, less creative, better for code preservation
 * Higher temperature (0.7-1.0) = more creative, but may introduce errors
 */
function createGeminiClient(apiKey, model = 'gemini-flash-lite-latest', temperature = 0.1) {
  if (!apiKey) {
    throw new Error('GEMINI_API_KEY is required');
  }
  
  const genAI = new GoogleGenerativeAI(apiKey);
  return genAI.getGenerativeModel({ 
    model,
    generationConfig: {
      temperature: temperature, // Low temperature for more deterministic translations
    },
  });
}

/**
 * Create translation prompt that preserves code blocks and technical terms
 */
function createTranslationPrompt(sourceContent, sourceLocale, targetLocale) {
  const localeNames = {
    en: 'English',
    ur: 'Urdu',
  };

  return `Translate the following ${localeNames[sourceLocale]} educational content to ${localeNames[targetLocale]}.

CRITICAL INSTRUCTIONS - DO NOT VIOLATE THESE RULES:
1. Preserve ALL code blocks exactly as-is (do not translate code, comments, code syntax, or any content inside code fences)
2. Preserve ALL MDX/JSX syntax exactly: <Component>, {variable}, import statements, export statements, function calls, etc.
3. Preserve ALL JavaScript/TypeScript syntax: variable names, function names, object properties, array syntax, etc.
4. Keep technical terms in English: ROS, URDF, API, SDK, GPU, CPU, etc. Add Urdu explanation in parentheses if helpful
5. Preserve frontmatter metadata exactly (do not translate YAML frontmatter)
6. Use conversational Urdu (not formal literary style)
7. Maintain markdown formatting (headers, lists, links, etc.)
8. Preserve all special characters and symbols
9. DO NOT translate anything that looks like code, variables, or technical syntax - even if it appears outside code blocks
10. If you see patterns like: <Component prop={value}>, import X from Y, export const Z, function name(), variable names, etc. - preserve them EXACTLY

Content to translate:

${sourceContent}

Translated ${localeNames[targetLocale]} content:`;
}

/**
 * Translate content using Gemini API
 */
async function translateContent(model, content, sourceLocale, targetLocale) {
  try {
    const prompt = createTranslationPrompt(content, sourceLocale, targetLocale);
    
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const translatedText = response.text();
    
    return translatedText;
  } catch (error) {
    throw new Error(`Translation failed: ${error.message}`);
  }
}

/**
 * Chunk content for large files (if needed)
 * Gemini has token limits, so we may need to chunk very large files
 */
function chunkContent(content, maxChunkSize = 50000) {
  if (content.length <= maxChunkSize) {
    return [content];
  }

  // Simple chunking by paragraphs (in production, use smarter markdown-aware chunking)
  const paragraphs = content.split(/\n\n+/);
  const chunks = [];
  let currentChunk = '';

  for (const para of paragraphs) {
    if ((currentChunk + para).length > maxChunkSize && currentChunk) {
      chunks.push(currentChunk);
      currentChunk = para;
    } else {
      currentChunk += (currentChunk ? '\n\n' : '') + para;
    }
  }

  if (currentChunk) {
    chunks.push(currentChunk);
  }

  return chunks;
}

module.exports = {
  createGeminiClient,
  translateContent,
  chunkContent,
};

