#!/usr/bin/env node
import * as dotenv from "dotenv";
dotenv.config({ path: ".env.local" });

import { neon } from "@neondatabase/serverless";
import { drizzle } from "drizzle-orm/neon-http";
import { pgTable, text, boolean, timestamp } from "drizzle-orm/pg-core";
import { eq } from "drizzle-orm";
import { TRUSTED_CLIENTS } from "../src/lib/trusted-clients";

// Schema definitions
const oauthApplication = pgTable("oauth_application", {
  id: text("id").primaryKey(),
  name: text("name"),
  icon: text("icon"),
  metadata: text("metadata"),
  clientId: text("client_id").unique(),
  clientSecret: text("client_secret"),
  redirectUrls: text("redirect_urls"),
  type: text("type"),
  disabled: boolean("disabled").default(false),
  userId: text("user_id"),
  createdAt: timestamp("created_at"),
  updatedAt: timestamp("updated_at"),
});

const organization = pgTable("organization", {
  id: text("id").primaryKey(),
  name: text("name").notNull(),
  slug: text("slug").unique(),
  logo: text("logo"),
  metadata: text("metadata"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

const member = pgTable("member", {
  id: text("id").primaryKey(),
  userId: text("user_id").notNull(),
  organizationId: text("organization_id").notNull(),
  role: text("role").notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

const user = pgTable("user", {
  id: text("id").primaryKey(),
  email: text("email").notNull().unique(),
});

const sql = neon(process.env.DATABASE_URL!);
const db = drizzle(sql);

// Test organization configuration
const TEST_ORG = {
  id: "test-organization-id",
  name: "RoboLearn Test Organization",
  slug: "robolearn-test",
  logo: null,
  metadata: JSON.stringify({ plan: "pro", features: ["multi-tenant"] }),
};

const TEST_USER_EMAIL = "admin@robolearn.io";

/**
 * Upsert OAuth client from trusted-clients.ts configuration
 */
async function upsertClient(client: typeof TRUSTED_CLIENTS[0]) {
  const dbClient = {
    id: `${client.clientId}-id`,
    clientId: client.clientId,
    clientSecret: null, // Public clients have no secret
    name: client.name,
    redirectUrls: client.redirectUrls.join(","),
    type: client.type,
    disabled: client.disabled,
    metadata: JSON.stringify({
      token_endpoint_auth_method: "none",
      grant_types: ["authorization_code", "refresh_token"],
      skip_consent: client.skipConsent,
      ...client.metadata,
    }),
  };

  const existing = await db
    .select()
    .from(oauthApplication)
    .where(eq(oauthApplication.clientId, client.clientId));

  if (existing.length > 0) {
    console.log(`  ✅ ${client.name} (updating...)`);
    await db
      .update(oauthApplication)
      .set({
        name: dbClient.name,
        redirectUrls: dbClient.redirectUrls,
        type: dbClient.type,
        disabled: dbClient.disabled,
        metadata: dbClient.metadata,
        updatedAt: new Date(),
      })
      .where(eq(oauthApplication.clientId, client.clientId));
  } else {
    console.log(`  ✅ ${client.name} (creating...)`);
    await db.insert(oauthApplication).values({
      ...dbClient,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
  }
}

/**
 * Seed test organization (optional)
 */
async function seedOrganization() {
  console.log("\n📊 Seeding test organization...\n");

  // Create or update organization
  const existingOrg = await db
    .select()
    .from(organization)
    .where(eq(organization.id, TEST_ORG.id));

  if (existingOrg.length > 0) {
    console.log(`  ✅ ${TEST_ORG.name} (updating...)`);
    await db
      .update(organization)
      .set({
        name: TEST_ORG.name,
        slug: TEST_ORG.slug,
        metadata: TEST_ORG.metadata,
      })
      .where(eq(organization.id, TEST_ORG.id));
  } else {
    console.log(`  ✅ ${TEST_ORG.name} (creating...)`);
    await db.insert(organization).values({
      ...TEST_ORG,
      createdAt: new Date(),
    });
  }

  // Find test user
  const testUser = await db
    .select()
    .from(user)
    .where(eq(user.email, TEST_USER_EMAIL));

  if (testUser.length === 0) {
    console.log(`  ⚠️  Test user not found (${TEST_USER_EMAIL})`);
    console.log(`     Sign up first, then run this script again to add organization membership`);
    return;
  }

  const userId = testUser[0].id;
  console.log(`  ✅ Found test user: ${TEST_USER_EMAIL}`);

  // Add user to organization as owner
  const existingMember = await db
    .select()
    .from(member)
    .where(eq(member.userId, userId));

  if (existingMember.length > 0) {
    console.log(`  ✅ User already member (updating role to owner...)`);
    await db
      .update(member)
      .set({ role: "owner" })
      .where(eq(member.userId, userId));
  } else {
    console.log(`  ✅ Adding user as organization owner`);
    await db.insert(member).values({
      id: `member-${userId}-${TEST_ORG.id}`,
      userId,
      organizationId: TEST_ORG.id,
      role: "owner",
      createdAt: new Date(),
    });
  }
}

/**
 * Main seed function
 */
async function seed() {
  const args = process.argv.slice(2);
  const isProd = args.includes("--prod");

  console.log("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
  console.log(`  🔐 OAuth Setup ${isProd ? "(Production Mode)" : "(Development Mode)"}`);
  console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n");

  // Verify database connection
  if (!process.env.DATABASE_URL) {
    console.error("❌ ERROR: DATABASE_URL not set!");
    console.error("   Please set DATABASE_URL in .env.local");
    process.exit(1);
  }

  const dbHost = process.env.DATABASE_URL.split("@")[1]?.split("/")[0] || "Connected";
  console.log(`📊 Database: ${dbHost}`);
  console.log(`📝 Source: src/lib/trusted-clients.ts`);
  console.log(`\n🔐 Seeding OAuth clients...\n`);

  // Filter clients based on mode
  const clientsToSeed = isProd
    ? TRUSTED_CLIENTS.filter((c) => c.clientId !== "robolearn-public-client")
    : TRUSTED_CLIENTS;

  // Seed OAuth clients
  for (const client of clientsToSeed) {
    await upsertClient(client);
  }

  // Seed test organization (only in dev mode)
  if (!isProd) {
    await seedOrganization();
  }

  // Display results
  const allClients = await db.select().from(oauthApplication);
  const seededClientIds = clientsToSeed.map((c) => c.clientId);
  const seededClients = allClients.filter((c) =>
    seededClientIds.includes(c.clientId!)
  );

  console.log("\n✅ Successfully configured!\n");
  console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
  console.log(`  ${isProd ? "Production" : "Development"} Clients`);
  console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n");

  seededClients.forEach((client, index) => {
    if (index > 0) console.log("\n" + "─".repeat(60) + "\n");
    console.log(`Client ID:       ${client.clientId}`);
    console.log(`Client Name:     ${client.name}`);
    console.log(`Client Type:     ${client.type} (PKCE flow)`);
    console.log(`Status:          ${client.disabled ? "DISABLED" : "ENABLED"}`);
    console.log(`\nRedirect URLs:`);
    client.redirectUrls?.split(",").forEach((url) => {
      console.log(`  - ${url}`);
    });
  });

  console.log("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n");
  console.log("📝 Next Steps:\n");
  console.log("1. Use these client IDs in your frontend applications");
  console.log("2. To manage redirect URLs, visit:");
  console.log(`   ${process.env.BETTER_AUTH_URL || "http://localhost:3001"}/admin/clients\n`);

  if (!isProd) {
    console.log("💡 Multi-Tenancy Enabled:\n");
    console.log("   - Test organization seeded (optional feature)");
    console.log("   - Use for testing tenant-scoped data access");
    console.log(`   - Test user: ${TEST_USER_EMAIL}\n`);
  }

  console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n");

  process.exit(0);
}

seed().catch((err) => {
  console.error("\n❌ Failed to seed:");
  console.error(err);
  process.exit(1);
});
