/**
 * Docusaurus Auto-Translate Plugin
 * 
 * Automatically translates English content to Urdu during build process using Gemini API.
 * Integrates with Docusaurus i18n infrastructure.
 */

const fs = require('fs');
const path = require('path');
const glob = require('glob');

const cache = require('./lib/cache');
const fileProcessor = require('./lib/file-processor');
const i18nStructure = require('./lib/i18n-structure');
const translator = require('./lib/translator');

module.exports = function autoTranslatePlugin(context, options) {
  const {
    enabled = true,
    sourceLocale = 'en',
    targetLocales = ['ur'],
    apiProvider = 'gemini',
    model = 'gemini-flash-lite-latest',
    apiKey = process.env.GEMINI_API_KEY,
    cacheDir = '.translation-cache',
    docsPath = 'docs',
    temperature = 0.1, // Low temperature for deterministic translations (preserves code better)
  } = options;

  return {
    name: 'docusaurus-plugin-auto-translate',

    async loadContent() {
      if (!enabled) {
        console.log('[Auto-Translate] Plugin disabled');
        return;
      }

      if (!apiKey) {
        console.warn('[Auto-Translate] GEMINI_API_KEY not set, skipping translation');
        return;
      }

      console.log('[Auto-Translate] Starting translation process...');

      const { siteDir } = context;
      const docsDir = path.join(siteDir, docsPath);
      const cacheDirPath = path.join(siteDir, cacheDir);

      // Ensure i18n structure exists
      targetLocales.forEach(locale => {
        i18nStructure.ensureI18nStructure(siteDir, locale);
      });

      // Find all markdown files in docs directory
      const mdFiles = glob.sync('**/*.md', {
        cwd: docsDir,
        absolute: true,
        ignore: ['**/*.summary.md', '**/node_modules/**'],
      });

      console.log(`[Auto-Translate] Found ${mdFiles.length} markdown files`);

      // Initialize Gemini client
      let geminiModel = null;
      if (apiProvider === 'gemini') {
        try {
          geminiModel = translator.createGeminiClient(apiKey, model, temperature);
        } catch (error) {
          console.error(`[Auto-Translate] Failed to initialize Gemini client: ${error.message}`);
          return;
        }
      }

      let translatedCount = 0;
      let cachedCount = 0;
      let errorCount = 0;

      // Process each target locale
      for (const targetLocale of targetLocales) {
        console.log(`[Auto-Translate] Translating to ${targetLocale}...`);

        for (const sourceFile of mdFiles) {
          try {
            const relativePath = i18nStructure.getRelativePathFromDocs(sourceFile, docsDir);
            const { frontmatter, content, original } = fileProcessor.readMarkdownFile(sourceFile);

            // Check cache
            if (cache.isCacheValid(cacheDirPath, relativePath, original, targetLocale)) {
              // Validate cached translation for common corruption patterns
              const cachedPath = cache.getCachedTranslationPath(cacheDirPath, relativePath, targetLocale);
              if (cachedPath && fs.existsSync(cachedPath)) {
                const cachedContent = fs.readFileSync(cachedPath, 'utf8');
                // Check for common MDX/JSX corruption patterns (errors that would break build)
                const corruptionPatterns = [
                  /ReferenceError:\s*\w+\s+is not defined/i,
                  /undefined variable/i,
                  /undefined identifier/i,
                  /\bundefined\s+is not a function/i,
                ];
                const hasCorruption = corruptionPatterns.some(pattern => cachedContent.match(pattern));
                
                if (hasCorruption) {
                  console.warn(`[Auto-Translate] Detected corruption in cached translation: ${relativePath}, invalidating cache and deleting corrupted file`);
                  cache.invalidateCache(cacheDirPath, relativePath, targetLocale);
                  // Delete corrupted translation file
                  try {
                    fs.unlinkSync(cachedPath);
                  } catch (err) {
                    // Ignore if file doesn't exist
                  }
                  // Continue to re-translate below
                } else {
                  cachedCount++;
                  console.log(`[Auto-Translate] Cache hit: ${relativePath}`);
                  continue;
                }
              } else {
                // Cache says valid but file doesn't exist, invalidate cache
                cache.invalidateCache(cacheDirPath, relativePath, targetLocale);
              }
            }

            // Translate content
            console.log(`[Auto-Translate] Translating: ${relativePath}`);
            const translatedContent = await translator.translateContent(
              geminiModel,
              content,
              sourceLocale,
              targetLocale
            );

            // Write translated file
            const targetPath = path.join(
              siteDir,
              i18nStructure.getI18nTargetPath(relativePath, targetLocale)
            );
            fileProcessor.writeTranslatedFile(targetPath, frontmatter, translatedContent);

            // Update cache
            cache.storeCache(cacheDirPath, relativePath, original, targetLocale, targetPath);

            translatedCount++;
          } catch (error) {
            errorCount++;
            console.error(`[Auto-Translate] Error translating ${sourceFile}: ${error.message}`);
            // Continue with next file (non-blocking)
          }
        }
      }

      console.log(`[Auto-Translate] Complete: ${translatedCount} translated, ${cachedCount} cached, ${errorCount} errors`);
    },
  };
};

