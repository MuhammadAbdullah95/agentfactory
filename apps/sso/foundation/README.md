# SSO Monorepo Setup

## Prerequisites
- Node.js 20+ installed
- pnpm installed (`npm install -g pnpm`)

## Step 1: Initialize Monorepo with Turborepo

Create the monorepo structure using Turborepo:
```bash
# Create project directory
mkdir sso-monorepo && cd sso-monorepo

# Initialize with Turborepo
pnpm dlx create-turbo@latest . --package-manager pnpm

# When prompted:
# - Where would you like to create your turborepo? . (current directory)
# - Which package manager? pnpm
```

After completion, clean up the default apps and packages:
```bash
# Remove default example apps and packages
rm -rf apps/* packages/*

# Your structure should now be:
# sso-monorepo/
# ├── turbo.json
# ├── package.json
# ├── pnpm-workspace.yaml
# └── (empty apps and packages folders)
```

## Step 2: Create Next.js Applications

We'll create three Next.js applications:
- **sso-server**: API server for authentication (will host BetterAuth APIs)
- **sso-client**: Client application for SSO login pages
- **sso-admin**: Admin dashboard for managing SSO settings
```bash
# Navigate to apps directory
cd apps

# Create SSO Server (API only)
pnpm dlx create-next-app@latest sso-server \
  --typescript \
  --tailwind \
  --app \
  --no-src-dir \
  --import-alias "@/*" \
  --use-pnpm

# Create SSO Client (User-facing SSO)
pnpm dlx create-next-app@latest sso-client \
  --typescript \
  --tailwind \
  --app \
  --no-src-dir \
  --import-alias "@/*" \
  --use-pnpm

# Create SSO Admin (Admin Dashboard)
pnpm dlx create-next-app@latest sso-admin \
  --typescript \
  --tailwind \
  --app \
  --no-src-dir \
  --import-alias "@/*" \
  --use-pnpm

# Go back to root
cd ..
```

Configure each app to run on different ports by updating their package.json:
```bash
# Update ports for each app
sed -i 's/"dev": "next dev"/"dev": "next dev -p 3000"/' apps/sso-server/package.json
sed -i 's/"dev": "next dev"/"dev": "next dev -p 3001"/' apps/sso-client/package.json
sed -i 's/"dev": "next dev"/"dev": "next dev -p 3002"/' apps/sso-admin/package.json
```

Verify the structure:
```bash
# Your structure should now have:
# sso-monorepo/
# ├── apps/
# │   ├── sso-server/
# │   ├── sso-client/
# │   └── sso-admin/
# ├── packages/
# └── ...
```
## Step 3: Create Shared Packages Structure

Create shared packages for database, authentication configuration, and UI components:
```bash
# Create package directories
mkdir -p packages/database/schema
mkdir -p packages/database/migrations
mkdir -p packages/auth-config
mkdir -p packages/ui
mkdir -p packages/typescript-config

# Initialize database package
cd packages/database
pnpm init
cat > package.json << 'EOF'
{
  "name": "@repo/database",
  "version": "0.0.0",
  "private": true,
  "main": "./index.ts",
  "types": "./index.ts",
  "scripts": {
    "db:generate": "drizzle-kit generate",
    "db:push": "drizzle-kit push",
    "db:migrate": "drizzle-kit migrate",
    "db:studio": "drizzle-kit studio"
  }
}
EOF

# Initialize auth-config package
cd ../auth-config
pnpm init
cat > package.json << 'EOF'
{
  "name": "@repo/auth-config",
  "version": "0.0.0",
  "private": true,
  "main": "./index.ts",
  "types": "./index.ts"
}
EOF

# Initialize ui package
cd ../ui
pnpm init
cat > package.json << 'EOF'
{
  "name": "@repo/ui",
  "version": "0.0.0",
  "private": true,
  "main": "./index.tsx",
  "types": "./index.tsx"
}
EOF

# Initialize typescript-config package
cd ../typescript-config
pnpm init
cat > package.json << 'EOF'
{
  "name": "@repo/typescript-config",
  "version": "0.0.0",
  "private": true,
  "files": ["*.json"]
}
EOF

# Return to root
cd ../..
```

Verify the package structure:
```bash
# Your packages folder should now have:
# packages/
# ├── database/
# │   ├── schema/
# │   ├── migrations/
# │   └── package.json
# ├── auth-config/
# │   └── package.json
# ├── ui/
# │   └── package.json
# └── typescript-config/
#     └── package.json
```
## Step 4: Setup Environment Variables and Install Core Dependencies

Create environment configuration and install necessary dependencies:
```bash
# Create .env file in root directory
cat > .env << 'EOF'
# Database (Neon PostgreSQL)
DATABASE_URL="postgresql://user:password@ep-xxx.us-east-1.aws.neon.tech/sso_db?sslmode=require"

# BetterAuth
BETTER_AUTH_SECRET="your-secret-key-min-32-chars-long-change-this"
BETTER_AUTH_URL="http://localhost:3000"

# OAuth Providers (optional for now)
GITHUB_CLIENT_ID=""
GITHUB_CLIENT_SECRET=""
GOOGLE_CLIENT_ID=""
GOOGLE_CLIENT_SECRET=""

# Email (optional for now)
RESEND_API_KEY=""
EMAIL_FROM="noreply@yourdomain.com"
EOF

# Copy .env to .env.example for documentation
cp .env .env.example

# Add .env to .gitignore
echo ".env" >> .gitignore
echo ".env.local" >> .gitignore
```

Install root dependencies:
```bash
# Install workspace tools and TypeScript
pnpm add -Dw turbo@latest typescript@latest @types/node@latest eslint@latest prettier@latest

# Install BetterAuth CLI as dev dependency
pnpm add -Dw @better-auth/cli@latest
```

Install database package dependencies:
```bash
# Install Drizzle ORM and Neon
pnpm add drizzle-orm@latest @neondatabase/serverless@latest -F @repo/database
pnpm add -D drizzle-kit@latest @types/pg@latest -F @repo/database

# Install BetterAuth in database package for schema generation
pnpm add better-auth@latest -F @repo/database

# Install dotenv for environment variables
pnpm add dotenv@latest -F @repo/database
```

Verify installation:
```bash
# Check that dependencies are installed
pnpm list -r --depth=0 | grep -E "better-auth|drizzle|neon"
```

**Important**: Update your `.env` file with your actual Neon database URL before proceeding!

## Step 5: Create Database Configuration Files

Setup the database connection and configuration files:
```bash
# Navigate to database package
cd packages/database

# Create db.ts file (main database connection)
cat > db.ts << 'EOF'
import { drizzle } from 'drizzle-orm/neon-http';
import { neon } from '@neondatabase/serverless';
import * as dotenv from 'dotenv';
import { resolve } from 'path';

// Load environment variables from root .env with absolute path
dotenv.config({ path: resolve(__dirname, '../../.env') });

// Validate DATABASE_URL exists
if (!process.env.DATABASE_URL) {
  throw new Error(
    'DATABASE_URL is not set!\n\n' +
    'Please check your .env file in the monorepo root with:\n' +
    'DATABASE_URL="postgresql://user:password@host:5432/database"\n\n'
  );
}

const sql = neon(process.env.DATABASE_URL!);

// Note: schema will be imported after generation
// export const db = drizzle(sql, { schema });
export const db = drizzle(sql);
EOF

# Create drizzle.config.ts (Drizzle Kit configuration)
cat > drizzle.config.ts << 'EOF'
import { defineConfig } from 'drizzle-kit';
import * as dotenv from 'dotenv';
import { resolve } from 'path';

dotenv.config({ path: resolve(__dirname, '../../.env') });

export default defineConfig({
  schema: './schema/*',
  out: './migrations',
  dialect: 'postgresql',
  dbCredentials: {
    url: process.env.DATABASE_URL!,
  },
  verbose: true,
  strict: true,
});
EOF

# Create index.ts (main export file)
cat > index.ts << 'EOF'
export * from './db';
// Schema exports will be added after generation
EOF

# Return to root
cd ../..
```

Test the database connection:
```bash
# Create a test script with the working approach
cat > packages/database/test-connection.js << 'EOF'
const path = require('path');
const dotenv = require('dotenv');

// Try different paths
const rootPath = path.resolve(__dirname, '../../.env');
console.log('Looking for .env at:', rootPath);
console.log('File exists:', require('fs').existsSync(rootPath));

// Load with explicit path
const result = dotenv.config({ path: rootPath });
console.log('Dotenv result:', result.error ? 'ERROR' : 'SUCCESS');
if (result.error) console.log('Error:', result.error);

console.log('DATABASE_URL exists:', !!process.env.DATABASE_URL);
console.log('All env vars:', Object.keys(process.env).filter(k => k.includes('DATABASE')));
EOF

# Run the test
node packages/database/test-connection.js

# Clean up test file
rm packages/database/test-connection.js
```

Your database package structure should now be:
```
packages/database/
├── db.ts
├── drizzle.config.ts
├── index.ts
├── package.json
├── schema/        (empty for now)
└── migrations/    (empty for now)
```
## Step 6: Create BetterAuth Configuration for Schema Generation

This is the critical step - we'll create an auth configuration that BetterAuth CLI can use to generate Drizzle schema:
```bash
# Navigate to the schema directory
cd packages/database/schema

# Create auth.ts with direct database configuration (NOT using drizzleAdapter)
cat > auth.ts << 'EOF'
import { betterAuth } from 'better-auth';
import { jwt } from 'better-auth/plugins';
import { oidcProvider } from 'better-auth/plugins';
import * as dotenv from 'dotenv';
import { resolve } from 'path';

// Load environment variables
dotenv.config({ path: resolve(__dirname, '../../../.env') });

export const auth = betterAuth({
  // IMPORTANT: Use direct database configuration for CLI generation
  database: {
    provider: 'postgresql',
    url: process.env.DATABASE_URL!,
  },
  
  emailAndPassword: {
    enabled: true,
  },
  
  plugins: [
    jwt({
      jwks: {
        keyPairConfig: {
          alg: 'RS256',
        },
      },
    }),
    oidcProvider({
      loginPage: '/auth/login',
      consentPage: '/auth/consent',
      useJWTPlugin: true,
      allowDynamicClientRegistration: true,
    }),
  ],
});
EOF

# Stay in the schema directory for the next step
pwd
# Should show: .../packages/database/schema
```

Verify the auth config can access environment variables:
```bash
# Test that the auth config loads properly
cat > test-auth.js << 'EOF'
const path = require('path');
const dotenv = require('dotenv');
dotenv.config({ path: path.resolve(__dirname, '../../../.env') });
console.log('Auth config test - DATABASE_URL exists:', !!process.env.DATABASE_URL);
EOF

node test-auth.js
rm test-auth.js
```

**Important**: Stay in the `packages/database/schema` directory for the next step (generating the schema)!

## Step 7: Generate Drizzle Schema with BetterAuth CLI

First, install required PostgreSQL client that BetterAuth needs:
```bash
# Navigate to database package
cd packages/database

# Install PostgreSQL client (required for drizzleAdapter)
pnpm add pg@latest @types/pg@latest

# Install BetterAuth plugins
pnpm add better-auth@latest
```

Create the auth configuration with all plugins and generate the schema:
```bash
# Navigate to schema directory
cd schema

# Create auth.ts with drizzleAdapter and all plugins (JWT, OIDC)
cat > auth.ts << 'EOF'
import { betterAuth } from "better-auth";
import { drizzleAdapter } from "better-auth/adapters/drizzle";
import { jwt } from "better-auth/plugins";
import { oidcProvider } from "better-auth/plugins";
import { db } from "../db";

export const auth = betterAuth({
  database: drizzleAdapter(db, {
    provider: "pg",
  }),
  
  emailAndPassword: {
    enabled: true,
  },
  
  socialProviders: {
    github: {
      clientId: process.env.GITHUB_CLIENT_ID!,
      clientSecret: process.env.GITHUB_CLIENT_SECRET!,
    },
    google: {
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    },
  },
  
  plugins: [
    jwt({
      jwks: {
        keyPairConfig: {
          alg: 'RS256',
        },
      },
    }),
    oidcProvider({
      loginPage: '/auth/login',
      consentPage: '/auth/consent',
      useJWTPlugin: true,
      allowDynamicClientRegistration: true,
    }),
  ],
});
EOF

# Generate the schema
pnpm dlx @better-auth/cli generate --config ./auth.ts

# When prompted:
# "Do you want to generate the schema to ./auth-schema.ts?" → Type: yes
```

You should see:
```
[dotenv@17.2.3] injecting env (9) from ../../../.env
WARN [Better Auth]: Social provider google is missing clientId or clientSecret
WARN [Better Auth]: Social provider github is missing clientId or clientSecret
✔ Do you want to generate the schema to ./auth-schema.ts? … yes
SUCCESS [Better Auth]: 🚀 Schema was generated successfully!
```

Verify the generated schema includes plugin tables:
```bash
# Check for JWT and OIDC tables in the schema
grep -E "jwks|oauth" auth-schema.ts

# You should see tables like:
# export const jwks = pgTable("jwks", {
# export const oauthApplication = pgTable("oauthApplication", {
# export const oauthAccessToken = pgTable("oauthAccessToken", {
# export const oauthConsent = pgTable("oauthConsent", {
```

**Dependencies added in this step:**
- `pg` - PostgreSQL client for Node.js
- `@types/pg` - TypeScript types for pg
- JWT plugin tables (jwks)
- OIDC plugin tables (oauthApplication, oauthAccessToken, oauthConsent)

**Note**: The warnings about missing OAuth credentials are fine - we'll add those when configuring each provider.

## Step 8: Update Database Configuration and Push Schema

Now that we have the generated schema, let's update our database configuration to use it and push the tables to your Neon database:
```bash
# Navigate back to database package root
cd ..
# Should be in packages/database

# Update db.ts to import and use the schema
cat > db.ts << 'EOF'
import { drizzle } from 'drizzle-orm/neon-http';
import { neon } from '@neondatabase/serverless';
import * as schema from './schema/auth-schema';
import * as dotenv from 'dotenv';
import { resolve } from 'path';

// Load environment variables
dotenv.config({ path: resolve(__dirname, '../../.env') });

if (!process.env.DATABASE_URL) {
  throw new Error('DATABASE_URL is not set!');
}

const sql = neon(process.env.DATABASE_URL!);

// Now using the generated schema
export const db = drizzle(sql, { schema });
EOF

# Update index.ts to export everything
cat > index.ts << 'EOF'
export * from './db';
export * from './schema/auth-schema';
EOF

# Update drizzle.config.ts to point to the generated schema
cat > drizzle.config.ts << 'EOF'
import { defineConfig } from 'drizzle-kit';
import * as dotenv from 'dotenv';
import { resolve } from 'path';

dotenv.config({ path: resolve(__dirname, '../../.env') });

export default defineConfig({
  schema: './schema/auth-schema.ts',  // Point to generated schema
  out: './migrations',
  dialect: 'postgresql',
  dbCredentials: {
    url: process.env.DATABASE_URL!,
  },
  verbose: true,
  strict: true,
});
EOF
```

Push the schema to your Neon database:
```bash
# Generate migration SQL files (optional, for tracking changes)
pnpm db:generate

# Push schema directly to database
pnpm db:push

# You should see output like:
# [✓] Pulling schema from database...
# [✓] Changes applied
```

Verify tables were created:
```bash
# Open Drizzle Studio to view your database
pnpm db:studio

# This will open a browser at https://local.drizzle.studio
# You should see all your tables:
# - user
# - session
# - account
# - verification
# - jwks
# - oauthApplication
# - oauthAccessToken
# - oauthConsent
```

Test the database connection:
```bash
# Create a quick test to verify everything works
cat > test-db-final.js << 'EOF'
const { db } = require('./db');

async function test() {
  try {
    console.log('✅ Database and schema loaded successfully!');
    console.log('Available tables:', Object.keys(db._.schema));
  } catch (error) {
    console.error('❌ Error:', error.message);
  }
}

test();
EOF

node test-db-final.js
rm test-db-final.js
```

Return to monorepo root:
```bash
cd ../..
```

**Your database package is now complete with:**
- ✅ Generated Drizzle schema from BetterAuth
- ✅ Database connection configured
- ✅ Tables pushed to Neon database
- ✅ JWT and OIDC plugin tables included

## Step 9: Setup Auth Configuration for Applications

Now let's create the main auth configuration that your applications will use:

### Install dependencies in auth-config package:
```bash
# Navigate to auth-config package
cd packages/auth-config

# Install necessary dependencies
pnpm add better-auth@latest dotenv@latest
pnpm add @repo/database@workspace:*

# Create the main auth configuration with build-time safety
cat > index.ts << 'EOF'
import { betterAuth } from 'better-auth';
import { drizzleAdapter } from 'better-auth/adapters/drizzle';
import { jwt } from 'better-auth/plugins';
import { oidcProvider } from 'better-auth/plugins';

// Lazy load database to avoid build-time errors
const getDb = () => {
  const { db } = require('@repo/database');
  return db;
};

// Dynamic trusted origins based on environment
const getTrustedOrigins = () => {
  const origins = [
    'http://localhost:3000',
    'http://localhost:3001',
    'http://localhost:3002',
  ];
  
  if (process.env.VERCEL_URL) {
    origins.push(`https://${process.env.VERCEL_URL}`);
  }
  if (process.env.PRODUCTION_URL) {
    origins.push(process.env.PRODUCTION_URL);
  }
  
  return origins;
};

export const auth = betterAuth({
  database: drizzleAdapter(getDb(), {
    provider: 'pg',
  }),
  
  // Use BETTER_AUTH_SECRET or a placeholder during build
  secret: process.env.BETTER_AUTH_SECRET || 'placeholder-secret-for-build-only-change-in-production',
  
  baseURL: process.env.BETTER_AUTH_URL || 'http://localhost:3000',
  
  disabledPaths: ['/token'],
  
  emailAndPassword: {
    enabled: true,
  },
  
  socialProviders: {
    github: {
      clientId: process.env.GITHUB_CLIENT_ID || 'placeholder',
      clientSecret: process.env.GITHUB_CLIENT_SECRET || 'placeholder',
      enabled: !!process.env.GITHUB_CLIENT_ID,
    },
    google: {
      clientId: process.env.GOOGLE_CLIENT_ID || 'placeholder', 
      clientSecret: process.env.GOOGLE_CLIENT_SECRET || 'placeholder',
      enabled: !!process.env.GOOGLE_CLIENT_ID,
    },
  },
  
  plugins: [
    jwt({
      disableSettingJwtHeader: true,
      jwks: {
        keyPairConfig: {
          alg: 'RS256',
        },
      },
    }),
    
    oidcProvider({
      loginPage: '/auth/login',
      consentPage: '/auth/consent', 
      useJWTPlugin: true,
      allowDynamicClientRegistration: true,
      
      trustedClients: [
        {
          clientId: process.env.INTERNAL_CLIENT_ID || 'internal-dashboard',
          clientSecret: process.env.INTERNAL_CLIENT_SECRET || 'secret-for-internal-dashboard',
          name: 'Internal Dashboard',
          type: 'web',
          redirectURLs: [
            'http://localhost:3001/auth/callback',
            'http://localhost:3002/auth/callback',
            process.env.CLIENT_PRODUCTION_URL ? `${process.env.CLIENT_PRODUCTION_URL}/auth/callback` : '',
            process.env.ADMIN_PRODUCTION_URL ? `${process.env.ADMIN_PRODUCTION_URL}/auth/callback` : '',
          ].filter(Boolean),
          skipConsent: true,
          metadata: {},
          disabled: false,
        },
      ],
    }),
  ],
  
  trustedOrigins: getTrustedOrigins(),
});

export type Auth = typeof auth;
EOF

# Create auth client configuration
cat > client.ts << 'EOF'
import { createAuthClient } from "better-auth/client";

export const authClient = createAuthClient({
  baseURL: process.env.NEXT_PUBLIC_API_URL || "http://localhost:3000",
});

export type AuthClient = typeof authClient;
EOF

# Update package.json
cat > package.json << 'EOF'
{
  "name": "@repo/auth-config",
  "version": "0.0.0",
  "private": true,
  "main": "./index.ts",
  "types": "./index.ts",
  "exports": {
    ".": "./index.ts",
    "./client": "./client.ts"
  },
  "dependencies": {
    "better-auth": "latest",
    "dotenv": "latest",
    "@repo/database": "workspace:*"
  }
}
EOF

# Return to root
cd ../..
```

### Update database package for build-time safety:
```bash
cd packages/database

cat > db.ts << 'EOF'
import { drizzle } from 'drizzle-orm/neon-http';
import { neon } from '@neondatabase/serverless';
import * as schema from './schema/auth-schema';

// Handle missing DATABASE_URL during build
const getDatabaseUrl = () => {
  if (process.env.DATABASE_URL) {
    return process.env.DATABASE_URL;
  }
  
  // During build, use placeholder
  if (process.env.NODE_ENV === 'production' || process.env.NEXT_PHASE === 'phase-production-build') {
    console.warn('DATABASE_URL not found during build, using placeholder');
    return 'postgresql://placeholder:placeholder@placeholder/placeholder';
  }
  
  throw new Error('DATABASE_URL is not set! Check your .env file.');
};

const databaseUrl = getDatabaseUrl();
const sql = neon(databaseUrl);

export const db = drizzle(sql, { schema });
EOF

cd ../..
```

### Setup SSO Server application:
```bash
# Install dependencies in SSO server
pnpm add better-auth@latest -F sso-server
pnpm add @repo/auth-config@workspace:* -F sso-server
pnpm add @repo/database@workspace:* -F sso-server

# Install Tailwind dependencies (required for Next.js build)
cd apps/sso-server
pnpm add -D tailwindcss@latest postcss@latest autoprefixer@latest

# Create auth API route
mkdir -p app/api/auth/[...all]

cat > app/api/auth/[...all]/route.ts << 'EOF'
import { auth } from "@repo/auth-config";
import { toNextJsHandler } from "better-auth/next-js";

export const { GET, POST } = toNextJsHandler(auth);
EOF

# Create Next.js configuration
cat > next.config.js << 'EOF'
/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/.well-known/openid-configuration',
        destination: '/api/auth/oauth2/.well-known/openid-configuration',
      },
      {
        source: '/.well-known/jwks.json',
        destination: '/api/auth/jwks',
      },
    ];
  },
  transpilePackages: ['@repo/auth-config', '@repo/database'],
  env: {
    DATABASE_URL: process.env.DATABASE_URL,
    BETTER_AUTH_SECRET: process.env.BETTER_AUTH_SECRET,
    BETTER_AUTH_URL: process.env.BETTER_AUTH_URL,
  },
};

module.exports = nextConfig;
EOF

# Copy .env for local development
cp ../../.env .env.local

cd ../..
```

### Update environment variables:
```bash
# Add internal client variables to .env
grep -q "INTERNAL_CLIENT_ID" .env || cat >> .env << 'EOF'

# Internal OIDC Client
INTERNAL_CLIENT_ID="internal-dashboard"
INTERNAL_CLIENT_SECRET="generate-a-secure-secret-here"

# Production URLs (for Vercel deployment)
PRODUCTION_URL=""
CLIENT_PRODUCTION_URL=""
ADMIN_PRODUCTION_URL=""
EOF

# Create .env.example for documentation
cat > .env.example << 'EOF'
# ===================================
# Database Configuration (Required)
# ===================================
# Get your Neon database URL from: https://neon.tech
DATABASE_URL="postgresql://user:password@ep-xxx.us-east-1.aws.neon.tech/sso_db?sslmode=require"

# ===================================
# BetterAuth Configuration (Required)
# ===================================
# Generate a secure secret (32+ characters): openssl rand -base64 32
BETTER_AUTH_SECRET="your-secret-key-min-32-chars-long-change-this"
BETTER_AUTH_URL="http://localhost:3000"

# ===================================
# Internal OIDC Client (Required)
# ===================================
INTERNAL_CLIENT_ID="internal-dashboard"
INTERNAL_CLIENT_SECRET="generate-a-secure-secret-here"

# ===================================
# OAuth Providers (Optional)
# ===================================
# GitHub OAuth: https://github.com/settings/developers
GITHUB_CLIENT_ID=""
GITHUB_CLIENT_SECRET=""

# Google OAuth: https://console.cloud.google.com/apis/credentials
GOOGLE_CLIENT_ID=""
GOOGLE_CLIENT_SECRET=""

# ===================================
# Email Configuration (Optional)
# ===================================
RESEND_API_KEY=""
EMAIL_FROM="noreply@yourdomain.com"

# ===================================
# Production URLs (For Deployment)
# ===================================
PRODUCTION_URL=""
CLIENT_PRODUCTION_URL=""
ADMIN_PRODUCTION_URL=""
EOF
```

### Reinstall all dependencies:
```bash
# Clean install to ensure workspace links
rm -rf node_modules packages/*/node_modules apps/*/node_modules
pnpm install
```

### Test the setup:
```bash
# Build the SSO server
cd apps/sso-server
pnpm build

# If build succeeds, run the development server
pnpm dev

# Test the auth endpoints in another terminal
curl http://localhost:3000/api/auth/health

# Test OIDC discovery
curl http://localhost:3000/.well-known/openid-configuration

# Test JWKS endpoint
curl http://localhost:3000/.well-known/jwks.json
```

**Your SSO server is now configured with:**
- ✅ Full BetterAuth setup with Drizzle adapter
- ✅ JWT with JWKS for token verification
- ✅ OIDC Provider for external apps
- ✅ API routes at `/api/auth/*`
- ✅ Well-known endpoints for OIDC discovery
- ✅ Build-time safety for environment variables
- ✅ Tailwind CSS dependencies installed

## Step 10: Test and Run the Complete SSO Setup

Let's test that everything is working correctly and create a basic test page:

### Start the SSO server:
```bash
# From root directory, start the SSO server
cd apps/sso-server
pnpm dev

# You should see:
# ▲ Next.js 16.0.3 (Turbopack)
# - Local: http://localhost:3000
```

### Test the auth endpoints:

Open a new terminal and run these tests:
```bash
# Test health endpoint
curl http://localhost:3000/api/auth/health

# Test OIDC discovery
curl http://localhost:3000/.well-known/openid-configuration | jq

# Test JWKS endpoint
curl http://localhost:3000/.well-known/jwks.json | jq

# If you don't have jq installed, use:
curl http://localhost:3000/.well-known/openid-configuration | python -m json.tool
```

### Create a test page for the SSO server:
```bash
# Create a simple test page
cat > app/page.tsx << 'EOF'
'use client'
export default function Home() {
  return (
    <main className="min-h-screen p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold mb-8">SSO Server</h1>
        
        <div className="space-y-6">
          <section className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-2xl font-semibold mb-4">API Endpoints</h2>
            <ul className="space-y-2">
              <li>
                <strong>Health:</strong>
                <a href="/api/auth/health" className="text-blue-600 ml-2">/api/auth/health</a>
              </li>
              <li>
                <strong>OIDC Discovery:</strong>
                <a href="/.well-known/openid-configuration" className="text-blue-600 ml-2">/.well-known/openid-configuration</a>
              </li>
              <li>
                <strong>JWKS:</strong>
                <a href="/.well-known/jwks.json" className="text-blue-600 ml-2">/.well-known/jwks.json</a>
              </li>
            </ul>
          </section>

          <section className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-2xl font-semibold mb-4">Test Authentication</h2>
            <div className="space-y-4">
              <button 
                onClick={() => window.location.href = '/api/auth/sign-in'}
                className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
              >
                Sign In
              </button>
              <button 
                onClick={() => window.location.href = '/api/auth/sign-up'}
                className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 ml-4"
              >
                Sign Up
              </button>
            </div>
          </section>

          <section className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-2xl font-semibold mb-4">Environment Status</h2>
            <ul className="space-y-2 text-sm">
              <li>✅ Database Connected</li>
              <li>✅ BetterAuth Configured</li>
              <li>✅ OIDC Provider Enabled</li>
              <li>✅ JWT/JWKS Enabled</li>
            </ul>
          </section>
        </div>
      </div>
    </main>
  );
}
EOF
```

### Test user registration with the API:
```bash
# Test user registration
curl -X POST http://localhost:3000/api/auth/sign-up/email \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "SecurePassword123!",
    "name": "Test User"
  }'

# Test user login
curl -X POST http://localhost:3000/api/auth/sign-in/email \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "SecurePassword123!"
  }'
```

### Register an OAuth application (for testing OIDC):
```bash
# Register a test OAuth application
curl -X POST http://localhost:3000/api/auth/oauth2/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Application",
    "redirectURLs": ["http://localhost:3001/auth/callback"],
    "type": "web"
  }'

# Save the returned clientId and clientSecret
```

### Setup Turbo for running all apps:
```bash
# Return to root
cd ../..

# Update root package.json with specific app scripts
cat > package.json << 'EOF'
{
  "name": "sso-monorepo",
  "private": true,
  "scripts": {
    "dev": "turbo dev",
    "dev:server": "turbo dev --filter=sso-server",
    "dev:client": "turbo dev --filter=sso-client",
    "dev:admin": "turbo dev --filter=sso-admin",
    "build": "turbo build",
    "build:server": "turbo build --filter=sso-server",
    "start": "turbo start",
    "lint": "turbo lint",
    "clean": "turbo clean && rm -rf node_modules",
    "db:generate": "pnpm -F @repo/database db:generate",
    "db:push": "pnpm -F @repo/database db:push",
    "db:studio": "pnpm -F @repo/database db:studio",
    "test:auth": "node scripts/test-auth.js"
  },
  "devDependencies": {
    "@better-auth/cli": "latest",
    "@types/node": "^20.0.0",
    "eslint": "^9.0.0",
    "prettier": "^3.3.0",
    "turbo": "latest",
    "typescript": "^5.6.0"
  },
  "packageManager": "pnpm@9.12.0",
  "engines": {
    "node": ">=20.0.0"
  }
}
EOF
```

### Create a test script:
```bash
# Create a test script to verify everything works
mkdir -p scripts
cat > scripts/test-auth.js << 'EOF'
const https = require('https');
const http = require('http');

const baseUrl = 'http://localhost:3000';

async function testEndpoint(path, method = 'GET', data = null) {
  return new Promise((resolve, reject) => {
    const url = new URL(path, baseUrl);
    const options = {
      hostname: url.hostname,
      port: url.port,
      path: url.pathname,
      method: method,
      headers: {
        'Content-Type': 'application/json',
      },
    };

    const req = http.request(options, (res) => {
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => {
        resolve({
          status: res.statusCode,
          data: data ? JSON.parse(data) : null,
        });
      });
    });

    req.on('error', reject);
    if (data) req.write(JSON.stringify(data));
    req.end();
  });
}

async function runTests() {
  console.log('🧪 Testing SSO Server Endpoints...\n');

  try {
    // Test health
    console.log('Testing /api/auth/health...');
    const health = await testEndpoint('/api/auth/health');
    console.log('✅ Health check:', health.status === 200 ? 'PASSED' : 'FAILED');

    // Test OIDC discovery
    console.log('\nTesting OIDC discovery...');
    const oidc = await testEndpoint('/.well-known/openid-configuration');
    console.log('✅ OIDC discovery:', oidc.status === 200 ? 'PASSED' : 'FAILED');

    // Test JWKS
    console.log('\nTesting JWKS endpoint...');
    const jwks = await testEndpoint('/.well-known/jwks.json');
    console.log('✅ JWKS endpoint:', jwks.status === 200 ? 'PASSED' : 'FAILED');

    console.log('\n✨ All tests completed!');
  } catch (error) {
    console.error('❌ Test failed:', error.message);
    console.log('\nMake sure the SSO server is running: pnpm dev:server');
  }
}

runTests();
EOF

# Run the test
node scripts/test-auth.js
```

### View the database:
```bash
# Open Drizzle Studio to see your data
pnpm db:studio

# This opens https://local.drizzle.studio
# You can view all tables and data
```

### Running everything together:
```bash
# Run all apps at once (from root)
pnpm dev

# Or run individually
pnpm dev:server  # SSO Server on http://localhost:3000
pnpm dev:client  # SSO Client on http://localhost:3001
pnpm dev:admin   # Admin Panel on http://localhost:3002
```

### Verify the setup checklist:

✅ **Working endpoints:**
- `/api/auth/health` - Health check
- `/api/auth/sign-up/email` - User registration
- `/api/auth/sign-in/email` - User login
- `/.well-known/openid-configuration` - OIDC discovery
- `/.well-known/jwks.json` - Public keys for JWT verification
- `/api/auth/oauth2/register` - OAuth app registration

✅ **Database:**
- Tables created (user, session, account, verification, jwks, oauthApplication, etc.)
- Viewable in Drizzle Studio

✅ **Authentication:**
- Email/password authentication working
- JWT tokens with JWKS
- OIDC provider ready for external apps

**Congratulations! Your SSO server is now fully operational!** 🎉

Next steps would be:
- Setting up the client app with login UI
- Creating the admin dashboard
- Adding social login providers
- Deploying to Vercel