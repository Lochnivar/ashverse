#!/usr/bin/env python3
"""
Cascade Impact Analyzer
Shows all files affected by a change (butterfly effect tracking)
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import deque

def extract_dependencies(file_path: str, base_dir: str = '.') -> List[Dict]:
    """Extract dependency declarations from markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return []
    
    dependencies = []
    
    # Find "Document Dependencies" section
    deps_section_match = re.search(
        r'##\s+Document\s+Dependencies.*?(?=\n##[^#]|\n\Z|\Z)',
        content,
        re.DOTALL | re.IGNORECASE
    )
    
    if not deps_section_match:
        return []
    
    deps_section = deps_section_match.group(0)
    lines = deps_section.split('\n')
    in_table = False
    
    for i, line in enumerate(lines):
        if '|' in line and ('Document' in line or 'Path' in line or 'Hash' in line):
            in_table = True
            continue
        
        if in_table and '---' in line:
            continue
        
        if in_table and line.strip().startswith('|') and line.strip() != '|':
            parts = [p.strip() for p in line.split('|') if p.strip()]
            
            if len(parts) >= 3:
                doc_name = parts[0] if len(parts) > 0 else ''
                doc_path_raw = parts[1] if len(parts) > 1 else ''
                
                doc_path = doc_path_raw.strip('`').strip()
                doc_path_normalized = doc_path.replace('\\', '/')
                
                if base_dir and base_dir != '.':
                    file_abs_path = os.path.abspath(os.path.join(base_dir, file_path))
                else:
                    file_abs_path = os.path.abspath(file_path)
                
                file_dir_path = Path(file_abs_path).parent
                joined_str = str(file_dir_path) + '/' + doc_path_normalized
                resolved_path_obj = Path(joined_str).resolve()
                resolved_path = str(resolved_path_obj)
                
                if doc_path:
                    dependencies.append({
                        'name': doc_name,
                        'path': doc_path,
                        'resolved_path': resolved_path
                    })
        
        if in_table and line.strip() and not line.strip().startswith('|'):
            in_table = False
    
    return dependencies

def build_dependency_graph(base_dir: str = '.') -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
    """
    Build dependency graph.
    Returns: (dependencies: file -> [deps], dependents: file -> [dependents])
    """
    base_path = Path(base_dir)
    md_files = list(base_path.rglob('*.md'))
    
    dependencies = {}  # file -> [dependencies]
    dependents = {}    # file -> [files that depend on it]
    
    for md_file in md_files:
        file_str = str(md_file)
        deps = extract_dependencies(file_str, base_dir)
        
        if deps:
            dependencies[file_str] = []
            for dep in deps:
                dep_path = dep['resolved_path']
                if os.path.exists(dep_path):
                    # Normalize paths for comparison
                    dep_normalized = str(Path(dep_path).resolve())
                    file_normalized = str(Path(file_str).resolve())
                    
                    dependencies[file_str].append(dep_normalized)
                    
                    # Build reverse graph
                    if dep_normalized not in dependents:
                        dependents[dep_normalized] = []
                    if file_normalized not in dependents[dep_normalized]:
                        dependents[dep_normalized].append(file_normalized)
    
    return dependencies, dependents

def find_all_dependents(target_file: str, dependents_graph: Dict[str, List[str]], base_dir: str = '.') -> Dict[int, List[str]]:
    """
    Find all files that depend on target_file (directly or indirectly).
    Returns: {depth: [files]}
    """
    target_normalized = str(Path(target_file).resolve())
    
    if target_normalized not in dependents_graph:
        return {0: []}
    
    visited = set()
    result = {}  # depth -> [files]
    queue = deque([(target_normalized, 0)])  # (file, depth)
    
    while queue:
        current_file, depth = queue.popleft()
        
        if current_file in visited:
            continue
        
        visited.add(current_file)
        
        if depth not in result:
            result[depth] = []
        result[depth].append(current_file)
        
        # Add dependents to queue
        if current_file in dependents_graph:
            for dependent in dependents_graph[current_file]:
                if dependent not in visited:
                    queue.append((dependent, depth + 1))
    
    return result

def print_cascade_report(target_file: str, base_dir: str = '.'):
    """Print cascade impact report for a file."""
    print("=" * 80)
    print(f"CASCADE IMPACT REPORT: {target_file}")
    print("=" * 80)
    
    if not os.path.exists(target_file):
        print(f"Error: File not found: {target_file}")
        return
    
    dependencies, dependents = build_dependency_graph(base_dir)
    
    # Find all dependents (cascade)
    cascade = find_all_dependents(target_file, dependents, base_dir)
    
    total_affected = sum(len(files) for files in cascade.values())
    
    print(f"\nTotal files affected: {total_affected}")
    print(f"Cascade depth: {max(cascade.keys()) if cascade else 0} levels")
    
    if total_affected == 0:
        print("\nNo dependencies tracked for this file.")
        print("(Either no files depend on it, or dependency tracking not set up)")
        return
    
    print("\n" + "=" * 80)
    print("CASCADE BREAKDOWN BY DEPTH:")
    print("=" * 80)
    
    for depth in sorted(cascade.keys()):
        files = cascade[depth]
        print(f"\nLevel {depth} ({len(files)} file{'s' if len(files) != 1 else ''}):")
        for file_path in sorted(files):
            # Show relative path
            try:
                rel_path = os.path.relpath(file_path, base_dir)
                print(f"  - {rel_path}")
            except:
                print(f"  - {file_path}")
    
    print("\n" + "=" * 80)
    print("BUTTERFLY EFFECT SUMMARY:")
    print("=" * 80)
    print(f"Changing '{target_file}' affects {total_affected} file(s) across {max(cascade.keys()) if cascade else 0} cascade level(s).")
    print("\nRecommendation: Review all affected files after making changes.")
    print("=" * 80)

def main():
    """Main function."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: cascade-impact.py <file-path> [base-dir]")
        print("\nShows all files affected by a change (butterfly effect tracking)")
        sys.exit(1)
    
    target_file = sys.argv[1]
    base_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
    
    print_cascade_report(target_file, base_dir)

if __name__ == '__main__':
    main()

