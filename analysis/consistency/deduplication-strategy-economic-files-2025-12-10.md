# Deduplication Strategy: Economic Systems Master File

**Date:** December 10, 2025  
**Status:** ANALYSIS & STRATEGY  
**Purpose:** Identify and eliminate duplication in economic systems consolidation

---

## DUPLICATION ANALYSIS

### 1. Raid Statistics (HIGH DUPLICATION)

**Appears in:**
- `northern-raids-comprehensive-catalog.md` - Full detailed catalog (1165 lines)
- `slavery-and-raids-master.md` - Summary statistics
- `planter-adaptive-responses-to-raids.md` - References
- `canon-refresher-for-ai.md` - Summary
- `canon-master-document.md` - Summary

**Duplicated Data:**
- Total raids: 350-450 (appears 5+ times)
- Phase 1: ~50 major raids (appears 4+ times)
- Phase 2: 300-400 raids (appears 4+ times)
- Total impact: $1.6 billion (appears 5+ times)
- Slaves freed: 200,000 (appears 4+ times)
- Success rates: 68-75% (appears 3+ times)

**Strategy:** 
- **Keep raid catalog as separate detailed reference** (it's a dataset, not narrative)
- **In master file:** Reference catalog, provide summary statistics only
- **One source of truth:** Catalog has full details, master file has summary + reference

---

### 2. Toombs Act Details (MEDIUM DUPLICATION)

**Appears in:**
- `slavery-and-raids-master.md` - Full details (Section 2)
- `northern-raids-comprehensive-catalog.md` - References in raid descriptions
- `economic-systems-master.md` - References in boycott section
- `compendium-outline-book-ii-the-fire.md` - Full details in Part 14.3
- `notes/questions-and-answers.md` - Full details

**Duplicated Data:**
- Full legal name (appears 3+ times)
- Dates (Dec 1867, Jan 1868, Mar 1868) (appears 4+ times)
- Specific provisions (appears 2+ times)
- Vote breakdown (appears 2+ times)
- International reaction (appears 2+ times)

**Strategy:**
- **Keep full details in master file** (Section: Toombs Act)
- **In catalog:** Reference only ("under Toombs Act")
- **In compendium outline:** Reference master file
- **In notes/Q&A:** Reference master file

---

### 3. Four Horsemen Framework (MEDIUM DUPLICATION)

**Appears in:**
- `compendium-outline-book-ii-the-fire.md` - Full framework (Part 14)
- `slavery-and-raids-master.md` - Mentions "four mechanisms"
- `economic-systems-master.md` - Mentions "four mechanisms"
- `canon-refresher-for-ai.md` - Mentions "four mechanisms"

**Duplicated Data:**
- Four Horsemen names/descriptions (appears 2+ times)
- Individual horseman details (appears 2+ times)
- Synthesis/timeline (appears 2+ times)

**Strategy:**
- **Keep full framework in master file** (Section: Four Horsemen)
- **In compendium outline:** Reference master file, provide summary only
- **Update terminology:** Change "four mechanisms" to "Four Horsemen" everywhere

---

### 4. Economic Impact Numbers (HIGH DUPLICATION)

**Appears in:**
- `slavery-and-raids-master.md` - Full breakdown
- `economic-systems-master.md` - References
- `northern-raids-comprehensive-catalog.md` - Summary
- `canon-refresher-for-ai.md` - Summary
- `canon-master-document.md` - Summary

**Duplicated Data:**
- $1.6B total impact (appears 5+ times)
- $55M/year average (appears 4+ times)
- 4.6% of GDP (appears 4+ times)
- 30% production drop (appears 4+ times)
- 20% efficiency loss (appears 4+ times)
- Contribution breakdowns (appears 3+ times)

**Strategy:**
- **Keep full breakdown in master file** (Section: Economic Impact)
- **In other files:** Reference master file, provide summary only
- **Create quick reference table** in master file for easy lookup

---

### 5. Timeline Information (MEDIUM DUPLICATION)

**Appears in:**
- `slavery-and-raids-master.md` - Full timeline (Section 1)
- `economic-systems-master.md` - References
- `northern-raids-comprehensive-catalog.md` - Timeline references
- `canon-refresher-for-ai.md` - Summary timeline
- `canon-master-document.md` - Summary timeline

**Duplicated Data:**
- 1865-1867: Last Hurrah (appears 4+ times)
- 1867-1894: Decentralized raids (appears 4+ times)
- 1894: Last Chain Falls (appears 4+ times)
- 1905: Legal abolition (appears 4+ times)

**Strategy:**
- **Keep full timeline in master file** (Section: Slavery Timeline)
- **In other files:** Reference master file, provide summary only

---

### 6. Rules of Engagement (LOW DUPLICATION)

**Appears in:**
- `slavery-and-raids-master.md` - Full details (Section 5)
- `northern-raids-comprehensive-catalog.md` - References in raid descriptions
- `planter-adaptive-responses-to-raids.md` - References

**Duplicated Data:**
- Standard rules (appears 2+ times)
- Renege retaliation exception (appears 2+ times)
- "Accidental" renege problem (appears 2+ times)

**Strategy:**
- **Keep full details in master file** (Section: Rules of Engagement)
- **In catalog:** Reference only, don't repeat full rules

---

### 7. Planter Adaptive Responses (LOW DUPLICATION)

**Appears in:**
- `planter-adaptive-responses-to-raids.md` - Full details (464 lines)
- `slavery-and-raids-master.md` - Brief mentions
- `northern-raids-comprehensive-catalog.md` - References in raid descriptions

**Duplicated Data:**
- Geographic flight strategy (appears 2+ times)
- Crop diversification (appears 2+ times)
- Manumission as protection (appears 2+ times)

**Strategy:**
- **Keep full details in master file** (Section: Planter Adaptive Responses)
- **In catalog:** Reference only, don't repeat full strategies

---

## CONSOLIDATION STRATEGY

### Master File Structure (Deduplicated)

**File:** `world-building/02-economic-systems.md`

**Sections:**
1. **Four Horsemen of Slavery's Apocalypse** (Framework - single source)
2. **Slavery Timeline (1865-1905)** (Full timeline - single source)
3. **Toombs Act (1867)** (Full details - single source)
4. **Second Middle Passage (1867-1894)** (Full details - single source)
5. **Economic Impact Summary** (Quick reference table - single source)
6. **Rules of Engagement** (Full details - single source)
7. **Planter Adaptive Responses** (Full details - single source)
8. **Joint Crackdown (1867-1869)** (Full details - single source)
9. **Night Riders & Second KKK Suppression** (Full details - single source)
10. **Cuba Mirror Effect** (Full details - single source)
11. **Economic Systems (Currencies, Tariffs, Trade)** (Full details - single source)
12. **Global Cotton Glut** (Full details - single source)
13. **Global Boycott Trigger** (Full details - single source)
14. **Transcontinental Rail Routes** (Full details - single source)
15. **Great Depression in NTL** (Full details - single source)
16. **Raid Catalog Reference** (Summary + reference to detailed catalog)

**Key Deduplication:**
- **Raid Catalog:** Keep as separate file, reference in master
- **Statistics:** One summary table in master, reference elsewhere
- **Four Horsemen:** Full framework in master, reference in compendium
- **Timelines:** Full timeline in master, summary elsewhere

---

## REFERENCE STRATEGY

### In Master File:
- **Full details** for all topics
- **Summary statistics** for raids (detailed catalog is separate)
- **Cross-references** to related sections

### In Other Files:
- **Reference master file** instead of duplicating
- **Summary only** where needed
- **"See [master file] for details"** links

### In Raid Catalog:
- **Keep as separate detailed dataset** (1165 lines is appropriate for a catalog)
- **Reference in master file** with summary
- **No duplication** of framework/timeline (reference master file)

---

## SIZE REDUCTION ESTIMATE

**Current Total:** ~3000+ lines across multiple files

**After Deduplication:**
- Master file: ~1500-2000 lines (consolidated, no duplication)
- Raid catalog: 1165 lines (keep separate, referenced)
- **Total:** ~2700 lines (10% reduction from deduplication)

**Plus:**
- Clear references instead of duplication
- Single source of truth per topic
- Easier maintenance

---

## IMPLEMENTATION PLAN

1. **Create master file** with full details (no duplication within file)
2. **Keep raid catalog separate** (it's a dataset, reference it)
3. **Update other files** to reference master instead of duplicating
4. **Create summary tables** in master for quick reference
5. **Use clear cross-references** throughout

---

**Status:** DEDUPLICATION STRATEGY COMPLETE

