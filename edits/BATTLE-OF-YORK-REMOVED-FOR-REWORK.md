# Battle of York — Removed for Rework

**Date:** 2025-01-31  
**Status:** Placeholder — content removed so it can be reworked.

## Why removed

The current Battle of York material (July 18, 1863, whole-army breakthrough, Early frontal + Pickett/Hampton flank, ~4,500 CSA / ~2,800 Union casualties) was built for the **old** POD campaign:

- Whole army returning from Reading through York
- Meade coming from Baltimore
- Longstreet’s “miscalculation” / “foul-up” at York

In the **new** version (see `DIALOGUE-PAGE.md`):

- **Axis and threats are different:** Early slips past York (July 10–11); Pickett breaks through at **Harrisburg**; reunion west of Gettysburg. Meade stays at Harrisburg and splits to York (catch-22), no Baltimore.
- **Dates are different:** York/Wrightsville window is July 10–11, not July 18.
- **Cavalry clash at Wrightsville** (Meade sends cavalry to scout Early; Longstreet sent Hampton; Custer’s dash kills Hampton; Fitz Lee promoted) is kept but is a separate beat from Early’s infantry slip-past.

So the old “Battle of York” narrative (pitched infantry battle, July 18, breakthrough, casualty counts) no longer applies. York/Wrightsville content needs to be reworked from scratch to match the new axis, dates, and causality.

## What was removed

- **References:** Battle of York pointer in `canon-refresher-for-ai-detailed.md`; Battle of York and map references in `ACT-1-CLOSING-CHAPTERS-OUTLINE.md`; maintenance log entry that created the Battle of York canon.
- **Map:** `maps/battle-of-york-07-18-1863.png` (deleted).
- **part-03:** The detailed York encounter section (July 17–18 approach, battle phases, casualties, outcome) remains in `world-building/reference/pod-campaign/part-03-reading-raid-return.md` but is **obsolete** — that file is UTF-16 and will be fully rewritten per `edits/POD-CAMPAIGN-IMPLEMENTATION-PLAN.md`. Do not rely on the current York narrative there.

## What to do when reworking

1. Use **DIALOGUE-PAGE.md** (Phases 4–5) as the source of truth: Early slips past York July 10–11 (light casualties); cavalry clash at Wrightsville (Meade cavalry scout, Hampton, Custer kills Hampton, Fitz Lee).
2. Rebuild any standalone “York” or “Wrightsville” reference (dates, axis, forces, outcomes) to match that.
3. If a new map is needed, create it for the new timeline (e.g. Early at York / Wrightsville July 10–11).

## Where to look

- **Current narrative for York/Wrightsville:** `DIALOGUE-PAGE.md` (Phase 5, including cavalry clash at Wrightsville).
- **Implementation plan:** `edits/POD-CAMPAIGN-IMPLEMENTATION-PLAN.md` (what to add/remove when rewriting pod-campaign and canon).
