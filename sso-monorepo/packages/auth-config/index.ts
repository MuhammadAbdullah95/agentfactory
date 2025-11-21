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
