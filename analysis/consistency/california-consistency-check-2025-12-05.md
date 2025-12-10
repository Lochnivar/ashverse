# California Date Consistency Check

**Date:** December 5, 2025  
**Last Updated:** December 5, 2025 (after unlocking California files)  
**Status:** PARTIALLY FIXED - REMAINING INCONSISTENCIES IDENTIFIED

---

## LOCKED CANON DATES

**California Independence Timeline (LOCKED):**
- **Great Native Toll War:** Jan–May 1872
- **Independence Referendum:** 5 Nov 1872 (69% YES)
- **Treaty Signed:** 14 Feb 1873
- **Full Sovereignty:** 4 July 1873

**1872–1873 independence timeline is locked. All other California content is now unlocked for development.**

---

## INCONSISTENCIES FOUND

### 1. **TREATY NAME INCONSISTENCY** ⚠️ PARTIALLY FIXED

**Problem:** Two different treaty names used:
- "Treaty of San Francisco" (most common, correct)
- "Treaty of Sacramento" (appears in some files, incorrect)

**Status:** ✅ FIXED in `california-independence-corrected.md` (line 34 changed to "Treaty of San Francisco")

**Files with "Treaty of San Francisco" (CORRECT):**
- ✅ `california-independence.md` (line 43)
- ✅ `california-independence-corrected.md` (lines 8, 19, 30) - **FIXED**
- ✅ `book-04-the-ashes/README.md` (line 80)
- ✅ `book-02-the-fire/README.md` (line 67)
- ✅ `notes/questions-and-answers.md` (multiple references)
- ✅ `world-building/treaty-of-san-francisco.md` (title and content)

**Files with "Treaty of Sacramento" (NEEDS FIX):**
- ✅ `world-building/currencies-ntl.md` (line 19) - **FIXED**
- ✅ `world-building/tariffs-ntl.md` (line 11) - **FIXED**

**Recommendation:** Standardize on **"Treaty of San Francisco"** everywhere. Two files still need updating.

---

### 2. **WRONG DATE: California Independence Listed as 1920** ✅ FIXED

**File:** `books/book-04-the-ashes/README.md`  
**Line:** 48  
**Error:** 
```
- **California becomes fully independent Republic of California (1920)** - No longer even pretending to be U.S. territory.
```

**Status:** ✅ **FIXED** - Changed to "(1873)"

**Note:** The same file correctly states "independent since 1873" and "47 years by 1920" elsewhere, so this was a single-line error that has been corrected.

---

### 3. **MATH ERROR: "150 years by WW1"** ✅ FIXED

**File:** `world-building/california-independence.md`  
**Line:** 128  
**Error:**
```
California has been its own country for 150 years by the time WW1 starts.
```

**Math check:**
- WW1 starts: 1914
- California independent: 1873
- Years: 1914 - 1873 = **41 years** (not 150)

**Status:** ✅ **FIXED** - Changed to "41 years"

**Also fixed in:** `california-independence-corrected.md` (line 42)

---

### 4. **MATH ERROR: "66 years by WW1"** ✅ FIXED

**File:** `world-building/master-timeline.md`  
**Line:** 45  
**Error:**
```
California has been its own country for 66 years by the time WW1 starts.
```

**Math check:**
- WW1 starts: 1914
- California independent: 1873
- Years: 1914 - 1873 = **41 years** (not 66)

**Status:** ✅ **FIXED** - Changed to "41 years"

**Note:** The same file correctly says "47 years by 1920" on the same line, which is correct (1920 - 1873 = 47).

---

### 5. **OLD DRAFT RESIDUE: 1931 Treaty Date** ✅ RESOLVED

**File:** `AI-DUMP.md`  
**Status:** ✅ **FILE DELETED** - No longer exists in codebase

**Resolution:** The AI-DUMP.md file has been removed as it was a distraction after content was extracted and organized. This issue is resolved.

---

### 6. **VERIFICATION: Correct References** ✅

These files have correct dates:
- ✅ `series-overview.md` - Correctly says "independent since 1873" and "47 years by 1920"
- ✅ `world-building/master-timeline.md` - Correctly says "47 years by 1920" (though has the 66-year error for WW1)
- ✅ `books/book-03-the-embers/README.md` - Correctly says "independent since 1873" and "22 years by 1895"
- ✅ `books/book-04-the-ashes/README.md` - Correctly says "independent since 1873" and "47 years by 1920" (but has the 1920 error on line 50)

---

## SUMMARY OF FIXES NEEDED

### ✅ COMPLETED FIXES:
1. ✅ **california-independence-corrected.md** - Fixed "Treaty of Sacramento" → "Treaty of San Francisco" (line 30)
2. ✅ **AI-DUMP.md** - File deleted (no longer a distraction)
3. ✅ **California files unlocked** - All California content (except independence timeline) is now open for development

### 🔴 REMAINING CRITICAL FIXES:
1. **Standardize treaty name** - Two files still need "Treaty of Sacramento" → "Treaty of San Francisco"
2. **Fix book-04-the-ashes/README.md line 48** - Change "(1920)" to "(1873)"
3. **Fix california-independence.md** - Change "150 years" to "41 years" or rephrase (line 9)
4. **Fix master-timeline.md** - Change "66 years" to "41 years" (line 45)

### ✅ ALL FIXES COMPLETED:
1. ✅ `world-building/currencies-ntl.md` - Line 19: Changed "Treaty of Sacramento" to "Treaty of San Francisco"
2. ✅ `world-building/tariffs-ntl.md` - Line 11: Changed "Treaty of Sacramento" to "Treaty of San Francisco"
3. ✅ `books/book-04-the-ashes/README.md` - Line 48: Changed "(1920)" to "(1873)"
4. ✅ `world-building/california-independence.md` - Line 128: Fixed "150 years" to "41 years"
5. ✅ `world-building/california-independence-corrected.md` - Line 42: Fixed "150 years" to "41 years"
6. ✅ `world-building/master-timeline.md` - Line 45: Fixed "66 years" to "41 years"

---

## VERIFICATION CHECKLIST

After fixes, verify:
- [ ] All references to California independence use 1872-1873 dates
- [ ] All treaty references use "Treaty of San Francisco" (not "Treaty of Sacramento")
- [ ] All math calculations are correct:
  - 1873 to 1895 = 22 years ✅
  - 1873 to 1914 (WW1) = 41 years ✅
  - 1873 to 1920 = 47 years ✅
  - 1873 to 1939 = 66 years ✅
- [ ] No references to 1920s-1930s independence dates
- [ ] No references to "1931 Treaty of San Francisco"

---

## CORRECT TIMELINE REFERENCE

**California Independence Timeline:**
- **1865-1870:** De-facto U.S. exclave
- **1870-1872:** Growing de-facto independence
- **Jan-May 1872:** Great Native Toll War (trigger)
- **5 Nov 1872:** Independence Referendum (69% YES)
- **14 Feb 1873:** Treaty of San Francisco signed
- **4 July 1873:** Republic of California fully sovereign

**Years of Independence (by key dates):**
- By 1895: 22 years (1895 - 1873 = 22)
- By 1914 (WW1): 41 years (1914 - 1873 = 41)
- By 1920: 47 years (1920 - 1873 = 47)
- By 1939: 66 years (1939 - 1873 = 66)

---

---

## RECENT CHANGES (December 5, 2025)

1. ✅ **AI-DUMP.md deleted** - Old draft residue file removed
2. ✅ **California files unlocked** - All California content (except 1872-1873 independence timeline) is now open for development
3. ✅ **Treaty name standardized** - All files now use "Treaty of San Francisco" (consistent with San Francisco being the capital)
4. ✅ **Capital established** - San Francisco is the capital of the Republic of California (proclaimed 4 July 1873)
5. ✅ **All date inconsistencies fixed** - All 5 remaining issues resolved

---

## CANON ESTABLISHMENT: San Francisco as Capital

**Capital of the Republic of California = San Francisco, proclaimed 4 July 1873**

**Rationale:**
- San Francisco is the largest city (~150k vs. Sacramento's ~25k in 1873)
- Main port and financial center (all money flows through SF)
- Symbolic prestige ("We are not an inland agricultural state; we are the gateway to Asia")
- No compelling reason to keep Sacramento as capital after independence

**This makes "Treaty of San Francisco" the natural and correct name for the 1873 treaty.**

---

**Status:** ✅ ALL INCONSISTENCIES FIXED

