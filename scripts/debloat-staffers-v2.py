"""
De-bloat staffers.md - Version 2

Problem: ~1,200 lines of planning/brainstorming notes mixed with character reference.

Strategy:
1. Identify planning note sections by patterns
2. Extract to separate archive file
3. Keep only actual character reference content
"""

import re
from pathlib import Path
import tiktoken

def count_tokens(text):
    enc = tiktoken.encoding_for_model('gpt-4')
    return len(enc.encode(text))

# Patterns that indicate planning notes (not reference content)
PLANNING_INDICATORS = [
    r'^WHY THIS (IS|WORKS)',
    r'^BOTTOM LINE:',
    r'^GO FOR IT',
    r'^M$',  # User initial
    r'^THE [A-Z]{4,}:$',  # ALL CAPS headers like "THE REAL BRILLIANCE:"
    r'^This is PERFECT',
    r'PERFECT\.$',
    r'^I recommend',
    r'^Option \d:',
    r'ðŸ',  # Emoji indicators
    r'^PRACTICAL IMPLEMENTATION:',
    r'^HOW THIS .* WORKS:',
    r'^THE .* SECTION',
]

# Sections to preserve (actual reference content)
REFERENCE_SECTIONS = [
    'Basic Information',
    'Academic Credentials',
    'Duties',
    'Character Voice',
    'Character Personality', 
    'Personality',
    'Relationship with',
    'Sacred Typewriter',
    'LOCKED CANON',
    'Examples of',
    'The 1985 Compendium',
    'The Famous Footnote',
    'The KKK/Night Riders',
    'The Woodrow Wilson',
    'The Jacobus Incident',
    'Notes',
    'Staff',
    'Location:',
    'Official Role',
    'Current Status',
]

def is_planning_content(line, context_lines=None):
    """Check if a line is planning content vs. reference content."""
    stripped = line.strip()
    
    # Check against planning indicators
    for pattern in PLANNING_INDICATORS:
        if re.search(pattern, stripped, re.IGNORECASE):
            return True
    
    return False

def is_reference_section_header(line):
    """Check if this is a header for a reference section."""
    stripped = line.strip()
    if not stripped.startswith('##'):
        return False
    
    for section in REFERENCE_SECTIONS:
        if section.lower() in stripped.lower():
            return True
    return False

def extract_planning_notes(content):
    """
    Separate content into reference and planning notes.
    
    Returns: (reference_content, planning_notes)
    """
    lines = content.split('\n')
    reference_lines = []
    planning_lines = []
    
    in_planning_section = False
    planning_section_start = None
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check for character headers (always keep)
        if stripped.startswith('# Character:') or stripped.startswith('# Compendium Staffers'):
            in_planning_section = False
            reference_lines.append(line)
            i += 1
            continue
        
        # Check for reference section headers
        if is_reference_section_header(line):
            in_planning_section = False
            reference_lines.append(line)
            i += 1
            continue
        
        # Check if this line starts a planning section
        if is_planning_content(line):
            if not in_planning_section:
                in_planning_section = True
                planning_section_start = i
                planning_lines.append(f"\n--- Line {i+1} ---")
            planning_lines.append(line)
            i += 1
            continue
        
        # If we're in a planning section, check if this continues it
        if in_planning_section:
            # Continue planning section until we hit a reference header or character header
            if stripped.startswith('#'):
                in_planning_section = False
                reference_lines.append(line)
            else:
                planning_lines.append(line)
            i += 1
            continue
        
        # Default: keep as reference
        reference_lines.append(line)
        i += 1
    
    return '\n'.join(reference_lines), '\n'.join(planning_lines)

def deep_clean(content):
    """Additional cleaning after separation."""
    
    # Remove duplicate blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Remove trailing whitespace
    lines = [line.rstrip() for line in content.split('\n')]
    content = '\n'.join(lines)
    
    return content

def process_file(input_path, dry_run=True):
    """Process staffers.md."""
    
    content = Path(input_path).read_text(encoding='utf-8', errors='ignore')
    original_tokens = count_tokens(content)
    original_lines = len(content.split('\n'))
    
    print(f"Original: {original_lines:,} lines, {original_tokens:,} tokens")
    print()
    
    # Extract planning notes
    reference_content, planning_notes = extract_planning_notes(content)
    reference_content = deep_clean(reference_content)
    
    ref_tokens = count_tokens(reference_content)
    ref_lines = len(reference_content.split('\n'))
    
    plan_tokens = count_tokens(planning_notes)
    plan_lines = len(planning_notes.split('\n'))
    
    print(f"Reference content: {ref_lines:,} lines, {ref_tokens:,} tokens")
    print(f"Planning notes:    {plan_lines:,} lines, {plan_tokens:,} tokens")
    print()
    
    saved_tokens = original_tokens - ref_tokens
    saved_pct = (saved_tokens / original_tokens) * 100 if original_tokens > 0 else 0
    
    print(f"Savings: {saved_tokens:,} tokens ({saved_pct:.1f}%)")
    
    if not dry_run:
        # Write reference content back
        Path(input_path).write_text(reference_content, encoding='utf-8')
        print(f"\nReference content written to: {input_path}")
        
        # Archive planning notes
        archive_path = Path(input_path).parent / 'staffers-planning-notes-archive.md'
        archive_header = f"""# Staffers Planning Notes Archive

**Archived:** December 29, 2025
**Source:** staffers.md
**Purpose:** Brainstorming and planning notes extracted during de-bloating

---

"""
        Path(archive_path).write_text(archive_header + planning_notes, encoding='utf-8')
        print(f"Planning notes archived to: {archive_path}")
    else:
        print("\n[DRY RUN - no changes written]")
        print("\nSample of detected planning notes (first 20 lines):")
        for line in planning_notes.split('\n')[:20]:
            print(f"  {line[:80]}")

if __name__ == "__main__":
    import sys
    
    dry_run = '--apply' not in sys.argv
    
    print("=" * 70)
    print("STAFFERS.MD DE-BLOATING (Version 2)")
    print("=" * 70)
    print()
    
    process_file("characters/staffers.md", dry_run=dry_run)

