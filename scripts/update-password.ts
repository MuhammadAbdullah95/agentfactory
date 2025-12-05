#!/usr/bin/env npx tsx
/**
 * Quick password update script for admin users
 * Usage: npx tsx scripts/update-password.ts <email> <new-password>
 */

import { neon } from "@neondatabase/serverless";
import bcrypt from "bcryptjs";

async function main() {
  const [email, newPassword] = process.argv.slice(2);

  if (!email || !newPassword) {
    console.error("Usage: npx tsx scripts/update-password.ts <email> <new-password>");
    process.exit(1);
  }

  if (newPassword.length < 8) {
    console.error("Password must be at least 8 characters");
    process.exit(1);
  }

  const databaseUrl = process.env.DATABASE_URL;
  if (!databaseUrl) {
    console.error("DATABASE_URL not set");
    process.exit(1);
  }

  const sql = neon(databaseUrl);

  // Find user
  const users = await sql`SELECT id, email, role FROM public."user" WHERE email = ${email}`;
  if (users.length === 0) {
    console.error(`User not found: ${email}`);
    process.exit(1);
  }

  const user = users[0];
  console.log(`Found user: ${user.email} (role: ${user.role})`);

  // Hash new password
  const hashedPassword = await bcrypt.hash(newPassword, 10);

  // Update password
  const result = await sql`
    UPDATE public.account
    SET password = ${hashedPassword}, updated_at = ${new Date().toISOString()}
    WHERE user_id = ${user.id} AND provider_id = 'credential'
    RETURNING user_id
  `;

  if (result.length === 0) {
    console.error("No credential account found for user");
    process.exit(1);
  }

  console.log(`✅ Password updated for ${email}`);
}

main().catch(console.error);
