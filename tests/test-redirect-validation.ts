/**
 * Test Suite for Redirect URL Validation
 * 
 * Verifies that the redirect validation logic correctly allows trusted origins
 * and blocks untrusted ones to prevent open redirect vulnerabilities.
 */

import { getTrustedOrigins, isValidRedirectUrl } from "../src/lib/redirect-utils";

console.log("============================================================");
console.log("Redirect URL Validation Test Suite");
console.log("============================================================\n");

// Mock window.location for testing
(global as any).window = {
  location: {
    origin: "http://localhost:3001"
  }
};

let passedTests = 0;
let totalTests = 0;

function test(name: string, fn: () => boolean) {
  totalTests++;
  try {
    const result = fn();
    if (result) {
      console.log(`✅ ${name}: PASS`);
      passedTests++;
    } else {
      console.log(`❌ ${name}: FAIL - Test returned false`);
    }
  } catch (error) {
    console.log(`❌ ${name}: FAIL - ${error instanceof Error ? error.message : String(error)}`);
  }
}

// Test 1: Get trusted origins returns expected origins
test("Get Trusted Origins - Contains localhost:3001", () => {
  const origins = getTrustedOrigins();
  return origins.includes("http://localhost:3001");
});

// Test 2: Get trusted origins includes RoboLearn
test("Get Trusted Origins - Contains RoboLearn", () => {
  const origins = getTrustedOrigins();
  return origins.includes("https://mjunaidca.github.io");
});

// Test 3: Get trusted origins includes AI Native
test("Get Trusted Origins - Contains AI Native", () => {
  const origins = getTrustedOrigins();
  return origins.includes("https://ai-native.panaversity.org");
});

// Test 4: Relative URLs are valid
test("Valid Redirect - Relative URL", () => {
  return isValidRedirectUrl("/account/profile");
});

// Test 5: Same origin URLs are valid
test("Valid Redirect - Same Origin", () => {
  return isValidRedirectUrl("http://localhost:3001/auth/sign-in");
});

// Test 6: RoboLearn origin is valid
test("Valid Redirect - RoboLearn Origin", () => {
  return isValidRedirectUrl("https://mjunaidca.github.io/robolearn");
});

// Test 7: RoboLearn with path is valid
test("Valid Redirect - RoboLearn with Path", () => {
  return isValidRedirectUrl("https://mjunaidca.github.io/robolearn/chapter/1");
});

// Test 8: AI Native origin is valid
test("Valid Redirect - AI Native Origin", () => {
  return isValidRedirectUrl("https://ai-native.panaversity.org");
});

// Test 9: AI Native with path is valid
test("Valid Redirect - AI Native with Path", () => {
  return isValidRedirectUrl("https://ai-native.panaversity.org/dashboard");
});

// Test 10: Untrusted origin is invalid
test("Invalid Redirect - Untrusted Origin", () => {
  return !isValidRedirectUrl("https://evil.example.com/steal-tokens");
});

// Test 11: Malicious URL with @ is invalid
test("Invalid Redirect - Malicious URL with @", () => {
  return !isValidRedirectUrl("https://mjunaidca.github.io@evil.com");
});

// Test 12: Empty string is invalid
test("Invalid Redirect - Empty String", () => {
  return !isValidRedirectUrl("");
});

// Test 13: Invalid URL format
test("Invalid Redirect - Malformed URL", () => {
  return !isValidRedirectUrl("not-a-valid-url");
});

// Test 14: localhost:3000 (client app) is valid
test("Valid Redirect - Client App (localhost:3000)", () => {
  return isValidRedirectUrl("http://localhost:3000");
});

// Test 15: Panaversity.org is valid
test("Valid Redirect - Panaversity.org", () => {
  const origins = getTrustedOrigins();
  // Check if panaversity.org is in trusted origins
  const hasPanaversity = origins.some(origin => origin.includes("panaversity.org"));
  return hasPanaversity && isValidRedirectUrl("https://panaversity.org/home");
});

console.log("\n============================================================");
console.log(`Results: ${passedTests}/${totalTests} tests passed`);
if (passedTests !== totalTests) {
  console.log("\nFailed tests:");
  process.exit(1);
} else {
  console.log("\n✅ All tests passed!");
}
console.log("============================================================");
