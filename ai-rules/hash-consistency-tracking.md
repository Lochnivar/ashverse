# AI Rule: Hash Consistency Tracking

**Date:** December 10, 2025  
**Status:** ACTIVE RULE  
**Purpose:** Ensure dependency hashes are updated when files are edited

---

## THE RULE

**When AI edits any markdown file, it MUST:**

1. **Calculate the new hash** of the edited file
2. **Update dependency hashes** in files that depend on the edited file
3. **Update the file's own hash** if it has a "Document Dependencies" section

---

## PROCEDURE

### Step 1: After Editing Any File

After making edits to a markdown file:

1. **Calculate the new hash:**
   ```bash
   python scripts/calculate-hash.py <edited-file-path>
   ```

2. **Update the file's own hash** (if it has a "Document Dependencies" section):
   - Find the line: `**This Document's Hash:** `hash``
   - Replace with the new hash
   - Update `**Last Updated:**` date

### Step 2: Update Dependent Files

If the edited file is a source document (has dependencies tracked by other files):

1. **Find files that depend on the edited file:**
   - Run: `python scripts/consistency-checker.py`
   - Look for hash mismatches for the edited file

2. **Update each dependent file:**
   - Open the dependent file
   - Find the dependency entry for the edited file
   - Update the hash in the dependency table
   - Update `Last Verified` date
   - Set status to `✅ Verified`

### Step 3: Verify

After updating hashes:

1. **Run consistency check:**
   ```bash
   python scripts/consistency-checker.py
   ```

2. **Verify no hash mismatches** for the edited file or its dependencies

---

## EXAMPLES

### Example 1: Editing a Source File

**Scenario:** Editing `world-building/01-core-foundation.md`

**Steps:**
1. Make edits to the file
2. Calculate new hash: `python scripts/calculate-hash.py world-building/01-core-foundation.md`
3. Find files that depend on it (e.g., `characters/union/frank-a-haskell.md`)
4. Update the hash in dependent files' dependency tables
5. Run consistency check to verify

### Example 2: Editing a File with Dependencies

**Scenario:** Editing `characters/union/frank-a-haskell.md` (which has dependencies)

**Steps:**
1. Make edits to the file
2. Calculate new hash: `python scripts/calculate-hash.py characters/union/frank-a-haskell.md`
3. Update the file's own hash in its "Document Dependencies" section
4. Find files that depend on it (e.g., `edits/book-01-final-scene-haskell-fairfax-confrontation-2025-12-05.md`)
5. Update hashes in dependent files
6. Run consistency check to verify

### Example 3: Adding Dependency Tracking

**Scenario:** Adding dependency tracking to a new file

**Steps:**
1. Add "Document Dependencies" section to the file
2. Calculate hashes for each dependency: `python scripts/calculate-hash.py <dependency-path>`
3. Add dependencies to the table with calculated hashes
4. Calculate the file's own hash: `python scripts/calculate-hash.py <file-path>`
5. Add the file's hash to the "This Document's Hash" line

---

## QUICK REFERENCE

### Hash Calculation
```bash
# Calculate hash for a file
python scripts/calculate-hash.py <file-path>

# Output: 8-character hash (e.g., "a1b2c3d4")
```

### Consistency Check
```bash
# Check all files
python scripts/consistency-checker.py

# Check specific file
python scripts/consistency-checker.py <file-path>
```

### Dependency Table Format
```markdown
| Document | Path | Hash | Last Verified | Status |
|----------|------|------|---------------|--------|
| Source Document | `../path/to/source.md` | `a1b2c3d4` | 2025-12-10 | ✅ Verified |

**This Document's Hash:** `98765432`  
**Last Updated:** 2025-12-10
```

---

## WHEN TO UPDATE HASHES

### Always Update:
- ✅ After editing any file content
- ✅ After adding/removing sections
- ✅ After changing substantive content
- ✅ After fixing inconsistencies

### Don't Update For:
- ❌ Whitespace-only changes (but hash will change anyway - that's fine)
- ❌ Comments-only changes (but hash will change anyway - that's fine)

**Note:** Since the hash includes the entire file content, any change will produce a new hash. This is correct behavior - it detects any change.

---

## AUTOMATION

### Manual Process (Current)
1. Edit file
2. Calculate hash
3. Update hashes in dependent files
4. Verify with consistency checker

### Future Enhancement
Consider automating hash updates:
- Pre-commit hook to update hashes
- Script to auto-update dependent files
- CI/CD integration

---

## TROUBLESHOOTING

### Hash Mismatch After Edit
**Symptom:** Consistency checker shows hash mismatch for edited file

**Solution:**
1. Recalculate hash: `python scripts/calculate-hash.py <file-path>`
2. Update hash in dependent files
3. Verify with consistency checker

### Dependent File Not Found
**Symptom:** Consistency checker shows "File not found" error

**Solution:**
1. Check path in dependency table (relative paths)
2. Verify file exists at that path
3. Update path if file was moved

### Multiple Dependencies
**Symptom:** Many files depend on the edited file

**Solution:**
1. Run consistency checker to see all affected files
2. Update hashes in all dependent files
3. Batch update if possible (future enhancement)

---

## INTEGRATION WITH OTHER RULES

This rule works alongside:
- **Golden Rule (No Original Text):** Hash tracking applies to all files, including edits folder
- **Consistency Rules:** Hash tracking helps maintain consistency
- **File Organization Rules:** Dependency tracking documents relationships

---

## STATUS

**Active Rule** - Must be followed for all file edits

**Last Updated:** 2025-12-10

---

## QUICK CHECKLIST

When editing any file:
- [ ] Make edits
- [ ] Calculate new hash: `python scripts/calculate-hash.py <file>`
- [ ] Update file's own hash (if it has dependencies section)
- [ ] Find dependent files: `python scripts/consistency-checker.py`
- [ ] Update hashes in dependent files
- [ ] Verify: `python scripts/consistency-checker.py`

---

**Remember:** Hash tracking is about change detection, not perfection. If a hash changes, it means the file changed - review for consistency, but don't panic. The system is designed to catch changes early, not to prevent them.

