"""Analyze files over 10K tokens."""
import tiktoken
import os
from pathlib import Path

enc = tiktoken.encoding_for_model('gpt-4')
files = []

EXCLUDED = {'books', '.git', 'venv', 'scripts', 'archive'}

for root, dirs, filenames in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in EXCLUDED]
    for f in filenames:
        if f.endswith('.md'):
            path = Path(root) / f
            try:
                content = path.read_text(encoding='utf-8', errors='ignore')
                tokens = len(enc.encode(content))
                lines = len(content.split('\n'))
                if tokens > 10000:
                    files.append((str(path), tokens, lines))
            except:
                pass

files.sort(key=lambda x: x[1], reverse=True)

print("=" * 80)
print("FILES OVER 10K TOKENS (AI Context Concerns)")
print("=" * 80)
print()
print(f"{'File':<55} {'Tokens':>10} {'Lines':>8}")
print("-" * 80)

for f, t, l in files:
    # Truncate path for display
    display_path = f if len(f) < 55 else "..." + f[-52:]
    print(f"{display_path:<55} {t:>10,} {l:>8}")

print("-" * 80)
total = sum(t for _, t, _ in files)
print(f"{'TOTAL in massive files':<55} {total:>10,}")
print()

# Context window comparison
print("=" * 80)
print("CONTEXT WINDOW IMPACT")
print("=" * 80)
print()
print("Typical AI context windows:")
print("  - GPT-4:        8K tokens (older) / 128K tokens (turbo)")
print("  - Claude:       100K-200K tokens")
print("  - Cursor:       Uses chunking, but large files still problematic")
print()
print(f"Your 5 largest files alone: {total:,} tokens")
print()

# Recommendations
print("=" * 80)
print("RECOMMENDED ACTIONS BY FILE")
print("=" * 80)
print()

for f, t, l in files:
    print(f"### {f}")
    print(f"    Tokens: {t:,} | Lines: {l}")
    
    if t > 30000:
        print("    ACTION: SPLIT into smaller focused files")
        print("    PRIORITY: HIGH - too large for most operations")
    elif t > 20000:
        print("    ACTION: Consider splitting OR create summary index")
        print("    PRIORITY: MEDIUM - usable but suboptimal")
    else:
        print("    ACTION: Create summary/quick-reference version")
        print("    PRIORITY: LOW - manageable size")
    print()

