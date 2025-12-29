#!/usr/bin/env python3
"""
Streamline character files by removing bloat sections.
Keeps: Basics, Personality (condensed), NTL Divergence, Key Relationships, Appearances, Best Casting
Removes: Duplicate sections, generic fears/desires, verbose arcs, multiple casting choices
"""

import re
from pathlib import Path

# Sections to completely remove
REMOVE_SECTIONS = [
    r'## Skills & Abilities.*?(?=\n## |\n# |\Z)',
    r'## Character Arc \(NTL\).*?(?=\n## |\n# |\Z)',
    r'## Voice & Dialogue.*?(?=\n## |\n# |\Z)',
    r'## Narrative Notes.*?(?=\n## |\n# |\Z)',
    r'### Fears\n.*?(?=\n### |\n## |\n# |\Z)',
    r'### Desires\n.*?(?=\n### |\n## |\n# |\Z)',
    r'### Quirks\n.*?(?=\n### |\n## |\n# |\Z)',
    r'### Alternative Choices.*?(?=\n## |\n# |\n---|\Z)',
    r'### Actor Archetype Suggestions.*?(?=\n## |\n# |\n---|\Z)',
    r'### NTL-Specific Notes.*?(?=\n## |\n# |\n---|\Z)',
    r'### Best Actual Portrayal.*?(?=\n### |\n## |\n# |\Z)',
]

def count_sections(content):
    """Count character entries in file"""
    return len(re.findall(r'^# [A-Z]', content, re.MULTILINE))

def streamline_file(filepath):
    """Process a single file"""
    content = filepath.read_text(encoding='utf-8')
    original_lines = len(content.split('\n'))
    
    # Remove bloat sections
    for pattern in REMOVE_SECTIONS:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Clean up multiple blank lines
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    new_lines = len(content.split('\n'))
    
    return content, original_lines, new_lines

def main():
    base = Path(r'C:\Users\MichaelL\Documents\Personal\ashverse\characters')
    
    files_to_process = [
        'union-military.md',
        'confederate-military.md', 
        'staffers.md'
    ]
    
    print("=" * 60)
    print("CHARACTER FILE STREAMLINING - DRY RUN")
    print("=" * 60)
    
    total_before = 0
    total_after = 0
    
    for filename in files_to_process:
        filepath = base / filename
        if filepath.exists():
            content, before, after = streamline_file(filepath)
            chars = count_sections(content)
            saved = before - after
            pct = (saved / before) * 100 if before > 0 else 0
            
            print(f"\n{filename}:")
            print(f"  Characters: {chars}")
            print(f"  Before: {before} lines")
            print(f"  After:  {after} lines")
            print(f"  Saved:  {saved} lines ({pct:.1f}%)")
            
            total_before += before
            total_after += after
    
    print("\n" + "=" * 60)
    print(f"TOTAL: {total_before} -> {total_after} lines")
    print(f"SAVED: {total_before - total_after} lines ({((total_before - total_after) / total_before) * 100:.1f}%)")
    print("=" * 60)
    print("\nTo apply changes, run with --apply flag")

if __name__ == '__main__':
    import sys
    if '--apply' in sys.argv:
        print("Applying changes...")
        base = Path(r'C:\Users\MichaelL\Documents\Personal\ashverse\characters')
        for filename in ['union-military.md', 'confederate-military.md', 'staffers.md']:
            filepath = base / filename
            if filepath.exists():
                content, _, _ = streamline_file(filepath)
                filepath.write_text(content, encoding='utf-8')
                print(f"  Updated: {filename}")
        print("Done!")
    else:
        main()

