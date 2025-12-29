"""
Split rapidan-campaign-timeline.md into 4 parts + index.

The file already has natural breaks at:
- Line 1: Part 1 (August)
- Line 894: Part 2 (September)
- Line 1766: Part 3 (October 10-23)
- Line 2930: Part 4 (October 24 - December)
"""

import re
from pathlib import Path
import tiktoken

def count_tokens(text):
    enc = tiktoken.encoding_for_model('gpt-4')
    return len(enc.encode(text))

def split_file(input_path, output_dir, dry_run=True):
    """Split the rapidan file into parts."""
    
    content = Path(input_path).read_text(encoding='utf-8', errors='ignore')
    lines = content.split('\n')
    
    original_tokens = count_tokens(content)
    original_lines = len(lines)
    
    print(f"Original file: {original_lines:,} lines, {original_tokens:,} tokens")
    print()
    
    # Find part boundaries
    part_starts = []
    for i, line in enumerate(lines):
        if line.startswith('# Rappahannock-Rapidan Campaign - Part'):
            part_starts.append(i)
    
    print(f"Found {len(part_starts)} parts at lines: {[s+1 for s in part_starts]}")
    print()
    
    # Extract each part
    parts = []
    for i, start in enumerate(part_starts):
        end = part_starts[i + 1] if i + 1 < len(part_starts) else len(lines)
        part_content = '\n'.join(lines[start:end])
        
        # Extract part number and title from first line
        first_line = lines[start]
        match = re.search(r'Part (\d+): (.+?) \(', first_line)
        if match:
            part_num = match.group(1)
            part_title = match.group(2)
        else:
            part_num = str(i + 1)
            part_title = f"Part {i + 1}"
        
        parts.append({
            'num': part_num,
            'title': part_title,
            'content': part_content,
            'lines': end - start,
            'tokens': count_tokens(part_content),
        })
    
    # Print summary
    print("Parts breakdown:")
    print(f"{'Part':<6} {'Title':<40} {'Lines':>8} {'Tokens':>10}")
    print("-" * 70)
    for p in parts:
        print(f"Part {p['num']:<3} {p['title']:<40} {p['lines']:>8,} {p['tokens']:>10,}")
    print("-" * 70)
    total_tokens = sum(p['tokens'] for p in parts)
    print(f"{'Total':<50} {sum(p['lines'] for p in parts):>8,} {total_tokens:>10,}")
    print()
    
    # Create index file content
    index_content = """# Rappahannock-Rapidan Campaign Index

**Campaign Period:** August 1 - December 31, 1863  
**Union Commander:** Gouverneur Warren (replaces Meade August 3)  
**Confederate Commander:** James Longstreet  
**Outcome:** Union strategic defeat; Warren relieved December 15

---

## Campaign Overview

The Rappahannock-Rapidan Campaign (August-December 1863) was the first major Union offensive after the POD Campaign disaster. Under intense political pressure, newly-appointed commander Gouverneur Warren attempted to break Longstreet's fortified line along the Rappahannock-Rapidan rivers.

The campaign ended in catastrophic Union defeat, with the Army of the Potomac suffering approximately 47,000 casualties while inflicting only 12,000 on the Confederates.

---

## Parts

| Part | Period | File | Tokens |
|------|--------|------|--------|
"""
    
    for p in parts:
        filename = f"rapidan-campaign-part-{p['num']}.md"
        index_content += f"| Part {p['num']} | {p['title']} | [{filename}]({filename}) | ~{p['tokens']:,} |\n"
    
    index_content += """
---

## Key Events (Quick Reference)

### August 1863 (Part 1)
- **Aug 1:** Meade relieved of command after POD Campaign failure
- **Aug 3:** Warren appointed, arrives at army headquarters
- **Aug 4-15:** Emergency reorganization, reinforcements arrive
- **Aug 16-31:** Initial positioning along Rappahannock

### September 1863 (Part 2)
- **Sep 1-10:** Warren's probing operations begin
- **Sep 11-20:** First attempts to find weakness in Confederate line
- **Sep 21-30:** Preparation for major offensive

### October 1863 (Part 3)
- **Oct 10:** Warren launches main assault ("The Fourteen Days")
- **Oct 10-23:** Bloody frontal assaults against fortified positions
- **Oct 23:** Warren suspends offensive after 35,000 casualties

### October-December 1863 (Part 4)
- **Oct 24-Nov 15:** Army disintegration begins, mass desertions
- **Nov 16-Dec 14:** "The Collapse" - army crumbles
- **Dec 15:** Warren relieved; Hooker appointed to salvage situation

---

## Casualty Summary

| Side | Killed | Wounded | Missing/Captured | Total |
|------|--------|---------|------------------|-------|
| Union | ~8,500 | ~26,000 | ~12,500 | ~47,000 |
| Confederate | ~2,100 | ~7,200 | ~2,700 | ~12,000 |

---

**Navigation:** Use the part links above to access detailed day-by-day accounts.
"""
    
    index_tokens = count_tokens(index_content)
    print(f"Index file: ~{index_tokens:,} tokens")
    print()
    
    if not dry_run:
        output_path = Path(output_dir)
        
        # Write parts
        for p in parts:
            part_file = output_path / f"rapidan-campaign-part-{p['num']}.md"
            part_file.write_text(p['content'], encoding='utf-8')
            print(f"Written: {part_file}")
        
        # Write index
        index_file = output_path / "rapidan-campaign-index.md"
        index_file.write_text(index_content, encoding='utf-8')
        print(f"Written: {index_file}")
        
        # Delete original
        Path(input_path).unlink()
        print(f"\nDeleted original: {input_path}")
    else:
        print("[DRY RUN - no files written]")

if __name__ == "__main__":
    import sys
    
    dry_run = '--apply' not in sys.argv
    
    print("=" * 70)
    print("RAPIDAN CAMPAIGN TIMELINE SPLIT")
    print("=" * 70)
    print()
    
    split_file(
        "world-building/reference/rapidan-campaign-timeline.md",
        "world-building/reference/",
        dry_run=dry_run
    )

