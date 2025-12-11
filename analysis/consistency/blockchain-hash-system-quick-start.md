# Blockchain Hash Consistency System - Quick Start Guide

**Date:** December 10, 2025  
**Status:** PROOF OF CONCEPT  
**Purpose:** Quick reference for using the hash-based consistency system

---

## OVERVIEW

The blockchain-like hash consistency system helps ensure document consistency by:

1. **Tracking dependencies** between documents
2. **Calculating content hashes** for each document
3. **Recording dependency hashes** in dependent documents
4. **Detecting changes** when source documents are modified

---

## QUICK START

### Step 1: Add Dependency Section to Your Document

Add this section at the end of your markdown file:

```markdown
---

## DOCUMENT DEPENDENCIES

<!-- Content Integrity System -->

### Verified Dependencies

| Document | Path | Hash | Last Verified | Status |
|----------|------|------|---------------|--------|
| Source Document | `../path/to/source.md` | `a1b2c3d4` | 2025-12-10 | ✅ Verified |

**This Document's Hash:** `98765432`  
**Last Updated:** 2025-12-10
```

### Step 2: Calculate Hashes for Dependencies

For each dependency, calculate its hash:

```bash
python scripts/calculate-hash.py path/to/dependency.md
```

Copy the hash (8 characters, e.g., `a1b2c3d4`) and add it to your dependency table. The hash is just for change detection - if it changes, you know the file changed and need to review consistency.

### Step 3: Check Consistency

Run the consistency checker:

```bash
# Check entire project
python scripts/consistency-checker.py

# Check specific file
python scripts/consistency-checker.py path/to/your-file.md
```

The checker will report:
- ✅ Verified dependencies (hash matches - file hasn't changed)
- ⚠️ Hash mismatches (dependency changed - review for consistency)
- ❌ Missing files (broken links)

---

## EXAMPLE

See `edits/book-01-final-scene-haskell-fairfax-confrontation-2025-12-05.md` for a working example with dependency tracking.

---

## WORKFLOW

### When You Edit a Document

1. **Make your changes**
2. **Run consistency checker:** `python scripts/consistency-checker.py`
3. **Review hash mismatches:** Check if dependent documents need updates
4. **Update dependent documents:** If needed, update content and re-verify hashes
5. **Update dependency hashes:** Recalculate and update hashes in dependent documents

### When You Add a New Dependency

1. **Add dependency to table** (with placeholder hash)
2. **Calculate hash:** `python scripts/calculate-hash.py dependency.md`
3. **Update table** with actual hash
4. **Set status** to "✅ Verified"
5. **Update "Last Verified"** date

---

## TOOLS

### `scripts/calculate-hash.py`
Calculates SHA-256 hash of a file.

**Usage:**
```bash
python scripts/calculate-hash.py file.md
```

### `scripts/consistency-checker.py`
Checks consistency across the project.

**Usage:**
```bash
# Check all files
python scripts/consistency-checker.py

# Check specific file
python scripts/consistency-checker.py file.md
```

---

## BEST PRACTICES

### 1. Track Critical Dependencies Only
- Don't track every reference
- Focus on documents that, if changed, would break your document
- Examples: Character files, world-building foundations, canon documents

### 2. Keep Hashes Current
- Update hashes when dependencies change
- Run consistency checks regularly
- Update "Last Verified" dates

### 3. Use Relative Paths
- Use relative paths from your document's location
- Example: `../characters/union/frank-a-haskell.md`

### 4. Document Status
- Use status indicators: ✅ Verified, ⚠️ Mismatch, ❌ Error
- Update status when you verify or fix issues

---

## INTERPRETING RESULTS

### ✅ Verified
Hash matches - dependency hasn't changed since last verification.

### ⚠️ Hash Mismatch
Dependency file has changed. Review changes to see if your document needs updates.

### ❌ File Not Found
Dependency path is broken. Check if file was moved or renamed.

---

## INTEGRATION

### Pre-commit Hook (Future)
```bash
# .git/hooks/pre-commit
python scripts/consistency-checker.py
# Exit with error if critical issues found
```

### CI/CD (Future)
```yaml
# .github/workflows/consistency.yml
- name: Check Consistency
  run: python scripts/consistency-checker.py
```

---

## LIMITATIONS

1. **Hash mismatch ≠ inconsistency**
   - Hash mismatch means the file changed
   - You still need to review if changes break your document

2. **Manual verification required**
   - System detects changes, not semantic issues
   - Human judgment still needed

3. **Maintenance overhead**
   - Need to keep hashes updated
   - More dependencies = more maintenance

4. **Not a replacement**
   - Complements manual consistency checks
   - Doesn't replace semantic review

---

## NEXT STEPS

1. **Review full analysis:** See `blockchain-hash-consistency-system-analysis.md`
2. **Try proof of concept:** Add dependency tracking to 2-3 documents
3. **Test workflow:** Make changes and verify detection works
4. **Evaluate:** Decide if system is worth expanding

---

## QUESTIONS?

- **Full documentation:** `analysis/consistency/blockchain-hash-consistency-system-analysis.md`
- **Tool documentation:** `scripts/README-consistency-tools.md`
- **Example:** `edits/book-01-final-scene-haskell-fairfax-confrontation-2025-12-05.md`

---

**Status:** PROOF OF CONCEPT - Ready for testing

