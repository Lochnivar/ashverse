# Consistency Checking Tools

This directory contains proof-of-concept scripts for the blockchain-like hash consistency system.

## Tools

### `calculate-hash.py`
Calculates the SHA-256 hash of a markdown file.

**Usage:**
```bash
python scripts/calculate-hash.py path/to/file.md
```

**Output:**
```
a1b2c3d4
```

(8-character hash for change detection)

Use this hash when adding dependency declarations to documents. The short hash (8 characters) is sufficient for change detection - if it changes, you know the file changed and need to review consistency.

### `consistency-checker.py`
Checks consistency of dependencies across the project.

**Usage:**
```bash
# Check entire project
python scripts/consistency-checker.py

# Check specific file
python scripts/consistency-checker.py path/to/file.md [base_dir]
```

**Output:**
- Report of all hash mismatches
- List of verified dependencies
- Files with dependency tracking

## Example Workflow

### 1. Add Dependency Tracking to a Document

Edit your markdown file and add a "Document Dependencies" section:

```markdown
---

## Document Dependencies

<!-- Content Integrity System: Tracks dependencies and their content hashes -->

### Verified Dependencies

| Document | Path | Hash | Last Verified | Status |
|----------|------|------|---------------|--------|
| Core Foundation | `world-building/01-core-foundation.md` | `sha256:...` | 2025-12-10 | ✅ Verified |

**This Document's Hash:** `sha256:...`  
**Last Updated:** 2025-12-10
```

### 2. Calculate Hash for Dependency

```bash
python scripts/calculate-hash.py world-building/01-core-foundation.md
```

Copy the hash and add it to your dependency table.

### 3. Check Consistency

```bash
python scripts/consistency-checker.py
```

This will report any hash mismatches, indicating that dependencies may have changed.

## Notes

- These are proof-of-concept scripts
- They require Python 3.6+
- Hash calculation includes full file content
- Uses short hashes (8 characters) - sufficient for change detection, not cryptographic security
- Relative paths are resolved from the document's directory
- Hash mismatch = file changed, review for consistency (not necessarily an error)

## Future Enhancements

- Pre-commit hook integration
- CI/CD integration
- Automatic hash updates
- Dependency graph visualization
- More robust markdown parsing

