#!/usr/bin/env python3
"""
Content Hash Calculator
Calculates short hash (8 chars) for a markdown file (for change detection)
"""

import hashlib
import sys
import os

def calculate_hash(file_path: str, length: int = 8) -> str:
    """Calculate short hash of file content (first N chars of SHA-256)."""
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
        full_hash = hashlib.sha256(content).hexdigest()
        return full_hash[:length]
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Calculate short content hash for change detection')
    parser.add_argument('file_path', help='Path to markdown file')
    parser.add_argument('-l', '--length', type=int, default=8, 
                       help='Hash length (default: 8, recommended: 6-10)')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file_path):
        print(f"Error: File not found: {args.file_path}", file=sys.stderr)
        sys.exit(1)
    
    hash_value = calculate_hash(args.file_path, args.length)
    
    if hash_value:
        print(hash_value)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()

