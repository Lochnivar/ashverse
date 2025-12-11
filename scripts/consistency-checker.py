#!/usr/bin/env python3
"""
Content Hash Consistency Checker - Proof of Concept
Calculates hashes and verifies dependencies between markdown documents
"""

import hashlib
import os
import re
from pathlib import Path, PurePath
from typing import Dict, List, Optional, Tuple
from datetime import datetime

def calculate_hash(file_path: str, length: int = 8) -> str:
    """Calculate short hash of file content (first N chars of SHA-256)."""
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
        full_hash = hashlib.sha256(content).hexdigest()
        return full_hash[:length]
    except Exception as e:
        return f"ERROR: {str(e)}"

def extract_dependencies(file_path: str, base_dir: str = '.') -> List[Dict]:
    """
    Extract dependency declarations from markdown file.
    Looks for dependency table in "Document Dependencies" section.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return []
    
    dependencies = []
    
    # Find "Document Dependencies" section
    # Match until next ## header (not ###) or end of file
    deps_section_match = re.search(
        r'##\s+Document\s+Dependencies.*?(?=\n##[^#]|\n\Z|\Z)',
        content,
        re.DOTALL | re.IGNORECASE
    )
    
    if not deps_section_match:
        return []
    
    deps_section = deps_section_match.group(0)
    
    # Extract table rows
    # Pattern: | Document Name | Path | Hash | Last Verified | Status |
    lines = deps_section.split('\n')
    in_table = False
    header_found = False
    
    for i, line in enumerate(lines):
        # Check for table header
        if '|' in line and ('Document' in line or 'Path' in line or 'Hash' in line):
            header_found = True
            in_table = True
            continue
        
        # Skip separator row
        if in_table and '---' in line:
            continue
        
        # Parse data rows
        if in_table and line.strip().startswith('|') and line.strip() != '|':
            parts = [p.strip() for p in line.split('|') if p.strip()]
            
            if len(parts) >= 3:
                doc_name = parts[0] if len(parts) > 0 else ''
                doc_path_raw = parts[1] if len(parts) > 1 else ''
                doc_hash_raw = parts[2] if len(parts) > 2 else ''
                
                # Clean up path (remove backticks, extract path)
                doc_path = doc_path_raw.strip('`').strip()
                
                # Clean up hash (remove sha256: prefix if present, handle short hashes)
                doc_hash = doc_hash_raw.strip('`').strip()
                if doc_hash.startswith('sha256:'):
                    doc_hash = doc_hash[7:]
                # Handle full SHA-256 hashes (64 chars) - take first 8 for comparison
                if len(doc_hash) == 64:
                    doc_hash = doc_hash[:8]
                
                # Accept hashes of 6-10 characters (or full 64-char SHA-256)
                if doc_path and doc_hash and (6 <= len(doc_hash) <= 10 or len(doc_hash) == 64):
                    # Resolve relative path
                    # Normalize path separators first
                    doc_path_normalized = doc_path.replace('\\', '/')
                    
                    # Get absolute path of the file containing the dependency
                    if base_dir and base_dir != '.':
                        file_abs_path = os.path.abspath(os.path.join(base_dir, file_path))
                    else:
                        file_abs_path = os.path.abspath(file_path)
                    
                    # Use pathlib for better path resolution
                    file_dir_path = Path(file_abs_path).parent
                    # Join as string first, then convert to Path to resolve
                    # This ensures .. is resolved relative to file_dir_path, not cwd
                    joined_str = str(file_dir_path) + '/' + doc_path_normalized
                    resolved_path_obj = Path(joined_str).resolve()
                    resolved_path = str(resolved_path_obj)
                    
                    dependencies.append({
                        'name': doc_name,
                        'path': doc_path,
                        'resolved_path': resolved_path,
                        'expected_hash': doc_hash,
                        'line': i + 1
                    })
        
        # Stop at end of table
        if in_table and line.strip() and not line.strip().startswith('|'):
            in_table = False
    
    return dependencies

def check_consistency(file_path: str, base_dir: str = '.') -> Tuple[List[Dict], List[Dict]]:
    """
    Check consistency of dependencies in a file.
    Returns: (issues, verified)
    """
    issues = []
    verified = []
    
    dependencies = extract_dependencies(file_path, base_dir)
    
    if not dependencies:
        return issues, verified
    
    for dep in dependencies:
        dep_path = dep['resolved_path']
        
        if not os.path.exists(dep_path):
            issues.append({
                'file': file_path,
                'dependency': dep['name'],
                'path': dep['path'],
                'resolved_path': dep_path,
                'issue': 'File not found',
                'severity': 'error',
                'expected_hash': dep['expected_hash']
            })
            continue
        
        current_hash = calculate_hash(dep_path)
        
        if current_hash.startswith('ERROR:'):
            issues.append({
                'file': file_path,
                'dependency': dep['name'],
                'path': dep['path'],
                'resolved_path': dep_path,
                'issue': f'Error reading file: {current_hash}',
                'severity': 'error',
                'expected_hash': dep['expected_hash']
            })
            continue
        
        expected_hash = dep['expected_hash']
        
        # Normalize hash lengths for comparison (use first 8 chars)
        current_hash_short = current_hash[:8] if len(current_hash) >= 8 else current_hash
        expected_hash_short = expected_hash[:8] if len(expected_hash) >= 8 else expected_hash
        
        if current_hash_short != expected_hash_short:
            issues.append({
                'file': file_path,
                'dependency': dep['name'],
                'path': dep['path'],
                'resolved_path': dep_path,
                'issue': 'Hash mismatch',
                'severity': 'warning',
                'expected_hash': expected_hash,
                'current_hash': current_hash
            })
        else:
            verified.append({
                'file': file_path,
                'dependency': dep['name'],
                'path': dep['path'],
                'hash': current_hash
            })
    
    return issues, verified

def get_file_hash(file_path: str) -> str:
    """Get hash for a file (for adding to dependency declarations)."""
    return calculate_hash(file_path)

def scan_project(base_dir: str = '.', pattern: str = '*.md') -> Dict:
    """Scan entire project for consistency issues."""
    base_path = Path(base_dir)
    md_files = list(base_path.rglob(pattern))
    
    all_issues = []
    all_verified = []
    files_with_deps = []
    files_without_deps = []
    
    for md_file in md_files:
        file_str = str(md_file)
        issues, verified = check_consistency(file_str, base_dir)
        
        deps = extract_dependencies(file_str, base_dir)
        
        if deps:
            files_with_deps.append(file_str)
            all_issues.extend(issues)
            all_verified.extend(verified)
        else:
            files_without_deps.append(file_str)
    
    return {
        'issues': all_issues,
        'verified': all_verified,
        'files_with_deps': files_with_deps,
        'files_without_deps': files_without_deps,
        'total_files': len(md_files)
    }

def print_report(results: Dict):
    """Print a formatted consistency report."""
    print("=" * 80)
    print("CONTENT HASH CONSISTENCY REPORT")
    print("=" * 80)
    print(f"\nScan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total Markdown Files: {results['total_files']}")
    print(f"Files with Dependencies: {len(results['files_with_deps'])}")
    print(f"Files without Dependencies: {len(results['files_without_deps'])}")
    
    print(f"\n✅ Verified Dependencies: {len(results['verified'])}")
    print(f"⚠️  Issues Found: {len(results['issues'])}")
    
    if results['issues']:
        print("\n" + "=" * 80)
        print("ISSUES:")
        print("=" * 80)
        
        errors = [i for i in results['issues'] if i['severity'] == 'error']
        warnings = [i for i in results['issues'] if i['severity'] == 'warning']
        
        if errors:
            print(f"\n❌ ERRORS ({len(errors)}):")
            for issue in errors:
                print(f"\n  File: {issue['file']}")
                print(f"    Dependency: {issue['dependency']}")
                print(f"    Path: {issue['path']}")
                print(f"    Issue: {issue['issue']}")
        
        if warnings:
            print(f"\n⚠️  WARNINGS ({len(warnings)}):")
            for issue in warnings:
                print(f"\n  File: {issue['file']}")
                print(f"    Dependency: {issue['dependency']}")
                print(f"    Path: {issue['path']}")
                print(f"    Issue: {issue['issue']}")
                print(f"    Expected: {issue['expected_hash']}")
                print(f"    Current:  {issue['current_hash']}")
    
    if results['files_with_deps']:
        print("\n" + "=" * 80)
        print("FILES WITH DEPENDENCY TRACKING:")
        print("=" * 80)
        for file in results['files_with_deps']:
            print(f"  - {file}")
    
    print("\n" + "=" * 80)

def main():
    """Main function."""
    import sys
    
    if len(sys.argv) > 1:
        # Check specific file
        file_path = sys.argv[1]
        base_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
        
        print(f"Checking: {file_path}\n")
        issues, verified = check_consistency(file_path, base_dir)
        
        if verified:
            print(f"✅ Verified ({len(verified)}):")
            for v in verified:
                print(f"  - {v['dependency']} ({v['path']})")
        
        if issues:
            print(f"\n⚠️  Issues ({len(issues)}):")
            for issue in issues:
                print(f"  - {issue['dependency']}: {issue['issue']}")
        else:
            print("\n✅ No issues found!")
    else:
        # Scan entire project
        print("Scanning project for consistency issues...\n")
        results = scan_project()
        print_report(results)

if __name__ == '__main__':
    main()

