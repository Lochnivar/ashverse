# Analysis Master Files

**Date:** December 10, 2025  
**Status:** CONSOLIDATION IN PROGRESS  
**Purpose:** Topic-based master analysis files consolidating original analyses

---

## FORMAT

All files follow the standardized topic-based format:

1. **ANALYSIS ASSUMPTION TESTED** - What is being analyzed
2. **PARAMETERS** - Key variables, constraints, historical context
3. **RESULTS** - Plausibility scores, breakdowns, key findings
4. **CAVEATS** - Assumptions, limitations, edge cases
5. **FINAL RESULT** - Overall plausibility and status
6. **DOCUMENT DEPENDENCIES** - Hash tracking for consistency checking
7. **REFERENCES** - Source files consolidated

---

## COMPLETED FILES (40)

### Military Topics (23):
1. `pickett-raid-dates-analysis.md` - Pickett's Raid date range
2. `pickett-raid-force-size-analysis.md` - Pickett's Raid force size
3. `hancock-wounding-analysis.md` - Hancock wounding date
4. `pod-lee-death-analysis.md` - POD: Lee's death
5. `pod-longstreet-decision-analysis.md` - POD: Longstreet's decision
6. `northern-collapse-sequence-analysis.md` - Northern collapse sequence
7. `grant-final-gamble-analysis.md` - Grant's Final Gamble
8. `meade-freeze-analysis.md` - Meade's 36-hour freeze
9. `casualty-figures-analysis.md` - Casualty plausibility
10. `atlanta-campaign-analysis.md` - Atlanta Campaign
11. `appomattox-surrender-analysis.md` - Appomattox surrender
12. `sherman-march-analysis.md` - Sherman's march to Appomattox
13. `pod-campaign-analysis.md` - POD campaign detailed timeline
14. `gamble-discovery-analysis.md` - Gamble's discovery of withdrawal
15. `lincoln-promotion-analysis.md` - Lincoln promotion analysis
16. `appomattox-college-analysis.md` - Appomattox College concept
17. `pennsylvania-campaign-analysis.md` - Pennsylvania Campaign
18. `hagerstown-battle-analysis.md` - Battle of Hagerstown
19. `warren-appointment-analysis.md` - Warren's appointment and relief
20. `rappahannock-rapidan-campaign-analysis.md` - Rappahannock-Rapidan Campaign
21. `winter-of-despair-analysis.md` - Winter of Despair
22. `mcclellan-election-analysis.md` - McClellan's election
23. `pickett-flying-corps-analysis.md` - Pickett's Flying Corps

### Economic Topics (3):
17. `slavery-death-mechanics-analysis.md` - Four mechanisms killing slavery
18. `roaring-twenties-analysis.md` - Roaring Twenties NTL
19. `great-depression-analysis.md` - Great Depression NTL

### Political Topics (10):
20. `csa-presidents-analysis.md` - CSA presidents timeline
21. `treaty-of-cincinnati-analysis.md` - Treaty of Cincinnati
22. `csa-usa-presidential-interactions-analysis.md` - CSA-USA interactions
23. `california-presidents-analysis.md` - California presidents
24. `california-political-system-analysis.md` - California political system
25. `california-japan-relations-analysis.md` - California-Japan relations
26. `usa-presidents-analysis.md` - USA presidents
27. `csa-cross-border-impact-analysis.md` - CSA cross-border impact
28. `washington-oregon-options-analysis.md` - Washington/Oregon options
29. `presidential-depression-impact-analysis.md` - Presidential depression impact

### OTL Divergence Topics (1):
30. `otl-events-analysis.md` - OTL events verification

### Narrative Topics (3):
31. `narrative-structure-analysis.md` - Narrative structure analysis
32. `compendium-concept-analysis.md` - Compendium concept
33. `family-structure-analysis.md` - Family structure analysis

---

## HASH TRACKING

All files include **DOCUMENT DEPENDENCIES** sections tracking:
- Dependencies on `world-building-master/` files
- Self-hashes (to be calculated)
- Last updated dates

**To check consistency:**
```bash
python scripts/consistency-checker.py
```

---

## REMAINING WORK

**Status:** ~61% complete (40/66 files consolidated)

**Remaining categories:**
- Additional military analyses
- Additional political analyses
- Narrative analyses
- Consistency/system analyses (may keep as reference)

**Next steps:**
1. Continue creating topic files for remaining analyses
2. Archive original files after consolidation
3. Update references to old file paths
4. Calculate final hashes for all files

---

## NOTES

- Original analysis files remain in `analysis/` until consolidation complete
- Hash tracking enables automated consistency checking
- Format standardized for AI parsing and reference
- Files track dependencies on world-building master files

