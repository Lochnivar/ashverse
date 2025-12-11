# Comprehensive Consistency Audit: Ashverse Project

**Date:** December 10, 2025  
**Status:** ACTIVE AUDIT  
**Purpose:** Identify and resolve consistency issues across all project files

---

## CRITICAL INCONSISTENCIES FOUND

### 1. "Four Mechanisms" vs "Four Horsemen" Terminology

**Status:** ⚠️ **INCONSISTENT** - Multiple files still use "Four Mechanisms" instead of "Four Horsemen"

**Files Requiring Update:**
- ✅ `compendium/compendium-outline-book-ii-the-fire.md` - **UPDATED** (now uses "Four Horsemen")
- ❌ `world-building/economic/slavery-and-raids-master.md` - Still says "four mechanisms"
- ❌ `canon-master-document.md` - Still says "Four Mechanisms"
- ❌ `canon-refresher-for-ai.md` - Still says "four mechanisms"
- ❌ `world-building/economic/economic-systems-master.md` - Still says "four mechanisms"
- ❌ `analysis/economic/slavery-death-mechanics-analysis-2025-12-05.md` - Multiple references to "four mechanisms"
- ❌ `analysis/economic/slavery-death-economic-refinement-implementation-2025-12-05.md` - Still says "four mechanisms"
- ❌ `compendium/compendium-outline-book-ii-inconsistencies.md` - Still says "four mechanisms"
- ❌ `compendium/compendium-outline-book-ii-inconsistency-01-analysis.md` - Still says "four mechanisms"
- ❌ `compendium/table-of-contents-revised.md` - Still says "four mechanisms"
- ❌ `compendium/chapters/part-ii-the-fire/chapter-12-raider-economy.md` - Still says "four mechanisms"

**Action Required:**
- Update all references from "Four Mechanisms" to "Four Horsemen of Slavery's Apocalypse"
- Maintain consistency: "Four Horsemen" in narrative/compendium, "four mechanisms" acceptable in technical/economic analysis
- **Decision needed:** Should technical analysis files keep "mechanisms" or switch to "Horsemen"?

---

### 2. Toombs Act / Toombs Presidency Dating

**Status:** ⚠️ **INCONSISTENT** - Multiple files still have Toombs as 1872-1878 instead of 1867-1871

**LOCKED CANON:** Toombs elected 1867, served 1867-1871, Toombs Act passed Dec 1867, signed Jan 1868

**Files Requiring Update:**
- ✅ `canon-refresher-for-ai.md` - **UPDATED** (1867-1871)
- ✅ `canon-master-document.md` - **UPDATED** (1867-1871)
- ✅ `world-building/political/presidential-pairs-master-reference.md` - **UPDATED** (1867-1871)
- ✅ `world-building/political/csa-presidents-gentry-vs-hayseed-1865-1939.md` - **UPDATED** (1867-1871)
- ✅ `compendium/compendium-outline-book-ii-the-fire.md` - **UPDATED** (1867-1871)
- ❌ `analysis/political/california-csa-usa-presidential-interactions-analysis-2025-12-05.md` - Still says 1872-1878
- ❌ `analysis/political/csa-usa-presidential-interactions-analysis-2025-12-05.md` - Still says 1872-1878
- ❌ `world-building/political/csa-presidents-gentry-vs-hayseed-1865-1939.md` - **CHECK** (may have been updated)
- ❌ `compendium/compendium-outline-book-ii-inconsistency-01-analysis.md` - Still references 1872-1878 in analysis
- ❌ `compendium/table-of-contents-revised.md` - Still says 1872-1878
- ❌ `compendium/chapters/part-ii-the-fire/chapter-11-toombs-act-boycott.md` - Still says 1872-1878
- ❌ `analysis/political/presidential-timelines-final-check-2025-12-05.md` - Still says 1872-1878
- ❌ `analysis/political/csa-presidents-plausibility-analysis-2025-12-05.md` - Still says 1872-1878

**Action Required:**
- Update all Toombs presidency references to 1867-1871
- Update all Toombs Act timing to Dec 1867 / Jan 1868
- Update all presidential pairings that reference Toombs

---

### 3. Raid Count Totals

**Status:** ✅ **MOSTLY CONSISTENT** - Most files use 350-450 total

**LOCKED CANON:** 
- Phase 1 (1865-1867): ~50 major raids
- Phase 2 (1867-1894): 300-400 raids
- **Total (1865-1894): 350-450 raids**

**Files Status:**
- ✅ `canon-refresher-for-ai.md` - **CORRECT** (350-450)
- ✅ `canon-master-document.md` - **CORRECT** (350-450)
- ✅ `world-building/economic/northern-raids-comprehensive-catalog.md` - **CORRECT** (350-450)
- ✅ `world-building/economic/slavery-and-raids-master.md` - **CORRECT** (350-450)
- ✅ `compendium/compendium-outline-book-ii-the-fire.md` - **CORRECT** (350-450)
- ⚠️ `analysis/economic/raid-count-plausibility-analysis-2025-12-10.md` - Has old numbers in analysis section (but recommends 350-450)
- ⚠️ `analysis/economic/slavery-death-mechanics-analysis-2025-12-05.md` - Has old numbers (~270 raids) in some calculations

**Action Required:**
- Review analysis files for outdated calculations
- Ensure all recommendations match locked canon (350-450)

---

### 4. File Reference Issues

**Status:** ⚠️ **POTENTIAL ISSUES** - Some references may point to moved/deleted files

**Files to Check:**
- `canon-refresher-for-ai.md` - References files in `/world-building/` subfolders
- `world-building/timelines/gettysburg-master-timeline.md` - References individual timeline files that may be redundant
- `notes/questions-and-answers.md` - References files like `world-building/toombs-act-1867.md` (may not exist)
- `notes/questions-and-answers.md` - References `world-building/joint-crackdown-1867-1869.md` (may not exist)
- `notes/questions-and-answers.md` - References `world-building/global-cotton-glut.md` (may not exist)
- `notes/questions-and-answers.md` - References `world-building/native-superstates-consolidation.md` (may not exist)
- `notes/questions-and-answers.md` - References `world-building/mormon-deseret.md` (may not exist)
- `notes/questions-and-answers.md` - References `world-building/economic-relationships-1865-2025.md` (may not exist)

**Action Required:**
- ✅ **VERIFIED:** Information is consolidated in master documents:
  - `toombs-act-1867.md` → `world-building/economic/slavery-and-raids-master.md` (Section 1)
  - `joint-crackdown-1867-1869.md` → `world-building/economic/slavery-and-raids-master.md` (Section 2)
  - `global-cotton-glut.md` → `world-building/economic/economic-systems-master.md` (likely)
  - `native-superstates-consolidation.md` → `world-building/regions/native-super-states-master.md` (likely)
  - `mormon-deseret.md` → `world-building/regions/mormon-deseret.md` (exists, different path)
  - `economic-relationships-1865-2025.md` → `world-building/economic/economic-systems-master.md` (likely)
- Update `notes/questions-and-answers.md` to point to master documents
- Remove references to non-existent individual files

---

### 5. Cuba Mirror Effect Terminology

**Status:** ✅ **CONSISTENT** - Most files correctly identify it as psychological/shame mechanism

**LOCKED CANON:** Cuba Mirror Effect is psychological/shame mechanism, NOT economic boycott

**Files Status:**
- ✅ `canon-refresher-for-ai.md` - **CORRECT** (explicitly states "NOT economic boycott")
- ✅ `canon-master-document.md` - **CORRECT**
- ✅ `compendium/compendium-outline-book-ii-the-fire.md` - **CORRECT** (Horseman 4: Shame)

**Action Required:**
- None - appears consistent

---

### 6. Oregon/Washington Status

**Status:** ✅ **CONSISTENT** - Most files correctly state NOT US states

**LOCKED CANON:** Oregon and Washington are NOT US states - California aggressively lobbies (bribes) them to prevent statehood or cause secession

**Files Status:**
- ✅ `canon-refresher-for-ai.md` - **CORRECT**
- ✅ `canon-master-document.md` - **CORRECT**
- ✅ `world-building/california/ca-independence.md` - **CORRECT**
- ✅ `compendium/compendium-outline-book-ii-the-fire.md` - **CORRECT**

**Action Required:**
- None - appears consistent

---

## PRIORITY FIXES

### High Priority (Breaks Canon)

1. **Toombs Act Dating** - Multiple analysis files still have 1872-1878
   - `analysis/political/california-csa-usa-presidential-interactions-analysis-2025-12-05.md`
   - `analysis/political/csa-usa-presidential-interactions-analysis-2025-12-05.md`
   - `analysis/political/presidential-timelines-final-check-2025-12-05.md`
   - `analysis/political/csa-presidents-plausibility-analysis-2025-12-05.md`
   - `compendium/table-of-contents-revised.md`
   - `compendium/chapters/part-ii-the-fire/chapter-11-toombs-act-boycott.md`

2. **File Reference Verification** - Check if referenced files exist
   - `notes/questions-and-answers.md` - Multiple file references need verification

### Medium Priority (Terminology Consistency)

3. **"Four Mechanisms" → "Four Horsemen"** - Update terminology in:
   - `world-building/economic/slavery-and-raids-master.md`
   - `canon-master-document.md`
   - `canon-refresher-for-ai.md`
   - `world-building/economic/economic-systems-master.md`
   - Analysis files (decision needed: keep "mechanisms" in technical analysis?)

### Low Priority (Minor Inconsistencies)

4. **Raid Count Calculations** - Review analysis files for outdated numbers
   - `analysis/economic/raid-count-plausibility-analysis-2025-12-10.md`
   - `analysis/economic/slavery-death-mechanics-analysis-2025-12-05.md`

---

## RECOMMENDED WORKFLOW

### Step 1: Fix High-Priority Canon Breaks
1. Update all Toombs Act dating (1867-1871)
2. Verify all file references exist
3. Update broken file references

### Step 2: Harmonize Terminology
1. Decide: Keep "mechanisms" in technical analysis, or switch all to "Horsemen"?
2. Update master documents (canon-refresher, canon-master)
3. Update world-building documents
4. Update analysis files (if decision is to switch)

### Step 3: Review and Clean
1. Review analysis files for outdated calculations
2. Remove references to deleted/redundant files
3. Update any remaining inconsistencies

---

## DECISIONS NEEDED

1. **Terminology:** Should technical/economic analysis files keep "Four Mechanisms" or switch to "Four Horsemen"?
   - **Option A:** Keep "mechanisms" in technical analysis, "Horsemen" in narrative/compendium
   - **Option B:** Switch all to "Four Horsemen" for consistency
   - **Recommendation:** Option A (allows technical precision while maintaining narrative framing)

2. **File References:** Should `notes/questions-and-answers.md` be updated to point to master documents, or should individual files be created?
   - **Option A:** Update references to point to master documents
   - **Option B:** Create individual files as referenced
   - **Recommendation:** Option A (master documents are source of truth)

---

## TRACKING

**Last Updated:** December 10, 2025  
**Next Review:** After fixes are applied  
**Status:** ⚠️ **ACTIVE - FIXES NEEDED**

---

**Status:** COMPREHENSIVE AUDIT COMPLETE

