# One-off fix: replace July 6-10 block in part-02 with short July 6-8 section (POD campaign)
path = 'world-building/reference/pod-campaign/part-02-harrisburg-occupation.md'
with open(path, 'r', encoding='utf-8', errors='replace') as f:
    text = f.read()

start_marker = "### Longstreet's Gradual East-Bank Shift"
end_marker = "## SUMMARY: HARRISBURG OCCUPATION (JULY 3-10)"
new_section = """### Main Body Holds; Early En Route to Reading

**July 6–8:**
- Main body (~50–55k) remains at Harrisburg (east bank and heights); no shift east of whole army; no Quaker guns
- Early's division (~5–6k) departed July 5 for Reading; en route July 6–7; hits Reading ~July 7–8 (see Part 3)
- Foraging, refit, and telegraph disinformation continue
- Meade holds west bank in strength; does not go to Baltimore; does not assault again after Camp Hill

**Union observation:** Cavalry reports Confederate positions unchanged at Harrisburg; no indication of evacuation. When Early hits Reading, Meade faces catch-22: split force between Harrisburg and York (see Part 3).

"""

idx_start = text.find(start_marker)
idx_end = text.find(end_marker)
if idx_start == -1 or idx_end == -1:
    print('Markers not found', idx_start, idx_end)
else:
    text = text[:idx_start] + new_section + "\n" + end_marker + text[idx_end + len(end_marker):]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print('July 6-10 block replaced with July 6-8 section')
