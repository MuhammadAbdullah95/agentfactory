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
