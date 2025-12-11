#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Butterfly Check: Evaluates flow of events from PoD forward using plausibility gating.

Checks for:
- Timeline inconsistencies (events out of order, impossible sequences)
- Causality violations (effects before causes)
- Missing prerequisites
- Plausibility scores below threshold (70%)
- Contradictory information
- Events that don't flow logically from PoD
"""

import re
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional

# Fix Windows console encoding
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except:
        pass

# Plausibility thresholds from rules
PLAUSIBILITY_THRESHOLD = 70
LOCKED_THRESHOLD = 90
HIGHLY_PLAUSIBLE_THRESHOLD = 80
PLAUSIBLE_THRESHOLD = 70

# PoD date
POD_DATE = datetime(1863, 7, 1)

class TimelineEvent:
    """Represents a single timeline event."""
    def __init__(self, date_str: str, event: str, plausibility: Optional[int], 
                 source_file: str, line_num: int, key_consequence: str = ""):
        self.date_str = date_str
        self.event = event
        self.plausibility = plausibility
        self.source_file = source_file
        self.line_num = line_num
        self.key_consequence = key_consequence
        self.date = self._parse_date(date_str)
    
    def _parse_date(self, date_str: str) -> Optional[datetime]:
        """Parse date string to datetime object."""
        # Handle various date formats
        date_str = date_str.strip()
        
        # Try "1 Jul 1863" format
        try:
            return datetime.strptime(date_str, "%d %b %Y")
        except:
            pass
        
        # Try "July 1, 1863" format
        try:
            return datetime.strptime(date_str, "%B %d, %Y")
        except:
            pass
        
        # Try "1863-07-01" format
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except:
            pass
        
        # Try "Jul 1863" format (month only)
        try:
            return datetime.strptime(date_str, "%b %Y")
        except:
            pass
        
        # Try "1863" format (year only)
        try:
            year = int(date_str)
            return datetime(year, 1, 1)
        except:
            pass
        
        return None
    
    def __repr__(self):
        return f"TimelineEvent({self.date_str}, {self.plausibility}%)"

class ButterflyChecker:
    """Checks timeline consistency and plausibility."""
    
    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)
        self.events: List[TimelineEvent] = []
        self.issues: List[Dict] = []
    
    def extract_timeline_events(self, file_path: Path) -> List[TimelineEvent]:
        """Extract timeline events from a markdown file."""
        events = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
                
            in_timeline_table = False
            table_headers = []
            
            for i, line in enumerate(lines, 1):
                # Look for timeline tables (markdown tables)
                if '|' in line:
                    # Check if this is a header row (has "Date" column)
                    if 'Date' in line or ('date' in line.lower() and '#' in line):
                        in_timeline_table = True
                        table_headers = [h.strip().lower() for h in line.split('|') if h.strip()]
                        continue
                    
                    # Check if this is a separator row
                    if line.strip().startswith('|---') or re.match(r'^\|\s*[-:]+\s*\|', line):
                        continue
                
                if in_timeline_table:
                    # End of table
                    if not '|' in line or (line.strip() == '' and i > 0):
                        in_timeline_table = False
                        table_headers = []
                        continue
                    
                    # Parse table row - split by | and get all parts
                    parts = [p.strip() for p in line.split('|')]
                    # Remove empty first/last if they exist
                    if parts and not parts[0]:
                        parts = parts[1:]
                    if parts and not parts[-1]:
                        parts = parts[:-1]
                    
                    # Need at least 2 columns
                    if len(parts) < 2:
                        continue
                    
                    # Skip header rows and separators
                    first_col = parts[0].lower().strip()
                    if first_col in ['#', 'date', '---', ''] or '---' in first_col:
                        continue
                    
                    # Try to identify which column is the date
                    # Format 1: # | Date | Event | Plausibility | Consequence
                    # Format 2: Date | Event | ...
                    date_str = ""
                    event = ""
                    plausibility = None
                    consequence = ""
                    
                    # Check if first column is a number (row number)
                    if first_col.isdigit() or first_col.endswith('a') or first_col.endswith('b') or first_col.endswith('c'):
                        # Format 1: # | Date | Event | Plausibility | Consequence
                        if len(parts) >= 3:
                            date_str = parts[1]  # Date is second column
                            event = parts[2]     # Event is third column
                            if len(parts) >= 4:
                                # Extract plausibility from 4th column
                                plausibility_match = re.search(r'(\d+)%', parts[3])
                                if plausibility_match:
                                    plausibility = int(plausibility_match.group(1))
                            if len(parts) >= 5:
                                consequence = parts[4]
                    else:
                        # Format 2: Date | Event | ...
                        date_str = parts[0]
                        event = parts[1] if len(parts) > 1 else ""
                        if len(parts) >= 3:
                            plausibility_match = re.search(r'(\d+)%', parts[2])
                            if plausibility_match:
                                plausibility = int(plausibility_match.group(1))
                    
                    # Verify date_str looks like a date
                    if date_str and re.search(r'\d{4}|\d{1,2}\s+(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)', date_str, re.IGNORECASE):
                        if event:
                            event_obj = TimelineEvent(
                                date_str=date_str,
                                event=event,
                                plausibility=plausibility,
                                source_file=str(file_path.relative_to(self.base_dir)),
                                line_num=i,
                                key_consequence=consequence
                            )
                            events.append(event_obj)
            
            # Skip narrative text extraction - focus only on timeline tables
        
        except Exception as e:
            print(f"Error reading {file_path}: {e}", file=sys.stderr)
        
        return events
    
    def check_chronological_order(self):
        """Check that events are in chronological order within the same timeline section."""
        # Group events by source file and check order within each file
        events_by_file = {}
        for event in self.events:
            if event.date:
                if event.source_file not in events_by_file:
                    events_by_file[event.source_file] = []
                events_by_file[event.source_file].append(event)
        
        for file_path, file_events in events_by_file.items():
            # Sort by line number first (preserve document order)
            file_events.sort(key=lambda x: x.line_num)
            
            # Check if dates are out of order
            for i in range(len(file_events) - 1):
                if file_events[i].date and file_events[i+1].date:
                    # Allow some flexibility for date ranges
                    if file_events[i].date > file_events[i+1].date:
                        # Check if it's a date range issue (e.g., "Jul-Oct" vs "Aug")
                        date1_str = file_events[i].date_str.lower()
                        date2_str = file_events[i+1].date_str.lower()
                        
                        # Skip if both are ranges or if it's clearly intentional
                        if '–' in date1_str or '-' in date1_str or 'late' in date1_str or 'early' in date1_str:
                            continue
                        if '–' in date2_str or '-' in date2_str or 'late' in date2_str or 'early' in date2_str:
                            continue
                        
                        self.issues.append({
                            'type': 'chronological_order',
                            'severity': 'error',
                            'message': f"Events out of order in {file_path}: {file_events[i].date_str} (line {file_events[i].line_num}) comes after {file_events[i+1].date_str} (line {file_events[i+1].line_num})",
                            'event1': file_events[i],
                            'event2': file_events[i+1]
                        })
    
    def check_plausibility_thresholds(self):
        """Check that plausibility scores meet thresholds."""
        # Only check actual timeline events with plausibility scores
        timeline_events = [e for e in self.events if e.plausibility is not None and e.date]
        
        for event in timeline_events:
            if event.plausibility < PLAUSIBILITY_THRESHOLD:
                self.issues.append({
                    'type': 'plausibility_below_threshold',
                    'severity': 'warning',
                    'message': f"Plausibility {event.plausibility}% below {PLAUSIBILITY_THRESHOLD}% threshold: {event.date_str} - {event.event[:80]}",
                    'event': event
                })
    
    def check_pod_flow(self):
        """Check that events flow logically from PoD."""
        # Events before PoD should not be affected
        # Only check events that are clearly timeline entries (not metadata)
        pre_pod_events = [e for e in self.events if e.date and e.date < POD_DATE and 
                         not any(skip in e.event.lower() for skip in ['date:', 'last updated:', 'status:', 'purpose:', 'note:', '##', '###'])]
        
        for event in pre_pod_events:
            # Check if event mentions NTL-specific things (but allow historical context)
            event_lower = event.event.lower()
            # Skip if it's clearly historical context (OTL mentions)
            if 'otl' in event_lower or 'historical' in event_lower or 'precedent' in event_lower:
                continue
            
            if any(keyword in event_lower for keyword in ['longstreet assumes', 'longstreet commands', 'longstreet orders', 'withdrawal', 'countermarch']):
                self.issues.append({
                    'type': 'pod_flow',
                    'severity': 'error',
                    'message': f"Event before PoD mentions NTL-specific actions: {event.event[:100]}",
                    'event': event
                })
    
    def check_causality(self):
        """Check for causality violations."""
        # Known causal chains that must be verified
        causal_chains = [
            # Toombs Act → Boycott (must be at least 30 days)
            {
                'cause': ['toombs act', 'toombs elected', 're-opens slave trade', 'toombs act disaster'],
                'effect': ['boycott', 'global boycott', 'british boycott', 'royal navy'],
                'min_delay_days': 30,
                'description': 'Toombs Act → Global Boycott'
            },
            # Raids → Joint Crackdown (must be at least 180 days)
            {
                'cause': ['last hurrah', 'organized raids'],
                'effect': ['joint crackdown', 'joint patrols'],
                'min_delay_days': 180,
                'description': 'Raids → Joint Crackdown'
            },
            # Toombs elected → Toombs Act signed (must be within 1 year)
            {
                'cause': ['toombs elected'],
                'effect': ['toombs act', 'signs toombs act'],
                'max_delay_days': 365,
                'description': 'Toombs Election → Toombs Act'
            }
        ]
        
        # Filter to only actual timeline events (not metadata)
        timeline_events = [e for e in self.events if e.date and 
                          not any(skip in e.event.lower() for skip in ['date:', 'last updated:', 'status:', 'purpose:', 'note:', '##', '###', '|'])]
        
        for chain in causal_chains:
            cause_events = [e for e in timeline_events if 
                          any(keyword in e.event.lower() for keyword in chain['cause'])]
            effect_events = [e for e in timeline_events if 
                           any(keyword in e.event.lower() for keyword in chain['effect'])]
            
            for cause in cause_events:
                for effect in effect_events:
                    if effect.date > cause.date:
                        delay = (effect.date - cause.date).days
                        
                        if 'min_delay_days' in chain and delay < chain['min_delay_days']:
                            self.issues.append({
                                'type': 'causality_violation',
                                'severity': 'error',
                                'message': f"{chain['description']}: {effect.date_str} happens {delay} days after {cause.date_str}, but needs at least {chain['min_delay_days']} days",
                                'cause': cause,
                                'effect': effect
                            })
                        
                        if 'max_delay_days' in chain and delay > chain['max_delay_days']:
                            self.issues.append({
                                'type': 'causality_violation',
                                'severity': 'warning',
                                'message': f"{chain['description']}: {effect.date_str} happens {delay} days after {cause.date_str}, expected max {chain['max_delay_days']} days",
                                'cause': cause,
                                'effect': effect
                            })
    
    def check_consolidation_consistency(self):
        """Check for inconsistencies introduced by consolidation."""
        # Check for duplicate events with different dates
        # Only check actual timeline events (not metadata)
        timeline_events = [e for e in self.events if e.date and 
                          not any(skip in e.event.lower() for skip in ['date:', 'last updated:', 'status:', 'purpose:', 'note:', '##', '###']) and
                          len(e.event) > 20]  # Filter out short metadata lines
        
        # Group by event description (normalized)
        event_groups = {}
        for event in timeline_events:
            # Normalize event text (remove dates, percentages, etc.)
            normalized = re.sub(r'\d+%', '', event.event.lower())
            normalized = re.sub(r'\d{4}', '', normalized)
            normalized = re.sub(r'\d{1,2}\s+(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)', '', normalized, flags=re.IGNORECASE)
            normalized = normalized.strip()[:100]  # First 100 chars
            
            if normalized and len(normalized) > 20:  # Only meaningful events
                if normalized not in event_groups:
                    event_groups[normalized] = []
                event_groups[normalized].append(event)
        
        for event_key, group in event_groups.items():
            if len(group) > 1:
                # Check if dates are significantly different (more than 1 year)
                dates = [e.date for e in group if e.date]
                if len(dates) > 1:
                    date_range = max(dates) - min(dates)
                    if date_range.days > 365:
                        self.issues.append({
                            'type': 'duplicate_event_different_dates',
                            'severity': 'error',
                            'message': f"Same event appears with dates {min(dates).strftime('%Y-%m-%d')} and {max(dates).strftime('%Y-%m-%d')} ({date_range.days} days apart)",
                            'events': group[:3]  # Show first 3
                        })
    
    def run_checks(self, file_paths: List[Path]):
        """Run all checks on specified files."""
        print("Extracting timeline events...")
        for file_path in file_paths:
            events = self.extract_timeline_events(file_path)
            self.events.extend(events)
            print(f"  Found {len(events)} events in {file_path.name}")
        
        print(f"\nTotal events extracted: {len(self.events)}")
        print(f"Events with dates: {len([e for e in self.events if e.date])}")
        print(f"Events with plausibility scores: {len([e for e in self.events if e.plausibility is not None])}")
        
        print("\nRunning checks...")
        self.check_chronological_order()
        self.check_plausibility_thresholds()
        self.check_pod_flow()
        self.check_causality()
        self.check_consolidation_consistency()
    
    def print_report(self):
        """Print comprehensive report."""
        print("\n" + "="*80)
        print("BUTTERFLY CHECK REPORT")
        print("="*80)
        print(f"\nPoD: July 1, 1863 (Lee dies)")
        print(f"Total Events Checked: {len(self.events)}")
        print(f"Issues Found: {len(self.issues)}")
        
        if not self.issues:
            print("\n[OK] No issues found! Timeline flows correctly from PoD.")
            return
        
        # Group by severity
        errors = [i for i in self.issues if i['severity'] == 'error']
        warnings = [i for i in self.issues if i['severity'] == 'warning']
        
        print(f"\n[ERROR] ERRORS: {len(errors)}")
        print(f"[WARNING] WARNINGS: {len(warnings)}")
        
        if errors:
            print("\n" + "="*80)
            print("ERRORS")
            print("="*80)
            for i, issue in enumerate(errors, 1):
                print(f"\n{i}. {issue['type'].upper().replace('_', ' ')}")
                print(f"   {issue['message']}")
                if 'event' in issue:
                    event = issue['event']
                    print(f"   File: {event.source_file}:{event.line_num}")
                    print(f"   Date: {event.date_str}")
                    print(f"   Event: {event.event}")
                if 'cause' in issue and 'effect' in issue:
                    print(f"   Cause: {issue['cause'].date_str} - {issue['cause'].event}")
                    print(f"   Effect: {issue['effect'].date_str} - {issue['effect'].event}")
        
        if warnings:
            print("\n" + "="*80)
            print("WARNINGS")
            print("="*80)
            for i, issue in enumerate(warnings, 1):
                print(f"\n{i}. {issue['type'].upper().replace('_', ' ')}")
                print(f"   {issue['message']}")
                if 'event' in issue:
                    event = issue['event']
                    print(f"   File: {event.source_file}:{event.line_num}")
                    print(f"   Date: {event.date_str}")
                    print(f"   Event: {event.event}")
        
        print("\n" + "="*80)
        print("RECOMMENDATIONS")
        print("="*80)
        
        if errors:
            print("\n1. Fix chronological order issues")
            print("2. Resolve causality violations")
            print("3. Check for duplicate events with different dates")
        
        if warnings:
            print("\n4. Review plausibility scores below threshold")
            print("5. Verify unusual delays in causal chains")

def main():
    """Main function."""
    base_dir = Path(".")
    
    # Files to check (master files)
    files_to_check = [
        base_dir / "world-building-master" / "06-timelines.md",
        base_dir / "world-building-master" / "01-core-foundation.md",
        base_dir / "world-building-master" / "02-economic-systems.md",
        base_dir / "world-building-master" / "03-political-systems.md",
    ]
    
    checker = ButterflyChecker(base_dir)
    checker.run_checks(files_to_check)
    checker.print_report()
    
    # Exit with error code if issues found
    errors = [i for i in checker.issues if i['severity'] == 'error']
    if errors:
        sys.exit(1)
    sys.exit(0)

if __name__ == '__main__':
    main()

