# POD Campaign Implementation Plan: DIALOGUE-PAGE Version

**Purpose:** Implement the DIALOGUE-PAGE version of the Harrisburg → Reading → York → reunion sequence. Recalculate POD timeline and remove all references to old canon (Meade to Baltimore, whole-army Reading destruction, Battle of York July 18, Hampton killed at York, etc.).

**Source of truth:** `DIALOGUE-PAGE.md`

---

## 1. NEW POD TIMELINE (July 3–~July 14, 1863)

Use this as the canonical timeline. All documents should align to it.

| Phase | Dates | Event |
|-------|-------|--------|
| **POD** | Night July 1, 1863 | Lee dies (heart attack), Gettysburg. |
| **Withdrawal** | Dawn July 2, 1863 | Longstreet assumes command, countermarch north (unchanged from canon). |
| **Phase 1** | July 3–8 | Occupation of Harrisburg. Longstreet east bank ~50–55k. **Early present only July 3–5; Early departs for Reading July 5.** Main body remains at Harrisburg through the week. Meade arrives south/central PA, holds west bank in strength (does **not** go to Baltimore). Telegraph disinformation. |
| **Phase 2** | July 4–5 | Longstreet’s decision: Reading raid as **planned contingency**. Early’s division (~5–6k) detached; **Early departs Harrisburg July 5.** Main body stays at Harrisburg to lock Meade down. |
| **Phase 3** | July 5–12 | Early’s raid: **departs Harrisburg July 5** → Reading (~60 mi, 2–3 days). Reading hit ~July 7–8. **24–36 hours** at Reading (not 48). Targets: P&R Railroad — select bridges, rolling stock, sidings; ransoms/supplies. Damage **as permanent as Early can make it** in 24–36 hrs; point is political panic/force diversion, not tonnage. Early withdraws SE to Lancaster, then toward York. |
| **Phase 4** | July 7–11 | Meade’s catch-22: knows Early hit Reading; splits force — 60–70% at Harrisburg, 30–40% to York. March to York ~25–26 mi; vanguard July 8–9, main body strung out July 9–10. Anticipates Early at York ~July 10–11. |
| **Phase 5** | July 10–11 | Early at York: Lancaster → York (~24–26 mi). **Slips past** piecemeal Union forces (feint Wrightsville, secondary roads). Escape ~July 11. **Light casualties (~200–300)**. No pitched battle. |
| **Phase 6** | July 15–16 | Pickett’s breakthrough at Harrisburg. Longstreet sees garrison thinning; Pickett (~6–8k) punches through thinned west-bank lines at Camp Hill. ANV withdraws south through Cumberland Valley gaps. Rear-echelon chaos aids Early’s slip past York. |
| **Phase 7** | July 12–14 | Force reunion **west of Gettysburg**. Early arrives first; Longstreet’s main body follows. Combined ANV south via South Mountain toward Potomac. |
| **After** | Late July–early Aug | Potomac crossings; Hood matador; Meade sacked ~Aug 1; Warren appointed. (Unchanged from canon.) |

**Key removals from old timeline:**
- Meade never goes to Baltimore or York to “wait.” He stays at Harrisburg (west bank) until he splits to cover York.
- No “Battle of York” July 18 (pitched battle, Hampton killed, Custer’s dash, ~4,500 CSA / ~2,800 Union casualties).
- No whole-army Reading raid; no 48-hour destruction; no 35 locks, 14 bridges, 150 locomotives, $15–20M.
- No **infantry** Battle of York (Early slips past; light casualties). **Keep** Custer kills Hampton / Fitz Lee promotion — reframe as **cavalry clash at Wrightsville** (Meade sends cavalry to scout Early; Longstreet sent Hampton with cavalry-heavy contingent; Custer's dash kills Hampton; Fitz Lee succeeds).

---

## 2. OPEN DECISIONS (resolve before or during implementation)

1. **Hampton / Fitz Lee:** Old canon: Hampton killed at York July 18, Fitz Lee promoted. New version: no battle at York, so no Hampton death there. Options: (a) Hampton survives (stays with Longstreet at Harrisburg); (b) Hampton dies in another engagement (e.g. during Pickett’s breakout at Harrisburg or later); (c) Fitz Lee promotion happens later for other reasons. **RESOLVED — KEEP.** Meade sends cavalry south and across at Wrightsville to scout Early. Longstreet sends a cavalry-heavy contingent (Hampton) to screen the raid axis (he is locked down at Harrisburg). Cavalry clash at Wrightsville/York area; Custer's dash kills Hampton; Fitz Lee promoted. Early's infantry still slips past York (light casualties); the cavalry fight is separate but simultaneous.
2. **Custer (resolved — see above):** Old canon gave Custer a “rare success (resolved — see item 1 above)” at York (dash that kills Hampton). If York is downgraded to Early slipping past, that beat disappears. Keep, move, or drop? **Decision needed.**
3. **Map `maps/battle-of-york-07-18-1863.png`:** Either repurpose/rename (e.g. “Early at York” or “York escape”) or remove/archive. **Decision needed.**
3. **Battle of York reference:** Canon-refresher and part-03 point to “Battle of York” in `world-building/04-military-history.md` or `world-building/reference/`. Part-03 also links to `../../military/battle-of-york-1863-07-18.md`. If no standalone Battle of York doc exists, remove/rewrite those references to describe “Early slips past York” (July 14–15, light casualties) instead of a pitched battle.

---

## 3. FILES TO CHANGE (by category)

### 3.1 World-building – POD campaign (major rewrites)

| File | Action |
|------|--------|
| `world-building/reference/pod-campaign/part-02-harrisburg-occupation.md` | **Rewrite.** Remove: Quaker guns; Meade’s maneuver to York then Baltimore; Meade’s HQ in Baltimore; “TO: General Meade, Baltimore”; “Positioned for NEXT move (Baltimore).” Add: Meade **stays** at Harrisburg (west bank) in strength; blocks Longstreet; no assault after Camp Hill (or keep July 5 probe if desired); Reading raid decision = **contingency plan** (Early only), not whole army. Align dates to Phase 1–2 (July 3–9). |
| `world-building/reference/pod-campaign/part-03-reading-raid-return.md` | **Rewrite.** Remove: whole-army march to Reading; 48-hour destruction; 35 locks, 14 bridges, 150 locomotives; July 15 departure; Battle of York July 18; Hampton killed at York; Custer’s dash; Pickett/Hampton flank at York; Fitz Lee promotion at York; “Baltimore corridor”; “Meade’s main force (Baltimore/York).” Add: **Early’s division only** to Reading (July 10–12); 24–36 hours at Reading; damage as permanent as Early can make it; point is political panic/force diversion; Early Lancaster → York (July 14–15); **slip past** York (light casualties); **cavalry clash at Wrightsville** (Meade sends cavalry to scout Early, Longstreet sent Hampton with cavalry-heavy contingent, Custer's dash kills Hampton, Fitz Lee promoted); Longstreet/Pickett breakthrough at **Harrisburg** (July 15–16); reunion west of Gettysburg (July 16–18). Meade splits between Harrisburg and York (catch-22); no Meade in Baltimore. |
| `world-building/reference/pod-campaign/README.md` | Update summary: Reading = Early only, 24–36 hrs, political/headline focus; no Battle of York; Pickett at Harrisburg; Meade at Harrisburg then split; remove “35 locks, 14 bridges, 150 locomotives,” “Battle of York July 18,” “Hampton killed.” |
| `world-building/reference/pod-campaign/part-01-withdrawal.md` | **Minimal.** Keep July 1–2 withdrawal; “Baltimore Street” in Gettysburg is a street name, not Meade—no change. Ensure no later reference to Meade going to Baltimore. |

### 3.2 World-building – timelines and military

| File | Action |
|------|--------|
| `world-building/06-timelines.md` | **Replace** Gettysburg Campaign timeline (Section II). Remove: “July 12, 13:00 Reading surrenders”; “July 13-14 Reading destruction (48 hours) - 35 locks, 14 bridges, 150 locomotives”; “July 26-31 Return to Virginia.” Add: New POD timeline from Section 1 above (Phases 1–7, through reunion July 16–18; Potomac crossings late July–early Aug). Keep “For brigade-level detail see pod-campaign/” but note that pod-campaign parts will be updated. |
| `world-building/04-military-history.md` | **Search for** “Battle of York,” “York,” “July 18,” “Hampton,” “Reading.” Remove or rewrite any section that describes Battle of York July 18 as a pitched battle, Hampton killed at York, or 48-hour Reading destruction. Replace with: Early slips past York (July 14–15, light casualties); Pickett breakthrough at Harrisburg (July 15–16). (Only one “York” grep was “New York/Pennsylvania” — confirm no dedicated Battle of York section; if there is, rewrite or remove.) |

### 3.3 Canon refreshers and master

| File | Action |
|------|--------|
| `canon-refresher-for-ai.md` | POD section: keep Lee dies, Longstreet north, Harrisburg occupied. Add one line: “Reading = Early’s raid (contingency); Meade stays at Harrisburg then splits (catch-22); Pickett breaks through at Harrisburg; Early slips past York; reunion west of Gettysburg.” Remove any “Battle of York July 18” or “Meade to Baltimore” if present. |
| `canon-refresher-for-ai-detailed.md` | **Northern Collapse Sequence / KEY TIMELINE:** Replace Harrisburg/Reading/York/return bullets with new timeline (Phases 1–7). **References:** Remove or update “Battle of York: … July 18, 1863 — Longstreet’s miscalculation, 1-day mobile breakthrough.” Replace with “Early at York: July 14–15, 1863 — slips past Meade’s strung-out detachment; light casualties.” Update “Harrisburg Occupation” pointer to reflect Meade stays west bank (no Baltimore). **Maintenance log:** Remove “Created Battle of York canon document (July 18, 1863)…”; add entry for POD campaign update (DIALOGUE-PAGE implementation). **Maps:** Change “battle-of-york-07-18-1863.png” to “Early at York / York escape” or remove per decision. |
| `canon-master-document.md` | **Section 3 (Longstreet’s raid):** Remove “Gets within sight of Baltimore” if it implies Meade-in-Baltimore or old raid route. Update to: Harrisburg occupation → Meade blocks south → Reading raid (Early) → Meade’s split → Pickett at Harrisburg, Early past York → reunion west of Gettysburg. Align “July-October 1863” summary with new sequence (raid ends with reunion, then march to Potomac, etc.). |

### 3.4 Analysis and compendium

| File | Action |
|------|--------|
| `analysis/pennsylvania-campaign-analysis.md` | Remove or reword “Gets within sight of Baltimore” so it doesn’t imply old Meade/Baltimore or old raid route. |
| `analysis/pod-campaign-analysis.md` | Full pass: remove Meade to Baltimore, whole-army Reading, Battle of York July 18, Hampton at York. Align to new timeline and causality. |
| `compendium/table-of-contents-revised.md` | Remove “Within sight of Baltimore” (or rephrase). Update any “Battle of York” or “July 18” references to Early at York / slip past. |
| `compendium/chapters/part-i-the-match/chapter-03-pennsylvania-raid.md` | Remove “[Burning railroads… within sight of Baltimore]” or replace with new summary (Early’s raid, political panic, slip past York, Pickett at Harrisburg). |
| `compendium/chapters/part-i-the-match/chapter-02-torch-passes-reference.md` | If it references POD campaign, Reading, York, Baltimore—update to new version. |
| `notes/questions-and-answers.md` | Update “Longstreet’s 10-week Pennsylvania–Maryland raid… gets within sight of Baltimore” to new sequence (no Meade in Baltimore; Early’s raid; slip past York; Pickett at Harrisburg). |

### 3.5 Books – outlines and references (no prose in `books/`)

| File | Action |
|------|--------|
| `books/book-01-the-match/ACT-1-CLOSING-CHAPTERS-OUTLINE.md` | **Major update.** Remove: “Meade’s reaction (Baltimore)”; “Reading over Philadelphia/Baltimore” as whole-army target; “The Burning of Reading” (July 13–14 full destruction); “The York Foul-Up” (July 17–18 pitched battle, Early frontal + Pickett/Hampton flank, Custer/Hampton). Add: Meade stays at Harrisburg, then split to York (catch-22); Early’s raid only (24–36 hrs Reading); Early slips past York (July 14–15); Pickett’s breakthrough at Harrisburg (July 15–16); reunion west of Gettysburg. Adjust chapter beats to match new timeline. |
| `books/book-01-the-match/ACT-STRUCTURE-SUMMARY.md` | If Act 1 summary mentions Reading/York/Baltimore/Battle of York—update to new version. |
| `books/book-01-the-match/CHAPTER-OUTLINE-PROPOSAL.md` | Same as ACT-1-CLOSING: remove Baltimore, 48-hour Reading, Battle of York July 18; add Early raid, slip past York, Pickett at Harrisburg, reunion. |
| `books/book-01-the-match/chapter-05.md` | If chapter-05 is “Reading” or “Baltimore”: align to Early’s raid only and no Meade in Baltimore. |
| `books/book-01-the-match/chapter-07.md` | Remove “Gets within sight of Baltimore” if present. |
| `books/book-01-the-match/chapter-14.md` | “Threatens Baltimore, Reading, York”—rephrase so “Baltimore” isn’t Meade’s position; keep as geographic threat if needed. |

### 3.6 Characters

| File | Action |
|------|--------|
| `characters/confederate-military.md` | If it mentions Hampton killed at York, Fitz Lee promotion at York, or cavalry command change July 18—update per Open Decision (Hampton/Fitz Lee). |

### 3.7 Maps and other references

| Item | Action |
|------|--------|
| `maps/battle-of-york-07-18-1863.png` | Per Open Decision: rename/repurpose (e.g. “early-at-york-1863-07-15.png”) or archive/remove. |
| `analysis/military/meade-36-hour-delay-telegraph-strategy-2025-12-17.md` | **Keep.** Still explains how Longstreet gets to Harrisburg. Optionally add one sentence: Meade then holds west bank (does not go to Baltimore). |
| Any file linking to `battle-of-york-1863-07-18.md` or `world-building/military/` | Update or remove broken link; point to new narrative (Early at York in timeline or part-03). |

---

## 4. PHRASES / ELEMENTS TO REMOVE EVERYWHERE

- Quaker guns (fake artillery at Harrisburg) — no longer needed; main body stays, no bluff required.
- Meade goes to Baltimore / Meade’s HQ Baltimore / “TO: General Meade, Baltimore” / “Positioned for NEXT move (Baltimore)” / “From York… then Baltimore.”
- Battle of York July 18 (pitched battle, breakthrough, Longstreet’s miscalculation).
- Hampton killed at York / Custer’s dash at York / Fitz Lee promoted at York (keep and reframe as cavalry clash at Wrightsville July 10–11.)
- Reading: 48 hours destruction; 35 locks, 14 bridges, 150 locomotives; $15–20M; whole army at Reading.
- “Longstreet fools Meade” / “Meade moved faster than I credited” (York foul-up)—replace with Meade’s catch-22 and Early slipping past.
- “Forward corps at York, reinforced rapidly from Baltimore corridor” (replace with Meade’s detachment strung out on march to York).
- July 26–31 Return to Virginia (replace with reunion July 16–18, then march to Potomac, crossings late July–early Aug).

---

## 5. PHRASES / ELEMENTS TO ADD (where relevant)

- Meade **stays** at Harrisburg (west bank) in strength; blocks Longstreet.
- Reading raid = **Early’s division only**; **planned contingency**; 24–36 hours; damage as permanent as Early can make it; point is political panic/force diversion, not tonnage.
- Meade’s **catch-22**: split between Harrisburg and York → not enough at either.
- Early **slips past** York (July 10–11); light casualties (~200–300); no pitched infantry battle.
- **Pickett’s breakthrough at Harrisburg** (July 11–12); thinned garrison.
- **Cavalry clash at Wrightsville** (July 10–11): Meade sends cavalry to scout Early; Longstreet sent Hampton (cavalry-heavy contingent); Custer's dash kills Hampton; Fitz Lee promoted.
- **Reunion west of Gettysburg** (~July 12–14); Early first, then Longstreet’s main body.
- Potomac crossings / Hood matador / Meade sacked ~Aug 1 (unchanged).

---

## 6. ORDER OF WORK (suggested)

1. **Decide** Hampton/Fitz Lee, Custer, and map (Section 2).
2. **Rewrite** `world-building/reference/pod-campaign/part-02-harrisburg-occupation.md` and `part-03-reading-raid-return.md` (and README) to new timeline and causality.
3. **Update** `world-building/06-timelines.md` (Section II) with new POD timeline.
4. **Update** canon-refresher (short + detailed) and canon-master-document.
5. **Update** analysis, compendium, notes (remove old, add new).
6. **Update** book outlines and chapter references (no prose in `books/` per golden rule).
7. **Update** character references (Hampton/Fitz Lee per decision).
8. **Handle** map file and any broken links.
9. **Run** `scripts/calculate-hash.py` and consistency-checker per process; update dependent hashes.

---

**Document hash:** (calculate after edits)  
**Last updated:** (date when plan is locked or revised)
