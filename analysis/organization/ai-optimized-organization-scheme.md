# AI-Optimized Organization Scheme

**Date:** December 10, 2025  
**Status:** PROPOSAL  
**Purpose:** Organize project data for optimal AI access, reading, and editing

---

## PRINCIPLES FOR AI-OPTIMIZED ORGANIZATION

### 1. **File Size Sweet Spot**
- **Optimal:** 500-2000 lines (~10-50KB)
- **Too small:** Fragmentation, hard to find related info
- **Too large:** Context limits, harder to edit precisely
- **Exception:** Master consolidated files can be larger (2000-5000 lines) if well-structured

### 2. **Clear Naming Conventions**
- **Prefixes indicate type:** `master-`, `analysis-`, `character-`, `timeline-`
- **Numbers indicate order:** `01-core-foundation.md`, `02-economic-systems.md`
- **Dates indicate versions:** `analysis-2025-12-10.md`
- **Descriptive names:** `northern-raids-comprehensive-catalog.md` (not `raids.md`)

### 3. **Two-Tier Structure**
- **Master Documents:** Consolidated, comprehensive views (for reading/searching)
- **Detail Documents:** Granular, focused files (for editing/specific work)
- **Relationship:** Master documents reference detail documents, detail documents link back

### 4. **Consistent Metadata**
Every file should have:
- **Status:** LOCKED / ACTIVE / DRAFT / ARCHIVED
- **Date:** Last updated
- **Dependencies:** Hash-tracked dependencies (we just set this up)
- **Purpose:** What this file is for

### 5. **Index Files**
- **Master indexes:** List all files in a category
- **Relationship maps:** Show how files connect
- **Quick reference:** Essential facts only

---

## RECOMMENDED STRUCTURE

### Tier 1: Master Documents (Consolidated Views)

**Location:** `world-building-master/` ✅ (You're already doing this!)

**Purpose:** 
- Single source of truth for major topics
- Easy to search semantically
- Comprehensive context in one place
- Reference documents for AI

**Structure:**
```
world-building-master/
├── 01-core-foundation.md          # POD, premise, settings
├── 02-economic-systems.md         # All economic systems
├── 03-political-systems.md        # All political systems
├── 04-military-history.md         # All military events
├── 05-regions-and-nations.md      # All geographic/political entities
├── 06-timelines.md                # All timelines consolidated
├── 07-thematic-framework.md       # Themes and narrative framework
└── 08-reference-data.md           # Quick reference facts
```

**File Size:** 1000-5000 lines each (comprehensive but structured)

**Benefits for AI:**
- Can read entire topic area in one file
- Understands relationships within topic
- Can search semantically across comprehensive content
- Clear boundaries (one file = one major topic)

---

### Tier 2: Detail Documents (Granular Work)

**Location:** `world-building/` (organized by topic)

**Purpose:**
- Specific, focused information
- Easy to edit without affecting other topics
- Detailed analysis and development
- Source material for master documents

**Structure:**
```
world-building/
├── economic/
│   ├── northern-raids-comprehensive-catalog.md
│   ├── slavery-and-raids-master.md
│   └── economic-systems-master.md
├── political/
│   ├── csa-presidents-gentry-vs-hayseed-1865-1939.md
│   └── presidential-pairs-master-reference.md
├── military/
│   └── [specific campaigns/events]
└── [other topics]
```

**File Size:** 200-1500 lines each (focused, manageable)

**Benefits for AI:**
- Can edit specific topic without loading entire domain
- Clear scope (one file = one specific topic)
- Easy to update master documents from detail files
- Can work on granular details efficiently

---

### Tier 3: Analysis Documents

**Location:** `analysis/` (organized by type)

**Purpose:**
- Analysis and evaluation
- Consistency checks
- Plausibility studies
- Cross-cutting concerns

**Structure:**
```
analysis/
├── economic/
│   ├── raid-count-plausibility-analysis-2025-12-10.md
│   └── [other economic analyses]
├── political/
│   └── [political analyses]
├── consistency/
│   ├── comprehensive-consistency-audit-2025-12-10.md
│   └── [consistency checks]
└── [other analysis types]
```

**File Size:** 300-2000 lines (analysis depth varies)

**Benefits for AI:**
- Separates analysis from source material
- Can reference multiple sources
- Clear purpose (analysis vs. canon)
- Easy to find related analyses

---

### Tier 4: Character Documents

**Location:** `characters/` (organized by affiliation)

**Purpose:**
- Character profiles and arcs
- Character relationships
- Character-specific world-building

**Structure:**
```
characters/
├── union/
│   └── frank-a-haskell.md
├── confederate/
│   └── [confederate characters]
└── [other categories]
```

**File Size:** 200-800 lines (character depth varies)

**Benefits for AI:**
- Clear character boundaries
- Easy to find character-specific info
- Can track character arcs separately
- Links to world-building naturally

---

### Tier 5: Working Documents

**Location:** `edits/`, `compendium/`, `books/`

**Purpose:**
- Active work in progress
- Drafts and suggestions
- Final compiled content

**Structure:** Keep current organization

**File Size:** Varies by purpose

**Benefits for AI:**
- Clear separation of work-in-progress
- Easy to identify draft vs. final
- Can work on edits without touching source

---

## NAMING CONVENTIONS

### Master Documents
- Format: `##-topic-name.md` (e.g., `01-core-foundation.md`)
- Numbers indicate order/priority
- Descriptive topic names

### Detail Documents
- Format: `topic-specific-name.md` (e.g., `northern-raids-comprehensive-catalog.md`)
- Descriptive, specific names
- No numbers (unless chronological)

### Analysis Documents
- Format: `topic-analysis-type-YYYY-MM-DD.md` (e.g., `raid-count-plausibility-analysis-2025-12-10.md`)
- Date indicates version/snapshot
- Type indicates analysis purpose

### Character Documents
- Format: `character-name.md` (e.g., `frank-a-haskell.md`)
- Simple, clear names
- Organized by folder (union/confederate/etc.)

---

## METADATA STANDARD

Every file should start with:

```markdown
# Document Title

**Date:** YYYY-MM-DD  
**Status:** LOCKED / ACTIVE / DRAFT / ARCHIVED  
**Purpose:** [What this file is for]

---

[Content]

---

## DOCUMENT DEPENDENCIES

[Hash-tracked dependencies]

**This Document's Hash:** `[hash]`  
**Last Updated:** YYYY-MM-DD
```

**Benefits:**
- AI understands file status immediately
- Can check dependencies automatically
- Knows when file was last updated
- Understands file purpose

---

## INDEX FILES

### Master Index Files

**Location:** Root or topic folders

**Purpose:**
- List all files in category
- Show relationships
- Quick reference

**Examples:**
- `world-building-master-index.md` - Lists all master documents
- `characters/cast-list-consolidated.md` - Lists all characters
- `analysis/consistency/consistency-checks-master-index.md` - Lists all consistency checks

**Format:**
```markdown
# Master Index: [Category]

## Files

| File | Purpose | Status | Last Updated |
|------|---------|--------|--------------|
| file1.md | Purpose | ACTIVE | 2025-12-10 |
| file2.md | Purpose | LOCKED | 2025-12-05 |

## Relationships

- file1.md → references → file2.md
- file2.md → referenced by → file1.md
```

**Benefits:**
- AI can quickly find all files in category
- Understands relationships
- Can navigate efficiently

---

## RELATIONSHIP TRACKING

### Dependency Links
- **Hash tracking:** We just set this up
- **Explicit links:** Markdown links between files
- **Index files:** Show relationships

### Cross-References
- **In master documents:** Reference detail documents
- **In detail documents:** Link back to master documents
- **In analysis:** Reference source documents

**Example:**
```markdown
## Related Documents
- [Master Document](../world-building-master/02-economic-systems.md)
- [Detail Document](../world-building/economic/northern-raids-comprehensive-catalog.md)
- [Analysis](../analysis/economic/raid-count-plausibility-analysis-2025-12-10.md)
```

---

## FILE SIZE GUIDELINES

### Master Documents
- **Target:** 2000-5000 lines
- **Maximum:** 8000 lines (then split)
- **Minimum:** 1000 lines (consolidate if smaller)

### Detail Documents
- **Target:** 500-1500 lines
- **Maximum:** 2500 lines (then split by subtopic)
- **Minimum:** 200 lines (consolidate if smaller)

### Analysis Documents
- **Target:** 500-2000 lines
- **Maximum:** 3000 lines (then split by analysis type)
- **Minimum:** 300 lines (consolidate if smaller)

### Character Documents
- **Target:** 300-800 lines
- **Maximum:** 1500 lines (then split by time period/arc)
- **Minimum:** 200 lines (consolidate if smaller)

**Rationale:**
- AI context limits favor moderate sizes
- Too small = fragmentation
- Too large = hard to edit precisely
- Sweet spot = comprehensive but manageable

---

## ORGANIZATION PATTERNS

### Pattern 1: Master → Detail
```
world-building-master/02-economic-systems.md (master)
  ↓ references
world-building/economic/northern-raids-comprehensive-catalog.md (detail)
world-building/economic/slavery-and-raids-master.md (detail)
```

**When to use:**
- Major topic areas
- Need comprehensive view AND granular detail
- Master consolidates, detail provides depth

### Pattern 2: Source → Analysis
```
world-building/economic/northern-raids-comprehensive-catalog.md (source)
  ↓ analyzed by
analysis/economic/raid-count-plausibility-analysis-2025-12-10.md (analysis)
```

**When to use:**
- Analysis of source material
- Evaluation and plausibility checks
- Cross-cutting concerns

### Pattern 3: Source → Character
```
world-building/01-core-foundation.md (source)
  ↓ referenced by
characters/union/frank-a-haskell.md (character)
```

**When to use:**
- Characters depend on world-building
- Character-specific world-building
- Character arcs reference events

---

## RECOMMENDATIONS FOR YOUR PROJECT

### ✅ Already Optimal
1. **Master documents in `world-building-master/`** - Perfect!
2. **Detail documents in `world-building/`** - Good organization
3. **Analysis separated** - Clear separation
4. **Characters organized** - Logical grouping

### 🔧 Improvements to Consider

1. **Add metadata headers** to all files:
   - Date, Status, Purpose
   - Dependencies section
   - Document hash

2. **Create master index files:**
   - `world-building-master-index.md` - List all master docs
   - `world-building-index.md` - List all detail docs
   - `analysis-index.md` - List all analyses

3. **Standardize file naming:**
   - Master: `##-topic-name.md`
   - Detail: `topic-specific-name.md`
   - Analysis: `topic-analysis-type-YYYY-MM-DD.md`

4. **Add relationship tracking:**
   - Cross-references in files
   - Index files show relationships
   - Dependency hashes track changes

5. **Consider file sizes:**
   - Split files > 5000 lines
   - Consolidate files < 200 lines
   - Aim for 500-2000 line sweet spot

---

## AI ACCESS PATTERNS

### Reading (Search/Understand)
- **Semantic search:** Works across all files
- **Master documents:** Comprehensive context
- **Index files:** Quick navigation
- **Metadata:** Understand file status/purpose

### Editing (Modify/Update)
- **Detail documents:** Focused edits
- **Master documents:** Update when detail changes
- **Dependencies:** Update hashes automatically
- **Analysis:** Update when sources change

### Creating (New Content)
- **Templates:** Use existing structure
- **Naming:** Follow conventions
- **Metadata:** Add standard headers
- **Dependencies:** Track from start

---

## QUICK REFERENCE

### File Organization
- **Master:** `world-building-master/##-topic.md` (2000-5000 lines)
- **Detail:** `world-building/topic/specific-name.md` (500-1500 lines)
- **Analysis:** `analysis/type/topic-analysis-YYYY-MM-DD.md` (500-2000 lines)
- **Character:** `characters/category/name.md` (300-800 lines)

### Metadata Standard
- Date, Status, Purpose at top
- Dependencies section at bottom
- Document hash tracked

### Naming Conventions
- Master: Numbered, descriptive
- Detail: Descriptive, specific
- Analysis: Dated, typed
- Character: Simple name

---

## IMPLEMENTATION PRIORITY

### Phase 1: Metadata (High Value, Low Effort)
1. Add metadata headers to all files
2. Add dependency tracking sections
3. Standardize status indicators

### Phase 2: Index Files (High Value, Medium Effort)
1. Create master index files
2. Add relationship maps
3. Update as files change

### Phase 3: Naming Standardization (Medium Value, Medium Effort)
1. Rename files to follow conventions
2. Update all references
3. Document conventions

### Phase 4: File Size Optimization (Low Priority)
1. Split oversized files
2. Consolidate undersized files
3. Monitor as project grows

---

**Status:** PROPOSAL - Ready for Review  
**Next Step:** Decide on implementation priority

