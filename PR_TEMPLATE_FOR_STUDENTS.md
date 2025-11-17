# GitHub Pull Request Template
## Professional Template with AI Transparency

**Use this template for EVERY pull request you create.**

Copy the text below into your GitHub PR description field. Fill out each section.

---

```markdown
## Summary
[One sentence: What does this PR do?]

[Optional: 2-3 sentences explaining the context and why this change matters]

## Changes
- [What file changed and what did it do?]
- [What file changed and what did it do?]
- [Any new files created?]

## Why This Change
[Explain the problem you're solving or feature you're adding]

## AI Assistance
**AI Tool Used**: [ChatGPT / Claude / Gemini / None / Other]

**What AI Generated** (if applicable):
- [AI contribution #1]
- [AI contribution #2]
- [Be specific: "Generated try/except structure" not just "generated code"]

**What I Modified** (if applicable):
- [Your modification #1 - explain why]
- [Your modification #2 - explain why]
- [Bugs found and fixed]
- [If no AI: "N/A - I wrote this from scratch"]

## Testing Done
- [Test case 1: What you tested, what happened]
- [Test case 2: What you tested, what happened]
- [Edge cases: What edge cases did you test?]

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)

## Checklist
- [ ] I have reviewed my own code
- [ ] I have tested my changes
- [ ] I have documented AI assistance (if applicable)
- [ ] My changes don't break anything

## Screenshots (if applicable)
[If this affects UI: paste before/after screenshots]

## Additional Notes
[Any other information reviewers should know]
```

---

## How to Use This Template

### Step 1: Copy Template
Copy the text above (the section in triple backticks).

### Step 2: Paste into GitHub
1. Open your PR on GitHub
2. Scroll to PR description box
3. Paste template

### Step 3: Fill Out Each Section
1. **Summary**: 1-3 sentences explaining what PR does
2. **Changes**: Bulleted list of files changed
3. **Why This Change**: Context and motivation
4. **AI Assistance**: THIS IS CRITICAL
   - Name the tool (ChatGPT, Claude, etc.)
   - List what AI generated
   - List what you modified and why
5. **Testing Done**: Specific test cases, not vague
6. **Type of Change**: Check relevant box
7. **Checklist**: Verify you've done everything
8. **Screenshots**: Only if visually relevant
9. **Additional Notes**: Anything else reviewers need

### Step 4: Create Pull Request
Click "Create pull request" button.

---

## Examples

### Example 1: Simple PR Without AI

**File**: `calculator.py`

```markdown
## Summary
Added multiplication function to calculator for basic arithmetic operations.

## Changes
- calculator.py: Added multiply(a, b) function

## Why This Change
Users requested multiplication feature. Simple addition to existing calculator.

## AI Assistance
**AI Tool Used**: None

**What AI Generated**:
N/A - I wrote this function manually.

**What I Modified**:
N/A - not applicable.

## Testing Done
- multiply(3, 4) = 12 ✓
- multiply(0, 5) = 0 ✓
- multiply(-2, 3) = -6 ✓

## Type of Change
- [ ] Bug fix
- [x] New feature
- [ ] Breaking change

## Checklist
- [x] I have reviewed my own code
- [x] I have tested my changes
- [x] I have documented AI assistance (not applicable)
- [x] My changes don't break anything
```

---

### Example 2: PR With AI-Generated Code

**File**: `calculator.py`

```markdown
## Summary
Added comprehensive error handling to calculator to prevent crashes on invalid input.

## Changes
- calculator.py: Added try/except blocks to all arithmetic functions
- calculator.py: Added validate_input() function
- calculator.py: Added user-friendly error messages

## Why This Change
Calculator was crashing on invalid input. Users need graceful error handling.

## AI Assistance
**AI Tool Used**: ChatGPT (via Claude Code)

**What AI Generated**:
- Try/except block structure for all arithmetic functions
- validate_input() function with regex pattern
- Initial error message templates

**What I Modified**:
1. Error Messages (Reason: Users need plain language, not technical jargon)
   - Original: "ValueError: Input does not match float pattern"
   - Changed to: "Error: Please enter a number"

2. Edge Cases (Reason: AI missed empty input case)
   - Added explicit check: `if not input_str: raise ValueError("Input required")`
   - Tested: empty input, very large numbers, special characters

3. Logging (Reason: Need debugging visibility)
   - Added print statements for debugging
   - Helps identify which operation caused error

## Testing Done
- Valid inputs: 5 + 3, 10 - 2, 4 * 3, 20 / 4 → All work ✓
- Edge cases:
  - Empty input: Shows "Input required" ✓
  - Text input: Shows "Please enter a number" ✓
  - Division by zero: Shows "Cannot divide by zero" ✓
  - Very large numbers (999999999): Works correctly ✓
  - Negative numbers (-5, -3): Works correctly ✓

## Type of Change
- [ ] Bug fix
- [x] New feature
- [ ] Breaking change

## Checklist
- [x] I have reviewed my own code
- [x] I have tested my changes
- [x] I have documented AI assistance
- [x] My changes don't break anything
```

---

### Example 3: Bug Fix PR

**File**: `calculator.py`

```markdown
## Summary
Fixed division by zero crash. Now displays user-friendly error message instead of crashing.

## Changes
- calculator.py: Added zero-check before division operation

## Why This Change
Bug: Dividing by zero crashes the program. User impact: Lost unsaved work if not committed.

## AI Assistance
**AI Tool Used**: Claude

**What AI Generated**:
- Suggested `if b == 0: raise ValueError(...)` pattern
- Suggested error message wording

**What I Modified**:
- Adjusted error message to match existing style
- Tested with various division scenarios to ensure fix works
- Found and fixed: Error message wasn't being displayed to user (bug in AI code)

## Testing Done
- Normal division (10 / 2) → Works ✓
- Division by zero (10 / 0) → Shows error message ✓
- Very small numbers (0.001 / 0.002) → Works ✓
- Negative division (-10 / 2) → Works ✓

## Type of Change
- [x] Bug fix
- [ ] New feature
- [ ] Breaking change

## Checklist
- [x] I have reviewed my own code
- [x] I have tested my changes
- [x] I have documented AI assistance
- [x] My changes don't break anything

## Additional Notes
This was discovered during testing in Lesson 5. The bug would have caused data loss if not caught.
```

---

## Key Points About This Template

### ✅ DO:

- **Name the AI tool**: "ChatGPT" not "an AI"
- **List specific AI contributions**: "Generated try/except structure" not "generated code"
- **Explain your modifications**: "Made error messages user-friendly because non-programmers review this" not just "modified it"
- **Be honest about bugs found**: "AI missed empty input edge case" shows your expertise
- **Test thoroughly**: List specific test cases and results
- **Use this template for EVERY PR**: Build the habit

### ❌ DON'T:

- **Hide AI usage**: Transparency is strength, not weakness
- **Overclaim credit**: Don't take credit for AI-generated code
- **Be vague**: "used AI to fix code" is not detailed enough
- **Skip testing**: Always verify before merging
- **Merge without reviewing diff**: Always check what you're merging
- **Use generic error messages**: Help future readers understand the code

---

## Template Sections Explained

### Summary
- **Purpose**: What does this PR do in plain English?
- **Length**: 1-3 sentences maximum
- **Audience**: Non-technical people should understand what changed

### Changes
- **Purpose**: Which files were affected?
- **Format**: Bullet points, one per file
- **Detail**: Brief description of what happened to each file

### Why This Change
- **Purpose**: Context—what problem are you solving?
- **Length**: 2-3 sentences
- **Value**: Helps reviewers understand importance

### AI Assistance (CRITICAL FOR SC-008)
- **Purpose**: Document exactly what AI contributed and what you added
- **AI Tool Used**: ChatGPT, Claude, Gemini, etc. (be specific)
- **What AI Generated**: Specific list (not vague like "generated code")
- **What I Modified**: Your improvements, bug fixes, tests
- **Why It Matters**: Shows you didn't blindly trust AI; you validated it

### Testing Done
- **Purpose**: Prove your changes work
- **Format**: Specific test cases with results
- **Examples**:
  - "multiply(3, 4) = 12 ✓"
  - "Empty input shows error message ✓"
  - "Division by zero doesn't crash ✓"

### Type of Change
- **Purpose**: Categorize the PR
- **Options**: Bug fix, new feature, breaking change
- **Why It Matters**: Helps reviewers assess impact

### Checklist
- **Purpose**: Self-verification before submitting
- **Critical**: Have you tested? Reviewed? Documented AI assistance?

---

## Customization: Your First PR

When you create your first PR, you might not have all sections completed. That's okay.

**Minimum viable PR**:
```markdown
## Summary
Added multiplication function

## Changes
- calculator.py: Added multiply(a, b)

## AI Assistance
**AI Tool Used**: None (I wrote it)

## Testing Done
- multiply(3, 4) = 12 ✓

## Checklist
- [x] I have reviewed my own code
- [x] I have tested my changes
- [x] My changes don't break anything
```

**As you gain experience**, add more detail.

---

## Real-World Professional PRs

Here's what professional developers include:

- **Google's PR template**: Summary, Risk level, Testing evidence
- **GitHub's template**: What, Why, How, Testing checklist
- **Facebook's template**: Intent, Approach, Testing, Related info

**This template is hybrid**: Combines professional practices with AI transparency (new requirement for AI-native development).

---

## When to Use This Template

### Every single PR:
- [ ] Feature PRs (new functionality)
- [ ] Bug fix PRs (fixing existing issues)
- [ ] Refactoring PRs (improving code structure)
- [ ] Documentation PRs (updating docs)

### Even if:
- [ ] PR is small (1 line change: use template)
- [ ] You're working solo (no reviewers: template is for YOU to think clearly)
- [ ] PR seems obvious (context in description helps future-you)

---

## Tips for Great PR Descriptions

### Tip 1: Think Like a Reviewer
What would help someone understand this PR 6 months from now?

### Tip 2: Tell the Story
Summary → Why → What Changed → How I Tested It

### Tip 3: Be Specific
❌ Bad: "Fixed code"
✅ Good: "Fixed division by zero crash by adding check before division"

### Tip 4: Document AI
❌ Bad: "Used AI"
✅ Good: "ChatGPT generated try/except structure. I simplified error messages and tested edge cases."

### Tip 5: Proof Your Work
❌ Bad: "Tested thoroughly"
✅ Good: "Tested: multiply(3,4)=12 ✓, multiply(-2,3)=-6 ✓, multiply(0,5)=0 ✓"

---

## Common Mistakes

### Mistake 1: Forgetting AI Transparency
**Wrong**:
```markdown
## AI Assistance
None
```

**Right**:
```markdown
## AI Assistance
**AI Tool Used**: ChatGPT
**What AI Generated**: Error handling structure
**What I Modified**: Simplified error messages, tested edge cases
```

### Mistake 2: Vague Summary
**Wrong**: "Bug fixes and improvements"
**Right**: "Fixed division by zero crash and added error message"

### Mistake 3: No Testing Evidence
**Wrong**: "Tested and works"
**Right**: "Tested: 10/0 shows error ✓, 10/2=5 ✓, -10/2=-5 ✓"

### Mistake 4: Overclaiming Credit
**Wrong**: "I built this error handling system" (when AI generated 80%)
**Right**: "ChatGPT generated error structure. I refined messages and tested edge cases."

---

## Using This Template in Lesson 7 (Capstone)

In Lesson 7, you'll create a complete project with AI assistance. You MUST use this template.

**Requirement (SC-008)**: 100% of capstone PRs include AI attribution section

**Your task**: Create at least 1 PR for your capstone project with:
- [ ] Clear summary of changes
- [ ] AI assistance documented (tool, what it generated, what you modified)
- [ ] Testing evidence
- [ ] All checklist items completed

---

## Need Help?

### If you're stuck on AI Assistance section:
Use this prompt with ChatGPT:

```
I just created a PR where ChatGPT helped me with [describe what you did].
ChatGPT generated [describe what it generated].
I modified [describe what you modified].

Write a professional PR description "AI Assistance" section for this work.
```

### If you're stuck on Testing section:
Think of 3-5 specific test cases:
1. Normal case (what should work)
2. Edge case 1 (boundary condition)
3. Edge case 2 (another boundary)
4. Error case (what shouldn't work)
5. Verify all work correctly

---

## Summary

**This template is your professional GitHub skill builder.**

Use it for:
- Every PR you create
- Every project you build
- Every AI collaboration you document

**It teaches**:
- Professional communication
- AI transparency
- Testing mindset
- Code review readiness

**When you graduate**: This template translates directly to professional development jobs where:
- Code review is required
- AI collaboration is documented
- Communication is valued
- Testing is verified

---

**Copy. Paste. Fill Out. Create PR. Merge With Confidence.**

That's the GitHub workflow.

