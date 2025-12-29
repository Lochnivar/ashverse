# Massive Files Reduction Plan

**Created:** December 29, 2025  
**Updated:** December 29, 2025  
**Goal:** Break up files >10K tokens so AI can process them effectively  
**Principle:** De-bloat first, then split by logical boundaries

---

## Results Summary

| File | Before | After | Action | Status |
|------|--------|-------|--------|--------|
| `rapidan-campaign-timeline.md` | 41,446 | Split (4 × ~11K) | Split into parts | ✅ DONE |
| `staffers.md` | 29,551 | 14,296 | Removed flavor chat | ✅ DONE |
| `northern-raids-catalog.md` | 22,034 | Split (3 files) | Split by phase | ✅ DONE |
| `canon-refresher-for-ai.md` | 17,276 | 17,276 | Keep as-is | ✅ OK |
| `questions-and-answers.md` | 16,985 | 16,985 | Keep as-is | ✅ OK |
| `canon-master-document.md` | 14,054 | 14,054 | Keep as-is | ✅ OK |

**Total massive file tokens: 164K → 122K (26% reduction)**

### Northern Raids Split Details
- `northern-raids-index.md`: 3,243 tokens (overview + stats)
- `northern-raids-phase-1.md`: 6,660 tokens (1865-1867)
- `northern-raids-phase-2.md`: 12,390 tokens (1867-1894)

### Current State
**No files over 18K tokens.** All files are now AI-manageable.

---

## Priority 1: rapidan-campaign-timeline.md (41K → 4 × ~10K)

### Current Structure
```
Lines 1-893:     Part 1: Meade's Fall & Warren's Rise (August)
Lines 894-1765:  Part 2: The Probing Phase (September)
Lines 1766-2929: Part 3: The Fourteen Days' Meat-Grinder (October 10-23)
Lines 2930-4149: Part 4: The Collapse (October 24 - December)
```

### Split Plan

Create 5 files:
1. `rapidan-campaign-index.md` (~500 tokens) - Overview + links to parts
2. `rapidan-campaign-part-1.md` (~10K tokens) - August 1863
3. `rapidan-campaign-part-2.md` (~10K tokens) - September 1863  
4. `rapidan-campaign-part-3.md` (~12K tokens) - October 10-23, 1863
5. `rapidan-campaign-part-4.md` (~12K tokens) - October 24 - December 1863

### Index File Content
```markdown
# Rappahannock-Rapidan Campaign Index

Quick reference and navigation for the 4-part campaign timeline.

## Campaign Overview
- **Dates:** August 1 - December 31, 1863
- **Union Commander:** Gouverneur Warren (replaces Meade)
- **Confederate Commander:** James Longstreet
- **Outcome:** Union defeat, Warren relieved

## Parts
1. [Part 1: Meade's Fall & Warren's Rise](rapidan-campaign-part-1.md) - August
2. [Part 2: The Probing Phase](rapidan-campaign-part-2.md) - September
3. [Part 3: The Fourteen Days](rapidan-campaign-part-3.md) - October 10-23
4. [Part 4: The Collapse](rapidan-campaign-part-4.md) - October 24 - December

## Key Events (Quick Reference)
- **Aug 1:** Meade relieved, Warren appointed
- **Sep 1-10:** Initial probing operations
- **Oct 10-23:** Main assault ("Meat-Grinder")
- **Oct 24+:** Army collapse, Warren relieved
```

---

## Priority 2: staffers.md (29K → 4 × ~7K)

### Current Structure
```
Lines 1-8:       File header
Lines 9-366:     Dr. General Fairfax-Lockwood (~358 lines)
Lines 367-683:   A.U.T.O. (~317 lines)
Lines 684-874:   G.R.O. Kronvoldt (~191 lines)
Lines 875-2342:  Claudette Oswald (~1467 lines)
```

### Split Plan

Create 5 files:
1. `staffers-index.md` (~500 tokens) - Overview + links
2. `staffer-fairfax-lockwood.md` (~8K tokens)
3. `staffer-auto.md` (~6K tokens)
4. `staffer-kronvoldt.md` (~4K tokens)
5. `staffer-claudette.md` (~11K tokens) - Largest, may need trimming

### Index File Content
```markdown
# Compendium Staffers Index

Meta-characters for the 1985 companion compendium. NOT in the actual novels.

## Characters
1. [Dr. General Michael J. Fairfax-Lockwood](staffer-fairfax-lockwood.md) - Author
2. [Archibald Ulysses Theophilus Oswald (A.U.T.O.)](staffer-auto.md) - Archival Assistant
3. [Gervais Rogerus Oscar Kronvoldt (G.R.O.K.)](staffer-kronvoldt.md) - Research Assistant
4. [Claudette Beatrice Oswald](staffer-claudette.md) - External Peer-Review Fellow

## Shared Elements
- **Sacred Typewriter Clause:** See Fairfax-Lockwood entry
- **Purpose:** Satirical academic framing for compendium
- **Setting:** Appomattox College of History and Strategy, 1985
```

---

## Priority 3: northern-raids-comprehensive-catalog.md (22K)

### Analysis Needed
- Check if it has natural section breaks
- Likely split by time period:
  - 1865-1870: Post-war raids
  - 1870-1880: Height of raiding
  - 1880-1894: Decline

### Defer until Priorities 1-2 complete

---

## Lower Priority Files (Keep + Summarize)

### canon-refresher-for-ai.md (17K)
- **Keep as-is** - This IS the AI quick reference
- Consider: Create even shorter "essential facts" version (~3K tokens)

### questions-and-answers.md (17K)
- **Archive answered questions** to separate file
- Keep only open/unanswered questions active
- Result: Much smaller working document

### canon-master-document.md (14K)
- **Keep as-is** - Detailed reference
- The `canon-refresher-for-ai.md` already serves as summary

### 02-economic-systems.md (13K)
- **Keep as-is** - Core world-building
- 13K is within acceptable range for focused work

### compendium-outline-book-ii.md (10K)
- **Keep as-is** - At threshold, not urgent

---

## Execution Order

### Session 1 (Do Now)
- [ ] Split `rapidan-campaign-timeline.md` into 4 parts + index
- [ ] Verify all content preserved
- [ ] Delete original after verification

### Session 2 (Next)
- [ ] Split `staffers.md` into 4 character files + index
- [ ] Move Sacred Typewriter Clause to index (single source)
- [ ] Delete original after verification

### Session 3 (Later)
- [ ] Analyze and split `northern-raids-comprehensive-catalog.md`
- [ ] Archive answered questions from Q&A file
- [ ] Create "essential facts" summary (~3K tokens)

---

## Post-Split Token Targets

| Category | Before | After | Savings |
|----------|--------|-------|---------|
| Rapidan timeline | 41K | 4 × 10K + index | Same tokens, better access |
| Staffers | 29K | 4 × 7K + index | Same tokens, better access |
| Northern raids | 22K | TBD | TBD |
| **Total massive files** | 164K | ~164K | **Better AI usability** |

**Note:** The goal isn't necessarily fewer total tokens, but smaller individual files that AI can process without truncation or confusion.

---

## Success Criteria

✅ No single file > 15K tokens (except essential reference docs)  
✅ All content preserved (verify before deleting originals)  
✅ Index files for navigation  
✅ Cross-references updated  
✅ AI can load any single file without context issues

---

**Ready to proceed with Session 1?**

