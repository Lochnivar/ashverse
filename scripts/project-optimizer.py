"""
Project Token Optimizer
========================
Reduces token usage while maintaining human readability.

Usage:
    python scripts/project-optimizer.py --analyze          # Show analysis only
    python scripts/project-optimizer.py --optimize         # Apply optimizations
    python scripts/project-optimizer.py --fix-encoding     # Fix encoding issues only
"""

import os
import re
import sys
import tiktoken
from pathlib import Path

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
EXCLUDED_DIRS = {'books', '.git', 'venv', 'scripts', 'archive', 'node_modules'}

def count_tokens(text, model_name="gpt-4"):
    """Count tokens using tiktoken."""
    try:
        encoding = tiktoken.encoding_for_model(model_name)
        return len(encoding.encode(text))
    except:
        # Fallback: rough estimate
        return len(text) // 4


# ============================================================================
# ENCODING FIXES
# ============================================================================

# Common mojibake patterns (UTF-8 interpreted as Latin-1/Windows-1252)
ENCODING_FIXES = [
    # Place names
    ('CÃ¡diz', 'Cadiz'),
    # Dashes - match the actual corrupted bytes
    ('â€"', '-'),   # em-dash mojibake
    ('â€"', '-'),   # en-dash mojibake  
    # Quotes
    ("â€™", "'"),   # right single quote
    ('â€œ', '"'),   # left double quote
    ('â€\x9d', '"'), # right double quote
    # Other
    ('â€¦', '...'), # ellipsis
    # Symbols (keep simple ASCII replacements)
]

def fix_encoding(content):
    """Fix common encoding issues (mojibake from UTF-8 misinterpretation)."""
    # Apply simple replacements
    for bad, good in ENCODING_FIXES:
        content = content.replace(bad, good)
    
    # Fix remaining mojibake patterns with regex
    # Pattern: Ã followed by another character (common in mojibake)
    # Only fix known safe patterns
    content = content.replace('Ã¡', 'a')  # á
    content = content.replace('Ã©', 'e')  # é
    content = content.replace('Ã³', 'o')  # ó
    content = content.replace('Ã±', 'n')  # ñ
    
    return content



# ============================================================================
# OVERHEAD REDUCTION
# ============================================================================

def reduce_overhead(content):
    """
    Reduce formatting overhead while maintaining readability.
    
    Patterns removed:
    - Consecutive blank lines → single blank
    - Consecutive dividers → single divider
    - blank + --- + blank before header → single blank
    - divider immediately followed by header → just header
    """
    lines = content.split('\n')
    result = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        is_blank = not stripped
        is_divider = bool(re.fullmatch(r'[-=]{3,}', stripped))
        
        # Skip consecutive blank lines
        if is_blank:
            # Check if we already have a blank at the end
            if result and not result[-1].strip():
                i += 1
                continue
        
        # Handle divider patterns
        if is_divider:
            # Look ahead: is next line blank and then a header?
            # Pattern: --- \n \n ## Header
            if (i + 2 < len(lines) and 
                not lines[i + 1].strip() and 
                lines[i + 2].strip().startswith('#')):
                # Skip the divider (and the next blank will be handled naturally)
                i += 1
                continue
            
            # Pattern: --- \n ## Header (no blank)
            if i + 1 < len(lines) and lines[i + 1].strip().startswith('#'):
                i += 1
                continue
            
            # Pattern: blank \n --- \n blank → just keep one blank
            if (result and not result[-1].strip() and 
                i + 1 < len(lines) and not lines[i + 1].strip()):
                # Skip divider, the trailing blank will be added
                i += 1
                continue
        
        result.append(line)
        i += 1
    
    # Clean up trailing blank lines
    while result and not result[-1].strip():
        result.pop()
    
    return '\n'.join(result) + '\n'


# ============================================================================
# FILE PROCESSING
# ============================================================================

def analyze_file(filepath):
    """Analyze a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        return None
    
    lines = content.split('\n')
    total_lines = len(lines)
    total_tokens = count_tokens(content)
    
    # Count overhead
    blank_lines = sum(1 for line in lines if not line.strip())
    divider_lines = sum(1 for line in lines if re.fullmatch(r'[-=]{3,}', line.strip()))
    overhead = blank_lines + divider_lines
    
    # Check for encoding issues
    encoding_issues = sum(1 for bad, _ in ENCODING_FIXES if bad in content)
    
    return {
        'lines': total_lines,
        'tokens': total_tokens,
        'blank_lines': blank_lines,
        'divider_lines': divider_lines,
        'overhead': overhead,
        'overhead_pct': (overhead / total_lines * 100) if total_lines > 0 else 0,
        'encoding_issues': encoding_issues,
    }


def optimize_file(filepath, dry_run=True):
    """Optimize a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            original = f.read()
    except:
        return None
    
    # Apply optimizations
    optimized = fix_encoding(original)
    optimized = reduce_overhead(optimized)
    
    # Calculate savings
    orig_tokens = count_tokens(original)
    opt_tokens = count_tokens(optimized)
    saved_tokens = orig_tokens - opt_tokens
    saved_pct = (saved_tokens / orig_tokens * 100) if orig_tokens > 0 else 0
    
    if not dry_run and optimized != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(optimized)
    
    return {
        'original_tokens': orig_tokens,
        'optimized_tokens': opt_tokens,
        'saved_tokens': saved_tokens,
        'saved_pct': saved_pct,
        'changed': optimized != original,
    }


def get_all_md_files():
    """Get all markdown files in project."""
    files = []
    for root, dirs, filenames in os.walk(PROJECT_ROOT):
        # Filter excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        
        for filename in filenames:
            if filename.endswith('.md'):
                filepath = Path(root) / filename
                rel_path = filepath.relative_to(PROJECT_ROOT)
                files.append(rel_path)
    
    return sorted(files)


# ============================================================================
# COMMANDS
# ============================================================================

def cmd_analyze():
    """Analyze all files and show optimization opportunities."""
    print("=" * 80)
    print("PROJECT TOKEN ANALYSIS")
    print("=" * 80)
    print()
    
    files = get_all_md_files()
    results = []
    total_tokens = 0
    total_overhead_tokens = 0
    files_with_encoding_issues = []
    
    for rel_path in files:
        filepath = PROJECT_ROOT / rel_path
        analysis = analyze_file(filepath)
        if analysis:
            results.append((rel_path, analysis))
            total_tokens += analysis['tokens']
            # Estimate overhead tokens (roughly)
            total_overhead_tokens += int(analysis['overhead'] * 2)  # ~2 tokens per blank/divider
            if analysis['encoding_issues'] > 0:
                files_with_encoding_issues.append(str(rel_path))
    
    # Sort by tokens
    results.sort(key=lambda x: x[1]['tokens'], reverse=True)
    
    print(f"{'File':<55} {'Tokens':>8} {'Lines':>6} {'Overhead':>8}")
    print("-" * 80)
    
    for rel_path, analysis in results[:25]:
        path_str = str(rel_path)[:54]
        overhead_str = f"{analysis['overhead']} ({analysis['overhead_pct']:.0f}%)"
        print(f"{path_str:<55} {analysis['tokens']:>8} {analysis['lines']:>6} {overhead_str:>8}")
    
    print("-" * 80)
    print(f"{'TOTAL':<55} {total_tokens:>8,}")
    print()
    
    if files_with_encoding_issues:
        print("=" * 80)
        print("FILES WITH ENCODING ISSUES")
        print("=" * 80)
        for f in files_with_encoding_issues[:15]:
            print(f"  - {f}")
        if len(files_with_encoding_issues) > 15:
            print(f"  ... and {len(files_with_encoding_issues) - 15} more")
        print()
    
    print("=" * 80)
    print("ESTIMATED SAVINGS FROM OVERHEAD REDUCTION")
    print("=" * 80)
    print(f"  Estimated saveable tokens: ~{total_overhead_tokens:,}")
    print(f"  Percentage of total: ~{(total_overhead_tokens/total_tokens*100):.1f}%")
    print()


def cmd_optimize(dry_run=True):
    """Apply optimizations to all files."""
    action = "DRY RUN" if dry_run else "APPLYING"
    print("=" * 80)
    print(f"PROJECT OPTIMIZATION ({action})")
    print("=" * 80)
    print()
    
    files = get_all_md_files()
    total_saved = 0
    files_changed = 0
    
    for rel_path in files:
        filepath = PROJECT_ROOT / rel_path
        result = optimize_file(filepath, dry_run=dry_run)
        if result and result['changed']:
            files_changed += 1
            total_saved += result['saved_tokens']
            if result['saved_pct'] >= 1:  # Only show files with 1%+ savings
                print(f"  {str(rel_path):<55} -{result['saved_tokens']:>5} tokens ({result['saved_pct']:.0f}%)")
    
    print()
    print("-" * 80)
    print(f"Files changed: {files_changed}")
    print(f"Total tokens saved: {total_saved:,}")
    if not dry_run:
        print("Changes applied successfully!")
    else:
        print("\nRun with --optimize --apply to apply changes.")


def cmd_fix_encoding():
    """Fix encoding issues only."""
    print("=" * 80)
    print("FIXING ENCODING ISSUES")
    print("=" * 80)
    print()
    
    files = get_all_md_files()
    files_fixed = 0
    
    for rel_path in files:
        filepath = PROJECT_ROOT / rel_path
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                original = f.read()
            
            fixed = fix_encoding(original)
            
            if fixed != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed)
                files_fixed += 1
                print(f"  Fixed: {rel_path}")
        except Exception as e:
            print(f"  Error: {rel_path}: {e}")
    
    print()
    print(f"Files fixed: {files_fixed}")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    args = sys.argv[1:]
    
    if '--fix-encoding' in args:
        cmd_fix_encoding()
    elif '--optimize' in args:
        apply = '--apply' in args
        cmd_optimize(dry_run=not apply)
    else:
        cmd_analyze()

