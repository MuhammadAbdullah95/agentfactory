# Better Auth OAuth/OIDC Setup Skill

## Purpose
Guide implementation of OAuth 2.1 / OIDC authentication using Better Auth with the OIDC Provider plugin.

## When to Use
- Setting up centralized authentication for multiple apps
- Implementing SSO (Single Sign-On) across a platform
- Creating an OAuth authorization server
- Integrating Better Auth as an identity provider

## Key Questions to Ask

1. **Architecture**
   - How many apps will use this auth server?
   - Is this for first-party apps only or third-party OAuth clients too?
   - Do you need dynamic client registration?

2. **Database**
   - Which database? (Postgres recommended with Neon for serverless)
   - Need user profiles beyond core auth fields?

3. **Features**
   - Role-based access control needed?
   - Admin dashboard for user management?
   - Consent screen for third-party apps?

## Implementation Checklist

### 1. Auth Server Setup

```typescript
// src/lib/auth.ts
import { betterAuth } from "better-auth";
import { drizzleAdapter } from "better-auth/adapters/drizzle";
import { oidcProvider } from "better-auth/plugins/oidc-provider";
import { admin } from "better-auth/plugins/admin";

export const auth = betterAuth({
  database: drizzleAdapter(db, { provider: "pg", schema }),

  emailAndPassword: { enabled: true },

  session: {
    expiresIn: 60 * 60 * 24 * 7, // 7 days
    updateAge: 60 * 60 * 24,     // Refresh daily
  },

  trustedOrigins: process.env.ALLOWED_ORIGINS?.split(","),

  plugins: [
    oidcProvider({
      loginPage: "/auth/sign-in",
      consentPage: "/auth/consent",
      trustedClients: [{
        clientId: "your-app",
        clientSecret: process.env.CLIENT_SECRET,
        redirectUrls: ["http://localhost:3000/auth/callback"],  // Note: lowercase 'urls'
        skipConsent: true,  // First-party apps
      }],
    }),
    admin({
      defaultRole: "user",
      adminRoles: ["admin"],
    }),
  ],
});
```

### 2. OAuth Client Integration

```typescript
// Client app: src/lib/auth-client.ts
export function getOAuthAuthorizationUrl(state: string) {
  const params = new URLSearchParams({
    client_id: 'your-app',
    redirect_uri: 'http://localhost:3000/auth/callback',
    response_type: 'code',
    scope: 'openid profile email',
    state,
  });
  return `${AUTH_SERVER_URL}/api/auth/oauth2/authorize?${params}`;
}

// Callback page: exchange code for tokens
const tokenResponse = await fetch(`${AUTH_SERVER_URL}/api/auth/oauth2/token`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  body: new URLSearchParams({
    grant_type: 'authorization_code',
    code,
    redirect_uri: 'http://localhost:3000/auth/callback',
    client_id: 'your-app',
    client_secret: 'your-secret',
  }),
});
```

### 3. Session Management (Client)

```typescript
// AuthContext.tsx pattern
const checkSession = async () => {
  const accessToken = localStorage.getItem('access_token');
  if (accessToken) {
    const response = await fetch(`${AUTH_URL}/api/auth/oauth2/userinfo`, {
      headers: { Authorization: `Bearer ${accessToken}` },
    });
    if (response.ok) {
      setSession({ user: await response.json() });
    } else {
      localStorage.removeItem('access_token');
    }
  }
};

const signOut = () => {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  setSession(null);
  window.location.href = '/';
};
```

## Common Pitfalls

### 1. Wrong Property Name
```typescript
// WRONG - causes "Cannot read properties of undefined (reading 'find')"
redirectURLs: ["http://..."]

// CORRECT
redirectUrls: ["http://..."]
```

### 2. Cookie vs Token Auth Confusion
- OAuth clients should ONLY use tokens from localStorage
- Don't fall back to cookie-based session checking
- Cookie sessions are for the auth server itself

### 3. CORS Configuration
```typescript
// Auth server must trust client origins
trustedOrigins: ["http://localhost:3000", "https://your-app.com"]

// Environment variable
ALLOWED_ORIGINS=http://localhost:3000,https://your-app.com
```

### 4. Logout Scope
- OAuth standard: client clears its own tokens
- Auth server session stays active (SSO pattern)
- Don't try to clear auth server session from client

## Database Schema (Drizzle)

Required tables for OIDC Provider:
- `user` - Core user data
- `session` - Server sessions
- `account` - Auth provider accounts
- `oauth_application` - Registered OAuth clients
- `oauth_access_token` - Issued tokens
- `oauth_consent` - User consent records

## Testing Checklist

1. [ ] OIDC Discovery endpoint works: `GET /.well-known/openid-configuration`
2. [ ] Authorization redirects to login when unauthenticated
3. [ ] Authorization returns code after login
4. [ ] Token exchange returns access_token
5. [ ] UserInfo returns user data with valid token
6. [ ] Sign out clears tokens and redirects

## Security Checklist

- [ ] HTTPS in production
- [ ] Strong BETTER_AUTH_SECRET (32+ chars)
- [ ] Unique client secrets per app
- [ ] Exact redirect URI matching
- [ ] Rate limiting enabled
- [ ] CORS properly configured
