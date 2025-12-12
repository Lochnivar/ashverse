# Wargaming Simulation Guide

**Purpose:** Guide for using the wargaming simulation template

**Status:** USER GUIDE  
**Version:** 1.0  
**Last Updated:** December 10, 2025

---

## OVERVIEW

The wargaming simulation template is a reusable tool for modeling military operations with realistic opposition. It was developed during the Pickett's Raid analysis and proved valuable for:

1. **Understanding dynamics** of complex military operations
2. **Testing plausibility** of narrative outcomes
3. **Identifying key decision points** and their consequences
4. **Modeling competent opposition** (anti-bias mechanism)
5. **Exploring alternatives** without affecting canon

---

## WHEN TO USE

### Good Use Cases:

✅ **Complex Military Operations:**
- Raids, campaigns, battles
- Multi-phase operations
- Operations with multiple forces

✅ **Plausibility Testing:**
- Testing if a narrative outcome is realistic
- Exploring "what if" scenarios
- Validating strategic decisions

✅ **Opposition Modeling:**
- Ensuring opposition is portrayed competently
- Avoiding "Lost Cause" or other bias
- Understanding realistic constraints

✅ **Decision Point Analysis:**
- Identifying critical moments
- Exploring alternative choices
- Understanding consequences

### Not Ideal For:

❌ **Simple Operations:**
- Single-day battles
- Straightforward engagements
- Operations with minimal complexity

❌ **Established Canon:**
- Operations already locked in canon
- Historical events with clear outcomes
- Operations where simulation won't add value

---

## HOW TO USE THE TEMPLATE

### Step 1: Copy Template

1. Copy `tools/wargaming-simulation-template.md`
2. Rename to `analysis/military/[operation-name]-simulation-[date].md`
3. Update header with operation name and date

### Step 2: Fill in Operation Details

**Replace all `[PLACEHOLDER]` sections:**

1. **Operation Name:** `[OPERATION NAME]`
2. **Dates:** `[DATES]`
3. **Forces:** `[SIDE A]` and `[SIDE B]` (e.g., "Confederate" and "Union")
4. **Commanders:** Names and ranks
5. **Force Sizes:** Numbers and composition
6. **Objectives:** Primary, secondary, tertiary
7. **Geographic Area:** Map scale and region

### Step 3: Customize Mechanics

**Adjust for your specific operation:**

1. **Time Scale:** 
   - Daily for short operations
   - 2-3 day turns for medium operations
   - Weekly for long campaigns

2. **Movement Rates:**
   - Based on force types (cavalry, infantry, mounted)
   - Terrain modifiers
   - Weather effects

3. **Combat Resolution:**
   - Scale appropriate to operation
   - Casualty ranges
   - Outcome probabilities

4. **Logistics:**
   - Supply methods
   - Endurance limits
   - Forage requirements

### Step 4: Define Phases

**Break operation into logical phases:**

1. **Phase 1:** Initial movement/crossing
2. **Phase 2:** Main operation
3. **Phase 3:** Opposition response
4. **Phase 4:** Withdrawal/escape
5. **Phase 5:** Final outcome

**Each phase should have:**
- Turn structure
- Key actions
- Opposition response
- Decision points
- Possible outcomes

### Step 5: Model Opposition Competence

**Critical Principle:** Opposition is competent and professional.

**Key Elements:**
1. **Response Times:** Realistic (24-48 hours), not slow
2. **Coordination:** Professional, not chaotic
3. **Combat Performance:** Competent, not inept
4. **Constraints:** Realistic military limitations, not failures

**Anti-Bias Failsafe:**
- If simulation makes opposition look foolish, parameters are wrong
- Rerun with tighter response times and better coordination
- Opposition should feel lethal, not incompetent

### Step 6: Run Simulation

**Turn-by-turn execution:**

1. **Intelligence Phase:** Gather information
2. **Command Phase:** Make decisions
3. **Movement Phase:** Move forces
4. **Combat Phase:** Resolve engagements
5. **Logistics Phase:** Check supply/endurance
6. **Assessment Phase:** Evaluate progress

**Document:**
- Decisions made
- Outcomes
- Casualties
- Key moments

### Step 7: Compare with Canon

**After simulation:**

1. **Compare outcomes** with established canon
2. **Identify discrepancies** or confirmations
3. **Assess plausibility** of narrative
4. **Note insights** for story development

**Remember:** Simulation is exploratory - does NOT change canon unless explicitly approved.

---

## KEY PRINCIPLES

### 1. Opposition Competence

**Always model opposition as competent:**
- Professional response times
- Skilled command decisions
- Effective coordination
- Competent combat performance

**Success comes from:**
- Inherent advantages (mobility, initiative, timing)
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
- ✅ Infantry slower than cavalry = physics
- ❌ Infantry doesn't pursue = incompetence
- ✅ 24-hour response time = professional
- ❌ 24-hour response time = slow (if context requires faster)

### 3. Anti-Bias Mechanism

**Built-in failsafe:**
- If opposition looks foolish, parameters are wrong
- Adjust until opposition feels lethal
- Success must feel earned, not handed

**Test:**
- Would a competent commander do this?
- Are constraints realistic or artificial?
- Does success feel earned?

### 4. Exploratory Nature

**Simulation is:**
- ✅ Tool for understanding
- ✅ Method for testing plausibility
- ✅ Way to explore alternatives
- ✅ Workshop for narrative development

**Simulation is NOT:**
- ❌ Canon unless explicitly approved
- ❌ Replacement for established facts
- ❌ Way to change locked events
- ❌ Final word on outcomes

---

## EXAMPLE: PICKETT'S RAID

**Reference:** `analysis/military/pickett-raid-wargame-simulation-2025-12-10.md`

**Key Features:**
- 10-turn simulation (2-3 day turns)
- Realistic Union opposition modeling
- Anti-bias mechanisms built in
- Phase-by-phase structure
- Decision points identified
- Victory conditions defined

**Result:**
- Validated narrative plausibility
- Identified key moments
- Confirmed Union competence
- Explored alternatives
- Enhanced understanding of dynamics

---

## TIPS FOR SUCCESS

### 1. Start Simple

- Begin with basic framework
- Add complexity as needed
- Don't overcomplicate initially

### 2. Focus on Key Dynamics

- Identify critical decision points
- Model key interactions
- Don't get lost in details

### 3. Test Alternatives

- Run multiple scenarios
- Explore "what if" questions
- Compare outcomes

### 4. Document Insights

- Note key findings
- Record decision points
- Capture narrative moments

### 5. Validate Against Canon

- Compare with established facts
- Identify discrepancies
- Assess plausibility

---

## COMMON PITFALLS

### ❌ Making Opposition Incompetent

**Problem:** Simulation makes opposition look foolish

**Solution:** Adjust parameters until opposition feels lethal

### ❌ Overcomplicating

**Problem:** Too many variables, too much detail

**Solution:** Focus on key dynamics, simplify where possible

### ❌ Ignoring Realistic Constraints

**Problem:** Treating all limitations as failures

**Solution:** Distinguish realistic constraints from failures

### ❌ Changing Canon

**Problem:** Using simulation to change established facts

**Solution:** Remember simulation is exploratory, not canonical

---

## CONCLUSION

The wargaming simulation template is a powerful tool for understanding military operations, testing plausibility, and modeling competent opposition. Use it wisely, keep it exploratory, and always model opposition as professional and competent.

**Remember:** Success must feel earned, not handed. Opposition must feel lethal, not incompetent. Simulation is a tool, not canon.

---

**Status:** ✅ **READY FOR USE**  
**Template:** `tools/wargaming-simulation-template.md`  
**Questions:** See example in `analysis/military/pickett-raid-wargame-simulation-2025-12-10.md`

