# Dependency Tracking Recommendations

**Date:** December 10, 2025  
**Status:** RECOMMENDATIONS  
**Purpose:** Prioritized list of files that should have dependency tracking added

---

## PRIORITY 1: CRITICAL MASTER DOCUMENTS (Source Files)

These are foundational documents that many other files depend on. **These files don't need dependency tracking themselves** (they're sources), but tracking them helps identify what breaks when they change.

### Already Tracked ✅
- `world-building-master/01-core-foundation.md` - Core POD and foundation
- `world-building/economic/northern-raids-comprehensive-catalog.md` - Raid catalog
- `canon-master-document.md` - Master canon reference

### Should Be Tracked (as sources)
- `canon-refresher-for-ai.md` - AI reference document (many files depend on this)
- `world-building-master/02-economic-systems.md` - Economic master (consolidated from slavery-and-raids-master.md and economic-systems-master.md)
- `world-building-master/03-political-systems.md` - Political master (consolidated from csa-presidents-gentry-vs-hayseed-1865-1939.md and other political files)
- `world-building/political/presidential-pairs-master-reference.md` - Political master reference (still exists, detailed pairings)

**Why:** These are frequently referenced master documents. When they change, many dependent files need review.

---

## PRIORITY 2: ANALYSIS FILES (High Dependency Risk)

Analysis files synthesize information from multiple sources. When sources change, analyses may become inconsistent.

### Already Tracked ✅
- `analysis/economic/raid-count-plausibility-analysis-2025-12-10.md`

### Should Be Tracked
1. **`analysis/economic/slavery-death-mechanics-analysis-2025-12-05.md`**
   - **Dependencies:**
     - `world-building-master/02-economic-systems.md`
     - `world-building/economic/northern-raids-comprehensive-catalog.md`
     - `canon-master-document.md`
   - **Why:** Analyzes raid mechanics and economic systems

2. **`analysis/economic/slavery-death-economic-refinement-implementation-2025-12-05.md`**
   - **Dependencies:**
     - `world-building-master/02-economic-systems.md`
     - `canon-master-document.md`
   - **Why:** Implements economic refinements based on master documents

3. **`analysis/political/california-csa-usa-presidential-interactions-analysis-2025-12-05.md`**
   - **Dependencies:**
     - `world-building-master/03-political-systems.md`
     - `world-building/political/presidential-pairs-master-reference.md`
     - `canon-master-document.md`
   - **Why:** Has known inconsistencies (Toombs dates) - tracking would catch these

4. **`analysis/political/csa-usa-presidential-interactions-analysis-2025-12-05.md`**
   - **Dependencies:**
     - `world-building-master/03-political-systems.md`
     - `world-building/political/presidential-pairs-master-reference.md`
   - **Why:** Similar to above, presidential timeline analysis

5. **`analysis/political/presidential-timelines-final-check-2025-12-05.md`**
   - **Dependencies:**
     - `world-building-master/03-political-systems.md`
     - `world-building/political/presidential-pairs-master-reference.md`
   - **Why:** Timeline verification document

6. **`analysis/political/csa-presidents-plausibility-analysis-2025-12-05.md`**
   - **Dependencies:**
     - `world-building-master/03-political-systems.md`
     - `canon-master-document.md`
   - **Why:** Plausibility analysis of presidential timelines

---

## PRIORITY 3: CHARACTER FILES (World-Building Dependencies)

Character files depend on world-building foundations, especially for timeline and historical context.

### Already Tracked ✅
- `characters/union/frank-a-haskell.md`

### Should Be Tracked
1. **Major character files in `characters/confederate/`**
   - **Dependencies:**
     - `world-building-master/01-core-foundation.md`
     - `characters/union/frank-a-haskell.md` (for family dynamics)
   - **Why:** Characters reference historical events and interact with other characters

2. **Fairfax family character files**
   - **Dependencies:**
     - `world-building-master/01-core-foundation.md`
     - `characters/union/frank-a-haskell.md` (for Fairfax-Haskell dynamic)
   - **Why:** Key witness family, interacts with Haskell family

---

## PRIORITY 4: COMPENDIUM FILES (Multi-Source Compilation)

Compendium files compile information from multiple sources. When sources change, compendium chapters may become inconsistent.

### Should Be Tracked
1. **`compendium/compendium-outline-book-ii-the-fire.md`**
   - **Dependencies:**
     - `world-building/economic/northern-raids-comprehensive-catalog.md`
     - `world-building-master/02-economic-systems.md`
     - `canon-master-document.md`
   - **Why:** Book outline references economic systems and raids

2. **`compendium/compendium-outline-book-ii-inconsistencies.md`**
   - **Dependencies:**
     - `canon-master-document.md`
     - `world-building-master/02-economic-systems.md`
   - **Why:** Documents inconsistencies - needs to track source changes

3. **`compendium/compendium-outline-book-ii-inconsistency-01-analysis.md`**
   - **Dependencies:**
     - `canon-master-document.md`
     - `world-building-master/02-economic-systems.md`
   - **Why:** Analysis of specific inconsistencies

4. **`compendium/chapters/part-ii-the-fire/chapter-11-toombs-act-boycott.md`**
   - **Dependencies:**
     - `world-building-master/03-political-systems.md`
     - `world-building/political/presidential-pairs-master-reference.md`
     - `canon-master-document.md`
   - **Why:** Has known inconsistency (Toombs dates 1872-1878 vs 1867-1871)

5. **`compendium/chapters/part-ii-the-fire/chapter-12-raider-economy.md`**
   - **Dependencies:**
     - `world-building/economic/northern-raids-comprehensive-catalog.md`
     - `world-building-master/02-economic-systems.md`
     - `canon-master-document.md`
   - **Why:** References "Four Mechanisms" vs "Four Horsemen" inconsistency

---

## PRIORITY 5: SCENE AND EDIT FILES (Character/World Dependencies)

Scene files depend on character files and world-building for consistency.

### Already Tracked ✅
- `edits/book-01-final-scene-haskell-fairfax-confrontation-2025-12-05.md`

### Should Be Tracked (if they reference specific characters/world-building)
- Other scene files in `edits/` that reference characters or world-building
- Scene files in `books/book-01-the-match/` that reference characters

---

## IMPLEMENTATION PRIORITY

### Phase 1: High-Value, High-Risk (Do First)
Focus on files with known inconsistencies or high dependency risk:

1. **Analysis files with known inconsistencies:**
   - `analysis/political/california-csa-usa-presidential-interactions-analysis-2025-12-05.md`
   - `analysis/political/csa-usa-presidential-interactions-analysis-2025-12-05.md`
   - `analysis/political/presidential-timelines-final-check-2025-12-05.md`
   - `compendium/chapters/part-ii-the-fire/chapter-11-toombs-act-boycott.md`

2. **Economic analysis files:**
   - `analysis/economic/slavery-death-mechanics-analysis-2025-12-05.md`
   - `analysis/economic/slavery-death-economic-refinement-implementation-2025-12-05.md`

### Phase 2: Compendium Files (Do Second)
Compendium files compile from multiple sources and benefit from tracking:

- `compendium/compendium-outline-book-ii-the-fire.md`
- `compendium/compendium-outline-book-ii-inconsistencies.md`
- `compendium/chapters/part-ii-the-fire/chapter-12-raider-economy.md`

### Phase 3: Remaining Analysis Files (Do Third)
Complete coverage of analysis files:

- `analysis/political/csa-presidents-plausibility-analysis-2025-12-05.md`
- Other analysis files as needed

### Phase 4: Character Files (Do Fourth)
Add tracking to major character files beyond Haskell:

- Fairfax family characters
- Other major characters

### Phase 5: Additional Files (As Needed)
Add tracking to other files as dependencies are identified:

- Scene files
- Other edit files
- Additional compendium chapters

---

## QUICK REFERENCE: FILES TO TRACK

### Immediate Priority (Known Inconsistencies)
- `analysis/political/california-csa-usa-presidential-interactions-analysis-2025-12-05.md`
- `analysis/political/csa-usa-presidential-interactions-analysis-2025-12-05.md`
- `analysis/political/presidential-timelines-final-check-2025-12-05.md`
- `compendium/chapters/part-ii-the-fire/chapter-11-toombs-act-boycott.md`

### High Value (Frequently Referenced)
- `analysis/economic/slavery-death-mechanics-analysis-2025-12-05.md`
- `analysis/economic/slavery-death-economic-refinement-implementation-2025-12-05.md`
- `compendium/compendium-outline-book-ii-the-fire.md`
- `compendium/compendium-outline-book-ii-inconsistencies.md`

### Medium Priority (Good Coverage)
- `analysis/political/csa-presidents-plausibility-analysis-2025-12-05.md`
- `compendium/chapters/part-ii-the-fire/chapter-12-raider-economy.md`
- Major character files (Fairfax, etc.)

---

## NOTES

- **Start small:** Begin with Phase 1 files (known inconsistencies)
- **Test workflow:** Verify the system works well before expanding
- **Focus on critical paths:** Track dependencies that, if broken, would cause major inconsistencies
- **Don't over-track:** Not every file needs tracking - focus on high-value dependencies

---

**Status:** RECOMMENDATIONS COMPLETE  
**Next Step:** Begin Phase 1 implementation

