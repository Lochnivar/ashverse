# Analyses Requiring Rerun/Reevaluation

**Date:** December 10, 2025  
**Purpose:** Identify analyses that need to be rerun due to timeline updates, file consolidation, or content changes

---

## CRITICAL PRIORITY: Timeline Date Changes

### 1. **Meade's Sacking Date Changed: November 1863 → August 1, 1863**

**Files Affected:**

#### **MUST RERUN:**
- ✅ `analysis/military/northern-collapse-sequence-analysis-2025-12-05.md`
  - **Issue:** Lists Meade sacked as "November 1863" (Event #5)
  - **Current Canon:** August 1, 1863 - "THE PANIC MOVE" (immediately after Longstreet returns to Virginia)
  - **Impact:** Changes sequence logic, Lincoln's learning curve analysis, narrative flow
  - **Priority:** CRITICAL - This is a foundational analysis

- ✅ `analysis/otl-divergence/otl-events-analysis-pod-to-war-end-2025-12-05.md`
  - **Issue:** Lists "November 1863 - Meade Sacked"
  - **Current Canon:** August 1, 1863
  - **Impact:** OTL divergence timeline incorrect
  - **Priority:** HIGH - Timeline accuracy

#### **NEEDS UPDATE:**
- ⚠️ `analysis/military/match-timeline-comprehensive-plausibility-analysis-2025-12-10.md`
  - **Status:** Already updated with "THE PANIC MOVE" framing (Event 3.1)
  - **Action:** Verify consistency with master timeline
  - **Priority:** MEDIUM - Verify only

- ⚠️ `analysis/military/grant-final-gamble-consistency-check-2025-12-05.md`
  - **Issue:** References "Meade relieved August 1863" but may need context update
  - **Action:** Verify "THE PANIC MOVE" context is included
  - **Priority:** LOW - Verify only

---

## HIGH PRIORITY: File Structure Changes (Old Paths → Master Files)

### 2. **References to Consolidated Timeline Files**

**Files Affected:**

#### **MUST UPDATE REFERENCES:**
- ✅ `analysis/military/pickett-raid-force-size-plausibility-2025-12-10.md`
  - **Issue:** References `world-building/timelines/master-timeline.md` (archived)
  - **New Location:** `world-building-master/06-timelines.md`
  - **Priority:** HIGH - Active analysis

- ✅ `analysis/military/casualty-plausibility-evaluation-2025-12-10.md`
  - **Issue:** References `world-building/timelines/rappahannock-rapidan-campaign-1863.md` (archived)
  - **New Location:** `world-building-master/06-timelines.md`
  - **Priority:** HIGH - Active analysis

- ✅ `analysis/military/pod-campaign-timeline-review-2025-12-09.md`
  - **Issue:** References old timeline file structure
  - **New Location:** `world-building-master/06-timelines.md`
  - **Priority:** MEDIUM - Review document

#### **NEEDS VERIFICATION:**
- ⚠️ `analysis/consistency/pickett-raid-date-analysis.md`
  - **Issue:** References multiple archived timeline files
  - **Action:** Verify all references updated or note archival status
  - **Priority:** MEDIUM - Consistency check

---

### 3. **References to Consolidated Economic Files**

**Files Affected:**

#### **MUST UPDATE REFERENCES:**
- ✅ `analysis/economic/slavery-death-mechanics-analysis-2025-12-05.md`
  - **Issue:** References `world-building/economic/northern-raids-comprehensive-catalog.md`
  - **Status:** File still exists (referenced, not consolidated)
  - **Action:** Verify hash still valid, update if needed
  - **Priority:** MEDIUM - Verify hash consistency

- ✅ `analysis/economic/raid-count-plausibility-analysis-2025-12-10.md`
  - **Issue:** References `world-building/economic/northern-raids-comprehensive-catalog.md`
  - **Status:** File still exists (referenced, not consolidated)
  - **Action:** Verify hash still valid
  - **Priority:** MEDIUM - Verify hash consistency

#### **NEEDS VERIFICATION:**
- ⚠️ `analysis/consistency/dependency-tracking-recommendations.md`
  - **Issue:** References old economic file paths
  - **Action:** Update to reference `world-building-master/02-economic-systems.md`
  - **Priority:** MEDIUM - System documentation

- ⚠️ `analysis/consistency/blockchain-hash-consistency-system-analysis.md`
  - **Issue:** References old economic file paths in examples
  - **Action:** Update examples to reference master files
  - **Priority:** LOW - Examples only

---

### 4. **References to Consolidated Political Files**

**Files Affected:**

#### **MUST UPDATE REFERENCES:**
- ✅ `analysis/README.md`
  - **Issue:** References old political file paths:
    - `world-building/political/presidents-and-parties.md`
    - `world-building/political/csa-presidents-gentry-vs-hayseed-1865-1939.md`
    - `world-building/political/ca-political-system-and-presidents.md`
  - **New Location:** `world-building-master/03-political-systems.md`
  - **Priority:** HIGH - Documentation file

#### **NEEDS VERIFICATION:**
- ⚠️ `analysis/consistency/dependency-tracking-recommendations.md`
  - **Issue:** References old political file paths
  - **Action:** Update to reference `world-building-master/03-political-systems.md`
  - **Priority:** MEDIUM - System documentation

- ⚠️ `analysis/consistency/butterfly-effect-implementation-summary.md`
  - **Issue:** References old political file paths
  - **Action:** Update to reference master files
  - **Priority:** LOW - Implementation summary

---

## MEDIUM PRIORITY: Content Updates from Consolidation

### 5. **Analyses Based on Now-Consolidated Content**

**Files Affected:**

#### **NEEDS VERIFICATION:**
- ⚠️ `analysis/military/grant-final-gamble-reconciled-analysis-2025-12-05.md`
  - **Issue:** May reference consolidated timeline content
  - **Action:** Verify all timeline references match `world-building-master/06-timelines.md`
  - **Priority:** MEDIUM - Verify consistency

- ⚠️ `analysis/military/atlanta-campaign-ntl-timeline-2025-12-05.md`
  - **Issue:** Timeline content now in master file
  - **Action:** Verify consistency with `world-building-master/06-timelines.md`
  - **Priority:** MEDIUM - Verify consistency

- ⚠️ `analysis/military/sherman-march-to-appomattox-option-c-modified-2025-12-05.md`
  - **Issue:** Timeline content now in master file
  - **Action:** Verify consistency with `world-building-master/06-timelines.md`
  - **Priority:** MEDIUM - Verify consistency

---

## LOW PRIORITY: Documentation Updates

### 6. **System Documentation Files**

**Files Affected:**

#### **NEEDS UPDATE (Examples Only):**
- ⚠️ `analysis/organization/ai-optimized-organization-scheme.md`
  - **Issue:** References old file structure in examples
  - **Action:** Update examples to reference master files
  - **Priority:** LOW - Examples/documentation only

- ⚠️ `analysis/consistency/unified-consolidation-and-ai-optimization-plan.md`
  - **Issue:** References old file structure
  - **Action:** Update to reference master files
  - **Priority:** LOW - Planning document

---

## SUMMARY BY PRIORITY

### **CRITICAL (Must Rerun):**
1. `analysis/military/northern-collapse-sequence-analysis-2025-12-05.md` - Meade sacking date wrong
2. `analysis/otl-divergence/otl-events-analysis-pod-to-war-end-2025-12-05.md` - Meade sacking date wrong

### **HIGH (Must Update References):**
3. `analysis/military/pickett-raid-force-size-plausibility-2025-12-10.md` - Old timeline path
4. `analysis/military/casualty-plausibility-evaluation-2025-12-10.md` - Old timeline path
5. `analysis/README.md` - Old political file paths

### **MEDIUM (Verify/Update):**
6. `analysis/military/match-timeline-comprehensive-plausibility-analysis-2025-12-10.md` - Verify consistency
7. `analysis/military/grant-final-gamble-consistency-check-2025-12-05.md` - Verify context
8. `analysis/military/pod-campaign-timeline-review-2025-12-09.md` - Update references
9. `analysis/consistency/pickett-raid-date-analysis.md` - Verify references
10. `analysis/economic/slavery-death-mechanics-analysis-2025-12-05.md` - Verify hash
11. `analysis/economic/raid-count-plausibility-analysis-2025-12-10.md` - Verify hash
12. `analysis/consistency/dependency-tracking-recommendations.md` - Update paths
13. `analysis/military/grant-final-gamble-reconciled-analysis-2025-12-05.md` - Verify consistency
14. `analysis/military/atlanta-campaign-ntl-timeline-2025-12-05.md` - Verify consistency
15. `analysis/military/sherman-march-to-appomattox-option-c-modified-2025-12-05.md` - Verify consistency

### **LOW (Documentation Only):**
16. `analysis/consistency/blockchain-hash-consistency-system-analysis.md` - Update examples
17. `analysis/consistency/butterfly-effect-implementation-summary.md` - Update paths
18. `analysis/organization/ai-optimized-organization-scheme.md` - Update examples
19. `analysis/consistency/unified-consolidation-and-ai-optimization-plan.md` - Update paths

---

## KEY CHANGES TO VERIFY

### **Timeline Changes:**
- ✅ Meade sacked: **November 1863** → **August 1, 1863** ("THE PANIC MOVE")
- ✅ Lincoln's learning curve: Now explicitly includes "panic = weakness" lesson
- ✅ Sequence logic: Meade sacking happens immediately after Longstreet returns to Virginia, not after Hagerstown

### **File Structure Changes:**
- ✅ Timeline files → `world-building-master/06-timelines.md`
- ✅ Economic files → `world-building-master/02-economic-systems.md`
- ✅ Political files → `world-building-master/03-political-systems.md`
- ✅ Military files → `world-building-master/04-military-history.md`
- ✅ Regional files → `world-building-master/05-regions-and-nations.md`

### **Content Updates:**
- ✅ All master files now have hash tracking
- ✅ All master files marked as "LOCKED"
- ✅ Purpose statements updated to "Single source of truth"

---

## RECOMMENDED ACTION PLAN

### **Phase 1: Critical Fixes (Immediate)**
1. Rerun `northern-collapse-sequence-analysis-2025-12-05.md` with correct Meade sacking date
2. Update `otl-events-analysis-pod-to-war-end-2025-12-05.md` with correct Meade sacking date

### **Phase 2: Reference Updates (High Priority)**
3. Update all file path references to master files
4. Update `analysis/README.md` with new file structure

### **Phase 3: Verification (Medium Priority)**
5. Verify all analyses match consolidated master files
6. Verify hash consistency where applicable

### **Phase 4: Documentation (Low Priority)**
7. Update examples in system documentation
8. Update planning documents with new structure

---

**Status:** Analysis complete  
**Next Steps:** Prioritize critical fixes, then proceed with reference updates

