"""
Split northern-raids-comprehensive-catalog.md into manageable parts.

Structure:
- Index file: Overview, summary stats, links
- Phase 1: Organized Raids (1865-1867)
- Phase 2: Decentralized/Viral Raids (1867-1894)
"""

from pathlib import Path
import tiktoken

def count_tokens(text):
    enc = tiktoken.encoding_for_model('gpt-4')
    return len(enc.encode(text))

def split_file(input_path, dry_run=True):
    content = Path(input_path).read_text(encoding='utf-8', errors='ignore')
    lines = content.split('\n')
    
    print(f"Original file: {len(lines)} lines, {count_tokens(content):,} tokens")
    print()
    
    # Find section boundaries
    phase1_start = None
    phase2_start = None
    analysis_start = None
    
    for i, line in enumerate(lines):
        if line.startswith('## PHASE 1:'):
            phase1_start = i
        elif line.startswith('## PHASE 2:'):
            phase2_start = i
        elif line.startswith('## SUCCESS RATE ANALYSIS'):
            analysis_start = i
    
    print(f"Found sections:")
    print(f"  Header + Signature: lines 1-{phase1_start}")
    print(f"  Phase 1: lines {phase1_start+1}-{phase2_start}")
    print(f"  Phase 2: lines {phase2_start+1}-{analysis_start}")
    print(f"  Analysis: lines {analysis_start+1}-{len(lines)}")
    print()
    
    # Extract sections
    header = '\n'.join(lines[:phase1_start])
    phase1 = '\n'.join(lines[phase1_start:phase2_start])
    phase2 = '\n'.join(lines[phase2_start:analysis_start])
    analysis = '\n'.join(lines[analysis_start:])
    
    # Create index file
    index_content = f"""# Northern Raids Catalog - Index

**Date:** December 29, 2025  
**Status:** COMPREHENSIVE DATASET (Split for AI processing)  
**Original:** northern-raids-comprehensive-catalog.md

## Overview

**Total Raids:** 350-450 (Phase 1: ~50, Phase 2: 300-400)  
**Total Impact:** $1.6 billion (1865 dollars), 200,000 slaves freed  
**Period:** 1865-1894 (29 years)

## Catalog Files

1. **[Phase 1: Organized Raids (1865-1867)](northern-raids-phase-1.md)**
   - ~50 raids, organized cells, Committee of Nine coordination
   - Includes signature raids and named operations

2. **[Phase 2: Decentralized Raids (1867-1894)](northern-raids-phase-2.md)**
   - 300-400 raids, viral spread, local initiative
   - Includes "accidental renege" raids and decline period

## Signature Raids (Emotional Anchors)

{header.split('## SIGNATURE RAIDS')[1].split('## PHASE 1')[0] if '## SIGNATURE RAIDS' in header else '(See Phase 1 file)'}

## Quick Statistics

{analysis}
"""

    # Create Phase 1 file
    phase1_content = f"""# Northern Raids - Phase 1: Organized Raids (1865-1867)

**Part of:** Northern Raids Comprehensive Catalog  
**See also:** [Index](northern-raids-index.md) | [Phase 2](northern-raids-phase-2.md)

---

{phase1}
"""

    # Create Phase 2 file
    phase2_content = f"""# Northern Raids - Phase 2: Decentralized Raids (1867-1894)

**Part of:** Northern Raids Comprehensive Catalog  
**See also:** [Index](northern-raids-index.md) | [Phase 1](northern-raids-phase-1.md)

---

{phase2}
"""

    # Calculate tokens
    print("Split results:")
    print(f"  Index:   {count_tokens(index_content):,} tokens")
    print(f"  Phase 1: {count_tokens(phase1_content):,} tokens")
    print(f"  Phase 2: {count_tokens(phase2_content):,} tokens")
    print(f"  Total:   {count_tokens(index_content) + count_tokens(phase1_content) + count_tokens(phase2_content):,} tokens")
    print()
    
    if not dry_run:
        base_dir = Path(input_path).parent
        
        # Write split files
        (base_dir / 'northern-raids-index.md').write_text(index_content, encoding='utf-8')
        (base_dir / 'northern-raids-phase-1.md').write_text(phase1_content, encoding='utf-8')
        (base_dir / 'northern-raids-phase-2.md').write_text(phase2_content, encoding='utf-8')
        
        # Remove original
        Path(input_path).unlink()
        
        print("Files created:")
        print(f"  {base_dir / 'northern-raids-index.md'}")
        print(f"  {base_dir / 'northern-raids-phase-1.md'}")
        print(f"  {base_dir / 'northern-raids-phase-2.md'}")
        print()
        print("Original file removed.")
    else:
        print("[DRY RUN - no files written]")

if __name__ == "__main__":
    import sys
    dry_run = '--apply' not in sys.argv
    
    print("=" * 60)
    print("NORTHERN RAIDS SPLIT")
    print("=" * 60)
    print()
    
    split_file("world-building/reference/northern-raids-comprehensive-catalog.md", dry_run=dry_run)

