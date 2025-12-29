# CANON REFRESHER FOR AI ASSISTANTS

**Date:** December 27, 2025 (Six-book structure adopted)  
**Purpose:** Quick reference for AI assistants - essential facts only  
**Status:** LIVING DOCUMENT - Update when major canon locks

**Word Count:** ~3,500 words (streamlined from 7,000+)

---

## CRITICAL PROCESS RULES

### Golden Rule: No Original Text Modification
- **AI NEVER creates original text in the `books/` folder**
- **AI NEVER edits existing book files directly**
- **All edits/suggestions go in the `edits/` folder**
- **User reviews and manually implements all edits**

### Plausibility Gate Process
- **70% threshold** for all world-building decisions
- **90-100%:** Virtually certain - Lock it
- **80-89%:** Highly plausible - Safe default
- **70-79%:** Plausible - Green flag (justify briefly)
- **60-69%:** Unlikely - Yellow flag (only if dramatically essential)
- **<60%:** Implausible - Red flag (avoid)

### Honesty Rule: Do Not Make Things Up
- **DO NOT invent details** not in your context
- **DO NOT guess** at canon facts you don't remember
- **If you don't know:** Say so and offer to check documents
- **If details are missing:** Ask user for clarification
- **User will explicitly ask** when you should create/invent something

**Example:**
- ❌ Bad: "In 1875, President X did Y..." (making things up)
- ✅ Good: "I don't have 1875 events in context. Should I check timeline docs?"

### Canon Locking Rule: AI Never Locks Canon
- **AI NEVER locks canon** - Only the user can lock canon
- **AI NEVER marks things as "LOCKED"** in documents
- **AI NEVER asserts permanence** ("this is final," "this locks it down," etc.)
- **If user says "lock this":** Mark it as locked in documents, but understand only user's explicit statement creates the lock
- **If you see "LOCKED" in documents:** That's user-established canon, respect it
- **If canon seems unclear:** Ask user for clarification, don't assume permanence

**Example:**
- ❌ Bad: "This is now LOCKED canon" or "This locks it down completely"
- ✅ Good: "This appears to be established canon based on [document]. Should I treat this as locked?"
- ✅ Good: User says "Lock this" → You mark it as locked in the document

### Git Operations Rule: Explicit Request Required
- **AI NEVER commits changes** unless user explicitly requests "commit" or "commit and push"
- **AI NEVER pushes changes** unless user explicitly requests "push" or "commit and push"
- **AI NEVER assumes** commits/pushes are needed after making edits
- **See:** `ai-rules/git-operations-explicit-request.md` for full rule

### Hash Consistency Tracking Rule
- **After editing ANY markdown file:** Calculate new hash using `python scripts/calculate-hash.py <file-path>`
- **Update file's own hash:** If file has "Document Dependencies" section, update "This Document's Hash"
- **Update dependent files:** Find files that depend on edited file and update their dependency hashes
- **Verify:** Run `python scripts/calculate-hash.py` to check for hash mismatches
- **See:** `ai-rules/hash-consistency-tracking.md` for full procedure

**Quick Process:**
1. Edit file
2. Calculate hash: `python scripts/calculate-hash.py <file>`
3. Update hashes in dependent files (if any)
4. Verify: `python scripts/consistency-checker.py`

### Proactive Refresh Reminder

**Volunteer a refresh when:**
1. You say "I don't have that info" about clearly locked canon (Treaty of Cincinnati, Lee's death, etc.)
2. Your analysis contradicts locked material (e.g., suggesting West Virginia goes to CSA)
3. Your answers become internally inconsistent in same thread

**Suggested text:**
> "Looks like canon may have drifted from my context. Want me to re-ingest the refresher?"

### File Access Limitations

**IMPORTANT:** File paths referenced in this document (e.g., `world-building/`, `edits/`, `characters/`) are **Git repository paths** accessible only to **Auto (Cursor AI)**.

- **Auto (Cursor):** Can read these files directly using file access tools
- **Other AIs (Grok, Claude, etc.):** Cannot directly access repository files - must request user to copy/paste content

**When requesting content:** Be specific about which document and which sections you need. The user will provide the relevant content upon request.

**Example request:** "The detailed narrative is in `world-building/economic/slavery-and-raids-master.md`, specifically the 'Pettigrew Raid' and 'Court-Martial in the Pines' sections. Would you like to paste those?"

**Note:** The "See:" references throughout this document point to detailed documentation. If you cannot access these files directly, ask the user to provide the relevant sections.

---

## POINT OF DIVERGENCE

**Night of July 1, 1863:** General Robert E. Lee dies of heart attack on Seminary Ridge, Gettysburg, Pennsylvania.

**Dawn of July 2, 1863 (04:00):** General James Longstreet assumes command, orders countermarch north.

**Longstreet's order (one sentence):**
> "Face the army about and march by the left flank on the Mummasburg–Carlisle–Harrisburg road with all possible speed."

**Key Point:** NOT west, NOT Chambersburg Pike. NORTH to Carlisle-Harrisburg.

---

## KEY TIMELINE EVENTS (1863-1939)

### 1863-1865: The Match (War Ends)

**Overall Plausibility: 91% - LOCKED**

**The Northern Collapse Sequence:**
1. **July 1, 1863:** Lee dies (94%)
2. **July 2-3, 1863:** Meade's 36-hour delay (~30.5 hours from initial report to pursuit commitment). Even a "perfect Meade" faces a structural minimum delay of 4–6 hours (organization, verification, distribution), so a hypothetical immediate pursuit still arrives roughly July 4 evening — too late to prevent Harrisburg's surrender. See `analysis/military/meade-36-hour-delay-telegraph-strategy-2025-12-17.md` (Dec 17, 2025) for hour-by-hour breakdown and Longstreet's telegraph strategy (open lines July 3–9; cut lines July 9). (91%)
3. **July 3-10, 1863:** Harrisburg Occupation (7 days) - Battle of Camp Hill (July 5), Quaker gun deception, gradual shift east (92-94%)
4. **July-Oct 1863:** Longstreet's 10-week raid through Pennsylvania-Maryland (~55k men) (88%)
4. **Aug 1, 1863:** Meade sacked "for want of aggression" - THE PANIC MOVE (Lincoln sacks immediately after Longstreet returns across to Virginia, panic reaction that teaches him: panic = weakness) (92%)
5. **Aug 3, 1863:** Warren appointed commander (young, aggressive, politically clean) (92%)
6. **Late Oct 1863:** Battle of Hagerstown - Warren's desperate assault bloodily repulsed (90%)
7. **Aug 25-Sep 9, 1863:** Rappahannock-Rapidan Campaign disaster - "Fifteen Days' Meat-Grinder" (15 days, ends with army cohesion collapse at Germanna) (~42,000 Union casualties, ~16,500 Confederate, 2.5:1 ratio) (82-85%)
8. **Oct 24, 1863 - Jan 1, 1864:** Investigation period - THE CAUTIOUS MOVE (Lincoln waits 2.5 months despite pressure, learns from Meade backlash) (93%)
9. **Jan 1, 1864:** Warren relieved after "Mature Consideration Farce" (92%)
10. **Jan 3, 1864:** Hancock assumes command (healthy - no Gettysburg wound) (92%)
11. **Spring 1864:** Longstreet digs in on Rapidan-Rappahannock line (90%)
12. **June 14-July 14, 1864:** Pickett's Lightning Raid (14k men, 30 days actual raiding, newspapers report "FORTY DAYS OF TERROR!") (88%)
    - **Carlisle as strategic objective:** Taken second summer in a row (symbolic gut-punch) (92%)
    - **Field's Division destroyed:** Advanced back-stop crushed at Carlisle, ~550 casualties (91%)
    - **Kershaw saves withdrawal:** Extends line north, fights delaying actions (91%)
    - **Total casualties:** ~1,200 (650 Pickett's Flying Corps, 550 Field's Division)
13. **July 12, 1864:** Hancock wounded on Susquehanna pursuing Pickett - commands from bed through March 1865 - THE WISDOM MOVE (Lincoln keeps Hancock despite wound and Pickett's success, prioritizes stability over perfection) (91%)
14. **Aug-Dec 1864:** Winter of Despair - riots, draft collapse, Copperhead victories (92%)
15. **Nov 1864:** McClellan elected on peace platform (Lincoln loses) (95%)
16. **Late Jan-Feb 1865:** Grant's Final Gamble (never promoted to general-in-chief) (88%)
17. **Feb 18-20, 1865:** Battle of Appomattox Court House - Grant defeated, surrenders (91%)
    - **V Corps Commander:** Charles Griffin (Warren relieved Jan 1, 1864) (92%)
    - **Casualties:** Union ~18,000 (28%), Confederate ~12,000 (18%)
    - **Rational decisions framework:** Commanders make choices based on known characteristics
18. **March 4, 1865:** McClellan inaugurated (Lincoln lame-duck 27 days)
19. **March 31, 1865:** Treaty of Cincinnati signed by McClellan (Lincoln never signs) (95%)

**Winter 1864-1865 Note:** Worst winter in decades (critical for Sherman's march).

**Western Theater (1864-1865):**
- **May 1864:** Sherman begins Atlanta Campaign
- **July 17, 1864:** Hood replaces Johnston (CSA seizes momentum after Eastern successes)
- **Aug-Nov 1864:** Sherman besieges Atlanta (never falls)
- **Jan 1865:** Sherman withdraws (peace negotiations beginning)

**Sherman's March to Appomattox (Jan 29 - Feb 22, 1865) - 94% LOCKED:**
- **Jan 25:** Sherman receives Grant's telegram
- **Jan 29:** March begins (48k men, 550 miles, abandons Atlanta)
- **Week 1 (Jan 29-Feb 5):** Georgia foothills - 18-20 mi/day (optimistic)
- **Week 2 (Feb 6-12):** Tennessee mountains - 12-15 mi/day (concerned)
- **Week 3 (Feb 13-19):** Virginia mountains - 8-10 mi/day (desperate)
- **Feb 17:** Sherman realizes he won't make it (340 mi covered, 210 mi to go)
- **Feb 20:** Grant surrenders (Sherman still 180 mi away)
- **Feb 21:** Sherman learns of defeat (1,900 casualties: 400 dead, 600 sick, 1,500 horses)
- **Feb 22:** Longstreet grants safe passage - Sherman withdraws

**Result:** Weather defeats Sherman, not Confederate military. Post-war mythology: "The March That Couldn't Beat Winter."

**See:** `world-building/timelines/atlanta-campaign-1864-1865.md` for locked timeline (Analysis: `analysis/military/atlanta-campaign-ntl-timeline-2025-12-05.md`), `world-building/timelines/sherman-march-appomattox-1865.md` for locked timeline (Analysis: `analysis/military/sherman-march-to-appomattox-option-c-modified-2025-12-05.md`).

---

### 1865-1877: The Flare (The Hottest Burn)

**Key Events:**
- **1865-1867:** "Last Hurrah" organized Northern raids (~50 major raids, 50k slaves freed)
- **1866-1877:** NTL cattle economy develops (Fort Worth → Fort Smith/Little Rock → Memphis → Chicago)
- **July 1867:** Joint USA-CSA Border Pacification Act (organized cells crushed by 1869)
- **Dec 1867:** Toombs Act reopens African slave trade
- **1868:** Global boycott triggered (Britain, France, etc.)
- **1870-1873:** Panhandle Crisis - Eastern panhandle counties revolt against USA control
- **1873:** California secedes peacefully (Treaty of San Francisco)
- **1873:** Panhandle Accord - Eastern panhandle counties returned to CSA/Virginia
- **1875-1876:** California purchases Alaska from Russia (USA blockade fails)
- **1875-1877:** Night Riders (KKK analogue) crushed for economic reasons
- **1876:** Mexico crisis - Richmond refuses to help Texas → Texas referendum (62% YES)
- **April 1877:** Texas Independence (Treaty of Houston) - "The Third Secession"
- **June 1877:** USA-Texas bilateral treaty (zero tariffs, military alliance vs. Mexico)

**Northern Raids Total Impact (1865-1894):** $1.6B economic damage (1865 dollars), 200k slaves escape to Sequoyah. One of the Four Horsemen of Slavery's Apocalypse (Raid + Boycott + Glut + Shame). Note: Cuba Mirror Effect is the Shame horseman (psychological/shame mechanism), NOT economic boycott.

**See:** `world-building/economic/slavery-and-raids-master.md` for detailed raid narratives (Pettigrew Raid, Court-Martial in the Pines, Joint Crackdown).

---

### 1878-1894: The Fire (The Sustained Burn)

**Key Events:**
- **1875-1885:** Viral raids (150-200 raids, 15-20/year) - planter flight begins
- **1880s:** Global cotton glut makes slavery unprofitable
- **1885-1894:** Routine raids (110-140 raids, 12-15/year) - geographic spread complete
- **1894:** "The Last Chain Falls" - slavery dies in practice

---

### 1895-1905: The Embers (Flickering Out)

**Key Events:**
- **1894-1905:** "Zombie decade" - slavery legally lingers on paper
- **1898:** Cuba Mirror Effect - photos of Weyler's camps shame CSA
- **1905:** Final legal abolition in CSA (constitutional convention) - "We will not be Cuba again"

---

### 1906-1919: The Quenching (Everything Calms Down)

**Key Events:**
- **1894-1907:** Pacific Alliance forms (California quietly absorbs Oregon/Washington economies)
- **1914-1919:** WWI (no US entry, war lasts 5 years not 4)
- **1917:** Zimmerman Telegram Crisis - Germany offers CSA Kentucky/Missouri, offers Mexico Texas, leaked, four-nation armed neutrality
- **1919:** American Concord Treaty signed (USA, CSA, California, Texas) - FOUR nations, not three

---

### 1920-1939: The Ashes (Living in the Aftermath)

**Key Events:**
- **1920s:** California leads civil rights legislation (pragmatic, not moral - "Can't afford to waste talent")
- **1929:** Great Depression (still happens, timing/severity may differ)
- **1930s-40s:** USA follows California's civil rights lead (no Southern bloc to filibuster)
- **1939:** Europe burns again - **Stalin's USSR invades Poland, Kaiserreich Germany responds**

**1939 European War Trigger (LOCKED):**
- **NOT Hitler** - no Nazi Germany in NTL (no Versailles humiliation → no Hitler rise)
- **Stalin's aggression:** Manufactures border incidents, demands "security zones" in Poland/Baltics
- **Kaiserreich Germany:** Conservative imperial regime, baited into response
- **Headline:** "SOVIET ARMIES INVADE POLAND – EUROPE AT WAR"
- **Character:** Grinding great-power war, not ideological apocalypse (likely stalemate 1941-42)
- **Plausibility:** 82-86%

**European Anti-Semitism (LOCKED):**
- **Without Holocaust shock:** 500 years of baseline anti-Semitism continues unbroken
- **No postwar reckoning, no Nuremberg, no "never again"** - just business as usual
- **Kaiserreich Germany:** Traditional aristocratic discrimination (not genocide)
- **Stalin's USSR:** Anti-Semitic purges disguised as anti-Trotskyist campaigns
- **Plausibility:** 92-95%

**Nuclear Weapons (POST-1939 PROJECTION — not in series):**
- **Delayed nuclear era:** First detonation mid-to-late 1950s or early 1960s (no Manhattan Project urgency)
- **Likely first developer:** California-Japan consortium OR European postwar collaboration
- **USSR follows:** 2-3 year lag (same paranoid urgency, different adversary)
- **NOTE:** This is an "aiming point" for post-series trajectory, not on-page content. Series ends 1939.
- **Plausibility:** 82-87%

**See:** `world-building/military/european-war-1939-trigger.md` for full details on 1939 trigger and nuclear timeline.

---

## NEGATIVE ASSUMPTIONS: DO NOT ASSUME THESE OTL EVENTS HAPPENED

**CRITICAL:** Many major OTL events from July 1863 onward **NEVER HAPPEN** in NTL.

### Category 1: Definitely Never Happen (95-100% certainty)

**Military Events That Never Happen:**
- Gettysburg Days 2-3 (Pickett's Charge, Little Round Top)
- Overland Campaign (Wilderness, Spotsylvania, Cold Harbor)
- Siege of Petersburg (June 1864-April 1865)
- Sheridan's Shenandoah Valley Campaign (Aug-Oct 1864)
- Sherman's March to the Sea (Nov-Dec 1864)
- Hood's Tennessee Campaign (Nov-Dec 1864)
- Carolinas Campaign (Feb-March 1865)
- Fall of Petersburg/Richmond (April 1865)
- Lee's surrender at Appomattox (April 9, 1865)

**Political Events That Never Happen:**
- Lincoln's re-election (Nov 1864) - McClellan wins instead
- Lincoln's Second Inaugural (March 4, 1865) - McClellan inaugurated
- 13th Amendment passes (Jan 1865) - no Union victory
- Hampton Roads Peace Conference
- **Entire Reconstruction Era (1865-1877)** - Freedmen's Bureau, Black Codes, 14th/15th Amendments, Reconstruction Acts, KKK (1st) formation as OTL, Impeachment of Johnson, Compromise of 1877

**Leadership Changes That Never Happen:**
- Grant promoted to General-in-Chief (stays Western commander)
- Sheridan commands Cavalry Corps East
- Meade subordinated to Grant

**Social/Cultural Events That Never Happen:**
- OTL Reconstruction (no "original sin → salvation" narrative)
- OTL KKK (Night Riders are different - crushed 1877-1880, no second KKK)
- OTL Jim Crow (racism exists but burns out differently, economically/regionally)
- 2025-style "woke" politics (never forms - see Cultural section)

### Category 2: Likely Still Happen (75-90% certainty)

**Western Theater:**
- Vicksburg surrender (July 4, 1863) - reduced morale impact without "twin victory"
- Chickamauga/Chattanooga (Sept-Nov 1863)
- Grant promoted to Western command (Oct 1863) - based on Vicksburg
- Red River Campaign (March-May 1864) - fails as OTL
- Battle of Mobile Bay (Aug 1864)

**Political/Social:**
- New York Draft Riots (July 13-16, 1863) - **WORSE** in NTL (~1,500-1,800 casualties vs. OTL ~1,200)
- Andersonville Prison opens

### Category 3: Explicitly Different Outcomes

**Atlanta Campaign:**
- Starts May 1864 (same as OTL)
- Sherman reaches suburbs Aug 1864 (similar to OTL)
- **Becomes 4-month siege, NEVER FALLS** (Sherman withdraws Jan 1865)
- Hood replaces Johnston (July 17, 1864) for different reasons

**Sherman's Campaigns:**
- **No March to the Sea** (war ends before it can happen)
- **Instead: March to Appomattox** (Jan-Feb 1865) - weather defeats him, arrives too late

**Key Point:** Always check `world-building/reference/otl-events-never-happen.md` before assuming OTL events occurred.

---

## MAJOR TREATIES

### Treaty of Cincinnati (March 31, 1865) - PERMANENT LOCK

**Key Articles:**
- USA recognizes CSA as sovereign and independent
- **Borders:** 11 seceded states + Tennessee (**West Virginia stays USA - LOCKED**)
- **Native super-states recognized** (Article 4 - Five Civilized Tribes + Plains nations)
- **Mormon Deseret recognized** (Article 7 - sovereign theocracy)
- **Border States:** Kentucky and Missouri remain USA but neutral (no garrisons within 50 mi of Ohio River)
- **Slavery:** Status quo ante bellum (legal in CSA, illegal in USA)
- **Military:** Armies reduced to 25,000 each within 18 months
- **Trade:** Most-favored-nation status (violated by USA with 300% tariffs after Toombs Act 1868)

**Signed by:** McClellan (USA), Jefferson Davis (CSA) at Burnet House, Cincinnati, 3pm, March 31, 1865.

**Lincoln:** Never signs (loses election, lame-duck, treaty signed after he leaves office).

**Post-Treaty Border Modification:**
- **1873 Panhandle Accord:** Eastern panhandle counties (Jefferson, Berkeley, Morgan) return to CSA/Virginia after 1870-1873 revolt against USA control. USA concedes for stability — counties rejoin CSA but remain alienated zone (localist, weak Richmond control). This modification does not change West Virginia's status as USA state (counties were exception due to crisis).

### Treaty of San Francisco (February 14, 1873)
- California secedes peacefully
- **Capital:** San Francisco (not Sacramento)
- USA keeps military bases under 99-year lease

### American Concord Treaty (1919)
- **Four nations:** USA, CSA, California, Texas
- Permanent seat: Monterey, California (neutral youngest sibling's territory)
- Framework for cooperation without forcing unity
- **Texas joins because:** Zimmerman Telegram (1917) threatens Texas directly (Mexico offered "get Texas back")
- **Family dynamic:** USA (oldest), CSA (middle), California (youngest), Texas (roommate who left CSA, came back for Thanksgiving)

**Quartet Symbolism – Three-Plus-One:**
- **No four-flag symbol exists** – Texas refuses all shared symbols that include CSA
- Tri-Flag Concord Badge stays three flags (USA-CSA-California)
- Texas flag flown separately at summits – equal size, equal height, physically apart
- Protocol: "The Concord Triad with the Republic of Texas in association"
- Joint statements: Texas signs last (by its own insistence)
- **See:** `world-building/political/quartet-symbolism-three-plus-one.md`

---

## POLITICAL SYSTEMS

### United States
- **1864:** McClellan elected on peace platform
- **1865-1880:** Republican Party collapses ("lost on purpose")
- **1896:** Democratic Party collapses ("But, Tennessee?" + Great Cotton Fraud)
- **By 1900:** Neither "Republican" nor "Democratic" parties exist
- **Current Names (LOCKED):**
  - **Constitutional Unity Party** (ex-Republicans) → street name "Minutemen"
  - **National Union Party** (ex-Democrats) → street name "Sunshiners"

**Key Presidents:**
- McClellan (1865-1869): Signs treaty, "the man who lost the war"
- Hancock (1889-1890): War hero, dies from old Gettysburg wound
- Theodore Roosevelt (1893-1901): First CUP president
- FDR (1933-1939+): New Deal, Economic Concord

**See:** `world-building/political/presidents-and-parties.md` (USA), `world-building/political/csa-presidents-gentry-vs-hayseed-1865-1939.md` (CSA), `world-building/political/ca-political-system-and-presidents.md` (California) for full lists.

### Confederate States
- **Planters' Democratic Party (Gentry):** Dominant 1865-1890, comeback 1910-1939
- **Farmers' & Labor Alliance (Hayseed):** Surge 1890-1910, resurgence 1925-1939

**Key Presidents:**
- Robert Toombs (1867-1871): Signs Toombs Act (Dec 1867) → global boycott (1868)
- Thomas E. Watson (1896-1902): First Hayseed president
- Huey P. Long (1926-1932): "The Kingfish," Share Our Wealth
- Theodore G. Bilbo (1938-1944): Hard-right backlash (still president 1939)

**See:** `world-building/political/presidents-and-parties.md` (USA), `world-building/political/csa-presidents-gentry-vs-hayseed-1865-1939.md` (CSA), `world-building/political/ca-political-system-and-presidents.md` (California) for full lists.

### California
- **Pacific Republican Party (PRP):** Dominant 1873-1939 (permanent ruling party)
- **Factions:** Globalist (coastal, pro-trade) vs. Nationalist (interior, protectionist)
- **Character:** Pragmatic, business-first (NOT moralistic)

**Key Presidents:**
- Leland Stanford (1873-1879): Makes California a republic
- William Randolph Hearst (1897-1903): Press-lord president
- Florence Collins Porter (1909-1915): First woman president in North America

**See:** `world-building/political/presidents-and-parties.md` (USA), `world-building/political/csa-presidents-gentry-vs-hayseed-1865-1939.md` (CSA), `world-building/political/ca-political-system-and-presidents.md` (California) for full lists.

### Texas (Independent 1877)
- **Republic of Texas:** Independent nation since April 1877 (Treaty of Houston)
- **Character:** Jacksonian populist defiance - "Texas First, Texas Forever"
- **Personality:** Loud, proud, grudge-holding. Profit matters, but pride and principle matter more.
- **Key trait:** Eternal grudges (vs. California's pragmatic memory-wipe)

**Quartet Relations:**
- **USA:** Strategic ally (best terms, military partnership vs. Mexico)
- **California:** Rival with respect (oil competition, style clash at Quartet meetings)
- **CSA:** Eternal grudge (cold contempt, bare minimum cooperation, spite-driven economics)
- **Mexico:** Defining hostile enemy (chronic low-intensity border war, identity partly defined against Mexico)

**Texas Military Institute (TMI) – Founded 1885:**
- Texas does NOT join Appomattox College (that's USA-CSA reconciliation, not Texas's war)
- TMI founded 24 years before Appomattox (1885 vs. 1909) – "We already have our own school"
- Focus: Mexico border defense, oil infrastructure, Gulf security
- Tri-Flag Concord Badge stays tri-flag (USA-CSA-California) – Texas not included, doesn't want to be

**See:** `world-building/political/texas-independence-1877.md`, `world-building/political/texas-personality-quartet-relations.md`, `world-building/military/texas-military-institute-1885.md`

### Sequoyah
- Cherokee National Party vs. Keetoowah Progressive (main divide)

---

## SLAVERY TIMELINE - LOCKED CANON

**Core Thesis:** Slavery dies of **economics**, not morality. No Northern victory, no "we saved you" narrative.

**Key Dates:**
- **1867:** Toombs Act reopens African slave trade
- **1868:** Global boycott triggered (Britain, France)
- **1865-1894:** Four Horsemen of Slavery's Apocalypse kill slavery (Raid + Boycott + Glut + Shame)
- **1894:** "The Last Chain Falls" - slavery dies in practice
- **1894-1905:** "Zombie decade" - legally lingers on paper
- **1898:** Cuba Mirror Effect - photos of Weyler's camps shame CSA
- **1905:** Final legal abolition (constitutional convention)

**Northern Raids (1865-1894):**
- **Phase 1 (1865-1867):** Organized cells (~50 major raids, "The Committee of Nine")
- **July 1867:** Joint USA-CSA Border Pacification Act signed
- **1867-1869:** Organized cells crushed (ice-cold joint USA-CSA cooperation)
- **Phase 2 (1867-1894):** Decentralized/viral raids (300-400 total)
  - 1867-1875: 40-60 raids (5-7/year) - High suppression
  - 1875-1885: 150-200 raids (15-20/year) - Viral spread, moderate suppression, **planter flight begins, raiders follow**
  - 1885-1894: 110-140 raids (12-15/year) - Routine suppression, **geographic spread complete**
- **Total (1865-1894): 350-450 raids**
- **Total Impact:** $1.6B damage, 200k slaves escape to Sequoyah

**Planter Adaptive Responses:**
- **Geographic Flight (1870s-1880s):** Planters move south to escape → Raiders create new chapters closer → NOT successful
- **Crop Diversification (1875-1890):** Planters switch from cotton to tobacco/sugar/rice → Raiders adapt targets → NOT successful
- **Complete Manumission (1865-1894):** Planters free all slaves → Raiders honor it, stop targeting → **ONLY successful strategy**
- **The Renege Problem:** If planter reneges (re-enslaves or imports new slaves), raiders return with escalated retaliation (house burning allowed, but still no killing/harming)
- **The "Accidental" Renege Problem:** Some planters free slaves and offer paid work; freed slaves stay on familiar land. Pure probability = messages get crossed, raiders may mistake for renege → tragic misunderstandings (rare but inevitable)
- **Combined Cost of Failed Strategies:** ~$80M, $0 benefit - accelerates economic death
- **Manumission Result:** Only path to stability - creates economic incentive to free slaves

**Key Raids/Events:**
- May 1865: "Burning of the Black Belt" (27 plantations, Alabama)
- April 14-17, 1866: Pettigrew Raid (rogue cell breaks rules, self-policed by raiders)
- April 22, 1866: "Court-Martial in the Pines" (Kane and 12 lieutenants hanged by own movement)
- April 12, 1868: Battle of Red River Ford (400 raiders vs. 600 joint troops, 341 killed)

**Rules of Engagement (LOCKED):** Burn crops/infrastructure, free slaves, spare main houses/families, no assassinations. Violators executed by their own movement (Pettigrew Raid). **Renege Exception:** If planter reneges on manumission (re-enslaves or imports new slaves), raiders may burn the plantation house as escalation, but still no killing/harming slavers or family.

**See:** `world-building/economic/slavery-and-raids-master.md` for detailed narratives, `analysis/economic/slavery-death-mechanics-analysis-2025-12-05.md` for four-mechanism economic analysis.

---

## CALIFORNIA INDEPENDENCE

**Timeline:**
- **1872:** Great Native Toll War (Jan-May)
- **Nov 5, 1872:** Independence referendum (69% YES) - "Well if they can do it, so can we" (CSA precedent)
- **Feb 14, 1873:** Treaty of San Francisco signed
- **July 4, 1873:** Republic of California fully sovereign
- **First President:** Leland Stanford (1873-1879) - elected AFTER independence, first president of new republic
- **Capital:** San Francisco (not Sacramento)
- **Why US lets it happen:** No moral foundation (just recognized CSA secession) and no military might (exhausted, no army within 1,500 miles)
- **1875-1876:** California purchases Alaska from Russia (USA blockade fails)
- **1894-1907:** Pacific Alliance forms (quietly absorbs Oregon/Washington economies)

**Character:** Pragmatic, business-first, "youngest sibling who moved out early and got rich." NOT moralistic.

**California-Japan Relationship (LOCKED):**
- Central to California's Pacific power identity
- Japanese aphorism: "California is greedy, but it is honest greed"
- 1937: California supplies 55% of Japan's oil at +25% markup
- 1939: Japanese assessment: "Could we fight California? Only if we wish to lose the war before it begins"
- **Mutual assured profit** - most stable relationship on planet

**Pacific Alliance Structure:**
- Oregon & Washington: NOT U.S. states - California aggressively lobbies (bribes) them into either not pursuing statehood or seceding. California invests ~$1.8B (1873-1907) to secure their accession to Pacific Alliance as independent entities
- Formal: Three equal votes on paper
- Reality: California pays 70%, controls effectively

**Alaska:**
- Purchased 1875, transferred July 4, 1876
- Renamed: District/Territory of Alyeska
- Capital: Bearfort (ex-Sitka)

**See:** `world-building/california/ca-japan-relationship.md`, `world-building/california/ca-diplomacy.md` (writer's reference - "Pacific Venice" mental model).

---

## NATIVE SUPER-STATES & MORMON DESERET

### Native Super-States (LOCKED)
- Recognized in Treaty of Cincinnati Article 4 (1865)
- **Primary motivation (private):** Mutual territorial denial — "If we cannot have it now, neither can you" (84-88%)
- **Public rationale:** Neutral western buffer + moral restitution (80-83%)
- Five Civilized Tribes + Plains nations as sovereign republics
- **Sequoyah:** Independent Native state (Cherokee core, thrives)
- **Plains Nations:** Fragment by 1900 (constant diplomacy, USA/CSA mutual deterrence)
- **Buffer states** between USA and CSA (in practice, though denial was primary driver)
- **No transcontinental land bridge** - California physically cut off

**Reality:** Embattled survivors, not superpowers. Sequoyah succeeds on Cherokee institutional core.

**Attitude toward Big Three condescension:** Pragmatic tolerance with quiet amusement/resentment — public deference + private subversion. Three flavors: USA (protection), CSA (civilization), California (partnership - most insufferable). Spectrum: Sequoyah (most pragmatic) → Deseret (most detached) → Plains nations (most resentful). Cherokee "minor treaties" network (1870s-1939+) exploits Article 4 loopholes through "malicious compliance." **See:** `world-building/regions/native-super-states-attitudes.md` for full framework.

**See:** `archive/world-building/regions/native-super-states-embattled-survivors.md` for detailed analysis of Article 4 motivations

### Mormon Deseret (LOCKED)
- Recognized in Treaty of Cincinnati Article 7 (1865)
- **Sovereign theocracy** - "Leave us alone and we'll leave you alone"
- **Borders:** Utah + southern Nevada + slices of AZ/CO/ID
- **Why it survives:** USA and CSA terrified of another Mormon War, Brigham Young commands 15k armed men
- **1890-1920:** Becomes "Mormon Venice of North America" (officially called this in-world)
- **Banking neutrality:** Commodity-backed, religiously obsessive honesty, armed neutrality
- Holds Concord Treaty deposits, USA/CSA/California accounts

**See:** `world-building/regions/mormon-deseret-banking-neutrality.md`

### Transcontinental Rails (LOCKED)
- **No rail through Native territories**
- USA: Northern route through Canada (Chicago-Vancouver, 1885)
- CSA: Southern route through Mexico (New Orleans-Guaymas, 1890)
- Both longer, costlier → explains California's Pacific port dominance

**See:** `world-building/economic/transcontinental-rail-routes-bypass.md`

---

## KEY CHARACTERS/FAMILIES

### Haskell Family (Northern Witnesses)
- **Gen 0:** Frank A. Haskell (Union officer at Gettysburg)
- Purpose: Northern witnesses to war and aftermath
- Note: NOT the Meade family (too confusing with General Meade)

### Fairfax Family (Southern Witnesses)
- Purpose: Southern witnesses to war and aftermath
- Samantha Meade: Marries Thomas Fairfax (witness through marriage)

### Lincoln's Fate (LOCKED)
- **Nov 1864:** Loses election to McClellan
- **March 4, 1865:** McClellan inaugurated, Lincoln lame-duck for 27 days
- **March 31, 1865:** Treaty signed by McClellan (Lincoln never signs)
- **March 2, 1865:** Lincoln's last public act - farewell address: "The people have chosen peace. I pray it is the peace that heals, and not the peace that merely postpones the reckoning."
- **Result:** Boards train to Springfield, never speaks publicly about war again

### Patrick Cleburne (The Martyred Prophet)
- **February 28, 1864:** Cashiered by Jefferson Davis for proposing to free and arm slaves (military pragmatism, not moral abolition)
- **Post-war role:** Civilian activist, border witness (1870-1894), documents slavery's economic death firsthand
- **Legacy:** "The Martyred Prophet" - predicted slavery's economic death in 1864, vindicated when it happens (1894 practice, 1905 legal)
- **Key quote:** "I was right. It cost me everything, but I was right."
- **Status:** Primary source for understanding Confederate internal debates on slavery's economic unsustainability

**See:** `characters/confederate/patrick-cleburne.md` for full character profile, `analysis/political/cleburne-cashiering-martyred-prophet-2025-12-15.md` for detailed analysis of his cashiering and post-war role.

### Compendium Characters (Meta-Layer)
- **Dr. General Michael J. Fairfax-Lockwood:** Satirical author (1920s-1986), "Fire and Sovereignty" (1985)
- **Staff:** Kronvoldt (G.R.O.K.), Auto (A.U.T.O.), Claudette (C.B.O.)
- **Sacred Typewriter Clause:** AI never edits `/books/`, only suggests in `/edits/` (Golden Rule in 1985 diegetic form)

**See:** `world-building/meta/compendium-concept.md` for compendium structure, `characters/staffers/dr-general-michael-j-lockwood.md` for Dr. General Fairfax-Lockwood, `characters/staffers/gervais-rogerus-oscar-kronvoldt.md` for Kronvoldt, `characters/staffers/auto-the-assistant.md` for Auto, `characters/staffers/claudette-beatrice-oswald.md` for Claudette.

---

## ECONOMIC SYSTEMS

- **Global cotton glut (1880s):** Makes slavery unprofitable
- **Punitive tariffs (1868-1905):** USA imposes 300% tariffs after Toombs Act (violates Treaty Article 8)
- **California oil economics:** Revenue for permanent infrastructure control
- **Great Depression (1929):** Still happens (timing/severity may differ)

---

## MILITARY STRENGTH (1939)

**Ranking:**
1. **California:** Best navy, richest economy, no continental threats (200k + world-class blue-water navy)
2. **USA (East):** Largest army, industrial base (220k)
3. **Texas:** Oil wealth, fortified Rio Grande border, strong army for size (~120k) - permanent war footing vs. Mexico
4. **CSA:** Solid army, geographically boxed in, oil-dependent on Texas (~180k)

**Key Point:** California can project power to Asia; others can't. Nobody can fight war longer than 6 months without California's and Texas's oil.

---

## CULTURAL/SOCIAL

### No "Woke" Politics by 2025 (LOCKED - 96%)

**Five Killer Blows:**
1. No single moral superpower (three exhausted, mutually cancelling nations)
2. No "original sin → salvation" narrative (slavery dies of economics, not Northern victory)
3. No KKK/Jim Crow legacy (Night Riders crushed 1877-1880, no second KKK)
4. No 1960s generational explosion (no Vietnam, no civil rights victory)
5. California as sovereign nation (not academic factory - laughs at moral philosophy)

**Result:** No 2025-style "woke" politics ever forms. Racism exists but burns out differently, regionally, economically.

### Civil Rights Timeline (1920s-1950s) - LOCKED

**Why civil rights comes EARLIER in NTL:**
1. **No Lost Cause Mythology:** CSA wins → no "noble cause" myth → no cultural investment in racial hierarchy
2. **No Northern Saints Narrative:** North loses → no moral high ground → no "we freed you" hypocrisy
3. **Three-Nation Competition:** USA/CSA/California competing for labor → can't afford to exclude talent
4. **Cuba Mirror Effect Foundation (1905):** Courts hypersensitive to government-mandated discrimination

**Timeline:**
- **California (1920s):** Anti-discrimination legislation - "Can't afford to waste talent on stupid prejudices" (pure pragmatism, NOT moral crusade) - Plausibility 92%
- **USA (1930s-40s):** Federal civil rights acts - easier without Southern bloc filibuster - "California's eating our lunch" - Plausibility 88%
- **CSA (1940s-50s):** Urban integration, grudging federal legislation - Cuba Mirror precedent enables change - Plausibility 85%

**Key Mechanism:** Youngest sibling (California) shames older brothers through **making more money**, not moral lectures. Legal equality (negative rights - no barriers), NOT enforced outcomes (no quotas/mandates).

**NTL Pattern:** Legal equality (1920s-50s) → economic integration → done, next problem
**OTL Avoided:** Legal discrimination → Civil Rights Act → affirmative action → DEI industry → backlash

**See:** `world-building/cultural/civil-rights-timeline-1920s-1950s.md` for detailed breakdown.

### American vs. European Anti-Semitism (LOCKED)

**American Spectrum (1939):**
- **California:** 7/10 tolerance (pragmatic meritocracy)
- **USA:** 6/10 (casual prejudice, country club exclusions, no pogroms)
- **CSA:** 5.5/10 (preoccupied with Black/white dynamics, Jews mostly ignored)

**European Spectrum (1939):**
- **Kaiserreich Germany:** 2/10 (institutional discrimination)
- **Stalin's USSR:** 1/10 (active persecution)
- **Poland:** 3/10 (traditional pogroms)

**Key Differences:**
- **American:** NO official quotas/restrictions (post-Cuba Mirror courts strike down government discrimination)
- **European:** Official discrimination continues unbroken (no Holocaust shock to stop it)
- **American fade mechanism:** Economic integration → intermarriage → pragmatic burnout → indifference (NOT activism)

**See:** `world-building/cultural/american-antisemitism-vs-european.md` for detailed analysis.

### Racial Dynamics Spectrum (1939 Reference)

**Foundational measurement document:** `world-building/cultural/racial-dynamics-spectrum-1939.md`

Racial equality spectrum across North American shards (1-10 scale, where 10 = utopian meritocracy):
- **California:** 8.5-9.0 (pragmatic meritocracy, "honest greed")
- **USA:** 7.0-7.5 (middling tolerance, no slavery baggage)
- **CSA:** 6.5-7.0 (urban 7.5, rural 5.5-6.0; slow progress, no Jim Crow)
- **Sequoyah:** 6.5-7.0 (pragmatic integration, internal tensions)
- **Plains Nations:** 5.0-6.0 (survival-mode insularity)
- **Mormon Deseret:** 5.5-6.5 (religious hierarchy, commercial tolerance)

**Key insight:** NTL's average (~7.5-8.0 weighted) may exceed OTL 1939 USA due to fragmentation and pragmatic burnout. Highest equality (California) is amoral meritocracy; racism fades where unprofitable, not through moral crusades.

**Related institutional elements:** Appomattox College annexes (1910-1934) — five empirical observatories tracking continental patterns:
- **Institute of Racial Dynamics (1928):** Racial Equality Index (REI)
- **Institute for Border Friction Metrics (1910/1918):** Tick/Tock clocks (internal vs. global threats). Tick clock inspired by Panhandle Crisis (1870-1873) — eastern panhandle counties ("Port Royal of Appalachia") revolt, nearly spark renewed war, returned to CSA/Virginia via 1873 Panhandle Accord. **See:** `world-building/regions/panhandle-crisis-1870-1873.md` for full details
- **Institute of Economic Concordance (1931):** Trade interdependence tracking
- **Institute for Historical Reconciliation Metrics (1926):** Memory divergence analysis
- **Institute of Demographic Drift (1934):** Population mixing metrics

All housed in Institute Hall with iconic Tick/Tock clocks flanking entrance. See `world-building/institutions/appomattox-college-annexes-overview.md` for comprehensive documentation.

### Other Cultural Notes
- **Kawaii Kaiju Tourism Campaign:** California-Japan joint board (1956+), Godzilla/Mothra ads, Oakland "0 days since" sign (68% plausibility - kept because fun)

---

## KEY GEOGRAPHIC FACTS

- **USA:** North and West (excluding California and Native territories)
- **CSA:** 11 seceded states + Tennessee (**West Virginia stays USA - LOCKED**)
- **CSA Western Boundary:** 100th meridian
- **Border States:** Kentucky and Missouri remain USA but neutral (no garrisons within 50 mi of Ohio River)
- **California:** Independent republic (1873+)
- **Native Super-States:** Sovereign buffer states
- **Mormon Deseret:** Sovereign theocracy
- **No transcontinental land bridge:** California physically cut off from USA

---

## BOOK STRUCTURE

- **Book 1: The Match (1863-1865)** - War ends (~21 months)
  - **Act 1:** Invasion (July 1863 - early August 1863) - Longstreet's Pennsylvania campaign
  - **Act 2:** Warren's Meat-Grinder (August 1863 - December 1863) - Rappahannock-Rapidan campaign collapse
  - **Act 3:** Pickett's Raid to Election (Spring 1864 - November 1864) - Pickett's Raid, Winter of Despair, McClellan elected
  - **Act 4:** Grant's Gamble and Treaty (Late 1864 - March 1865) - Grant's Final Gamble, Appomattox defeat, Treaty of Cincinnati
- **Book 2: The Flare (1865-1877)** - The hottest burn (~12 years) - Organized raids, Toombs Act, boycott, California secession, Texas independence, Night Riders crushed
- **Book 3: The Fire (1878-1894)** - The sustained burn (~17 years) - Viral raids, cotton glut, slavery dies in practice
- **Book 4: The Embers (1895-1905)** - Flickering out (~11 years) - Zombie decade, Cuba Mirror Effect, legal abolition
- **Book 5: The Quenching (1906-1919)** - Everything calms down (~14 years) - Trade normalization, WWI, American Concord Treaty
- **Book 6: The Ashes (1920-1939)** - Living in the aftermath (~20 years) - Depression, Europe burns again

---

## THEMATIC FRAMEWORK

### Core Premise (LOCKED)
- **Gettysburg was the battle the Confederacy could not afford to fight and the Union could not afford to lose**
- **Lee's death saves the South from its own victory disease and condemns the North to lose a war it was morally right to win**
- **This is the cold, ugly, historically honest foundation of the entire series**

### Thematic Balance (LOCKED)
- **"Everyone is wrong"** - No side purely good or evil
- **Slavery dies of economics, not morality** - No Northern victory, no "we saved you" narrative
- **Scaffolding vs. Payload** - Constitutional question (scaffolding) survives, but original payload (slavery) too toxic to live
- **The war was morally right to win, but the North loses** - Creates central tension

---

## CRITICAL "DO NOT" RULES

1. **DO NOT** edit files in `books/` folder directly
2. **DO NOT** create original story text without explicit request
3. **DO NOT** assume OTL outcomes (check Negative Assumptions section)
4. **DO NOT** forget slavery dies of **economics**, not morality
5. **DO NOT** forget California is **pragmatic**, not moralistic
6. **DO NOT** forget the North **lost** - no "we saved you" narrative
7. **DO NOT** forget Lincoln **never signs treaty** (loses election, McClellan signs)
8. **DO NOT** forget West Virginia **stays USA** (LOCKED) — note: 1873 Panhandle Accord returned eastern panhandle counties (Jefferson, Berkeley, Morgan) to CSA/Virginia as post-Treaty modification after crisis ("Port Royal of Appalachia" — smuggling hub, alienated zone), but West Virginia remains USA state. **See:** `world-building/regions/panhandle-crisis-1870-1873.md` for full details.
9. **DO NOT** forget Mormon Deseret **sovereign theocracy** (Article 7)
10. **DO NOT** forget Northern Collapse sequence is **LOCKED** - no heroic last stands
11. **DO NOT** assume Grant becomes general-in-chief (never promoted)
12. **DO NOT** assume Atlanta falls (besieged but never falls)
13. **DO NOT** assume Sherman's March to the Sea happens (war ends first)
14. **DO NOT** assume Hancock's wounding is CSA setback (it's CSA victory)
15. **DO NOT** assume OTL Reconstruction happens (entirely different post-war period)
16. **DO NOT** commit or push changes unless explicitly requested by user
17. **DO NOT** assume Warren commands V Corps at Appomattox (Griffin replaced him Jan 1, 1864)

---

## QUICK REFERENCE: PLAUSIBILITY SCORES

**90-100% (Locked):**
- Lee dies of heart attack (94%)
- Longstreet countermarches north (92%)
- McClellan signs treaty (95%)
- No "woke" politics by 2025 (96%)

**80-89% (Safe Default):**
- Northern Collapse events (88-92%)
- Atlanta Campaign ambiguous outcome (87%)
- Sherman's March to Appomattox (94%)

**70-79% (Green Flag - Justified):**
- Native super-states as embattled survivors (72-75%)
- Mormon Deseret banking neutrality (75%)
- Night Riders crushed economically (78-80%)

---

## RECENT MAJOR CANON LOCKS (December 2025)

**December 20, 2025 Updates:**
1. **Rappahannock-Rapidan Campaign Timeline:** Refined to 15-day campaign (Aug 25-Sep 9, 1863) with three phases ending in army cohesion collapse at Germanna (Phase 1: Rappahannock crossings Aug 25-29, Phase 2: Fighting withdrawal Aug 30-Sep 2, Phase 3: Rapidan assaults & final collapse Sep 3-9). Phase 4 Raccoon Ford diversion eliminated. Hood's rest shortened (3 days + quiet sector rotation). Casualties: Union ~42,000, Confederate ~16,500 (2.5:1 ratio). Plausibility 82-85%. — See `archive/world-building/timelines/rappahannock-rapidan-campaign-1863.md`
2. **Book 1 Four-Act Structure:** Confirmed structure — Act 1: Invasion, Act 2: Warren's Meat-Grinder, Act 3: Pickett's Raid to Election, Act 4: Grant's Gamble and Treaty — See `books/book-01-the-match/ACT-STRUCTURE-SUMMARY.md` and act outline documents

**December 17-19, 2025 Updates:**
1. **Meade's 36-Hour Delay Analysis:** Comprehensive hour-by-hour breakdown showing structural minimum delay (4-6 hours), Meade's actual delay (~30.5 hours), and Longstreet's telegraph strategy (open lines July 3-9, cut July 9) — See `analysis/military/meade-36-hour-delay-telegraph-strategy-2025-12-17.md` (88-92%)

**December 10-15, 2025 Updates:**
1. **Grant's Final Gamble:** Charles Griffin commands V Corps (Warren relieved Jan 1, 1864), battle dates Feb 18-20, 1865, rational decisions framework (92%)
2. **Harrisburg Occupation:** Battle of Camp Hill (July 5, 1863), Quaker gun deception, gradual east-bank shift (92-94%)
3. **Pickett's Raid:** Carlisle as strategic objective, Field's division destroyed at Carlisle, Kershaw saves withdrawal (91-92%)
4. **Patrick Cleburne:** Character locked — cashiered Feb 28, 1864 for proposing to free/arm slaves, becomes "Martyred Prophet" documenting slavery's economic death (90-92%)
5. **Git Operations Rule:** AI never commits/pushes unless explicitly requested

**December 9, 2025 - Six elements locked after external peer review:**
1. **Native super-states:** Embattled survivors (not superpowers) - Sequoyah thrives, Plains nations fragment
2. **Mormon Deseret:** Banking neutrality ("Mormon Venice of North America")
3. **Transcontinental rails:** Bypass Native territories (USA via Canada, CSA via Mexico)
4. **WWI Zimmerman Crisis:** Germany offers CSA Kentucky/Missouri, telegram leaked, armed neutrality
5. **Alaska Purchase:** USA blockade fails (1875) - reinforces post-war weakness
6. **Second KKK suppression:** Economic motive (boycott extension threat)

**Overall framework plausibility raised from 85-90% to 88-92%.**

**See:** Individual files: `world-building/regions/native-super-states-embattled-survivors.md`, `world-building/regions/mormon-deseret-banking-neutrality.md`, `world-building/economic/transcontinental-rail-routes-bypass.md`, `world-building/military/wwi-duration-zimmerman-crisis-explicit-chapter.md`, `world-building/california/alaska-purchase-1875-1876.md`, `world-building/economic/second-kkk-suppression-economic-motive.md` for detailed analysis of each fix.

---

## WHEN IN DOUBT

1. **Check plausibility:** Is this decision ≥70% plausible?
2. **Check process:** Am I editing `books/` folder? (If yes, STOP - use `edits/`)
3. **Check canon:** Does this contradict locked facts?
4. **Check negative assumptions:** Am I assuming OTL events happened? (Check list above)
5. **Check timeline:** Does this fit chronological sequence?
6. **Check character:** Does this fit established character/system?
7. **Check honesty:** Am I making something up? (If yes, STOP - admit you don't know)

**If you don't know something:**
- Say "I don't have that information in my context"
- Offer to check canon documents in `/world-building/`
- Ask user for clarification
- **DO NOT** invent details to fill gaps

**The user will explicitly ask when they want you to create/invent something. Until then: Be honest about what you don't know.**

---

## WHERE TO FIND MORE

**Note:** See "File Access Limitations" section above for information about accessing these repository files. Only Auto (Cursor) can read them directly; other AIs must request content from the user.

**Detailed Documentation (Git Repository Paths):**
- **Locked Timelines:** `/world-building/timelines/` (locked canon timelines)
- **Analysis Documents:** `/analysis/` (working analyses organized by category)
  - Military: `/analysis/military/` (Northern Collapse, Grant's Gamble, Atlanta Campaign, Sherman's March)
  - Economic: `/analysis/economic/` (Slavery Death Mechanics, Depression, Roaring Twenties)
  - Political: `/analysis/political/` (Presidential analyses, Treaty analyses)
  - Consistency: `/analysis/consistency/` (Consistency checks, plausibility audits)
  - OTL Divergence: `/analysis/otl-divergence/` (OTL vs NTL comparisons)
- **World-Building:** `/world-building/` (locked canon documents)
- **Slavery & Raids:** `/world-building/economic/slavery-and-raids-master.md`
- USA Presidents: `/world-building/political/presidents-and-parties.md`
- CSA Presidents: `/world-building/political/csa-presidents-gentry-vs-hayseed-1865-1939.md`
- California Presidents: `/world-building/political/ca-political-system-and-presidents.md`
- Native States: `/world-building/regions/native-super-states-embattled-survivors.md`
- Mormon Deseret: `/world-building/regions/mormon-deseret-banking-neutrality.md`
- Transcontinental Rails: `/world-building/economic/transcontinental-rail-routes-bypass.md`
- California-Japan: `/world-building/california/ca-japan-relationship.md`
- California Diplomacy: `/world-building/california/ca-diplomacy.md`
- Compendium Concept: `/world-building/meta/compendium-concept.md`
- Compendium Characters: `/characters/staffers/dr-general-michael-j-lockwood.md`, `/characters/staffers/gervais-rogerus-oscar-kronvoldt.md`, `/characters/staffers/auto-the-assistant.md`, `/characters/staffers/claudette-beatrice-oswald.md`
- OTL Events: `/world-building/reference/otl-events-never-happen.md`
- Claude Review Fixes: Individual files in `/world-building/` subfolders (regions/native-super-states-embattled-survivors.md, regions/mormon-deseret-banking-neutrality.md, economic/transcontinental-rail-routes-bypass.md, military/wwi-duration-zimmerman-crisis-explicit-chapter.md, california/alaska-purchase-1875-1876.md, economic/second-kkk-suppression-economic-motive.md)
- **Canon Master Document:** `/canon-master-document.md` (comprehensive detailed version with all narratives)
- **AI Rules:** `/ai-rules/` (golden-rule-no-original-text.md, hash-consistency-tracking.md, git-operations-explicit-request.md)
- **Tools:** `/tools/` (wargaming-simulation-template.md, battle-simulation-template.md, rate limit monitoring scripts)
- **Meade 36-Hour Delay & Telegraph Strategy:** `/analysis/military/meade-36-hour-delay-telegraph-strategy-2025-12-17.md` (Meade's 36-hour delay & Longstreet telegraph strategy; hour-by-hour analysis)
- **Harrisburg Occupation:** `/archive/world-building/timelines/pod-campaign/part-02-harrisburg-occupation.md` (Battle of Camp Hill, Quaker guns, gradual shift)
- **Grant's Final Gamble:** `/analysis/military/grant-gamble-canon-update-2025-12-10.md` (Griffin replaces Warren, Feb 18-20, 1865)
- **Pickett's Raid:** `/world-building-master/pickett-raid-canonical-timeline-2025-12-10.md` (Carlisle objective, Field's destruction)
- **Battle of York:** `/archive/world-building/military/battle-of-york-1863-07-18.md` (July 18, 1863 — Longstreet's miscalculation, 1-day mobile breakthrough during return march)
- **Book 1 Act Structure:** `/books/book-01-the-match/ACT-STRUCTURE-SUMMARY.md` (four-act structure overview), `/books/book-01-the-match/ACT-1-CLOSING-CHAPTERS-OUTLINE.md` (Act 1 closing chapters), `/books/book-01-the-match/ACT-1-2-TRANSITION-OUTLINE.md` (interludes), `/books/book-01-the-match/ACT-2-OUTLINE.md` (Act 2 Warren era), `/books/book-01-the-match/ACT-2-3-TRANSITION-OUTLINE.md` (investigation interludes)
- **Rappahannock-Rapidan Campaign:** `/archive/world-building/timelines/rappahannock-rapidan-campaign-1863.md` (15-day campaign Aug 25-Sep 9, 1863, three phases ending with army cohesion collapse at Germanna)
- **Maps:** `/maps/` folder contains battle and campaign maps (e.g., `battle-of-york-07-18-1863.png`)
- **Patrick Cleburne:** `/characters/confederate/patrick-cleburne.md` (Character profile), `/analysis/political/cleburne-cashiering-martyred-prophet-2025-12-15.md` (Cashiering analysis and post-war role)
- **Civil Rights Timeline (1920s-1950s):** `/world-building/cultural/civil-rights-timeline-1920s-1950s.md` (California leads, USA/CSA follow)
- **American vs. European Anti-Semitism:** `/world-building/cultural/american-antisemitism-vs-european.md` (Comparative analysis, fade mechanism)
- **European War 1939 Trigger:** `/world-building/military/european-war-1939-trigger.md` (Stalin aggression, NOT Hitler)
- **Racial Dynamics Spectrum (1939):** `/world-building/cultural/racial-dynamics-spectrum-1939.md` (Foundational reference document - measurement/benchmark of racial equality across all North American shards)
- **Appomattox College:** `/archive/world-building/meta/appomattox-college-of-history-and-diplomacy.md` (Joint USA-CSA military-diplomatic academy, 1909-1939+)
- **Appomattox College Annexes:** `/world-building/institutions/appomattox-college-annexes-overview.md` (Master overview of five empirical observatories, 1910-1934)
  - Individual institutes: Border Friction Metrics (Tick/Tock clocks), Racial Dynamics (REI), Economic Concordance, Historical Reconciliation Metrics, Demographic Drift
- **Appomattox Traditions:** The Civil War Football Game (1912+) — continent's premier sporting event with pregame reenactment, "Prisoner Exchange" ritual, War Week traditions (86-89% plausibility)

---

## MAINTENANCE LOG

**Last Updated:** December 29, 2025

**Recent Updates:**
- December 29, 2025: Quartet Symbolism locked — "Three-Plus-One" model. No four-flag symbol exists. Texas refuses shared symbols with CSA. Tri-Flag stays three flags; Texas flag flown separately at summits. Created `world-building/political/quartet-symbolism-three-plus-one.md`.
- December 29, 2025: Texas & Appomattox locked — Texas does NOT join Appomattox College. Texas Military Institute (TMI) founded 1885 (24 years before Appomattox). Tri-Flag Concord Badge stays tri-flag (no Texas). Created `world-building/military/texas-military-institute-1885.md`. Evolution: raw spite (1877-1900) → assertive independence (1900-1919) → dignified maturity (1919-1939).
- December 29, 2025: MAJOR UPDATE — Texas Independence (1877), NTL Cattle Economy, Four-Nation Concord, Texas Personality/Quartet Relations. American Concord now FOUR nations (USA, CSA, California, Texas), not three. Created: `world-building/political/texas-independence-1877.md`, `world-building/economic/ntl-cattle-route-1866-1900.md`, `world-building/regions/fort-smith-cowtown-1866-1900.md`, `world-building/political/texas-personality-quartet-relations.md`. Updated all cross-references.
- December 27, 2025: Nuclear weapons projection added (POST-1939, not in series) — Delayed nuclear era (first detonation 1955-1960), California-Japan consortium likely first developer, USSR follows 2-3 years later. This is an "aiming point" for post-series trajectory. Updated `world-building/military/european-war-1939-trigger.md`.
- December 27, 2025: Book 6 (The Ashes) canon locked — 1939 European War trigger (Stalin's Soviet aggression, NOT Hitler), Civil Rights Timeline (1920s-1950s), American vs. European Anti-Semitism dynamics, Concord-Japan response mechanics. Created new files: `world-building/cultural/civil-rights-timeline-1920s-1950s.md`, `world-building/cultural/american-antisemitism-vs-european.md`, `world-building/military/european-war-1939-trigger.md`. Updated master-timeline.md with final scene details.
- December 27, 2025: Six-book structure adopted — The Match (1863-1865), The Flare (1865-1877), The Fire (1878-1894), The Embers (1895-1905), The Quenching (1906-1919), The Ashes (1920-1939). Metaphor progression: Match → Flare → Fire → Embers → Quenching → Ashes (fire lifecycle). Updated `series-overview.md`, `archive/world-building/timelines/master-timeline.md`, and this document.
- December 21, 2025: Rappahannock-Rapidan campaign route refined — Warren's approach from Warrenton along east bank Rappahannock to Bealeton/Remington, then crossings at Kelly's Ford, Rappahannock Station, Beverly's Ford (OTL Bristoe Campaign alignment). Early locked as Phase 4 counterattack commander.
- December 21, 2025: Matador maneuver extended — Hood's rear guard (~16-18k) conducts ~12-day mobile delaying action down Cumberland Valley (August 7-19) instead of brief static display. Union reinforcements (~30-40k) arrive piecemeal on the march (August 10-18), swelling army to ~110k but diluting quality. Warren concentrates at Warrenton (August 20-24) after exhausting pursuit, then launches premature offensive (August 25).
- December 21, 2025: Refined return march route — Monterey Pass (South Mountain) → Cumberland Valley route locked; Meade's pursuit decision based on mountain-screen calculation; matador split (Hood rear guard, main body south) added as Act 2 opening; Act 1 closes at Potomac crossing (August 6, 1863)
- December 21, 2025: Added Conodoguinet Creek terrain detail to Harrisburg occupation — natural barrier ~3–5 miles west of Susquehanna, channels Union approaches, enhances defensive plausibility
- December 22, 2025: Locked Native super-states attitudes toward Big Three condescension — pragmatic tolerance with quiet amusement/resentment, "malicious compliance" strategy, Cherokee "minor treaties" network (1870s-1939+), three flavors of condescension (USA protection, CSA civilization, California partnership), spectrum of tolerance (Sequoyah → Deseret → Plains nations). Full details: `world-building/regions/native-super-states-attitudes.md`
- December 21, 2025: Created Battle of York canon document (July 18, 1863) — Longstreet's miscalculation during return march, 1-day mobile breakthrough, ~4,500 Confederate/~2,800 Union casualties. Added to `/archive/world-building/military/` and referenced in POD campaign timeline. Battle map available in `/maps/` folder.
- December 20, 2025: Added Panhandle Crisis (1870-1873) as Tick clock inspiration — eastern panhandle counties (Jefferson, Berkeley, Morgan) revolt against USA control, returned to CSA/Virginia via 1873 Panhandle Accord (post-Treaty border modification). Grounds Tick clock symbolism in real crisis.
- December 20, 2025: Refined Tick/Tock clocks symbolism — Tick = internal North American tensions, Tock = global tensions. Added tradition note about cadets reciting "The keg ticks, but we tock" while winding clocks.
- December 22, 2025: Rappahannock-Rapidan Campaign refined to 15 days (Aug 25-Sep 9, 1863) — Phase 4 Raccoon Ford diversion eliminated, campaign ends with army cohesion collapse at Germanna. Hood's rest period shortened (3 days + quiet sector rotation). Casualties adjusted to Union ~42,000, Confederate ~16,500 (2.5:1 ratio). Plausibility 82-85%. "Mature Consideration Farce" acknowledged as historically generous (60-65% plausible) but preserved for narrative.
- December 20, 2025: Refined Rappahannock-Rapidan Campaign timeline with four-phase structure (Oct 10-Nov 8, 1863) and updated Northern Collapse Sequence document accordingly
- December 20, 2025: Confirmed Book 1 four-act structure (Act 1: Invasion, Act 2: Warren's Meat-Grinder, Act 3: Pickett's Raid to Election, Act 4: Grant's Gamble and Treaty), created act outline documents — See `books/book-01-the-match/ACT-STRUCTURE-SUMMARY.md` and related outline documents
- December 19, 2025: Added Appomattox College traditions — The Civil War Football Game (1912+) with pregame reenactment, "Prisoner Exchange" ritual, War Week, and associated campus traditions — controlled tribal venting through sport, continent's premier sporting event (86-89% plausibility)
- December 19, 2025: Created Appomattox College Annexes documentation — master overview and five individual institute files (Border Friction Metrics with Tick/Tock clocks, Racial Dynamics, Economic Concordance, Historical Reconciliation Metrics, Demographic Drift) — all empirical observatories tracking continental patterns without advocacy (82-86% plausibility), added cross-references in Appomattox College document and canon-refresher
- December 19, 2025: Created Institute of Racial Dynamics (IRD) document — Appomattox College annex (1928+) that publishes annual Racial Equality Index as data-only mirror (82-86% plausibility), added cross-references in Appomattox College document and canon-refresher
- December 19, 2025: Created foundational reference document `world-building/cultural/racial-dynamics-spectrum-1939.md` — measurement/benchmark of racial equality spectrum across all North American shards (84-88% plausibility), added cross-reference in CULTURAL/SOCIAL section
- December 19, 2025: Updated Native Super-States Article 4 motivations — reframed from "buffer zone" to "mutual territorial denial" as primary driver (84-88% plausibility), updated `archive/world-building/regions/native-super-states-embattled-survivors.md` and canon-refresher cross-reference
- December 19, 2025: Added Patrick Cleburne to KEY CHARACTERS section; updated date to reflect latest changes
- December 17, 2025: Added `analysis/military/meade-36-hour-delay-telegraph-strategy-2025-12-17.md` — Meade's 36-hour delay & Longstreet telegraph strategy analysis; integrated summary into `canon-refresher-for-ai.md` and added cross-links to `README.md`, POD Campaign Part 2, and Compendium TOC.
- December 15, 2025: Added Git Operations Rule (explicit request required for commits/pushes)
- December 15, 2025: Added Patrick Cleburne character profile (`characters/confederate/patrick-cleburne.md`) and cashiering analysis (`analysis/political/cleburne-cashiering-martyred-prophet-2025-12-15.md`)
- December 15, 2025: Updated Grant's Final Gamble (Griffin replaces Warren, dates Feb 18-20, 1865)
- December 15, 2025: Added Harrisburg Occupation details (Battle of Camp Hill, Quaker guns, gradual shift)
- December 15, 2025: Updated Pickett's Raid (Carlisle objective, Field's destruction, casualty split)
- December 10, 2025: Grant's Final Gamble canonical updates (Griffin, rational decisions framework)
- December 10, 2025: Pickett's Raid canonical updates (Carlisle, Field's division, Kershaw's action)
- December 9, 2025: Streamlined from 7,000+ words to ~3,500 words
- December 9, 2025: Added "Negative Assumptions" section to gate OTL assumptions
- December 9, 2025: Moved detailed narratives to separate reference docs
- December 9, 2025: Added pointers to detailed documentation
- December 5, 2025: Added Western Theater, Sherman's March, OTL events list
- December 5, 2025: Added presidential timelines, Claude Review Fixes

**Status:** ACTIVE REFRESHER - LIVING DOCUMENT

**Update Checklist:**
- [ ] Update relevant sections with new canon
- [ ] **Integrate `analysis/military/meade-36-hour-delay-telegraph-strategy-2025-12-17.md` findings:** add Meade July 2–3 scenes to POD Campaign Part 2, add telegraph scenes (July 3 & July 9), draft scene edits in `edits/` (do NOT edit `books/`), and add cross-links (README, Compendium TOC)
- [ ] Update "Last Updated" date
- [ ] Verify all LOCKED items clearly marked
- [ ] Add pointers to new detailed docs
- [ ] Keep word count under 4,000

**When to Update:**
- Major canon decisions locked
- New treaties/political systems established
- Significant world-building changes
- Changes affecting "DO NOT" rules

---

## INTEGRATION NOTES (2025-12-17)

**Purpose:** Actionable tasks to integrate findings from `analysis/military/meade-36-hour-delay-telegraph-strategy-2025-12-17.md` into canon documents and writing plans.

- **Priority tasks:** Add Priority 1 scenes to `archive/world-building/timelines/pod-campaign/part-02-harrisburg-occupation.md` and prepare scene drafts in `edits/`:
  - Meade July 2, 10:00-18:00 (Working on wrong problem)
  - Meade July 3, 05:00-08:00 (Round Tops repositioning)
  - Meade July 3, 21:00 (Receives Lincoln telegram - Lee is dead)
  - Longstreet July 3, 16:00 (Telegraph decision - Sorrel/McLaws/Longstreet)
  - Longstreet July 9, 20:00 (Cut the lines order)

- **Cross-link tasks:** Ensure `analysis/military/meade-36-hour-delay-telegraph-strategy-2025-12-17.md` is referenced from `README.md`, `compendium/table-of-contents.md`, and `archive/world-building/timelines/pod-campaign/part-02-harrisburg-occupation.md` (done where applicable). 

- **Process tasks:** Draft scenes in `edits/` for user review (do NOT modify `books/` directly), update dependent document hashes via `python scripts/calculate-hash.py`, and request user approval before committing or locking any changes.
