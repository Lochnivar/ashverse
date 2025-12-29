# AshVerse Radical Consolidation Checklist

**Created:** December 29, 2025  
**Goal:** Reduce from 458 files → ~200 files (consistency-critical files from ~150 → ~60)  
**Principle:** Consolidate first, then delete. No content loss.

---

## QUICK STATUS

| Phase | Description | Files Removed | Status |
|-------|-------------|---------------|--------|
| 1 | Verify consolidations complete | 0 | ⬜ Not Started |
| 2 | Delete archive/ (deprecated) | -82 | ⬜ Not Started |
| 3 | Delete old analysis/ | -93 | ⬜ Not Started |
| 4 | Delete old world-building/ details | -19 | ⬜ Not Started |
| 5 | Consolidate characters/ | -34 | ⬜ Not Started |
| 6 | Merge ai-rules/ into process/ | -4 | ⬜ Not Started |
| 7 | Clean root + rename folders | ~0 | ⬜ Not Started |
| 8 | Final verification | 0 | ⬜ Not Started |

**Running Total:** 458 → **~226 files** (50% reduction)

**Last Updated:** December 29, 2025  
**Last Action:** Checklist created

---

## PHASE 1: Verify Consolidations Are Complete

**Purpose:** Before deleting ANYTHING, confirm all content exists in master files.

### 1A: Verify archive/world-building/ → world-building-master/

Per `archive/README.md`, these consolidations were done on Dec 10, 2025:

| Archive Folder | Consolidated Into | Verify | Status |
|----------------|-------------------|--------|--------|
| `archive/world-building/core/` (4 files) | `world-building-master/01-core-foundation.md` | Spot-check | ⬜ |
| `archive/world-building/economic/` (6 files) | `world-building-master/02-economic-systems.md` | Spot-check | ⬜ |
| `archive/world-building/political/` (7 files) | `world-building-master/03-political-systems.md` | Spot-check | ⬜ |
| `archive/world-building/military/` (8 files) | `world-building-master/04-military-history.md` | Spot-check | ⬜ |
| `archive/world-building/regions/` (7 files) | `world-building-master/05-regions-and-nations.md` | Spot-check | ⬜ |
| `archive/world-building/timelines/` (13 files) | `world-building-master/06-timelines.md` | Spot-check | ⬜ |
| `archive/world-building/thematic/` (3 files) | `world-building-master/07-thematic-framework.md` | Spot-check | ⬜ |
| `archive/world-building/reference/` (6 files) | `world-building-master/08-reference-data.md` | Spot-check | ⬜ |
| `archive/world-building/california/` (13 files) | `world-building-master/05-regions-and-nations.md` | Spot-check | ⬜ |
| `archive/world-building/meta/` (8 files) | Various masters | Spot-check | ⬜ |
| `archive/world-building/treaties/` (4 files) | `world-building-master/03-political-systems.md` | Spot-check | ⬜ |

**Checkpoint 1A:** ⬜ All archive content verified in masters

### 1B: Verify analysis/ → analysis-master/

Per `analysis-master/CONSOLIDATION-SUMMARY.md`, 40 topic files were created from ~66 original files:

| Original Location | Consolidated Into | Status |
|-------------------|-------------------|--------|
| `analysis/military/` (36 files) | 23 military analyses in `analysis-master/` | ⬜ |
| `analysis/economic/` (5 files) | 3 economic analyses in `analysis-master/` | ⬜ |
| `analysis/political/` (18 files) | 10 political analyses in `analysis-master/` | ⬜ |
| `analysis/consistency/` (20 files) | Process docs (can delete) | ⬜ |
| `analysis/otl-divergence/` (2 files) | 1 OTL analysis in `analysis-master/` | ⬜ |
| `analysis/narrative/` (1 file) | In `analysis-master/` | ⬜ |
| `analysis/organization/` (1 file) | Process doc (can delete) | ⬜ |
| Root `analysis/` files (10 files) | Process docs (can delete) | ⬜ |

**Checkpoint 1B:** ⬜ All analysis content verified in analysis-master/

### 1C: Verify world-building/ details → world-building-master/

These are NEW files created AFTER the Dec 10 consolidation — need to integrate:

| Current File | Must Integrate Into | Status |
|--------------|---------------------|--------|
| `world-building/cultural/american-antisemitism-vs-european.md` | 07-thematic-framework.md | ⬜ |
| `world-building/cultural/civil-rights-timeline-1920s-1950s.md` | 06-timelines.md | ⬜ |
| `world-building/cultural/racial-dynamics-spectrum-1939.md` | 07-thematic-framework.md | ⬜ |
| `world-building/economic/northern-raids-comprehensive-catalog.md` | Keep as separate reference | ⬜ |
| `world-building/economic/ntl-cattle-route-1866-1900.md` | 02-economic-systems.md | ⬜ |
| `world-building/institutions/*.md` (6 files) | 08-reference-data.md (new section) | ⬜ |
| `world-building/military/european-war-1939-trigger.md` | 04-military-history.md | ⬜ |
| `world-building/military/texas-military-institute-1885.md` | 04-military-history.md | ⬜ |
| `world-building/political/quartet-symbolism-three-plus-one.md` | 03-political-systems.md | ⬜ |
| `world-building/political/texas-independence-1877.md` | 03-political-systems.md | ⬜ |
| `world-building/political/texas-personality-quartet-relations.md` | 03-political-systems.md | ⬜ |
| `world-building/regions/fort-smith-cowtown-1866-1900.md` | 05-regions-and-nations.md | ⬜ |
| `world-building/regions/native-super-states-attitudes.md` | 05-regions-and-nations.md | ⬜ |
| `world-building/regions/panhandle-crisis-1870-1873.md` | 05-regions-and-nations.md | ⬜ |

**Checkpoint 1C:** ⬜ All new world-building content integrated into masters

---

## PHASE 2: Delete archive/ (82 files)

**Prerequisite:** Phase 1A complete (verified content in masters)

### 2A: Delete Archive Subfolders

| Folder | Files | Status |
|--------|-------|--------|
| `archive/world-building/california/` | 13 | ⬜ |
| `archive/world-building/core/` | 4 | ⬜ |
| `archive/world-building/economic/` | 6 | ⬜ |
| `archive/world-building/meta/` | 8 | ⬜ |
| `archive/world-building/military/` | 8 | ⬜ |
| `archive/world-building/political/` | 7 | ⬜ |
| `archive/world-building/reference/` | 6 | ⬜ |
| `archive/world-building/regions/` | 7 | ⬜ |
| `archive/world-building/thematic/` | 3 | ⬜ |
| `archive/world-building/timelines/` | 9 | ⬜ |
| `archive/world-building/timelines/pod-campaign/` | 4 | ⬜ |
| `archive/world-building/treaties/` | 4 | ⬜ |
| `archive/world-building/` root files | 2 | ⬜ |
| `archive/README.md` | 1 | ⬜ |

**Checkpoint 2A:** ⬜ Archive folder deleted (82 files removed)

---

## PHASE 3: Delete Old analysis/ (93 files)

**Prerequisite:** Phase 1B complete (verified content in analysis-master/)

### 3A: Delete Analysis Subfolders

| Folder | Files | Status |
|--------|-------|--------|
| `analysis/consistency/` | 20 | ⬜ |
| `analysis/economic/` | 5 | ⬜ |
| `analysis/military/` | 36 | ⬜ |
| `analysis/narrative/` | 1 | ⬜ |
| `analysis/organization/` | 1 | ⬜ |
| `analysis/otl-divergence/` | 2 | ⬜ |
| `analysis/political/` | 18 | ⬜ |
| `analysis/` root files | 10 | ⬜ |

**Checkpoint 3A:** ⬜ Old analysis folder deleted (93 files removed)

### 3B: Rename analysis-master/ → analysis/

| Step | Status |
|------|--------|
| Rename `analysis-master/` to `analysis/` | ⬜ |

**Checkpoint 3B:** ⬜ Analysis folder renamed

---

## PHASE 4: Delete Old world-building/ Details (19 files)

**Prerequisite:** Phase 1C complete (all content integrated into masters)

### 4A: Delete World-Building Subfolders

| Folder | Files | Status |
|--------|-------|--------|
| `world-building/cultural/` | 3 | ⬜ |
| `world-building/economic/` | 2 | ⬜ |
| `world-building/institutions/` | 6 | ⬜ |
| `world-building/military/` | 2 | ⬜ |
| `world-building/political/` | 3 | ⬜ |
| `world-building/regions/` | 3 | ⬜ |
| Empty subfolders (california, core, meta, reference, thematic, timelines, treaties) | 0 | ⬜ |

**Checkpoint 4A:** ⬜ Old world-building details deleted (19 files removed)

### 4B: Rename world-building-master/ → world-building/

| Step | Status |
|------|--------|
| Delete empty `world-building/` folder | ⬜ |
| Rename `world-building-master/` to `world-building/` | ⬜ |

**Checkpoint 4B:** ⬜ World-building folder renamed

---

## PHASE 5: Consolidate characters/ (40 → 6 files)

### 5A: Create Consolidated Character Files

| New File | Source Files | Status |
|----------|--------------|--------|
| `characters/fairfax-family.md` | `FAIRFAX-FAMILY-SUMMARY.md` + `confederate/fairfax-bloodline.md` + `confederate/dunbar-lockwood.md` | ⬜ |
| `characters/haskell-family.md` | `HASKELL-FAMILY-SUMMARY.md` + `union/haskell-bloodline.md` + `union/frank-a-haskell.md` | ⬜ |
| `characters/meade-family.md` | `union/meade-bloodline.md` + `union/george-meade.md` | ⬜ |
| `characters/union-military.md` | All `union/*.md` (15 files) except family files | ⬜ |
| `characters/confederate-military.md` | All `confederate/*.md` (13 files) except family files | ⬜ |
| `characters/staffers.md` | All `staffers/*.md` (5 files) | ⬜ |

**Checkpoint 5A:** ⬜ New consolidated character files created

### 5B: Delete Old Character Files

| Folder | Files | Status |
|--------|-------|--------|
| `characters/confederate/` | 13 | ⬜ |
| `characters/union/` | 15 | ⬜ |
| `characters/staffers/` | 5 | ⬜ |
| `characters/` root files (old) | 7 | ⬜ |

**Checkpoint 5B:** ⬜ Old character files deleted (34 files removed, 6 new created)

---

## PHASE 6: Merge ai-rules/ into process/

### 6A: Move Files

| File | Action | Status |
|------|--------|--------|
| `ai-rules/git-operations-explicit-request.md` | Move to `process/` | ⬜ |
| `ai-rules/golden-rule-no-original-text.md` | Delete (duplicate in process/) | ⬜ |
| `ai-rules/hash-consistency-tracking.md` | Move to `process/` | ⬜ |
| `ai-rules/README.md` | Delete | ⬜ |

**Checkpoint 6A:** ⬜ ai-rules/ merged (4 files removed/moved)

### 6B: Delete Empty Folder

| Step | Status |
|------|--------|
| Delete `ai-rules/` folder | ⬜ |

**Checkpoint 6B:** ⬜ ai-rules/ folder deleted

---

## PHASE 7: Clean Root + Final Renames

### 7A: Move Root Timeline Files

| File | Action | Status |
|------|--------|--------|
| `final-gasp-timeline.md` | Integrate into `world-building/06-timelines.md` | ⬜ |
| `picketts-raid-timeline.md` | Delete (exists in world-building-master/) | ⬜ |
| `rapidan-campaign-timeline.md` | Integrate into `world-building/06-timelines.md` | ⬜ |

**Checkpoint 7A:** ⬜ Root timelines handled

### 7B: Move/Delete Process Documents

| File | Action | Status |
|------|--------|--------|
| `FOLDER-STRUCTURE-RULES.md` | Move to `process/` | ⬜ |
| `CONSISTENCY-CHECK-2025-12-21.md` | Delete (obsolete) | ⬜ |
| `CANON_UPDATE_SOURCE.md` | Review: keep or delete | ⬜ |
| `CONSOLIDATION-CHECKLIST.md` | Delete after completion | ⬜ |

**Checkpoint 7B:** ⬜ Root cleaned

### 7C: Update References

| Document | Update Needed | Status |
|----------|---------------|--------|
| `canon-refresher-for-ai.md` | Update all file paths | ⬜ |
| `README.md` | Update folder descriptions | ⬜ |

**Checkpoint 7C:** ⬜ References updated

---

## PHASE 8: Final Verification

### 8A: Verify Final Structure

```
ashverse/                          Target
├── books/                         72 files (unchanged)
├── world-building/                8-9 files (THE source of truth)
├── characters/                    6 files (consolidated)
├── analysis/                      ~43 files (consolidated)
├── compendium/                    52 files (unchanged)
├── edits/                         11 files (unchanged)
├── process/                       ~6 files (merged)
├── scripts/                       7 files (unchanged)
├── tools/                         4 files (unchanged)
├── notes/                         3 files (unchanged)
├── maps/                          1 file (unchanged)
├── plot/                          1 file (unchanged)
├── scenes/                        1 file (unchanged)
├── canon-refresher-for-ai.md
├── canon-master-document.md
├── series-overview.md
└── README.md
```

**Expected total: ~220 files**

### 8B: Consistency Check Scope

After consolidation, consistency checking only requires cross-referencing:

| Category | Files | Purpose |
|----------|-------|---------|
| World-building masters | 8 | THE source of truth |
| Character files | 6 | Character canon |
| Canon refresher | 1 | AI quick reference |
| Series overview | 1 | Structure reference |
| **TOTAL** | **16** | Consistency-critical files |

**Checkpoint 8B:** ⬜ Structure verified

---

## DELETION SUMMARY

| Phase | What | Files Removed |
|-------|------|---------------|
| 2 | archive/ | 82 |
| 3 | old analysis/ | 93 |
| 4 | old world-building/ details | 19 |
| 5 | old character files | 34 |
| 6 | ai-rules/ | 4 |
| 7 | root cleanup | ~5 |
| **TOTAL** | | **~237 files** |

**Net result:** 458 - 237 + 6 (new character files) = **~227 files**

---

## NOTES

```
2025-12-29 - Checklist created with radical reduction approach
           - Goal: 458 → ~227 files
           - Consistency scope: ~150 files → 16 files
```

---

## RESUMPTION INSTRUCTIONS

1. Find the last ✅ checkpoint
2. Update "Last Updated" and "Last Action" 
3. Continue from next ⬜ item
4. **CRITICAL:** Complete Phase 1 verifications BEFORE any deletions

**Symbols:**
- ⬜ = Not started
- 🔄 = In progress  
- ✅ = Complete
