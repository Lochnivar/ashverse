# Butterfly Check Report

**Date:** December 10, 2025  
**Purpose:** Evaluate flow of events from PoD forward using plausibility gating  
**Focus:** Timeline inconsistencies and implausibilities caused by consolidation

---

## Summary

The butterfly check evaluates the flow of events from the Point of Divergence (July 1, 1863) forward, checking for:
- Timeline inconsistencies (events out of order)
- Causality violations (effects before causes)
- Missing prerequisites
- Plausibility scores below 70% threshold
- Contradictory information
- Events that don't flow logically from PoD

---

## Methodology

The butterfly check script (`scripts/butterfly-check.py`) extracts timeline events from master files and checks:

1. **Chronological Order:** Events must be in chronological order within each document
2. **Plausibility Thresholds:** All events must meet the 70% plausibility gate
3. **PoD Flow:** Events before PoD should not mention NTL-specific elements
4. **Causality:** Known causal chains must have appropriate delays:
   - Toombs Act → Global Boycott (minimum 30 days)
   - Raids → Joint Crackdown (minimum 180 days)
   - Toombs Election → Toombs Act (maximum 365 days)
5. **Consolidation Consistency:** Same events should not appear with significantly different dates (>1 year apart)

---

## Results

Run the butterfly check:
```bash
python scripts/butterfly-check.py
```

This will generate a comprehensive report showing:
- Total events checked
- Events with dates
- Events with plausibility scores
- Any errors or warnings found

---

## Known Issues to Monitor

### Toombs Presidency Dates
- **Political Systems:** 1867-1871 ✅
- **Timeline:** 1867 (elected), Dec 1867 (Toombs Act), 1867-1871 (disaster period) ✅
- **Status:** Consistent after consolidation fixes

### Timeline Order
- Master timeline table should be in chronological order
- Check for events that appear out of sequence

### Plausibility Scores
- All events in master timeline should have plausibility scores ≥70%
- Events below threshold need justification

---

## Recommendations

1. **Run butterfly check regularly** after major edits or consolidations
2. **Fix chronological order issues** immediately
3. **Review plausibility scores** below threshold and add justification if needed
4. **Verify causality chains** for known dependencies
5. **Check for duplicate events** with different dates after consolidation

---

## Integration with Hash System

The butterfly check complements the hash consistency system:
- **Hash system:** Tracks content changes and dependencies
- **Butterfly check:** Validates logical flow and plausibility

Both systems work together to ensure consistency across the project.

