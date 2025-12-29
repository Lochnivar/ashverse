#!/usr/bin/env python3
"""
Transform character files to token-optimized Lincoln format.
Preserves essential info, removes redundancy, maintains readability.
VERSION 2: Fixed truncation issues
"""

import re
from pathlib import Path

def extract_section(text, section_name):
    """Extract content from a section"""
    pattern = rf'## {section_name}\s*\n(.*?)(?=\n## |\n# |\Z)'
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ""

def extract_field(text, field_name):
    """Extract a single field value"""
    pattern = rf'\*\*{field_name}:\*\*\s*([^\n]+)'
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ""

def parse_character(text):
    """Parse a character entry into structured data"""
    data = {}
    
    # Name from header
    header_match = re.match(r'# (?:Character: )?([^\n]+)', text)
    if header_match:
        data['name'] = header_match.group(1).strip()
    
    # Basic info
    basic = extract_section(text, 'Basic Information')
    data['birth'] = extract_field(basic, 'Birth')
    data['rank'] = extract_field(basic, 'Rank')
    data['role'] = extract_field(basic, 'Role')
    data['nickname'] = extract_field(basic, 'Nickname') or extract_field(basic, 'Nicknames')
    
    # Age extraction
    age_match = re.search(r'\*\*Age in 1863:\*\*\s*(\d+)', basic)
    data['age_1863'] = age_match.group(1) if age_match else ""
    age_match = re.search(r'\*\*Age in 1865:\*\*\s*(\d+)', basic)
    data['age_1865'] = age_match.group(1) if age_match else ""
    
    # Physical description - extract key parts
    physical = extract_section(text, 'Physical Description')
    height = extract_field(physical, 'Height')
    build = extract_field(physical, 'Build')
    hair = extract_field(physical, 'Hair')
    eyes = extract_field(physical, 'Eyes')
    features = extract_field(physical, 'Distinguishing Features')
    
    # Build condensed physical
    phys_parts = []
    if height:
        phys_parts.append(height.split('(')[0].strip())
    if build:
        phys_parts.append(build.split(',')[0].strip())
    if hair:
        phys_parts.append(f"hair: {hair.split(',')[0].strip()}")
    if eyes:
        phys_parts.append(f"eyes: {eyes.split(',')[0].strip()}")
    if features and len(features) < 80:
        phys_parts.append(features)
    data['physical'] = '; '.join(phys_parts) if phys_parts else ""
    
    # Core traits from Personality
    personality = extract_section(text, 'Personality')
    traits = re.findall(r'\d+\.\s*\*\*([^*]+)\*\*\s*-\s*([^\n]+)', personality)
    data['traits'] = [(t[0].strip(), t[1].strip()) for t in traits[:5]]
    
    # Weaknesses
    weak_section = re.search(r'### Weaknesses\s*\n(.*?)(?=\n### |\n## |\Z)', personality, re.DOTALL)
    if weak_section:
        weaknesses = re.findall(r'\*\*([^*]+)\*\*', weak_section.group(1))
        data['weaknesses'] = [w.strip() for w in weaknesses[:3]]
    else:
        data['weaknesses'] = []
    
    # NTL Divergence - keep full content
    background = extract_section(text, 'Background')
    ntl_match = re.search(r'### NTL Divergence\s*\n(.*?)(?=\n## |\n# |\Z)', background, re.DOTALL)
    if ntl_match:
        data['ntl'] = ntl_match.group(1).strip()
    else:
        data['ntl'] = ""
    
    # Relationships - extract key ones
    relationships = extract_section(text, 'Relationships')
    rels = re.findall(r'### With ([^\n]+)\s*\n-\s*\*\*(?:Relationship|Dynamic):\*\*\s*([^\n]+)', relationships)
    data['relationships'] = [(r[0].strip(), r[1].strip()) for r in rels[:5]]
    
    # Appearances - extract key scenes
    appearances = extract_section(text, 'Appearances')
    data['appearances'] = appearances
    
    # Casting - get primary choice
    casting = extract_section(text, 'Casting Reference')
    primary_match = re.search(r'### Primary Choice\s*\n\*\*([^*]+)\*\*', casting)
    if primary_match:
        data['casting'] = primary_match.group(1).strip()
    else:
        # Look for first bold actor name
        actor_match = re.search(r'\*\*([A-Z][a-z]+ [A-Z][a-z]+)\*\*', casting)
        data['casting'] = actor_match.group(1) if actor_match else ""
    
    return data

def format_optimized_character(data):
    """Format character data in optimized template"""
    lines = []
    
    # Header with casting
    name = data.get('name', 'Unknown')
    casting = data.get('casting', '')
    
    lines.append(f"# {name}")
    if casting:
        lines.append(f"**Visualize as:** {casting}")
    lines.append("")
    
    # Basics
    lines.append("## Basics")
    
    # Birth/Age line
    birth = data.get('birth', '')
    age = data.get('age_1865') or data.get('age_1863', '')
    rank = data.get('rank', '')
    
    basic_parts = []
    if birth:
        # Shorten to year and place
        birth_short = re.sub(r'^[A-Za-z]+ \d+, ', '', birth)
        basic_parts.append(f"**Born:** {birth_short}")
    if age:
        basic_parts.append(f"**Age 1865:** {age}")
    if rank:
        basic_parts.append(f"**Rank:** {rank}")
    
    if basic_parts:
        lines.append(f"- {' | '.join(basic_parts)}")
    
    role = data.get('role', '')
    if role:
        lines.append(f"- **Role:** {role}")
    
    nickname = data.get('nickname', '')
    if nickname:
        lines.append(f"- **Nicknames:** {nickname}")
    
    physical = data.get('physical', '')
    if physical:
        lines.append(f"- **Physical:** {physical}")
    
    lines.append("")
    
    # Personality
    lines.append("## Personality")
    if data.get('traits'):
        trait_strs = [f"{t[0]}" for t in data['traits']]
        lines.append(f"- **Core:** {', '.join(trait_strs)}")
    if data.get('weaknesses'):
        lines.append(f"- **Flaws:** {'; '.join(data['weaknesses'])}")
    
    lines.append("")
    
    # NTL Divergence - the important stuff, keep full
    if data.get('ntl'):
        lines.append("## NTL Divergence")
        lines.append(data['ntl'])
        lines.append("")
    
    # Relationships
    if data.get('relationships'):
        lines.append("## Key Relationships")
        for name_rel, desc in data['relationships']:
            lines.append(f"- **{name_rel}:** {desc}")
        lines.append("")
    
    # Appearances - condense
    if data.get('appearances'):
        lines.append("## Book Appearances")
        app = data['appearances']
        # Extract key scenes only
        scenes = re.findall(r'-\s*(?:\*\*)?([^:\n*]+)(?:\*\*)?:\s*([^\n]+)', app)
        for date, desc in scenes[:6]:
            lines.append(f"- {date.strip()}: {desc.strip()}")
        lines.append("")
    
    lines.append("---")
    lines.append("")
    
    return '\n'.join(lines)

def process_file(filepath, output_path):
    """Process a character file"""
    content = filepath.read_text(encoding='utf-8')
    
    # Split into individual character entries
    entries = re.split(r'\n(?=# [A-Z])', content)
    
    optimized = []
    
    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue
        
        # File header
        if entry.startswith('# Union Military') or entry.startswith('# Confederate Military'):
            lines = entry.split('\n')[:6]
            optimized.append('\n'.join(lines))
            optimized.append('\n---\n')
            continue
        
        # Already-optimized Lincoln - keep as-is
        if entry.startswith('# Abraham Lincoln') and '## Basics' in entry:
            optimized.append(entry)
            continue
        
        # Parse and optimize other characters
        if entry.startswith('# '):
            try:
                data = parse_character(entry)
                opt = format_optimized_character(data)
                optimized.append(opt)
            except Exception as e:
                print(f"Error processing: {e}")
                optimized.append(entry)
    
    result = '\n'.join(optimized)
    output_path.write_text(result, encoding='utf-8')
    return result

def main():
    base = Path(r'C:\Users\MichaelL\Documents\Personal\ashverse\characters')
    
    files = ['union-military.md', 'confederate-military.md']
    
    for filename in files:
        filepath = base / filename
        output_path = base / filename.replace('.md', '-optimized.md')
        
        print(f"\nProcessing {filename}...")
        
        original = filepath.read_text(encoding='utf-8')
        original_lines = len(original.split('\n'))
        original_tokens = int(len(original.split()) * 1.3)
        
        result = process_file(filepath, output_path)
        
        opt_lines = len(result.split('\n'))
        opt_tokens = int(len(result.split()) * 1.3)
        
        print(f"  Original:  {original_lines:>5} lines, {original_tokens:>6,} tokens")
        print(f"  Optimized: {opt_lines:>5} lines, {opt_tokens:>6,} tokens")
        print(f"  Savings:   {original_lines - opt_lines:>5} lines ({((original_lines - opt_lines)/original_lines)*100:.0f}%), {original_tokens - opt_tokens:,} tokens ({((original_tokens - opt_tokens)/original_tokens)*100:.0f}%)")
        print(f"  Written:   {output_path.name}")

if __name__ == '__main__':
    main()
