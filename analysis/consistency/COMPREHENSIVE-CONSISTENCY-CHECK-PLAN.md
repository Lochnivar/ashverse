# Comprehensive Consistency Check Plan

**Date:** December 10, 2025  
**Purpose:** Systematic checks to ensure no inconsistencies remain in the project

---

## AUTOMATED CHECKS (Scripts Available)

### 1. **Hash Consistency Check** ✅
**Script:** `python scripts/consistency-checker.py`

**What it checks:**
- Verifies all dependency hashes match current file hashes
- Detects when source files have changed
- Reports hash mismatches and missing files

**How to run:**
```bash
# Check entire project
python scripts/consistency-checker.py

# Check specific file
python scripts/consistency-checker.py analysis/economic/slavery-death-mechanics-analysis-2025-12-05.md
```

**Expected output:**
- List of verified dependencies (✅)
- List of hash mismatches (⚠️)
- List of missing files (❌)

---

### 2. **Cascade Impact Check** ✅
**Script:** `python scripts/cascade-impact.py <file-path>`

**What it checks:**
- Shows all files that depend on a given file
- Helps identify what needs review when a master file changes

**How to run:**
```bash
# Check impact of changing a master file
python scripts/cascade-impact.py world-building-master/02-economic-systems.md
```

**Use case:** Before editing a master file, see what will be affected

---

### 3. **Butterfly Effect Check** ✅
**Script:** `python scripts/butterfly-check.py`

**What it checks:**
- Tracks butterfly effects from POD changes
- Verifies downstream impacts are consistent

**How to run:**
```bash
python scripts/butterfly-check.py
```

---

## MANUAL CHECKS (Pattern Searches)

### 4. **Old File Path References** 🔍
**Check for:** References to archived/consolidated files

**Patterns to search:**
```bash
# Old timeline paths
grep -r "world-building/timelines/master-timeline.md" --include="*.md"
grep -r "world-building/timelines/rappahannock-rapidan" --include="*.md"
grep -r "world-building/timelines/northern-collapse" --include="*.md"
grep -r "world-building/timelines/gettysburg-master" --include="*.md"

# Old economic paths (if not consolidated)
grep -r "world-building/economic/slavery-and-raids-master.md" --include="*.md"
grep -r "world-building/economic/economic-systems-master.md" --include="*.md"

# Old political paths (if not consolidated)
grep -r "world-building/political/csa-presidents-gentry-vs-hayseed-1865-1939.md" --include="*.md"
grep -r "world-building/political/presidents-and-parties.md" --include="*.md"
grep -r "world-building/political/ca-political-system" --include="*.md"
```

**Expected:** Only references should be in:
- Archive documentation
- Historical analysis files (noted as archived)
- This check plan itself

---

### 5. **Date Consistency Checks** 📅
**Check for:** Conflicting dates for same events

**Key dates to verify:**
```bash
# Meade sacking (should be August 1, 1863, not November 1863)
grep -r "Meade.*sack" --include="*.md" -i
grep -r "November.*1863.*Meade" --include="*.md" -i
grep -r "August.*1863.*Meade" --include="*.md" -i

# Warren command dates
grep -r "Warren.*command" --include="*.md" -i
grep -r "Warren.*relieved" --include="*.md" -i

# Pickett's Raid dates (should be June 14 - July 14, 1864)
grep -r "Pickett.*Raid" --include="*.md" -i
grep -r "June.*8.*1864" --include="*.md"  # Old date
grep -r "June.*14.*July.*14.*1864" --include="*.md"  # Correct date

# Toombs Act / Toombs presidency (should be 1867-1871)
grep -r "Toombs.*1867" --include="*.md" -i
grep -r "Toombs.*1871" --include="*.md" -i
grep -r "Toombs.*1872" --include="*.md" -i  # Old date
```

**Expected:** All dates should match master timeline

---

### 6. **Terminology Consistency** 📝
**Check for:** Inconsistent terminology

**Key terms to verify:**
```bash
# "Four Mechanisms" vs "Four Horsemen"
grep -r "Four Mechanisms" --include="*.md" -i
grep -r "Four Horsemen" --include="*.md" -i

# "Cuba Mirror Effect" vs "Cuba Mirror"
grep -r "Cuba Mirror" --include="*.md" -i

# "Northern Raids" vs "Raids" (should be consistent)
grep -r "Northern.*Raid" --include="*.md" -i
```

**Expected:** Terminology should be consistent per established canon

---

### 7. **Number Consistency** 🔢
**Check for:** Conflicting numbers

**Key numbers to verify:**
```bash
# Raid counts (should be 350-450 total)
grep -r "50.*raid" --include="*.md" -i
grep -r "300.*400.*raid" --include="*.md" -i
grep -r "350.*450.*raid" --include="*.md" -i

# Economic impact (should be $1.6 billion)
grep -r "\$1\.6.*billion" --include="*.md" -i
grep -r "\$5\.0.*billion" --include="*.md" -i  # Old number

# Production drop (should be 30% total, shared across mechanisms)
grep -r "30.*production.*drop" --include="*.md" -i
grep -r "10.*production.*drop" --include="*.md" -i  # Raids alone
```

**Expected:** Numbers should match locked canon

---

### 8. **Character Name Consistency** 👤
**Check for:** Spelling variations, name changes

**Key names to verify:**
```bash
# Fairfax names
grep -r "John.*Walter.*Fairfax" --include="*.md" -i
grep -r "Thomas.*Reginald.*Fairfax" --include="*.md" -i

# Haskell
grep -r "Frank.*A.*Haskell" --include="*.md" -i
grep -r "Frank.*Haskell" --include="*.md" -i

# Appomattox spelling (not Appomatox)
grep -r "Appomatox" --include="*.md" -i  # Should find none
grep -r "Appomattox" --include="*.md" -i
```

**Expected:** Names should be consistent

---

### 9. **Timeline Sequence Consistency** ⏱️
**Check for:** Events out of order

**Key sequences to verify:**
```bash
# Meade sacking → Warren command → Hagerstown → Warren relieved
grep -r "Meade.*sack.*Warren" --include="*.md" -i
grep -r "Warren.*Hagerstown" --include="*.md" -i
grep -r "Hagerstown.*Warren.*relieved" --include="*.md" -i

# Pickett Raid → Hancock wounded → Hood replaces Johnston
grep -r "Pickett.*Hancock" --include="*.md" -i
grep -r "Hancock.*wound.*Hood" --include="*.md" -i
```

**Expected:** Event sequences should be logically consistent

---

### 10. **Cross-Reference Consistency** 🔗
**Check for:** Files that reference each other but have conflicting info

**How to check:**
1. Find files that reference each other
2. Compare specific facts between them
3. Verify they match

**Key cross-references:**
- `canon-refresher-for-ai.md` ↔ `canon-master-document.md`
- `world-building-master/06-timelines.md` ↔ analysis files
- `world-building-master/02-economic-systems.md` ↔ economic analysis files
- `world-building-master/03-political-systems.md` ↔ political analysis files

---

## SEMANTIC CHECKS (Content Analysis)

### 11. **Plausibility Score Consistency** 📊
**Check for:** Files claiming different plausibility scores for same events

**How to check:**
- Search for plausibility scores in analysis files
- Compare scores for same events across files
- Flag significant discrepancies (>10% difference)

---

### 12. **Status Consistency** ✅
**Check for:** Files marked as LOCKED but with outdated information

**How to check:**
- Find all files with "LOCKED" status
- Verify their content matches current master files
- Check if they reference outdated information

---

### 13. **Master File Completeness** 📚
**Check for:** Information in detail files not reflected in master files

**How to check:**
- Compare detail files (e.g., `northern-raids-comprehensive-catalog.md`) with master files
- Verify master files reference detail files correctly
- Ensure no critical information is missing from masters

---

## RECOMMENDED CHECK SEQUENCE

### Phase 1: Automated Checks (Quick)
1. Run hash consistency checker
2. Fix any hash mismatches
3. Run cascade impact on master files

### Phase 2: Pattern Searches (Medium)
4. Search for old file paths
5. Search for date inconsistencies
6. Search for terminology inconsistencies
7. Search for number inconsistencies

### Phase 3: Content Review (Thorough)
8. Character name consistency
9. Timeline sequence consistency
10. Cross-reference consistency
11. Plausibility score consistency

### Phase 4: Master File Verification (Final)
12. Status consistency check
13. Master file completeness check

---

## QUICK CHECK COMMAND

Run all automated checks at once:
```bash
# Hash consistency
python scripts/consistency-checker.py > consistency-report.txt

# Cascade impact on all master files
for file in world-building-master/*.md; do
    echo "=== $file ==="
    python scripts/cascade-impact.py "$file"
done > cascade-impact-report.txt
```

---

## EXPECTED RESULTS

**If all checks pass:**
- ✅ All hash dependencies verified
- ✅ No old file path references (except in archive docs)
- ✅ All dates consistent with master timeline
- ✅ Terminology consistent
- ✅ Numbers match locked canon
- ✅ Character names consistent
- ✅ Timeline sequences logical
- ✅ Cross-references match
- ✅ Master files complete

**If issues found:**
- Create issue list
- Prioritize by severity (errors > warnings > suggestions)
- Fix systematically
- Re-run checks after fixes

---

**Status:** Ready to execute  
**Next Step:** Run Phase 1 automated checks


