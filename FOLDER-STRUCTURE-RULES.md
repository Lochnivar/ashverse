# Folder Structure Rules - AshVerse Project

**Date:** December 9, 2025  
**Status:** FORMAL RULES - Update when structure changes

---

## FOLDER PURPOSE RULES

### `/books/` - Protected Story Content
**Purpose:** Actual book chapters and story content  
**Rule:** AI NEVER creates or edits files here directly (Golden Rule)  
**Status:** Protected - only user can modify

### `/edits/` - Book Edit Proposals Only
**Purpose:** Edit proposals and suggestions for book files  
**Rule:** ONLY book edit proposals. Analysis documents belong in `/analysis/`  
**Status:** Edit proposals only

### `/analysis/` - Working Analyses (Pre-Lock)
**Purpose:** Analysis documents, research, plausibility studies  
**Structure:** Organized by category:
- `/analysis/military/` - Military/tactical analyses
- `/analysis/economic/` - Economic analyses
- `/analysis/political/` - Political analyses
- `/analysis/consistency/` - Consistency checks, plausibility audits
- `/analysis/otl-divergence/` - OTL vs NTL comparisons

**Workflow:** Analysis → Review → Lock → Transcribe to `/world-building/`  
**Status:** Working documents (pre-lock)

### `/world-building/` - Locked Canon Only
**Purpose:** Locked canon documents (transcribed from approved analyses)  
**Structure:** Organized by topic (see Q&A document for proposed structure)  
**Rule:** Only locked canon goes here. Analysis stays in `/analysis/`  
**Status:** Locked canon repository

### `/characters/` - Character Profiles
**Purpose:** Character profiles and family trees  
**Rule:** Character profiles only. World-building context stays in `/world-building/`  
**Status:** Character documentation

### `/world-building/timelines/` - Locked Timeline Documents
**Purpose:** Locked timeline documents (transcribed from timeline analyses)  
**Rule:** Each locked timeline references its source analysis document  
**Status:** Locked timelines only

---

## FILE NAMING CONVENTIONS

### Analysis Files
**Format:** `[topic]-analysis-YYYY-MM-DD.md` or `[topic]-timeline-YYYY-MM-DD.md`  
**Example:** `northern-collapse-sequence-analysis-2025-12-05.md`

### Locked Canon Files
**Format:** Descriptive names WITHOUT "analysis" tags  
**Example:** `atlanta-campaign-1864-1865.md` (not `atlanta-campaign-analysis.md`)

### Edit Proposal Files
**Format:** `book-[number]-[description]-YYYY-MM-DD.md`  
**Example:** `book-01-chapter-01-edits-2025-12-05.md`

---

## WORKFLOW RULES

### Analysis → Lock → Transcribe Workflow

1. **Analysis Phase:** Create analysis in `/analysis/[category]/`
2. **Review & Approval:** User reviews analysis
3. **Lock & Transcribe:** Once approved, locked content transcribed into appropriate `/world-building/` file
4. **Reference:** Analysis file remains in `/analysis/` as reference/justification

**Key Principle:** Analysis files are working documents. Locked canon goes in `/world-building/`.

---

## FILE MOVEMENT RULES

### When to Move Files

**Move Analysis to `/analysis/`:**
- Any document with "analysis" in name
- Timeline analyses (before transcription)
- Consistency checks
- Plausibility studies
- OTL comparison documents

**Transcribe to `/world-building/`:**
- After analysis is approved/locked
- Extract locked content only
- Use descriptive name (no "analysis" tag)
- Reference source analysis document

**Keep in `/edits/`:**
- Edit proposals for book files only
- Scene suggestions
- Dialogue suggestions
- Book README updates

---

## FOLDER ORGANIZATION RULES

### `/world-building/` Subfolders (Proposed)

**Topic-Based Organization:**
- `/core/` - Core foundation documents
- `/timelines/` - Timeline documents (EXISTS)
- `/treaties/` - Treaty documents
- `/political/` - Political systems and parties
- `/california/` - All California-related documents
- `/military/` - Military and conflict documents
- `/economic/` - Economic systems
- `/regions/` - Regional/geographic documents
- `/thematic/` - Thematic framework documents
- `/meta/` - Meta-documents (indexes, maps, process)
- `/reference/` - Reference documents (optional)

**Rule:** Files organized by topic, not by date or analysis status

---

## REFERENCE RULES

### File References in Documents

**In Canon Refresher:**
- Point to locked files in `/world-building/`
- Reference analysis documents in `/analysis/` for detailed justification
- Use format: `[locked-file.md]` (Analysis: `[analysis-file.md]`)

**In Master Timeline:**
- Link to locked timeline files
- Reference analysis documents for detailed narratives

**In Analysis Documents:**
- Reference related world-building files
- Note when content has been transcribed

---

## STATUS MARKING RULES

### File Status Indicators

**In File Headers:**
- `✅ LOCKED CANON` - Locked, no changes
- `WORKSHOPPING` - Still being developed
- `REFERENCE` - Reference document, not locked canon
- `CONSOLIDATED` - Consolidated from multiple files

**In Folder Names:**
- No status indicators in folder names
- Status marked in file headers only

---

## DUPLICATE HANDLING RULES

### Complementary Files (Keep Both)
- General overview + specific detail (e.g., `mormon-deseret.md` + `mormon-deseret-banking-neutrality.md`)
- Concept + timeline (e.g., `cuba-mirror-effect.md` + `cuba-mirror-effect-timeline.md`)
- Master + detail (e.g., `native-super-states-master.md` + `native-super-states-embattled-survivors.md`)

### True Duplicates (Consolidate)
- If two files contain identical content, consolidate into one
- Keep the more comprehensive version
- Update references

---

## MAINTENANCE RULES

### When to Update Structure

**Update folder structure when:**
- New major topic emerges (e.g., new region, new war)
- Folder becomes too large (>20 files)
- User requests reorganization

**Update references when:**
- Files are moved to new folders
- Files are renamed
- Files are consolidated

**Update master index when:**
- New files added
- Files moved
- Files consolidated

---

## EXCEPTIONS

### Files That Stay in Root

**Project Root:**
- `canon-refresher-for-ai.md` - AI reference document
- `canon-master-document.md` - Comprehensive master document
- `README.md` - Project overview

**World-Building Root:**
- `world-building-master-index.md` - Navigation index
- `document-relationship-map.md` - Relationship map
- `master-timeline.md` - Master timeline reference

**Reason:** These are navigation/reference documents that should be easy to find

---

## ENFORCEMENT

**AI Assistants Must:**
- Follow folder structure rules
- Use correct naming conventions
- Update references when moving files
- Ask user before creating new folders

**User Reviews:**
- User approves folder structure changes
- User approves file movements
- User approves consolidations

---

**Status:** FORMAL RULES - Update when structure changes  
**Last Updated:** December 9, 2025

