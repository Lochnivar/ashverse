# Battle-Level Simulation Template

**Purpose:** General-use framework for simulating tactical battles with realistic opposition modeling

**Status:** REUSABLE TOOL  
**Version:** 1.0  
**Last Updated:** December 10, 2025

---

## HOW TO USE THIS TEMPLATE

1. **Copy this template** to your analysis folder
2. **Fill in battle-specific details** (replace all `[PLACEHOLDER]` sections)
3. **Define terrain features** (general features, not exact maps)
4. **Customize mechanics** as needed for your specific battle
5. **Run simulation** turn-by-turn (1-2 hour chunks)
6. **Document results** and compare with canon

**⚠️ IMPORTANT:** This is an exploratory exercise. Simulation results will NOT change established canon unless explicitly approved. This is a workshop tool for understanding tactical dynamics.

**Note on Terrain:** Exact terrain knowledge is not required. Use general features (hills, woods, open ground, rivers) and relative positioning. Focus on tactical effects, not precise maps.

---

## SIMULATION FRAMEWORK

### Purpose
This document provides a granular, turn-based simulation framework for the Battle of `[BATTLE NAME]` (`[DATE]`), modeling **realistic, competent opposition** and dynamic tactical interactions between forces.

**Critical Principle:** The opposition is competent, professional, and fights hard. Any success is earned through tactical skill, positioning, and timing — never because the opposition is portrayed as incompetent.

### Simulation Structure
- **Time Scale:** `[1-2 hour turns]` (granular enough for tactical decisions, not minute-by-minute)
- **Map Scale:** `[BATTLEFIELD AREA]` (`[GEOGRAPHIC LOCATION]`)
- **Unit Scale:** `[Brigade-level / Division-level]` (preferred: Brigade-level)
- **Focus:** `[Tactical positioning, firepower, maneuver, morale, casualties]`

---

## BATTLEFIELD TERRAIN

### General Terrain Features

**Note:** Exact terrain knowledge not required. Use general features and relative positioning.

**Key Terrain Features:**
- **`[TERRAIN FEATURE 1]:`** `[DESCRIPTION]` - `[TACTICAL EFFECT]`
- **`[TERRAIN FEATURE 2]:`** `[DESCRIPTION]` - `[TACTICAL EFFECT]`
- **`[TERRAIN FEATURE 3]:`** `[DESCRIPTION]` - `[TACTICAL EFFECT]`
- **`[TERRAIN FEATURE 4]:`** `[DESCRIPTION]` - `[TACTICAL EFFECT]`

**Terrain Types:**
- **Open Ground:** `[DESCRIPTION]` - `[EFFECT]` (movement: `[MODIFIER]`, cover: `[MODIFIER]`)
- **Woods:** `[DESCRIPTION]` - `[EFFECT]` (movement: `[MODIFIER]`, cover: `[MODIFIER]`)
- **Hills:** `[DESCRIPTION]` - `[EFFECT]` (movement: `[MODIFIER]`, cover: `[MODIFIER]`)
- **Rivers/Streams:** `[DESCRIPTION]` - `[EFFECT]` (movement: `[MODIFIER]`, cover: `[MODIFIER]`)
- **Urban:** `[DESCRIPTION]` - `[EFFECT]` (movement: `[MODIFIER]`, cover: `[MODIFIER]`)

**Relative Positioning:**
- **`[SIDE A]` Starting Position:** `[GENERAL LOCATION]` (relative to `[LANDMARK]`)
- **`[SIDE B]` Starting Position:** `[GENERAL LOCATION]` (relative to `[LANDMARK]`)
- **Key Positions:** `[POSITION 1]`, `[POSITION 2]`, `[POSITION 3]`

**Terrain Effects:**
- **Cover:** `[EFFECT ON CASUALTIES]`
- **Concealment:** `[EFFECT ON DETECTION]`
- **Movement:** `[EFFECT ON SPEED]`
- **Firepower:** `[EFFECT ON EFFECTIVENESS]`

---

## STARTING CONDITIONS

### [SIDE A] Forces: Initial Disposition

**Commander:** `[COMMANDER NAME AND RANK]`  
**Total Force:** `[NUMBER]` men  
**Artillery:** `[NUMBER]` guns

**Brigade/Division Composition:**
- **`[UNIT 1]:`** `[SIZE]` men, `[COMMANDER]` - `[DESCRIPTION]`
- **`[UNIT 2]:`** `[SIZE]` men, `[COMMANDER]` - `[DESCRIPTION]`
- **`[UNIT 3]:`** `[SIZE]` men, `[COMMANDER]` - `[DESCRIPTION]`
- **`[UNIT 4]:`** `[SIZE]` men, `[COMMANDER]` - `[DESCRIPTION]`

**Initial Positions:**
- **`[UNIT 1]:`** `[POSITION]` (relative to `[LANDMARK]`)
- **`[UNIT 2]:`** `[POSITION]` (relative to `[LANDMARK]`)
- **`[UNIT 3]:`** `[POSITION]` (relative to `[LANDMARK]`)
- **`[UNIT 4]:`** `[POSITION]` (relative to `[LANDMARK]`)

**Artillery Positions:**
- **`[BATTERY 1]:`** `[POSITION]` - `[NUMBER]` guns
- **`[BATTERY 2]:`** `[POSITION]` - `[NUMBER]` guns

**Capabilities:**
- **Firepower:** `[RATING]` (based on weapons, training, experience)
- **Mobility:** `[RATING]` (based on unit type, condition)
- **Morale:** `[RATING]` (high/medium/low - based on recent events)
- **Endurance:** `[RATING]` (fresh/tired/exhausted)

**Mission Objectives:**
1. **Primary:** `[OBJECTIVE]`
2. **Secondary:** `[OBJECTIVE]`
3. **Tertiary:** `[OBJECTIVE]`

---

### [SIDE B] Forces: Initial Disposition

**Commander:** `[COMMANDER NAME AND RANK]`  
**Total Force:** `[NUMBER]` men  
**Artillery:** `[NUMBER]` guns

**Brigade/Division Composition:**
- **`[UNIT 1]:`** `[SIZE]` men, `[COMMANDER]` - `[DESCRIPTION]`
- **`[UNIT 2]:`** `[SIZE]` men, `[COMMANDER]` - `[DESCRIPTION]`
- **`[UNIT 3]:`** `[SIZE]` men, `[COMMANDER]` - `[DESCRIPTION]`
- **`[UNIT 4]:`** `[SIZE]` men, `[COMMANDER]` - `[DESCRIPTION]`

**Initial Positions:**
- **`[UNIT 1]:`** `[POSITION]` (relative to `[LANDMARK]`)
- **`[UNIT 2]:`** `[POSITION]` (relative to `[LANDMARK]`)
- **`[UNIT 3]:`** `[POSITION]` (relative to `[LANDMARK]`)
- **`[UNIT 4]:`** `[POSITION]` (relative to `[LANDMARK]`)

**Artillery Positions:**
- **`[BATTERY 1]:`** `[POSITION]` - `[NUMBER]` guns
- **`[BATTERY 2]:`** `[POSITION]` - `[NUMBER]` guns

**Capabilities:**
- **Firepower:** `[RATING]` (based on weapons, training, experience)
- **Mobility:** `[RATING]` (based on unit type, condition)
- **Morale:** `[RATING]` (high/medium/low - based on recent events)
- **Endurance:** `[RATING]` (fresh/tired/exhausted)

**Advantages:**
- **Numbers:** `[SUPERIORITY RATIO]` (if applicable)
- **Position:** `[POSITIONAL ADVANTAGE]` (if applicable)
- **Artillery:** `[ARTILLERY ADVANTAGE]` (if applicable)
- **Terrain:** `[TERRAIN ADVANTAGE]` (if applicable)

**Realistic Constraints (NOT Ineptitude):**
- **Command/Control:** Realistic delays in orders reaching units (`[X-Y]` minutes)
- **Coordination:** Multiple units require time to coordinate (`[X-Y]` minutes)
- **Fatigue:** Units tire over time (realistic degradation)
- **Ammunition:** Limited supply (realistic constraint, not poor planning)
- **Visibility:** Fog of war (don't know exact enemy positions)
- **Terrain:** Cannot be everywhere (geography limits options)

**Key Point:** Every limitation listed above is a real military constraint faced by every army in history. They are not excuses; they are physics and command reality. Opposition limitations are REALISTIC military constraints, not incompetence. Commanders are professional, competent officers facing legitimate challenges.

---

## SIMULATION MECHANICS

### Turn Structure

**Each Turn = `[1-2 hours]`**

**Turn Sequence:**
1. **Intelligence Phase:** Both sides assess situation, gather information
2. **Command Phase:** Orders issued, decisions made
3. **Movement Phase:** Units maneuver, reposition
4. **Artillery Phase:** Artillery fires, positions adjust
5. **Combat Phase:** Units engage, firefights occur
6. **Casualty Phase:** Casualties assessed, morale checked
7. **Assessment Phase:** Positions, casualties, morale, objectives

---

### Movement & Maneuver

**Movement Rates (Brigade/Division Level):**

**`[SIDE A]` Forces:**
- **Formation Change:** `[X-Y]` minutes (deploy from column to line, etc.)
- **Advance:** `[X-Y]` yards/hour (depending on terrain, opposition)
- **Retreat:** `[X-Y]` yards/hour (faster, but risky)
- **Flank Movement:** `[X-Y]` yards/hour (slower, but safer)

**`[SIDE B]` Forces:**
- **Formation Change:** `[X-Y]` minutes
- **Advance:** `[X-Y]` yards/hour
- **Retreat:** `[X-Y]` yards/hour
- **Flank Movement:** `[X-Y]` yards/hour

**Terrain Modifiers:**
- **Open Ground:** `[MODIFIER]` (movement speed)
- **Woods:** `[MODIFIER]` (movement speed, concealment)
- **Hills:** `[MODIFIER]` (movement speed, cover)
- **Rivers/Streams:** `[MODIFIER]` (movement delay, crossing time)
- **Urban:** `[MODIFIER]` (movement speed, cover)

**Formation Types:**
- **Column:** Fast movement, vulnerable to fire
- **Line:** Slow movement, maximum firepower
- **Skirmish:** Slower movement, good cover, reduced firepower
- **Square:** Very slow, maximum defense, minimal offense

---

### Firepower & Combat

**Combat Resolution:**

**Ranges:**
- **Artillery:** `[X-Y]` yards (effective range)
- **Rifles:** `[X-Y]` yards (effective range)
- **Close Range:** `[X-Y]` yards (maximum effectiveness)

**Firepower Factors:**
- **Weapons:** Type, quality, condition
- **Training:** Experience, discipline
- **Position:** Cover, elevation, angle
- **Range:** Distance to target
- **Morale:** Unit confidence, cohesion

**Combat Outcomes:**
- **Suppression:** Unit pinned, reduced effectiveness
- **Casualties:** Light (`[X-Y]%`), Moderate (`[X-Y]%`), Heavy (`[X-Y]%`)
- **Rout:** Unit breaks, retreats
- **Advance:** Unit gains ground
- **Stalemate:** No significant change

**Casualty Rates (per hour of combat):**
- **Light Fire:** `[X-Y]%` casualties
- **Moderate Fire:** `[X-Y]%` casualties
- **Heavy Fire:** `[X-Y]%` casualties
- **Artillery:** `[X-Y]%` casualties (area effect)

---

### Artillery

**Artillery Capabilities:**
- **Range:** `[X-Y]` yards
- **Rate of Fire:** `[X]` rounds/hour (sustained)
- **Effectiveness:** `[RATING]` (based on type, position, target)

**Artillery Effects:**
- **Suppression:** Reduces enemy firepower
- **Casualties:** Area effect, `[X-Y]%` casualties per hour
- **Morale:** Reduces enemy morale
- **Position:** Can force enemy to move

**Artillery Limitations:**
- **Ammunition:** Limited supply (realistic constraint)
- **Positioning:** Requires time to move, set up
- **Visibility:** Need clear line of sight
- **Counter-battery:** Vulnerable to enemy artillery

---

### Morale & Endurance

**Morale Levels:**
- **High:** Unit fights aggressively, high effectiveness
- **Medium:** Unit fights competently, normal effectiveness
- **Low:** Unit fights defensively, reduced effectiveness
- **Breaking:** Unit routs, retreats

**Morale Factors:**
- **Casualties:** High casualties reduce morale
- **Leadership:** Commander presence/absence
- **Position:** Advantageous/disadvantageous position
- **Support:** Friendly units nearby
- **Artillery:** Enemy artillery fire reduces morale
- **Recent Events:** Success/failure affects morale

**Endurance:**
- **Fresh:** Full effectiveness
- **Tired:** Reduced effectiveness (`[X]%`)
- **Exhausted:** Significantly reduced effectiveness (`[X]%`)
- **Broken:** Unit cannot continue

**Endurance Factors:**
- **Time:** Units tire over hours of combat
- **Casualties:** Losses reduce effectiveness
- **Movement:** Extensive movement exhausts units
- **Weather:** Heat/cold affects endurance

---

## PHASE-BY-PHASE SIMULATION

### PHASE 1: `[PHASE NAME]` (`[TIME]`)

**Turn `[NUMBER]:` `[TIME RANGE]` (`[DURATION]` hours)**

**`[SIDE A]` Actions:**
- **`[UNIT 1]:`** `[ACTION]` - `[POSITION]`
- **`[UNIT 2]:`** `[ACTION]` - `[POSITION]`
- **Artillery:** `[ACTION]` - `[TARGET]`
- **Objective:** `[OBJECTIVE]`

**`[SIDE B]` Response:**
- **Detection:** `[X-Y]` minutes (time to observe, report)
- **Assessment:** `[X-Y]` minutes (`[COMMANDER]` evaluates threat)
- **Orders:** `[X-Y]` minutes (orders issued, units respond)
- **Response:** `[RESPONSE]`

**Key Dynamics:**
- **`[DYNAMIC 1]:`** `[DESCRIPTION]`
- **`[DYNAMIC 2]:`** `[DESCRIPTION]`
- **`[DYNAMIC 3]:`** `[DESCRIPTION]`

**Combat Resolution:**
- **`[UNIT 1]` vs. `[UNIT X]:`** `[OUTCOME]` - `[CASUALTIES]`
- **Artillery:** `[EFFECT]` - `[CASUALTIES]`
- **Morale:** `[CHANGES]`

**Possible Outcomes:**
- ✅ `[OUTCOME 1]` (`[REASON]`)
- ✅ `[OUTCOME 2]` (`[REASON]`)
- ⚠️ `[OUTCOME 3]` (`[REASON]`)
- ❌ `[OUTCOME 4]` (`[REASON]`)
- **Key Point:** `[SIDE B]` response is professional and timely, but `[SIDE A]` has tactical advantages

---

### PHASE 2: `[PHASE NAME]` (`[TIME]`)

**Turn `[NUMBER]:` `[TIME RANGE]` (`[DURATION]` hours)**
**Turn `[NUMBER]:` `[TIME RANGE]` (`[DURATION]` hours)**

**`[SIDE A]` Actions:**
- **`[UNIT 1]:`** `[ACTION]` - `[POSITION]`
- **`[UNIT 2]:`** `[ACTION]` - `[POSITION]`
- **Artillery:** `[ACTION]` - `[TARGET]`
- **Objective:** `[OBJECTIVE]`

**`[SIDE B]` Response:**
- **`[COMMANDER]`'s Decision:** `[DECISION]`
- **`[UNIT 1]:`** `[ACTION]` - `[POSITION]`
- **`[UNIT 2]:`** `[ACTION]` - `[POSITION]`
- **Artillery:** `[ACTION]` - `[TARGET]`

**Key Dynamics:**
- **`[DYNAMIC 1]:`** `[DESCRIPTION]`
- **`[DYNAMIC 2]:`** `[DESCRIPTION]`
- **`[DYNAMIC 3]:`** `[DESCRIPTION]`

**Combat Resolution:**
- **`[UNIT 1]` vs. `[UNIT X]:`** `[OUTCOME]` - `[CASUALTIES]`
- **Artillery:** `[EFFECT]` - `[CASUALTIES]`
- **Morale:** `[CHANGES]`

**Possible Outcomes:**
- ✅ `[OUTCOME 1]` (`[REASON]`)
- ⚠️ `[OUTCOME 2]` (`[REASON]`)
- ⚠️ `[OUTCOME 3]` (`[REASON]`)
- ❌ `[OUTCOME 4]` (`[REASON]`)
- **Key Point:** `[SIDE B]` performs competently - `[SIDE A]` succeeds through tactical advantages, not `[SIDE B]` failures

---

### PHASE 3: `[PHASE NAME]` (`[TIME]`)

**[REPEAT STRUCTURE AS NEEDED]**

---

## OPPOSITION MODELING

### `[SIDE B]` Command Decisions (Competent Professional Response)

**Initial Response (`[TIME]`):**
- **Assessment:** Professional evaluation - `[THREAT ASSESSMENT]`
- **Decision:** `[DECISION]` (not panic, not dismiss)
- **Action:** 
  - `[ACTION 1]` (professional procedure)
  - `[ACTION 2]` (standard procedure)
  - `[ACTION 3]` (measured response)
  - `[ACTION 4]` (proper command structure)
- **Timeline:** `[X-Y]` minute response time (realistic for command decision cycle)

**`[PHASE NAME]` (`[TIME]`):**
- **Strategy:** Professional tactical approach - `[STRATEGY]`
- **Tactics:** 
  - `[TACTIC 1]` (`[PURPOSE]`)
  - `[TACTIC 2]` (`[PURPOSE]`)
  - `[TACTIC 3]` (`[PURPOSE]`)
  - `[TACTIC 4]` (`[PURPOSE]`)
- **Challenges:** 
  - `[CHALLENGE 1]` (`[REASON]`, not `[SIDE B]` failure)
  - `[CHALLENGE 2]` (`[REASON]`, not `[SIDE B]` failure)
  - `[CHALLENGE 3]` (`[REASON]`, legitimate tactical constraint)
- **Performance:** Competent execution, but facing inherent advantages of `[SIDE A]`

**Final `[PHASE]` (`[TIME]`):**
- **Strategy:** `[STRATEGY]` - maximize effort to `[OBJECTIVE]`
- **Tactics:** 
  - `[TACTIC 1]` (`[PURPOSE]`)
  - `[TACTIC 2]` (`[PURPOSE]`)
  - `[TACTIC 3]` (`[PURPOSE]`)
  - `[TACTIC 4]` (`[PURPOSE]`)
- **Performance:** 
  - Competent execution
  - Aggressive but not reckless
  - Professional tactical response
- **Outcome:** `[SIDE A]` succeeds, but NOT due to `[SIDE B]` incompetence - due to `[SIDE A]` advantages (`[LIST ADVANTAGES]`)

---

### `[SIDE B]` Unit Performance

**`[UNIT TYPE 1]` (`[SIZE]` men):**
- **Role:** `[ROLE]`
- **Capability:** `[CAPABILITY]`
- **Limitation:** `[LIMITATION]`
- **Effectiveness:** `[EFFECTIVENESS]`
- **Performance:** Competent within limitations - perform their role professionally

**`[UNIT TYPE 2]` (`[SIZE]` men):**
- **Role:** `[ROLE]`
- **Capability:** `[CAPABILITY]` (competent performance)
- **Limitation:** `[LIMITATION]` (realistic constraint, not incompetence)
- **Effectiveness:** `[EFFECTIVENESS]` (professional)
- **Performance:** Competent within limitations - perform their role professionally

---

## KEY DECISION POINTS

### `[SIDE A]` Decisions

1. **`[DECISION TYPE 1]:`**
   - `[OPTION 1]` - `[CONSEQUENCE]`
   - `[OPTION 2]` - `[CONSEQUENCE]`
   - `[OPTION 3]` - `[CONSEQUENCE]`

2. **`[DECISION TYPE 2]:`**
   - `[OPTION 1]` - `[CONSEQUENCE]`
   - `[OPTION 2]` - `[CONSEQUENCE]`
   - `[OPTION 3]` - `[CONSEQUENCE]`

3. **`[DECISION TYPE 3]:`**
   - `[OPTION 1]` - `[CONSEQUENCE]`
   - `[OPTION 2]` - `[CONSEQUENCE]`
   - `[OPTION 3]` - `[CONSEQUENCE]`

---

### `[SIDE B]` Decisions

1. **`[DECISION TYPE 1]:`**
   - `[OPTION 1]` - `[CONSEQUENCE]`
   - `[OPTION 2]` - `[CONSEQUENCE]`
   - `[OPTION 3]` - `[CONSEQUENCE]`

2. **`[DECISION TYPE 2]:`**
   - `[OPTION 1]` - `[CONSEQUENCE]`
   - `[OPTION 2]` - `[CONSEQUENCE]`
   - `[OPTION 3]` - `[CONSEQUENCE]`

---

## VICTORY CONDITIONS

### `[SIDE A]` Victory (Canon Outcome)

**Objectives Achieved:**
- ✅ `[OBJECTIVE 1]`
- ✅ `[OBJECTIVE 2]`
- ✅ `[OBJECTIVE 3]`

**Success Metrics:**
- `[METRIC 1]:` `[TARGET]`
- `[METRIC 2]:` `[TARGET]`
- Casualties: `[RANGE]` (acceptable for objective)
- `[SIDE B]` response: Professional and competent, but `[SIDE A]` succeeds through advantages
- **Success is measured in `[MEASURE]`, not in the absence of `[SIDE B]` resistance. The battle must feel like it was hard-fought.**

---

### `[SIDE B]` "Victory" (Preventing Disaster)

**Objectives:**
- ⚠️ `[OBJECTIVE 1]`
- ⚠️ `[OBJECTIVE 2]`
- ⚠️ `[OBJECTIVE 3]` (did not happen — but came uncomfortably close)

**Success Metrics:**
- Casualties inflicted: `[RANGE]` (`[SIDE B]` competent combat performance)
- `[METRIC 1]:` `[TARGET]` (`[SIDE A]` succeeded despite `[SIDE B]` competence)
- `[METRIC 2]:` `[TARGET]` (but `[SIDE A]` achieved objective)
- **Key Point:** `[SIDE B]` performs competently - `[SIDE A]` succeeds through `[SIDE A]` advantages, not `[SIDE B]` failures

---

## SIMULATION VARIABLES

### Random Factors

1. **Weather:**
   - `[CONDITION 1]:` `[EFFECT]` (visibility, movement, morale)
   - `[CONDITION 2]:` `[EFFECT]`
   - `[CONDITION 3]:` `[EFFECT]`

2. **Intelligence:**
   - Detection timing: Variable (`[X-Y]` minutes)
   - False reports: Can mislead
   - Visibility: Fog of war

3. **Combat:**
   - Fire effectiveness: Variable (within realistic ranges)
   - Casualties: Random within ranges
   - Morale: Can shift with events

4. **Leadership:**
   - Commander presence: Affects morale, coordination
   - Order delays: Realistic command/control delays
   - Unit cohesion: Can degrade under pressure

---

## MODELING OPPOSITION COMPETENCE

### Key Principles

1. **`[SIDE B]` Response Time:** `[X-Y]` minutes is PROFESSIONAL, not slow
   - Detection: `[X-Y]` minutes (realistic observation, reporting)
   - Assessment: `[X-Y]` minutes (professional command decision cycle)
   - Response: `[X-Y]` minutes (realistic order transmission, unit response)
   - **This is competent performance, not incompetence**

2. **`[SIDE B]` Coordination:** Multiple units is REALISTIC challenge
   - `[UNIT 1]:` Professional coordination
   - `[UNIT 2]:` Competent within limitations
   - `[UNIT 3]:` Professional performance
   - **Challenges are realistic command/control issues, not failures**

3. **`[SIDE B]` Tactics:** `[CONSTRAINT]` is PHYSICS/REALITY
   - Not incompetence
   - Not poor planning
   - Realistic tactical constraint
   - **`[SIDE B]` uses `[COMPENSATION]` competently to compensate**

4. **`[SIDE B]` Combat Performance:** When engaged, `[SIDE B]` fights COMPETENTLY
   - Professional tactics
   - Skilled execution
   - Effective fire discipline
   - **`[SIDE B]` performs well in combat - `[SIDE A]` succeeds through advantages (`[LIST ADVANTAGES]`), not `[SIDE B]` failures**
   - **When `[SIDE B]` units do engage `[SIDE A]` effectively, they fight hard. The only question is whether they can prevent `[SIDE A]` from achieving objectives.**

### Why `[SIDE A]` Succeeds (Despite `[SIDE B]` Competence)

**`[SIDE A]` Advantages:**
1. **`[ADVANTAGE 1]:`** `[DESCRIPTION]`
2. **`[ADVANTAGE 2]:`** `[DESCRIPTION]`
3. **`[ADVANTAGE 3]:`** `[DESCRIPTION]`
4. **`[ADVANTAGE 4]:`** `[DESCRIPTION]`

**`[SIDE B]` Competence:**
1. **Professional Response:** Appropriate and timely
2. **Skilled Command:** `[COMMANDER]` and subordinates competent
3. **Effective Tactics:** Maintains pressure, fights competently
4. **Competent Combat:** Fights well when engaged
5. **Realistic Constraints:** Faces legitimate tactical challenges

**Conclusion:** `[SIDE A]` succeeds through inherent advantages and tactical skill, NOT because `[SIDE B]` is incompetent. `[SIDE B]` performs professionally throughout - the battle succeeds despite competent opposition.

**Anti-Bias Failsafe:** If the simulation ever makes `[SIDE B]` forces look foolish, the parameters are wrong — rerun with tighter response times and better coordination until `[SIDE B]` feels lethal.

---

## TERRAIN WORKAROUNDS

### Working Without Exact Maps

**General Features Approach:**
- Use general terrain types (hills, woods, open ground)
- Define relative positions (north of X, south of Y)
- Identify key terrain features (high ground, river crossing)
- Focus on tactical effects, not precise coordinates

**Relative Positioning:**
- "Unit A is positioned north of Unit B"
- "Artillery on high ground overlooking approach"
- "Woods provide cover for flank movement"
- "River creates natural barrier"

**Tactical Effects:**
- Focus on how terrain affects combat
- Cover, concealment, movement, firepower
- Not exact distances or coordinates

**Example:**
- Instead of: "Unit at coordinates 42.123, -71.456"
- Use: "Unit positioned on high ground overlooking the approach, with woods to the left providing cover for potential flank movement"

---

## NEXT STEPS FOR SIMULATION

### To Complete Framework:

1. **Define Terrain:**
   - General features (hills, woods, rivers)
   - Relative positions
   - Key terrain features
   - Tactical effects

2. **Define Forces:**
   - Unit composition
   - Initial positions
   - Capabilities
   - Objectives

3. **Model `[SIDE B]` Response:**
   - `[COMMANDER]`'s exact decisions
   - Unit movements
   - Tactical responses

4. **Run Simulation:**
   - Turn-by-turn execution (1-2 hour chunks)
   - Decision points
   - Combat resolution
   - Outcome assessment

5. **Refine Based on Results:**
   - Adjust variables
   - Test alternatives
   - Validate against canon

---

## DOCUMENT DEPENDENCIES

<!--
Content Integrity System: Tracks dependencies and their content hashes
This section enables automated consistency checking across the project.

To add a dependency:
1. Run: python scripts/calculate-hash.py <dependency-file-path>
2. Copy the hash and add it to the table below
3. Update "Last Verified" date

To check consistency:
Run: python scripts/consistency-checker.py
-->

| Document | Path | Hash | Status |
|----------|------|------|--------|
| `[DEPENDENCY 1]` | `[PATH]` | [To be calculated] | ✅ Tracked |
| `[DEPENDENCY 2]` | `[PATH]` | [To be calculated] | ✅ Tracked |

**This Document's Hash:** [To be calculated]  
**Last Updated:** [DATE]

---

**Status:** 🎲 **EXPLORATORY SIMULATION FRAMEWORK**  
**Purpose:** Battle-level wargaming simulation with realistic opposition  
**Canon Status:** Does NOT affect established canon - exploratory workshop only  
**Next Step:** Fill in specific details and run simulation turns to explore tactical dynamics

