# Battle-Level Simulation Guide

**Purpose:** Guide for using the battle-level simulation template

**Status:** USER GUIDE  
**Version:** 1.0  
**Last Updated:** December 29, 2025

## OVERVIEW

The battle-level simulation template is a reusable tool for modeling tactical battles with realistic opposition. It operates at a much more granular level than campaign simulations:

- **Time Scale:** 1-2 hour turns (vs. 2-3 day turns for campaigns)
- **Unit Scale:** Brigade/Division level (vs. Corps/Army for campaigns)
- **Focus:** Tactical positioning, firepower, maneuver, morale
- **Terrain:** General features approach (no exact maps required)

## KEY DIFFERENCES FROM CAMPAIGN SIMULATION

### Time Scale
- **Campaign:** 2-3 day turns (strategic movement)
- **Battle:** 1-2 hour turns (tactical decisions)

### Unit Scale
- **Campaign:** Corps/Army level (thousands of men)
- **Battle:** Brigade/Division level (hundreds to low thousands)

### Focus
- **Campaign:** Movement, logistics, strategic decisions
- **Battle:** Positioning, firepower, tactical decisions

### Terrain
- **Campaign:** Regional features (rivers, mountains, cities)
- **Battle:** Tactical features (hills, woods, open ground, cover)

## TERRAIN KNOWLEDGE: NOT A LIMITING FACTOR

### The General Features Approach

**You don't need exact maps.** Use:

1. **General Terrain Types:**
   - Hills (high ground, elevation)
   - Woods (cover, concealment)
   - Open ground (movement, visibility)
   - Rivers/streams (barriers, crossing points)
   - Urban (buildings, streets)

2. **Relative Positioning:**
   - "Unit A is north of Unit B"
   - "Artillery on high ground"
   - "Woods provide cover for flank"
   - "River creates barrier"

3. **Tactical Effects:**
   - How terrain affects combat
   - Cover, concealment, movement
   - Firepower effectiveness
   - Not exact coordinates

### Example: Working Without Exact Maps

**Instead of:**
- "Unit at coordinates 42.123, -71.456"
- "Distance: 347.8 yards"
- "Elevation: 234 feet"

**Use:**
- "Unit positioned on high ground overlooking the approach"
- "Woods to the left provide cover for potential flank movement"
- "Open ground in front allows clear fields of fire"
- "River to the right creates natural barrier"

**Focus on tactical effects, not precise measurements.**

## WHEN TO USE

### Good Use Cases:

✅ **Tactical Battles:**
- Specific battles or engagements
- Multi-hour battles
- Brigade/Division level operations

✅ **Tactical Decision Analysis:**
- Testing tactical choices
- Exploring "what if" scenarios
- Understanding tactical dynamics

✅ **Opposition Modeling:**
- Ensuring opposition fights competently
- Avoiding bias
- Understanding realistic tactical constraints

✅ **Morale & Endurance:**
- Modeling unit degradation over time
- Understanding fatigue effects
- Assessing combat effectiveness

### Not Ideal For:

❌ **Strategic Operations:**
- Multi-day campaigns
- Theater-level operations
- Use campaign simulation instead

❌ **Very Small Engagements:**
- Skirmishes (too granular)
- Company-level actions
- Use narrative instead

## HOW TO USE THE TEMPLATE

### Step 1: Copy Template

1. Copy `tools/battle-simulation-template.md`
2. Rename to `analysis/military/[battle-name]-simulation-[date].md`
3. Update header with battle name and date

### Step 2: Define Terrain (General Features)

**Use general terrain types:**

1. **Identify Key Features:**
   - Hills, woods, open ground, rivers
   - High ground, low ground
   - Natural barriers, crossing points

2. **Define Relative Positions:**
   - "Unit A is north of Unit B"
   - "Artillery on high ground"
   - "Woods provide cover"

3. **Identify Tactical Effects:**
   - Cover, concealment
   - Movement modifiers
   - Firepower effectiveness

**Don't worry about exact coordinates or precise distances.**

### Step 3: Define Forces

**Brigade/Division Level:**

1. **Unit Composition:**
   - Brigade/Division names
   - Sizes (men, guns)
   - Commanders
   - Capabilities

2. **Initial Positions:**
   - Relative to landmarks
   - General positions
   - Formation types

3. **Capabilities:**
   - Firepower rating
   - Mobility rating
   - Morale rating
   - Endurance rating

### Step 4: Customize Mechanics

**Adjust for your specific battle:**

1. **Time Scale:**
   - 1 hour for intense battles
   - 2 hours for longer engagements
   - Adjust based on battle duration

2. **Movement Rates:**
   - Based on unit types
   - Terrain modifiers
   - Formation effects

3. **Combat Resolution:**
   - Firepower factors
   - Casualty rates
   - Morale effects

4. **Artillery:**
   - Range, effectiveness
   - Suppression effects
   - Counter-battery considerations

### Step 5: Define Phases

**Break battle into logical phases:**

1. **Phase 1:** Initial deployment/contact
2. **Phase 2:** Main engagement
3. **Phase 3:** Key decision points
4. **Phase 4:** Resolution/outcome

**Each phase should have:**
- Turn structure (1-2 hour chunks)
- Key actions
- Opposition response
- Decision points
- Possible outcomes

### Step 6: Model Opposition Competence

**Critical Principle:** Opposition fights competently.

**Key Elements:**
1. **Response Times:** Realistic (minutes), not slow
2. **Tactics:** Professional, not inept
3. **Combat Performance:** Competent, not weak
4. **Constraints:** Realistic tactical limitations, not failures

**Anti-Bias Failsafe:**
- If simulation makes opposition look foolish, parameters are wrong
- Rerun with better tactics and coordination
- Opposition should feel lethal, not incompetent

### Step 7: Run Simulation

**Turn-by-turn execution (1-2 hour chunks):**

1. **Intelligence Phase:** Assess situation
2. **Command Phase:** Issue orders
3. **Movement Phase:** Maneuver units
4. **Artillery Phase:** Fire, adjust positions
5. **Combat Phase:** Engage, resolve firefights
6. **Casualty Phase:** Assess casualties, check morale
7. **Assessment Phase:** Evaluate progress

**Document:**
- Decisions made
- Unit positions (relative)
- Combat outcomes
- Casualties
- Morale changes
- Key moments

### Step 8: Compare with Canon

**After simulation:**

1. **Compare outcomes** with established canon
2. **Identify discrepancies** or confirmations
3. **Assess plausibility** of narrative
4. **Note insights** for story development

**Remember:** Simulation is exploratory - does NOT change canon unless explicitly approved.

## KEY PRINCIPLES

### 1. Opposition Competence

**Always model opposition as competent:**
- Professional response times (minutes, not hours)
- Skilled tactical decisions
- Effective coordination
- Competent combat performance

**Success comes from:**
- Tactical advantages (position, timing, firepower)
- Skill and audacity
- Luck and circumstances

**NOT from:**
- Opposition incompetence
- Unrealistic failures
- Bias or caricature

### 2. Realistic Constraints

**Distinguish between:**
- **Realistic constraints:** Physics, command reality, legitimate limitations
- **Failures:** Incompetence, poor planning, mistakes

**Examples:**
- ✅ Units tire over hours = realistic
- ❌ Units don't fight = incompetence
- ✅ Command delays = realistic
- ❌ No command = failure

### 3. Terrain: General Features

**Don't need exact maps:**
- Use general terrain types
- Define relative positions
- Focus on tactical effects
- Not precise coordinates

### 4. Morale & Endurance

**Model degradation over time:**
- Units tire during long battles
- Casualties reduce effectiveness
- Morale affects combat performance
- Leadership matters

## TIPS FOR SUCCESS

### 1. Start with General Terrain

- Identify key terrain features
- Define relative positions
- Focus on tactical effects
- Don't worry about exact maps

### 2. Focus on Tactical Dynamics

- Positioning and maneuver
- Firepower and casualties
- Morale and endurance
- Decision points

### 3. Use Relative Positioning

- "North of X, south of Y"
- "On high ground"
- "In woods"
- "Behind river"

### 4. Model Time Realistically

- 1-2 hour turns
- Units tire over time
- Casualties accumulate
- Morale degrades

### 5. Test Alternatives

- Run multiple scenarios
- Explore "what if" questions
- Compare outcomes

## COMMON PITFALLS

### ❌ Requiring Exact Maps

**Problem:** Thinking you need precise terrain knowledge

**Solution:** Use general features and relative positioning

### ❌ Making Opposition Incompetent

**Problem:** Simulation makes opposition look foolish

**Solution:** Adjust parameters until opposition feels lethal

### ❌ Ignoring Time Effects

**Problem:** Units don't tire, casualties don't accumulate

**Solution:** Model endurance and casualty degradation

### ❌ Overcomplicating

**Problem:** Too many variables, too much detail

**Solution:** Focus on key tactical dynamics

## EXAMPLE STRUCTURE

**Battle: [Example]**

**Terrain:**
- High ground to the north (artillery position)
- Open ground in center (main engagement area)
- Woods to the west (cover for flank movement)
- River to the east (natural barrier)

**Forces:**
- Side A: 3 brigades, 2,000 men each, positioned on high ground
- Side B: 4 brigades, 1,800 men each, positioned in open ground

**Turns:**
- Turn 1 (08:00-09:00): Initial contact, artillery opens fire
- Turn 2 (09:00-11:00): Main engagement, units advance
- Turn 3 (11:00-13:00): Key decision point, flank movement
- Turn 4 (13:00-15:00): Resolution, outcome determined

## CONCLUSION

The battle-level simulation template is a powerful tool for understanding tactical battles, testing plausibility, and modeling competent opposition. You don't need exact terrain knowledge - use general features and relative positioning. Focus on tactical dynamics, not precise coordinates.

**Remember:** Success must feel earned, not handed. Opposition must feel lethal, not incompetent. Terrain knowledge is helpful but not required - use general features.

**Status:** ✅ **READY FOR USE**  
**Template:** `tools/battle-simulation-template.md`  
**Campaign Template:** `tools/wargaming-simulation-template.md` (for comparison)
