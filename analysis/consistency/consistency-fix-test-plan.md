# Consistency Fix Test Plan: Toombs Act Dating

**Date:** December 10, 2025  
**Status:** TEST PLAN  
**Purpose:** Test hash consistency system by fixing documented inconsistency

---

## THE INCONSISTENCY

### Master Document (CORRECT)
- **File:** `world-building/political/csa-presidents-gentry-vs-hayseed-1865-1939.md`
- **Toombs Dates:** 1867-1871 ✅ CORRECT
- **Status:** LOCKED CANON

### Analysis Files (INCORRECT)
- **File:** `analysis/political/california-csa-usa-presidential-interactions-analysis-2025-12-05.md`
  - Line 37: `[CSA President 1872-1878]` ❌ WRONG
  - Line 94: `Toombs (1872-1878)` ❌ WRONG

- **File:** `analysis/political/csa-usa-presidential-interactions-analysis-2025-12-05.md`
  - Line 93: `Toombs (1872-1878)` ❌ WRONG
  - Line 123: `Toombs (1872-1878)` ❌ WRONG
  - Line 577: `THE TOOMBS ACT DISASTER (1872-1877)` ❌ WRONG

- **File:** `analysis/political/presidential-timelines-final-check-2025-12-05.md`
  - Line 51: `1872-1878 | Robert Toombs` ❌ WRONG

---

## CASCADE IMPACT

**Master file affects:** 4 files (3 analysis files + master itself)

**Cascade depth:** 1 level

**Files that need review:**
1. `analysis/political/california-csa-usa-presidential-interactions-analysis-2025-12-05.md`
2. `analysis/political/csa-usa-presidential-interactions-analysis-2025-12-05.md`
3. `analysis/political/presidential-timelines-final-check-2025-12-05.md`

---

## TEST WORKFLOW

### Step 1: Check Current State
- Run consistency checker
- Verify hash mismatches (should show mismatches if master changed)
- Document current hashes

### Step 2: Fix Inconsistencies
- Update Toombs dates in analysis files (1872-1878 → 1867-1871)
- Update Toombs Act timing references
- Fix presidential pairing overlaps

### Step 3: Update Hashes
- Calculate new hashes for fixed files
- Update dependency hashes
- Run consistency checker to verify

### Step 4: Verify Cascade
- Run cascade impact tool on master file
- Verify all affected files are tracked
- Confirm system caught the inconsistency

---

## EXPECTED RESULTS

### Before Fix
- Hash mismatches in analysis files (if master was updated)
- Inconsistent dates in analysis files
- Cascade tool shows affected files

### After Fix
- All hashes verified ✅
- Dates consistent across files ✅
- Cascade tool confirms tracking ✅

---

## TESTING THE SYSTEM

This test will demonstrate:
1. ✅ **Cascade detection** - Tool shows affected files
2. ✅ **Hash tracking** - System detects when master changes
3. ✅ **Consistency verification** - Checker confirms fixes
4. ✅ **Butterfly effect tracking** - See full impact of changes

---

**Status:** READY TO TEST  
**Next:** Fix inconsistencies and verify system works

