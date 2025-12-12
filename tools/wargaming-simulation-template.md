# Wargaming Simulation Template

**Purpose:** General-use framework for simulating military operations with realistic opposition modeling

**Status:** REUSABLE TOOL  
**Version:** 1.0  
**Last Updated:** December 10, 2025

---

## HOW TO USE THIS TEMPLATE

1. **Copy this template** to your analysis folder
2. **Fill in operation-specific details** (replace all `[PLACEHOLDER]` sections)
3. **Customize mechanics** as needed for your specific operation
4. **Run simulation** turn-by-turn
5. **Document results** and compare with canon

**⚠️ IMPORTANT:** This is an exploratory exercise. Simulation results will NOT change established canon unless explicitly approved. This is a workshop tool for understanding dynamics.

---

## SIMULATION FRAMEWORK

### Purpose
This document provides a granular, turn-based simulation framework for `[OPERATION NAME]` (`[DATES]`), modeling **realistic, competent opposition** and dynamic interactions between forces.

**Critical Principle:** The opposition is competent, professional, and fights hard. Any success is earned through audacity, luck, and inherent advantages — never because the opposition is portrayed as incompetent.

### Simulation Structure
- **Time Scale:** `[2-3 day turns / daily / weekly]` (granular enough for tactical decisions, not micro-management)
- **Map Scale:** `[Regional / Theater / Strategic]` (`[GEOGRAPHIC AREA]`)
- **Unit Scale:** `[Brigade-level / Division-level / Corps-level]`
- **Focus:** `[Movement, intelligence, pursuit, blocking, skirmishing, effectiveness]`

---

## STARTING CONDITIONS

### [SIDE A] Forces: [FORCE NAME]

**Commander:** `[COMMANDER NAME AND RANK]`  
**Force Size:** `[NUMBER]` men  
**Composition:**
- `[UNIT 1]:` `[SIZE]` - `[DESCRIPTION]`
- `[UNIT 2]:` `[SIZE]` - `[DESCRIPTION]`
- Total: `[TOTAL]` men

**Capabilities:**
- **Mobility:** `[X-Y]` miles/day (`[CONDITIONS]`)
- **Combat:** `[COMBAT CAPABILITIES]`
- **Endurance:** `[DURATION]` operational (`[LIMITING FACTOR]`)
- **Logistics:** `[SUPPLY METHOD]`

**Starting Position:** `[LOCATION]`
- **Date:** `[DATE]`
- **Objective:** `[PRIMARY OBJECTIVE]`

**Mission Objectives:**
1. **Primary:** `[PRIMARY OBJECTIVE]`
2. **Secondary:** `[SECONDARY OBJECTIVE]`
3. **Tertiary:** `[TERTIARY OBJECTIVE]`
4. **Constraint:** `[CONSTRAINT]`

---

### [SIDE B] Forces: Initial Disposition

**Commander:** `[COMMANDER NAME AND RANK]`  
**Force Size:** `[NUMBER]` men  
**Initial Position:** `[LOCATION]`

**Available Forces:**
- **`[FORCE TYPE 1]:`** `[SIZE]` men (`[CAPABILITY]`)
- **`[FORCE TYPE 2]:`** `[SIZE]` men (`[CAPABILITY]`)
- **`[FORCE TYPE 3]:`** `[SIZE]` men (`[CAPABILITY]`)

**Advantages:**
- **Numbers:** `[SUPERIORITY RATIO]`
- **Intelligence:** `[INTELLIGENCE CAPABILITIES]`
- **Supply:** `[SUPPLY ADVANTAGES]`
- **Terrain Knowledge:** `[TERRAIN ADVANTAGES]`
- **Other:** `[ADDITIONAL ADVANTAGES]`

**Realistic Constraints (NOT Ineptitude):**
- **Response Time:** `[X-Y]` hours minimum (legitimate military delay: detect → assess → react)
- **Coordination Challenges:** Real command/control issues (`[SPECIFIC CHALLENGES]`)
- **Mobility Limitation:** `[PHYSICAL CONSTRAINTS]` (not incompetence, physics)
- **Intelligence Uncertainty:** Don't know exact route/objectives (normal fog of war)
- **Resource Allocation:** Must balance `[COMPETING PRIORITIES]` (legitimate strategic choice)
- **Terrain Constraints:** Cannot be everywhere at once (geography limits options)

**Key Point:** Every limitation listed above is a real military constraint faced by every army in history. They are not excuses; they are physics and command reality. Opposition limitations are REALISTIC military constraints, not incompetence. Commanders are professional, competent officers facing legitimate challenges.

---

## SIMULATION MECHANICS

### Turn Structure

**Each Turn = `[DURATION]`**

**Turn Sequence:**
1. **Intelligence Phase:** Both sides gather information
2. **Command Phase:** Orders issued, decisions made
3. **Movement Phase:** Units move (`[SIDE A]` faster, `[SIDE B]` slower)
4. **Combat Phase:** Skirmishes, blocking actions, pursuits
5. **Logistics Phase:** Forage, supply, endurance checks
6. **Assessment Phase:** Objectives, casualties, morale

---

### Movement Rates

**`[SIDE A]` Forces:**
- **`[MOVEMENT TYPE 1]:`** `[X-Y]` miles/day (`[CONDITIONS]`)
- **`[MOVEMENT TYPE 2]:`** `[X-Y]` miles/day (`[CONDITIONS]`)
- **`[MOVEMENT TYPE 3]:`** `[X-Y]` miles/day (`[CONDITIONS]`)
- **Terrain Modifiers:**
  - `[TERRAIN TYPE 1]:` `[MODIFIER]`
  - `[TERRAIN TYPE 2]:` `[MODIFIER]`
  - `[TERRAIN TYPE 3]:` `[MODIFIER]`

**`[SIDE B]` Forces:**
- **`[MOVEMENT TYPE 1]:`** `[X-Y]` miles/day (`[CONDITIONS]`)
- **`[MOVEMENT TYPE 2]:`** `[X-Y]` miles/day (`[CONDITIONS]`)
- **`[MOVEMENT TYPE 3]:`** `[X-Y]` miles/day (`[CONDITIONS]`)

---

### Intelligence & Fog of War

**`[SIDE A]` Intelligence:**
- **Local Knowledge:** `[LEVEL]` (`[DESCRIPTION]`)
- **Scouts:** `[CAPABILITY]` (`[RANGE]`)
- **Civilians:** `[ATTITUDE]` (`[DESCRIPTION]`)
- **Communications:** `[CAPABILITY]`

**`[SIDE B]` Intelligence:**
- **`[INTELLIGENCE SOURCE 1]:`** `[CAPABILITY]`
- **`[INTELLIGENCE SOURCE 2]:`** `[CAPABILITY]`
- **`[INTELLIGENCE SOURCE 3]:`** `[CAPABILITY]`
- **`[INTELLIGENCE SOURCE 4]:`** `[CAPABILITY]`

**Intelligence Delays:**
- **Detection:** `[X-Y]` hours (time to report, verify)
- **Assessment:** `[X-Y]` hours (command decision)
- **Response:** `[X-Y]` hours (forces mobilized, moved)

---

### Combat Resolution

**Combat Types:**

1. **Skirmishes (Small Scale):**
   - `[SIDE A]` vs. `[SIDE B]` `[FORCE TYPE]`
   - Outcome: `[TYPICAL OUTCOME]`
   - Delay: `[X-Y]` hours
   - Casualties: `[RANGE]` per side

2. **Blocking Actions (Medium Scale):**
   - `[SIDE A]` vs. `[SIDE B]` `[FORCE TYPE]`
   - Outcome: Depends on terrain, surprise, numbers
   - Delay: `[X-Y]` hours
   - Casualties: `[RANGE]` per side

3. **Pursuit Engagements (Large Scale):**
   - `[SIDE A]` vs. `[SIDE B]` `[FORCE TYPE]`
   - Outcome: `[TYPICAL OUTCOME]`
   - Delay: `[X-Y]` hours
   - Casualties: `[RANGE]` per side

**Combat Factors:**
- **Terrain:** `[EFFECT]`
- **Surprise:** `[EFFECT]`
- **Numbers:** `[EFFECT]`
- **Morale:** `[EFFECT]`

---

### Logistics & Endurance

**`[SIDE A]` Forces:**
- **`[LOGISTIC FACTOR 1]:`** `[REQUIREMENT]`
- **`[LOGISTIC FACTOR 2]:`** `[REQUIREMENT]`
- **Endurance:** `[DURATION]` operational (`[LIMITING FACTOR]`)
- **Supply:** `[SUPPLY METHOD]`

**`[SIDE B]` Forces:**
- **Supply:** `[SUPPLY ADVANTAGES]`
- **Endurance:** `[DURATION]` (`[LIMITING FACTOR]`)
- **Logistics:** `[LOGISTIC CAPABILITIES]`

**`[LOGISTIC CHECKS]:`**
- **`[CONDITION 1]:`** `[EFFECT]`
- **`[CONDITION 2]:`** `[EFFECT]`
- **`[CONDITION 3]:`** `[EFFECT]`
- **Failure:** `[CONSEQUENCE]`

---

## PHASE-BY-PHASE SIMULATION

### PHASE 1: `[PHASE NAME]` (`[DATES]`)

**Turn `[NUMBER]:` `[DATE RANGE]` (`[DURATION]` days)**

**`[SIDE A]` Actions:**
- `[ACTION 1]`
- `[ACTION 2]`
- `[ACTION 3]`
- Objective: `[OBJECTIVE]`
- Movement: `[DISTANCE]` miles

**`[SIDE B]` Response:**
- **Detection:** `[X-Y]` hours (`[METHOD]`)
- **Assessment:** `[X-Y]` hours (`[COMMANDER]` evaluates threat)
- **Initial Response:** `[RESPONSE]`
- **Mobilization:** `[MOBILIZATION]`

**Key Dynamics:**
- **`[DYNAMIC 1]:`** `[DESCRIPTION]`
- **`[DYNAMIC 2]:`** `[DESCRIPTION]`
- **`[DYNAMIC 3]:`** `[DESCRIPTION]`

**Possible Outcomes:**
- ✅ `[OUTCOME 1]` (`[REASON]`)
- ✅ `[OUTCOME 2]` (`[REASON]`)
- ⚠️ `[OUTCOME 3]` (`[REASON]`)
- ❌ `[OUTCOME 4]` (`[REASON]`)
- **Key Point:** `[SIDE B]` response is professional and timely, but `[SIDE A]` has inherent advantages

---

### PHASE 2: `[PHASE NAME]` (`[DATES]`)

**Turn `[NUMBER]:` `[DATE RANGE]` (`[DURATION]` days)**
**Turn `[NUMBER]:` `[DATE RANGE]` (`[DURATION]` days)**

**`[SIDE A]` Actions:**
- `[ACTION 1]`
- `[ACTION 2]`
- Movement: `[DISTANCE]` miles per turn
- Objective: `[OBJECTIVE]`

**`[SIDE B]` Response:**
- **`[COMMANDER]`'s Decision:** `[DECISION]`
- **`[FORCE TYPE]` Pursuit:** `[SIZE]` men moving to intercept
- **`[FORCE TYPE]` Response:** `[ACTION]`
- **`[FORCE TYPE]`:** `[ACTION]`

**Key Dynamics:**
- **`[DYNAMIC 1]:`** `[DESCRIPTION]`
- **`[DYNAMIC 2]:`** `[DESCRIPTION]`
- **`[DYNAMIC 3]:`** `[DESCRIPTION]`

**Possible Outcomes:**
- ✅ `[OUTCOME 1]` (`[REASON]`)
- ⚠️ `[OUTCOME 2]` (`[REASON]`)
- ⚠️ `[OUTCOME 3]` (`[REASON]`)
- ❌ `[OUTCOME 4]` (`[REASON]`)
- **Key Point:** `[SIDE B]` performs competently - `[SIDE A]` succeeds through advantages, not `[SIDE B]` failures

---

### PHASE 3: `[PHASE NAME]` (`[DATES]`)

**[REPEAT STRUCTURE AS NEEDED]**

---

## OPPOSITION MODELING

### `[SIDE B]` Command Decisions (Competent Professional Response)

**Initial Response (`[DATES]`):**
- **Assessment:** Professional evaluation - `[THREAT ASSESSMENT]`
- **Decision:** `[DECISION]` (not panic, not dismiss)
- **Action:** 
  - `[ACTION 1]` (professional procedure)
  - `[ACTION 2]` (standard procedure)
  - `[ACTION 3]` (measured response)
  - `[ACTION 4]` (proper command structure)
- **Timeline:** `[X-Y]` hour response time (realistic for command decision cycle)

**`[PHASE NAME]` (`[DATES]`):**
- **Strategy:** Professional military approach - `[STRATEGY]`
- **Tactics:** 
  - `[TACTIC 1]` (`[PURPOSE]`)
  - `[TACTIC 2]` (`[PURPOSE]`)
  - `[TACTIC 3]` (`[PURPOSE]`)
  - `[TACTIC 4]` (`[PURPOSE]`)
- **Challenges:** 
  - `[CHALLENGE 1]` (`[REASON]`, not `[SIDE B]` failure)
  - `[CHALLENGE 2]` (`[REASON]`, not `[SIDE B]` failure)
  - `[CHALLENGE 3]` (`[REASON]`, legitimate strategic constraint)
- **Performance:** Competent execution, but facing inherent advantages of `[SIDE A]`

**Final `[PHASE]` (`[DATES]`):**
- **Strategy:** `[STRATEGY]` - maximize effort to `[OBJECTIVE]`
- **Tactics:** 
  - `[TACTIC 1]` (`[PURPOSE]`)
  - `[TACTIC 2]` (`[PURPOSE]`)
  - `[TACTIC 3]` (`[PURPOSE]`)
  - `[TACTIC 4]` (`[PURPOSE]`)
- **Performance:** 
  - Competent execution
  - Aggressive but not reckless
  - Professional military response
- **Outcome:** `[SIDE A]` succeeds, but NOT due to `[SIDE B]` incompetence - due to `[SIDE A]` advantages (`[LIST ADVANTAGES]`)

---

### `[SIDE B]` Force Availability

**`[FORCE TYPE 1]` (`[SIZE]` men):**
- **Role:** `[ROLE]`
- **Capability:** `[CAPABILITY]`
- **Limitation:** `[LIMITATION]`
- **Effectiveness:** `[EFFECTIVENESS]`

**`[FORCE TYPE 2]` (`[SIZE]` men):**
- **Role:** `[ROLE]`
- **Capability:** `[CAPABILITY]`
- **Limitation:** `[LIMITATION]`
- **Effectiveness:** `[EFFECTIVENESS]`

**`[FORCE TYPE 3]` (`[SIZE]` men):**
- **Role:** `[ROLE]`
- **Capability:** `[CAPABILITY]` (competent performance)
- **Limitation:** `[LIMITATION]` (realistic constraint, not incompetence)
- **Effectiveness:** `[EFFECTIVENESS]` (professional)
- **Performance:** Competent within limitations - perform their role professionally

---

## KEY DECISION POINTS

### `[SIDE A]` Decisions

1. **`[DECISION TYPE 1]:`**
   - `[OPTION 1]`
   - `[OPTION 2]`
   - `[OPTION 3]`

2. **`[DECISION TYPE 2]:`**
   - `[OPTION 1]`
   - `[OPTION 2]`
   - `[OPTION 3]`

3. **`[DECISION TYPE 3]:`**
   - `[OPTION 1]`
   - `[OPTION 2]`
   - `[OPTION 3]`

4. **`[DECISION TYPE 4]:`**
   - `[OPTION 1]`
   - `[OPTION 2]`
   - `[OPTION 3]`

---

### `[SIDE B]` Decisions

1. **`[DECISION TYPE 1]:`**
   - `[OPTION 1]`
   - `[OPTION 2]`
   - `[OPTION 3]`

2. **`[DECISION TYPE 2]:`**
   - `[OPTION 1]`
   - `[OPTION 2]`
   - `[OPTION 3]`

3. **`[DECISION TYPE 3]:`**
   - `[OPTION 1]`
   - `[OPTION 2]`
   - `[OPTION 3]`

4. **`[DECISION TYPE 4]:`**
   - `[OPTION 1]`
   - `[OPTION 2]`
   - `[OPTION 3]`

---

## VICTORY CONDITIONS

### `[SIDE A]` Victory (Canon Outcome)

**Objectives Achieved:**
- ✅ `[OBJECTIVE 1]`
- ✅ `[OBJECTIVE 2]`
- ✅ `[OBJECTIVE 3]`
- ✅ `[OBJECTIVE 4]`
- ✅ `[OBJECTIVE 5]`

**Success Metrics:**
- `[METRIC 1]:` `[TARGET]`
- `[METRIC 2]:` `[TARGET]`
- `[METRIC 3]:` `[TARGET]`
- `[METRIC 4]:` `[TARGET]`
- `[SIDE B]` response: Professional and competent, but `[SIDE A]` succeeds through advantages
- **Success is measured in `[MEASURE]`, not in the absence of `[SIDE B]` resistance. The operation must feel like it barely succeeded.**

---

### `[SIDE B]` "Victory" (Preventing Disaster)

**Objectives:**
- ⚠️ `[OBJECTIVE 1]`
- ⚠️ `[OBJECTIVE 2]`
- ⚠️ `[OBJECTIVE 3]`
- ⚠️ `[OBJECTIVE 4]`
- ⚠️ `[OBJECTIVE 5]` (did not happen — but came uncomfortably close)

**Success Metrics:**
- `[METRIC 1]:` `[TARGET]` (`[SIDE B]` competent defense)
- `[METRIC 2]:` `[TARGET]` (but after `[DURATION]` - `[SIDE A]` advantage)
- `[METRIC 3]:` `[TARGET]` (`[SIDE B]` competent combat performance)
- `[METRIC 4]:` `[TARGET]` (`[SIDE A]` succeeded despite `[SIDE B]` competence)
- `[METRIC 5]:` `[TARGET]` (boosted `[EFFECT]`)
- **Key Point:** `[SIDE B]` performs competently - `[SIDE A]` succeeds through `[SIDE A]` advantages, not `[SIDE B]` failures

---

## SIMULATION VARIABLES

### Random Factors

1. **Weather:**
   - `[CONDITION 1]:` `[EFFECT]`
   - `[CONDITION 2]:` `[EFFECT]`
   - `[CONDITION 3]:` `[EFFECT]`

2. **Intelligence:**
   - Detection timing: Variable
   - False reports: Can mislead
   - `[INTELLIGENCE FACTOR]:` Variable

3. **Combat:**
   - Skirmish outcomes: Variable
   - Casualties: Random within ranges
   - Morale: Can shift with events

4. **Logistics:**
   - `[LOGISTIC FACTOR 1]:` Variable (realistic resource constraints)
   - `[LOGISTIC FACTOR 2]:` Degrades randomly (realistic wear and tear)
   - `[LOGISTIC FACTOR 3]:` Random opportunities (realistic advantage)
   - **Note:** `[SIDE B]` logistics are professional - constraints are realistic, not failures

---

## MODELING OPPOSITION COMPETENCE

### Key Principles

1. **`[SIDE B]` Response Time:** `[X-Y]` hours is PROFESSIONAL, not slow
   - Detection: `[X-Y]` hours (realistic intelligence gathering)
   - Assessment: `[X-Y]` hours (professional command decision cycle)
   - Response: `[X-Y]` hours (realistic mobilization and movement)
   - **This is competent performance, not incompetence**

2. **`[SIDE B]` Coordination:** Multiple commands is REALISTIC challenge
   - `[COMMAND 1]:` Professional coordination
   - `[COMMAND 2]:` Competent within limitations
   - `[COMMAND 3]:` Professional performance
   - **Challenges are realistic command/control issues, not failures**

3. **`[SIDE B]` Mobility:** `[CONSTRAINT]` is PHYSICS
   - Not incompetence
   - Not poor planning
   - Realistic military constraint
   - **`[SIDE B]` uses `[COMPENSATION]` competently to compensate**

4. **`[SIDE B]` Intelligence:** Uncertainty is REALISTIC fog of war
   - Professional intelligence gathering
   - Realistic uncertainty (don't know exact route/objectives)
   - Competent assessment
   - **Not incompetence, realistic military challenge**

5. **`[SIDE B]` Combat Performance:** When engaged, `[SIDE B]` fights COMPETENTLY
   - Professional tactics
   - Skilled execution
   - Effective coordination
   - **`[SIDE B]` performs well in combat - `[SIDE A]` succeeds through advantages (`[LIST ADVANTAGES]`), not `[SIDE B]` failures**
   - **When `[SIDE B]` troops do catch `[SIDE A]` in a stand-up fight, they win — hard. The only question is whether they can force that fight before the clock runs out.**

### Why `[SIDE A]` Succeeds (Despite `[SIDE B]` Competence)

**`[SIDE A]` Advantages:**
1. **`[ADVANTAGE 1]:`** `[DESCRIPTION]`
2. **`[ADVANTAGE 2]:`** `[DESCRIPTION]`
3. **`[ADVANTAGE 3]:`** `[DESCRIPTION]`
4. **`[ADVANTAGE 4]:`** `[DESCRIPTION]`
5. **`[ADVANTAGE 5]:`** `[DESCRIPTION]`

**`[SIDE B]` Competence:**
1. **Professional Response:** Appropriate and timely
2. **Skilled Command:** `[COMMANDER]` and subordinates competent
3. **Effective `[ACTION]`:** Maintains pressure, forces engagement when possible
4. **Competent Combat:** Fights well when engaged
5. **Realistic Constraints:** Faces legitimate military challenges

**Conclusion:** `[SIDE A]` succeeds through inherent advantages and skill, NOT because `[SIDE B]` is incompetent. `[SIDE B]` performs professionally throughout - the operation succeeds despite competent opposition.

**Anti-Bias Failsafe:** If the simulation ever makes `[SIDE B]` forces look foolish, the parameters are wrong — rerun with tighter response times and better coordination until `[SIDE B]` feels lethal.

---

## NEXT STEPS FOR SIMULATION

### To Complete Framework:

1. **Determine Starting Point:**
   - Exact `[LOCATION]` details
   - Initial `[SIDE B]` dispositions
   - Terrain features

2. **Define Route/Plan:**
   - `[SIDE A]` intended route/plan
   - Key targets
   - Escape route/exit strategy

3. **Model `[SIDE B]` Response:**
   - `[COMMANDER]`'s exact decisions
   - Force movements
   - Blocking positions

4. **Run Simulation:**
   - Turn-by-turn execution
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
**Purpose:** Wargaming simulation of `[OPERATION NAME]` with realistic opposition  
**Canon Status:** Does NOT affect established canon - exploratory workshop only  
**Next Step:** Fill in specific details and run simulation turns to explore dynamics

