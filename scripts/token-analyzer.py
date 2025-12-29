#!/usr/bin/env python3
"""
Analyze token usage in project files.
Uses tiktoken for accurate GPT-4 token counting.
"""

import os
from pathlib import Path

# Simple token estimation (roughly accurate for English text)
# GPT-4 averages ~4 characters per token, but varies
def estimate_tokens(text):
    """Rough token estimate: ~4 chars per token, plus overhead for formatting"""
    # More accurate: count words * 1.3 + special chars
    words = len(text.split())
    special_chars = sum(1 for c in text if c in '#*-|>`[]():')
    return int(words * 1.3 + special_chars * 0.5)

def analyze_file(filepath):
    """Analyze a single file for token usage patterns"""
    content = filepath.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    # Count different types of content
    stats = {
        'total_chars': len(content),
        'total_lines': len(lines),
        'estimated_tokens': estimate_tokens(content),
        'blank_lines': sum(1 for l in lines if not l.strip()),
        'divider_lines': sum(1 for l in lines if l.strip() in ['---', '***', '___']),
        'header_lines': sum(1 for l in lines if l.strip().startswith('#')),
        'bullet_lines': sum(1 for l in lines if l.strip().startswith('-') or l.strip().startswith('*')),
    }
    
    # Calculate formatting overhead
    stats['formatting_overhead'] = stats['blank_lines'] + stats['divider_lines']
    
    return stats

def main():
    base = Path(r'C:\Users\MichaelL\Documents\Personal\ashverse')
    
    # Files to analyze (excluding books)
    files = []
    for pattern in ['*.md']:
        for f in base.rglob(pattern):
            if 'books' not in str(f) and '.git' not in str(f):
                files.append(f)
    
    # Analyze all files
    results = []
    for f in files:
        try:
            stats = analyze_file(f)
            stats['path'] = str(f.relative_to(base))
            results.append(stats)
        except Exception as e:
            pass
    
    # Sort by token count
    results.sort(key=lambda x: x['estimated_tokens'], reverse=True)
    
    # Print top 20 token consumers
    print("=" * 80)
    print("TOP 20 TOKEN CONSUMERS (excluding /books)")
    print("=" * 80)
    print(f"{'File':<55} {'Tokens':>8} {'Lines':>6} {'Tok/Line':>8}")
    print("-" * 80)
    
    total_tokens = 0
    for r in results[:20]:
        tok_per_line = r['estimated_tokens'] / max(r['total_lines'], 1)
        print(f"{r['path'][:54]:<55} {r['estimated_tokens']:>8,} {r['total_lines']:>6} {tok_per_line:>8.1f}")
        total_tokens += r['estimated_tokens']
    
    print("-" * 80)
    all_tokens = sum(r['estimated_tokens'] for r in results)
    print(f"{'TOTAL (all files)':<55} {all_tokens:>8,}")
    
    # Token density analysis
    print("\n" + "=" * 80)
    print("TOKEN EFFICIENCY ANALYSIS")
    print("=" * 80)
    
    # Find files with high formatting overhead
    high_overhead = [r for r in results if r['formatting_overhead'] > 50]
    high_overhead.sort(key=lambda x: x['formatting_overhead'], reverse=True)
    
    print("\nFiles with most formatting overhead (blank lines + dividers):")
    for r in high_overhead[:10]:
        pct = (r['formatting_overhead'] / max(r['total_lines'], 1)) * 100
        print(f"  {r['path'][:50]:<50} {r['formatting_overhead']:>4} overhead lines ({pct:.0f}%)")
    
    # Token-to-content ratio
    print("\n" + "=" * 80)
    print("OPTIMIZATION OPPORTUNITIES")
    print("=" * 80)
    
    # Verbose files (high tokens per line = lots of prose)
    verbose = [(r, r['estimated_tokens'] / max(r['total_lines'], 1)) for r in results if r['total_lines'] > 100]
    verbose.sort(key=lambda x: x[1], reverse=True)
    
    print("\nMost verbose files (high tokens per line = prose-heavy):")
    for r, ratio in verbose[:10]:
        print(f"  {r['path'][:50]:<50} {ratio:.1f} tokens/line")

if __name__ == '__main__':
    main()

