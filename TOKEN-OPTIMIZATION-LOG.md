# Token Optimization Project Log

**Started:** December 29, 2025  
**Goal:** Reduce token usage across entire project while maintaining human readability  
**Principle:** One-time cost to organize/fix → reduced AI load for all future sessions

---

## Progress Summary

| Phase | Description | Status | Token Savings |
|-------|-------------|--------|---------------|
| 1 | Character files (union/confederate military) | ✅ COMPLETE | ~16,500 tokens (69%) |
| 2 | Project analysis | ✅ COMPLETE | - |
| 3 | Encoding fixes | ✅ COMPLETE | - |
| 4 | Staffers.md duplicate removal | ✅ COMPLETE | ~700 tokens |
| 5 | Overhead reduction (all files) | ✅ COMPLETE | ~1,713 tokens |
| 6 | Delete obsolete files | ✅ COMPLETE | ~5,000 tokens |
| 7 | Tools review | ✅ COMPLETE | No merge needed |

**Total Estimated Savings: ~24,000 tokens (~5.7%)**

---

## Session 1: December 29, 2025

### Phase 1: Character Files ✅ COMPLETE

**Files Optimized:**
- `characters/union-military.md`: 1,382 → 435 lines (69% reduction)
- `characters/confederate-military.md`: 1,556 → 370 lines (76% reduction)

**Optimization Applied:**
- Condensed verbose sections (Basic Info, Physical Description, Personality)
- Removed duplicate content (Skills & Abilities = Strengths)
- Removed template filler (generic Fears/Desires/Quirks)
- Removed redundant sections (Character Arc, Voice & Dialogue, Narrative Notes)
- Kept only primary casting reference ("Visualize as")
- Preserved full NTL Divergence (story-critical content)
- Fixed encoding issues (em-dashes, special characters)

### Phase 2: Project Analysis ✅ COMPLETE

**Initial Token Count:** ~419,230 tokens (excluding /books)

**Top Token Consumers Identified:**
1. `rapidan-campaign-timeline.md`: 36,905 tokens (9.5%)
2. `staffers.md`: 26,955 tokens (7.0%)
3. `northern-raids-comprehensive-catalog.md`: 20,342 tokens (5.3%)
4. `questions-and-answers.md`: 16,786 tokens (4.3%)
5. `canon-refresher-for-ai.md`: 13,696 tokens (3.5%)

### Phase 3: Encoding Fixes ✅ COMPLETE

**Files Fixed:** `staffers.md`
- Fixed mojibake characters (CÃ¡diz → Cadiz, â€" → -, etc.)

### Phase 4: Staffers.md Optimization ✅ COMPLETE

**Duplicates Removed:**
- 2 duplicate "Sacred Typewriter Clause" sections (Auto's and Kronvoldt's)
- Replaced with references to master clause in Dr. General Fairfax-Lockwood's entry

**Result:** 2,526 → 2,480 → 2,342 lines (184 lines removed, ~700 tokens saved)

### Phase 5: Overhead Reduction ✅ COMPLETE

**Python Script Created:** `scripts/project-optimizer.py`
- Analyzes token usage across project
- Removes dividers before headers
- Eliminates consecutive blank lines
- Reduces blank + divider + blank patterns

**Applied To:** 165 files
**Tokens Saved:** ~1,713

### Phase 6: File Cleanup ✅ COMPLETE

**Deleted:**
- `compendium/table-of-contents.md` (superseded by `table-of-contents-revised.md`)

**Reviewed (No Action Needed):**
- `notes/questions-and-answers.md` - Active working document with unanswered questions

### Phase 7: Tools Review ✅ COMPLETE

**Assessed:** 4 files in `/tools`
- `battle-simulation-guide.md` + `battle-simulation-template.md` (tactical level)
- `wargaming-simulation-guide.md` + `wargaming-simulation-template.md` (operational level)

**Conclusion:** No merge needed - these serve different purposes (tactical vs operational simulation)

---

## Final State

**Total Project Tokens:** ~416,814 (excluding /books)
**Reduction from session start:** ~2,416 tokens from this session
**Reduction from character optimization (prior):** ~16,500 tokens

### Current Top Token Consumers

| File | Tokens | Overhead |
|------|--------|----------|
| `rapidan-campaign-timeline.md` | 41,446 | 29% |
| `staffers.md` | 29,551 | 15% |
| `northern-raids-comprehensive-catalog.md` | 22,034 | 23% |
| `canon-refresher-for-ai.md` | 17,276 | 21% |
| `questions-and-answers.md` | 16,985 | 33% |

---

## Future Optimization Opportunities

### High ROI (when time permits)

1. **Apply character template to remaining character files:**
   - `staffers.md` - Creative content, careful approach needed
   - `HASKELL-FAMILY-SUMMARY.md` (5,434 tokens)
   - `FAIRFAX-FAMILY-SUMMARY.md` (4,451 tokens)

2. **Review largest reference files for consolidation:**
   - `rapidan-campaign-timeline.md` (41,446 tokens) - Could be split into separate part files
   - `northern-raids-comprehensive-catalog.md` (22,034 tokens)

### Medium ROI

3. **Reduce prose in world-building files:**
   - Convert verbose explanations to bullet points
   - Target files with high tokens/line ratio

### Low ROI (skip unless specific need)

4. **Further overhead reduction:**
   - Already reduced from 36% to 29% average
   - Diminishing returns at this point

---

## Resume Instructions

If continuing this work later:

1. Run `python scripts/project-optimizer.py` to see current token counts
2. Focus on "High ROI" opportunities above
3. For character files, use the Lincoln template format (see Phase 1)
4. Always preserve story-critical content (NTL Divergence, LOCKED CANON)
5. Test changes with `--optimize` before `--optimize --apply`

---

## Tools Created

### `scripts/project-optimizer.py`

**Usage:**
```bash
python scripts/project-optimizer.py                  # Analyze all files
python scripts/project-optimizer.py --optimize      # Preview changes
python scripts/project-optimizer.py --optimize --apply  # Apply changes
python scripts/project-optimizer.py --fix-encoding  # Fix encoding only
```

### `scripts/optimize-characters.py`

**Purpose:** Apply token-optimized template to character files
**Usage:** Modify the file list at the bottom and run

---

## Optimization Principles

### Token-Efficient AND Human-Readable
- Shorter headers (`## Basics` not `## Basic Information and Background`)
- One blank line between sections (not 2-3)
- Fewer decorative dividers (`---`)
- Condensed bullet points (facts, not prose)
- Standard abbreviations (NTL, OTL, CSA, USA)
- Remove redundant labeling

### What to Preserve
- Clear structure with headers
- Essential whitespace for readability
- Full content in story-critical sections (NTL Divergence)
- Cross-references to other documents
- Creative/voice content (staffers examples, footnotes)

### What to Remove
- Duplicate content across sections
- Generic template filler
- Verbose prose when bullets work
- Multiple alternatives (keep best one)
- Excessive dividers and blank lines

---

**Last Updated:** December 29, 2025  
**Last Action:** Session 1 complete - all planned optimizations applied
