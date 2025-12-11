# Blockchain-Like Hash Consistency System: Analysis & Proposal

**Date:** December 10, 2025  
**Status:** PROPOSAL - UNDER INVESTIGATION  
**Purpose:** Investigate using content hashing and dependency links to ensure consistency across project documents

---

## EXECUTIVE SUMMARY

This document explores implementing a blockchain-like content integrity system for the Ashverse project. The system would:

1. **Calculate content hashes** for each document
2. **Establish dependency links** between related documents
3. **Record dependency hashes** in dependent documents
4. **Validate consistency** by comparing recorded hashes to current hashes

This would provide automated detection of inconsistencies when source documents change, complementing existing manual consistency checks.

---

## CURRENT STATE ANALYSIS

### Existing Consistency Management

**Strengths:**
- Manual consistency checks documented in `analysis/consistency/`
- "Related Documents" sections in many files using markdown links
- Master documents (e.g., `canon-master-document.md`, `world-building/01-core-foundation.md`)
- Comprehensive audit trails

**Challenges:**
- Manual process is time-consuming
- Inconsistencies discovered reactively (after changes made)
- No automated way to detect when a source document changes
- Dependency relationships not explicitly tracked
- Hash verification not currently used

### Example Dependency Patterns

From analyzing the codebase, common dependency patterns include:

1. **Character files → World-building files**
   - `characters/union/frank-a-haskell.md` depends on:
     - `world-building-master/01-core-foundation.md` (point of divergence)
     - `world-building/economic/northern-raids-comprehensive-catalog.md` (raid details)

2. **Analysis files → Source files**
   - `analysis/economic/raid-count-plausibility-analysis-2025-12-10.md` depends on:
     - `world-building/economic/northern-raids-comprehensive-catalog.md`
     - `canon-master-document.md`

3. **Scene files → Character files**
   - `edits/book-01-final-scene-haskell-fairfax-confrontation-2025-12-05.md` depends on:
     - `characters/union/frank-a-haskell.md`
     - `characters/confederate/john-walter-fairfax.md` (implied)

4. **Compendium files → Multiple sources**
   - Compendium chapters depend on world-building, character, and timeline files

---

## PROPOSED SYSTEM DESIGN

### Core Concept

**Blockchain-like properties:**
- **Content addressing:** Each document has a unique hash based on its content
- **Dependency chains:** Documents record hashes of their dependencies
- **Integrity verification:** Hash mismatches indicate inconsistencies
- **Immutable history:** Hash changes reveal when documents were modified

**Key difference from blockchain:**
- Not distributed/consensus-based
- Not proof-of-work
- Focused on content integrity, not transaction validation
- More like a Merkle tree or content-addressable storage

### System Components

#### 1. Content Hash Calculation

**Algorithm:** SHA-256 (standard, widely supported)

**What to hash:**
- Full document content (markdown text)
- Exclude metadata sections (date, status) from hash calculation
- Include only substantive content

**Hash format:**
```
Hash: a1b2c3d4
```

**Note:** Short hashes (6-10 characters) are sufficient for change detection. We use the first 8 characters of SHA-256, which provides excellent change detection with minimal overhead.

#### 2. Dependency Declaration

**Format in markdown:**
```markdown
## Document Dependencies

<!-- Hash-verified dependencies -->
- [Source Document Title](./path/to/source.md)  
  - **Hash:** `a1b2c3d4`  
  - **Last Verified:** 2025-12-10  
  - **Status:** ✅ Verified

- [Another Source](./path/to/another.md)  
  - **Hash:** `98765432`  
  - **Last Verified:** 2025-12-10  
  - **Status:** ⚠️ Hash Mismatch (document may have changed)
```

#### 3. Consistency Check Process

**Automated check:**
1. Read all markdown files
2. Extract dependency declarations
3. Calculate current hash of each dependency
4. Compare to recorded hash
5. Report mismatches

**Manual verification:**
- When a document changes, update dependent documents
- Recalculate and update hash in dependent documents
- Or: Accept hash mismatch as signal to review dependency

---

## IMPLEMENTATION APPROACHES

### Option 1: Frontmatter Metadata (Recommended)

**Format:**
```markdown
---
title: Document Title
dependencies:
  - path: world-building/01-core-foundation.md
    hash: sha256:a1b2c3d4e5f6...
    verified: 2025-12-10
  - path: characters/union/frank-a-haskell.md
    hash: sha256:9876543210ab...
    verified: 2025-12-10
content-hash: sha256:current-doc-hash...
---

# Document Title

[Content here]
```

**Pros:**
- Clean separation of metadata
- Easy to parse programmatically
- Standard YAML frontmatter format
- Doesn't clutter document content

**Cons:**
- Requires YAML parser
- Some markdown processors may not handle frontmatter well

### Option 2: Markdown Section (Current Format Compatible)

**Format:**
```markdown
# Document Title

[Content here]

---

## Document Dependencies

<!-- 
Content Integrity System
This section tracks dependencies and their content hashes
-->

### Verified Dependencies

| Document | Path | Hash | Last Verified | Status |
|----------|------|------|---------------|--------|
| Core Foundation | `world-building/01-core-foundation.md` | `sha256:a1b2c3...` | 2025-12-10 | ✅ Verified |
| Frank Haskell | `characters/union/frank-a-haskell.md` | `sha256:987654...` | 2025-12-10 | ⚠️ Mismatch |

**This Document's Hash:** `sha256:current-doc-hash...`  
**Last Updated:** 2025-12-10
```

**Pros:**
- Works with existing markdown structure
- Human-readable
- No special parsing needed
- Visible in document

**Cons:**
- Clutters document content
- Requires manual maintenance
- Table format may be verbose

### Option 3: Separate Metadata File

**Format:**
- `document.md` (content)
- `document.md.meta` (JSON/YAML with dependencies and hashes)

**Pros:**
- Complete separation
- Easy to parse
- Doesn't affect document readability

**Cons:**
- Two files per document
- Risk of files getting out of sync
- More complex file management

---

## RECOMMENDED IMPLEMENTATION

### Phase 1: Proof of Concept

**Scope:** Implement for high-value dependency chains

**Target documents:**
1. `edits/book-01-final-scene-haskell-fairfax-confrontation-2025-12-05.md`
   - Dependencies: Character files, world-building foundation
2. `analysis/economic/raid-count-plausibility-analysis-2025-12-10.md`
   - Dependencies: Raid catalog, canon master document
3. `characters/union/frank-a-haskell.md`
   - Dependencies: World-building foundation, raid catalog

**Implementation:**
- Use Option 2 (Markdown Section) for compatibility
- Add dependency tracking section to target documents
- Create simple script to calculate and verify hashes

### Phase 2: Tooling

**Scripts needed:**
1. **Hash Calculator:**
   - `scripts/calculate-hash.py` or `scripts/calculate-hash.js`
   - Input: markdown file path
   - Output: SHA-256 hash

2. **Dependency Extractor:**
   - `scripts/extract-dependencies.py`
   - Input: markdown file
   - Output: list of declared dependencies

3. **Consistency Checker:**
   - `scripts/check-consistency.py`
   - Input: directory or file
   - Output: report of hash mismatches

4. **Hash Updater:**
   - `scripts/update-dependency-hash.py`
   - Input: file path, dependency path
   - Output: updated file with new hash

### Phase 3: Integration

**Workflow integration:**
- Pre-commit hook: Check consistency before commits
- CI/CD: Automated consistency checks
- Manual tool: Run checks before major edits

---

## EXAMPLE IMPLEMENTATION

### Example 1: Character File with Dependencies

**File:** `characters/union/frank-a-haskell.md`

**Add at end:**
```markdown
---

## Document Dependencies

<!-- Content Integrity System: Tracks dependencies and their content hashes -->

### Verified Dependencies

| Document | Path | Hash | Last Verified | Status |
|----------|------|------|---------------|--------|
| Core Foundation | `world-building/01-core-foundation.md` | `sha256:...` | 2025-12-10 | ✅ Verified |
| Northern Raids Catalog | `world-building/economic/northern-raids-comprehensive-catalog.md` | `sha256:...` | 2025-12-10 | ✅ Verified |

**This Document's Hash:** `sha256:...`  
**Last Updated:** 2025-12-10
```

### Example 2: Analysis File with Dependencies

**File:** `analysis/economic/raid-count-plausibility-analysis-2025-12-10.md`

**Add at end:**
```markdown
---

## Document Dependencies

<!-- Content Integrity System -->

### Verified Dependencies

| Document | Path | Hash | Last Verified | Status |
|----------|------|------|---------------|--------|
| Northern Raids Catalog | `world-building/economic/northern-raids-comprehensive-catalog.md` | `a1b2c3d4` | 2025-12-10 | ✅ Verified |
| Canon Master Document | `canon-master-document.md` | `98765432` | 2025-12-10 | ✅ Verified |
| Economic Systems Master | `world-building-master/02-economic-systems.md` | `[hash]` | 2025-12-10 | ✅ Verified |

**This Document's Hash:** `12345678`  
**Last Updated:** 2025-12-10
```

### Example 3: Scene File with Dependencies

**File:** `edits/book-01-final-scene-haskell-fairfax-confrontation-2025-12-05.md`

**Add at end:**
```markdown
---

## Document Dependencies

<!-- Content Integrity System -->

### Verified Dependencies

| Document | Path | Hash | Last Verified | Status |
|----------|------|------|---------------|--------|
| Frank A. Haskell | `characters/union/frank-a-haskell.md` | `a1b2c3d4` | 2025-12-10 | ✅ Verified |
| John Walter Fairfax | `characters/confederate/john-walter-fairfax.md` | `98765432` | 2025-12-10 | ✅ Verified |
| Core Foundation | `world-building/01-core-foundation.md` | `fedcba98` | 2025-12-10 | ✅ Verified |

**This Document's Hash:** `12345678`  
**Last Updated:** 2025-12-10
```

---

## ADVANTAGES

### 1. Automated Detection
- **Immediate feedback:** Know when dependencies change
- **No manual scanning:** Scripts can check entire project
- **Early warning:** Catch inconsistencies before they propagate

### 2. Explicit Dependencies
- **Documentation:** Clear record of what each file depends on
- **Impact analysis:** Know what breaks when you change a file
- **Dependency graph:** Can visualize document relationships

### 3. Version Tracking
- **Change detection:** Hash changes reveal modifications
- **History:** Can track when dependencies were last verified
- **Audit trail:** Record of consistency checks

### 4. Scalability
- **Handles growth:** Works as project expands
- **Automated:** Reduces manual consistency checking burden
- **Complements existing:** Works alongside manual audits

---

## CHALLENGES & CONSIDERATIONS

### 1. Hash Calculation Scope

**Question:** What exactly should be hashed?

**Options:**
- **Full file:** Includes metadata, dates, status
- **Content only:** Excludes frontmatter/metadata sections
- **Normalized:** Remove whitespace, normalize line endings

**Recommendation:** Hash full file content (including metadata) for simplicity. If metadata changes frequently, consider excluding it.

**Hash Length:** We use short hashes (6-10 characters, default 8) from SHA-256. This is sufficient for change detection - we're not looking for cryptographic security, just "did this file change?" The collision risk is negligible for this use case.

### 2. False Positives

**Scenario:** Document content changes but dependency relationship is still valid

**Example:**
- Source document: Adds new section
- Dependent document: Hash mismatch, but dependency still valid

**Solution:**
- Hash mismatch = signal to review, not automatic error
- Manual verification still required
- Can mark as "reviewed, still valid"

### 3. Maintenance Overhead

**Challenge:** Keeping dependency hashes up to date

**Solutions:**
- **Automated updates:** Script to update hashes after changes
- **Selective tracking:** Only track critical dependencies
- **Lazy updates:** Update hashes during consistency checks

### 4. Circular Dependencies

**Risk:** Document A depends on B, B depends on A

**Solution:**
- Dependency graph validation
- Detect cycles and flag for review
- Prefer unidirectional dependencies

### 5. File Moves/Renames

**Challenge:** Paths in dependency declarations become invalid

**Solution:**
- Use relative paths (already standard)
- Script to detect broken links
- Consider using file identifiers instead of paths

---

## INTEGRATION WITH EXISTING WORKFLOW

### Current Workflow
1. Make edits to documents
2. Manual consistency checks
3. Update related documents
4. Document in consistency audit files

### Enhanced Workflow
1. Make edits to documents
2. **Run consistency checker** (automated)
3. **Review hash mismatches** (automated detection)
4. Update dependent documents
5. **Update dependency hashes** (automated or manual)
6. Document in consistency audit files

### Complementary, Not Replacement

**This system:**
- Detects when dependencies change
- Provides early warning of potential inconsistencies
- Documents dependency relationships

**Still needed:**
- Manual review of content changes
- Semantic consistency checks (not just hash matching)
- Human judgment on whether changes break dependencies

---

## PROOF OF CONCEPT SCRIPT

### Python Implementation Example

```python
#!/usr/bin/env python3
"""
Content Hash Consistency Checker
Calculates hashes and verifies dependencies
"""

import hashlib
import re
import os
from pathlib import Path
from typing import Dict, List, Tuple

def calculate_hash(file_path: str) -> str:
    """Calculate SHA-256 hash of file content."""
    with open(file_path, 'rb') as f:
        content = f.read()
    return hashlib.sha256(content).hexdigest()

def extract_dependencies(file_path: str) -> List[Dict]:
    """Extract dependency declarations from markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    dependencies = []
    
    # Look for dependency table
    # Pattern: | Document | Path | Hash | Last Verified | Status |
    table_pattern = r'\|.*?\|.*?\|.*?\|.*?\|.*?\|'
    
    # Extract table rows (simplified - would need more robust parsing)
    lines = content.split('\n')
    in_table = False
    
    for i, line in enumerate(lines):
        if '| Document | Path | Hash |' in line:
            in_table = True
            continue
        if in_table and line.strip().startswith('|') and '---' not in line:
            # Parse table row
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) >= 3:
                doc_name = parts[0]
                doc_path = parts[1].strip('`')
                doc_hash = parts[2].strip('`')
                dependencies.append({
                    'name': doc_name,
                    'path': doc_path,
                    'expected_hash': doc_hash,
                    'line': i + 1
                })
        elif in_table and not line.strip().startswith('|'):
            in_table = False
    
    return dependencies

def check_consistency(file_path: str, base_dir: str = '.') -> List[Dict]:
    """Check consistency of dependencies in a file."""
    issues = []
    
    dependencies = extract_dependencies(file_path)
    
    for dep in dependencies:
        dep_path = os.path.join(base_dir, dep['path'])
        
        if not os.path.exists(dep_path):
            issues.append({
                'file': file_path,
                'dependency': dep['name'],
                'path': dep['path'],
                'issue': 'File not found',
                'severity': 'error'
            })
            continue
        
        current_hash = calculate_hash(dep_path)
        expected_hash = dep['expected_hash'].replace('sha256:', '')
        
        if current_hash != expected_hash:
            issues.append({
                'file': file_path,
                'dependency': dep['name'],
                'path': dep['path'],
                'issue': 'Hash mismatch',
                'expected': expected_hash,
                'current': current_hash,
                'severity': 'warning'
            })
    
    return issues

def main():
    """Main function - check all markdown files."""
    base_dir = Path('.')
    md_files = list(base_dir.rglob('*.md'))
    
    all_issues = []
    
    for md_file in md_files:
        issues = check_consistency(str(md_file), str(base_dir))
        all_issues.extend(issues)
    
    # Report
    if all_issues:
        print("Consistency Issues Found:\n")
        for issue in all_issues:
            print(f"File: {issue['file']}")
            print(f"  Dependency: {issue['dependency']}")
            print(f"  Issue: {issue['issue']}")
            if 'expected' in issue:
                print(f"  Expected: {issue['expected'][:16]}...")
                print(f"  Current:  {issue['current'][:16]}...")
            print()
    else:
        print("No consistency issues found!")

if __name__ == '__main__':
    main()
```

---

## NEXT STEPS

### Immediate Actions
1. **Review this proposal** - Determine if approach is suitable
2. **Select implementation option** - Frontmatter vs. Markdown section
3. **Choose pilot documents** - Select 3-5 files for proof of concept
4. **Create tooling** - Build hash calculator and consistency checker

### Short-term (1-2 weeks)
1. **Implement proof of concept** - Add dependency tracking to pilot documents
2. **Test workflow** - Make changes and verify detection works
3. **Refine approach** - Adjust based on experience
4. **Document process** - Create guide for adding dependencies

### Medium-term (1-2 months)
1. **Expand coverage** - Add dependency tracking to more documents
2. **Automate checks** - Integrate into workflow (pre-commit, CI)
3. **Build dependency graph** - Visualize document relationships
4. **Create update tools** - Scripts to update hashes automatically

### Long-term (ongoing)
1. **Maintain system** - Keep dependency hashes current
2. **Refine tooling** - Improve scripts based on usage
3. **Document patterns** - Identify common dependency patterns
4. **Scale up** - Apply to entire project

---

## CONCLUSION

A blockchain-like hash consistency system would provide:

✅ **Automated detection** of dependency changes  
✅ **Explicit documentation** of document relationships  
✅ **Early warning** of potential inconsistencies  
✅ **Scalable solution** that complements manual checks  

**Recommendation:** Proceed with proof of concept using Option 2 (Markdown Section) for 3-5 high-value documents, then evaluate and expand if successful.

**Key Success Factors:**
- Simple, maintainable format
- Easy-to-use tooling
- Clear workflow integration
- Complementary to existing processes (not replacement)

---

**Status:** PROPOSAL - READY FOR REVIEW  
**Next Action:** Decision on implementation approach and pilot documents

