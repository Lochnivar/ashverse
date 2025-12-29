"""
De-bloat staffers.md by removing redundant content.

Strategy:
1. Keep ONE master disclaimer at file header (not per-character)
2. Remove repeated phrases after first occurrence per character
3. Consolidate overlapping sections
4. Keep all unique content (examples, LOCKED CANON, creative exchanges)
"""

import re
from pathlib import Path
import tiktoken

def count_tokens(text):
    enc = tiktoken.encoding_for_model('gpt-4')
    return len(enc.encode(text))

def debloat_content(content):
    """Apply de-bloating transformations."""
    
    lines = content.split('\n')
    result = []
    
    # Track state
    current_char = None
    seen_phrases = {}  # Per-character phrase tracking
    skip_until_next_section = False
    
    # Phrases to track (only keep first occurrence per character)
    redundant_phrases = [
        r'\*\*IMPORTANT:\*\* .+ is \*\*NOT a character in the actual novels\*\*',
        r'- \*\*Role:\*\* Fictional .+ in the companion compendium \(meta-framing device\)',
        r'- \*\*Appears In:\*\* Only in the compendium',
    ]
    
    # Sections that are often redundant
    redundant_sections = [
        '### Signature Style',  # Usually duplicates Character Voice > Tone
    ]
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Track current character
        if stripped.startswith('# Character:'):
            current_char = stripped
            seen_phrases[current_char] = set()
        
        # Skip redundant sections
        if any(stripped == sec for sec in redundant_sections):
            # Skip until next ## or ###
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('#'):
                i += 1
            continue
        
        # Check for redundant phrases (skip if seen before for this character)
        skip_line = False
        if current_char:
            for pattern in redundant_phrases:
                if re.search(pattern, stripped):
                    if pattern in seen_phrases.get(current_char, set()):
                        skip_line = True
                    else:
                        seen_phrases[current_char].add(pattern)
                    break
        
        if not skip_line:
            result.append(line)
        
        i += 1
    
    return '\n'.join(result)

def consolidate_disclaimers(content):
    """Move per-character disclaimers to single file-level disclaimer."""
    
    # Pattern for the verbose disclaimers
    disclaimer_pattern = r'\*\*IMPORTANT:\*\* [^.]+\. He/She/They (is|are|exists?) \*\*ONLY\*\* [^.]+\. [^.]+\.'
    
    # Remove individual disclaimers (they'll be replaced by file header)
    content = re.sub(
        r'\*\*IMPORTANT:\*\* [A-Za-z\. ]+is \*\*NOT a character in the actual novels\*\*\. .*?(?=\n\n|\n##)',
        '',
        content,
        flags=re.DOTALL
    )
    
    return content

def remove_duplicate_info(content):
    """Remove fields that duplicate other fields."""
    
    # Remove "Appears In" lines (redundant with IMPORTANT disclaimer)
    content = re.sub(
        r'- \*\*Appears In:\*\* Only in the compendium[^\n]*\n',
        '',
        content
    )
    
    # Remove duplicate role lines within Basic Information
    content = re.sub(
        r'- \*\*Role:\*\* Fictional [^\n]*\(meta-framing device\)\n',
        '',
        content
    )
    
    return content

def process_file(input_path, output_path=None, dry_run=True):
    """Process the staffers file."""
    
    content = Path(input_path).read_text(encoding='utf-8', errors='ignore')
    original_tokens = count_tokens(content)
    original_lines = len(content.split('\n'))
    
    print(f"Original: {original_lines} lines, {original_tokens:,} tokens")
    
    # Apply transformations
    content = debloat_content(content)
    content = consolidate_disclaimers(content)
    content = remove_duplicate_info(content)
    
    # Clean up multiple blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    new_tokens = count_tokens(content)
    new_lines = len(content.split('\n'))
    
    saved_tokens = original_tokens - new_tokens
    saved_pct = (saved_tokens / original_tokens) * 100
    
    print(f"After:    {new_lines} lines, {new_tokens:,} tokens")
    print(f"Saved:    {original_lines - new_lines} lines, {saved_tokens:,} tokens ({saved_pct:.1f}%)")
    
    if not dry_run:
        out_path = output_path or input_path
        Path(out_path).write_text(content, encoding='utf-8')
        print(f"Written to: {out_path}")
    else:
        print("\n[DRY RUN - no changes written]")
    
    return content, saved_tokens

if __name__ == "__main__":
    import sys
    
    input_file = "characters/staffers.md"
    dry_run = '--apply' not in sys.argv
    
    print("=" * 60)
    print("STAFFERS.MD DE-BLOATING")
    print("=" * 60)
    print()
    
    process_file(input_file, dry_run=dry_run)

