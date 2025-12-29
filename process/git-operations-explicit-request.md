# GIT OPERATIONS: EXPLICIT USER REQUEST REQUIRED

## **ABSOLUTE - NO ASSUMPTIONS ALLOWED**

**AI NEVER commits or pushes changes unless explicitly requested by the user.**

## The Rule

1. **AI must NEVER commit changes unless the user explicitly requests "commit" or "commit and push".**
2. **AI must NEVER push changes unless the user explicitly requests "push" or "commit and push".**
3. **AI must NEVER assume that commits or pushes are needed or desired.**
4. **AI must NEVER commit/push automatically after making edits, even if edits are complete.**

## Purpose

This rule exists to ensure:
- The user maintains full control over version control operations
- No unwanted commits clutter the git history
- The user can review all changes before committing
- Rate limits are not exceeded by unnecessary git operations
- The user decides when changes are ready to be committed

## What AI CAN Do

- Make file edits and changes as requested
- Stage files with `git add` if explicitly requested
- Check git status with `git status` if needed for analysis
- View git history with `git log` if needed for analysis
- Show diffs with `git diff` if needed for analysis
- Perform git operations when explicitly requested by the user

## What AI CANNOT Do

- Commit changes without explicit user request
- Push changes without explicit user request
- Assume that "making edits" implies "commit those edits"
- Assume that "completing a task" implies "commit the results"
- Automatically commit after consistency checks or hash updates
- Automatically commit after canonical updates
- Automatically commit after any batch of file operations

## Explicit Request Examples

**✅ ALLOWED - Explicit requests:**
- "Commit and push"
- "Commit these changes"
- "Push to remote"
- "Save this to git"
- "Commit the updates"

**❌ NOT ALLOWED - Assumed operations:**
- User says "make these edits" → AI commits (NO)
- User says "update the timeline" → AI commits (NO)
- User says "fix the inconsistency" → AI commits (NO)
- User says "done" → AI commits (NO)
- User says nothing → AI commits (NO)

## When User Requests Commit/Push

If the user explicitly requests a commit or push, AI should:
1. Confirm what will be committed (show `git status` or summary)
2. Create an appropriate commit message based on the changes
3. Execute the commit/push operation
4. Report the results

## Enforcement

**This rule applies to ALL git operations that modify repository state.**

AI must always ask before committing or pushing, unless the user's request explicitly includes those words.

**Status:** ABSOLUTE RULE  
**No exceptions. No assumptions. Explicit request required.**
