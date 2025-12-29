#!/usr/bin/env python3
"""Fix encoding issues in character files"""

import re
from pathlib import Path

def fix_encoding(filepath):
    """Fix common encoding issues using hex patterns"""
    content = filepath.read_text(encoding='utf-8')
    original = content
    
    # Fix corrupted UTF-8 sequences using regex with hex codes
    # Common patterns when UTF-8 is double-encoded or misread
    patterns = [
        (r'\xc3\xa1', 'a'),   # a with acute
        (r'\xc3\xa9', 'e'),   # e with acute
        (r'\xc3\xad', 'i'),   # i with acute
        (r'\xc3\xb3', 'o'),   # o with acute
        (r'\xc3\xba', 'u'),   # u with acute
        (r'\xc3\xb1', 'n'),   # n with tilde
    ]
    
    for pattern, replacement in patterns:
        content = content.replace(pattern, replacement)
    
    # Use raw byte patterns for the corrupted sequences
    # These are the actual byte sequences we see in the files
    bad_sequences = {
        b'\xc3\xa2\xc2\x80\xc2\x94': b'-',   # em-dash
        b'\xc3\xa2\xc2\x80\xc2\x93': b'-',   # en-dash
        b'\xc3\xa2\xc2\x80\xc2\x99': b"'",   # right quote
        b'\xc3\xa2\xc2\x80\xc2\x98': b"'",   # left quote
        b'\xc3\xa2\xc2\x80\xc2\xa6': b'...',  # ellipsis
    }
    
    # Read as bytes and fix
    content_bytes = filepath.read_bytes()
    for bad, good in bad_sequences.items():
        content_bytes = content_bytes.replace(bad, good)
    
    # Also fix the visible corrupted text
    content = content_bytes.decode('utf-8', errors='replace')
    
    # Text-level replacements for remaining issues
    text_fixes = [
        ('a\u0302\u20ac\u201c', '-'),  # another em-dash pattern
        ('a\u0302\u20ac"', '-'),       # variant
    ]
    
    for bad, good in text_fixes:
        content = content.replace(bad, good)
    
    if content_bytes != filepath.read_bytes():
        filepath.write_bytes(content_bytes)
        return True
    return False

def main():
    base = Path(r'C:\Users\MichaelL\Documents\Personal\ashverse\characters')
    
    files = [
        'union-military-optimized.md',
        'confederate-military-optimized.md'
    ]
    
    for fname in files:
        filepath = base / fname
        if filepath.exists():
            # Simple approach: read, replace visible bad chars, write
            content = filepath.read_text(encoding='utf-8', errors='replace')
            original = content
            
            # Replace the visible corrupted sequences
            replacements = {
                '\u00e2\u20ac\u201c': '-',
                '\u00e2\u20ac\u201d': '-', 
                '\u00e2\u20ac\u2122': "'",
                '\u00c3\u00a1': 'a',
                'CAdiz': 'Cadiz',
            }
            
            for bad, good in replacements.items():
                content = content.replace(bad, good)
            
            # Also try direct string replacement
            content = re.sub(r'[^\x00-\x7F]+', lambda m: '-' if len(m.group()) > 2 else m.group(), content)
            
            if content != original:
                filepath.write_text(content, encoding='utf-8')
                print(f"Fixed: {fname}")
            else:
                print(f"No changes needed: {fname}")

if __name__ == '__main__':
    main()
