# python merge_files.py proc/heb.md proc/aram.md
# for info: python merge_files.py -h


"""
Script to merge aram.md content into heb.md
Each verse marker is preserved, followed by the aram line, then two newlines, then the original heb line.
"""

import re
import argparse

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_sections(content):
    """Extract sections by h2 headers"""
    sections = {}
    current_header = None
    current_lines = []

    for line in content.split('\n'):
        if line.startswith('## '):
            if current_header:
                sections[current_header] = current_lines
            current_header = line.strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_header:
        sections[current_header] = current_lines

    return sections

def extract_text_lines(lines):
    """Extract only text lines (non-empty, non-verse markers for heb)"""
    text_lines = []
    for line in lines:
        line = line.strip()
        if line:  # Non-empty
            text_lines.append(line)
    return text_lines

def extract_text_lines_from_heb(lines):
    """Extract text lines from Hebrew, joining split lines and excluding verse markers"""
    text_lines = []
    current_text = None

    for line in lines:
        line = line.strip()
        if not line:  # Skip empty lines
            continue

        if is_verse_marker(line):
            # Save any accumulated text before this verse marker
            if current_text:
                text_lines.append(current_text)
                current_text = None
            # Don't add the verse marker itself
            continue

        # This is text content
        if current_text is None:
            # Start a new text line
            current_text = line
        else:
            # This line is a continuation of the previous text
            current_text = current_text + ' ' + line

    # Don't forget the last accumulated text
    if current_text:
        text_lines.append(current_text)

    return text_lines

def is_verse_marker(line):
    """Check if a line is a Hebrew verse marker"""
    line = line.strip()
    # Verse markers are single Hebrew letters or short Hebrew sequences on their own line
    if not line:
        return False
    # Check if it's a short Hebrew sequence (likely a verse number)
    # Hebrew letters: א-ת
    hebrew_pattern = re.compile(r'^[\u05D0-\u05EA]+$')
    if hebrew_pattern.match(line) and len(line) <= 3:
        return True
    return False

def merge_section(heb_lines, aram_lines):
    """Merge aram lines into heb structure"""
    result = []
    aram_index = 0

    i = 0
    while i < len(heb_lines):
        line = heb_lines[i].strip()

        if not line:  # Empty line
            result.append('')
            i += 1
            continue

        if is_verse_marker(line):
            # This is a verse marker
            verse_marker = line
            result.append(f'**{verse_marker.strip()}**')
            result.append('')  # Single newline below verse marker

            # Get the next non-empty line from heb (the heb text for this verse)
            i += 1
            while i < len(heb_lines) and not heb_lines[i].strip():
                i += 1

            if i < len(heb_lines):
                heb_text = heb_lines[i].strip()

                # Add corresponding aram line
                if aram_index < len(aram_lines):
                    aram_text = aram_lines[aram_index].strip()
                    result.append(aram_text)
                    result.append('')
                    # Add original heb line
                    result.append(heb_text)
                    aram_index += 1
                else:
                    # No more aram lines, just add heb text
                    result.append(heb_text)
                i += 1
        else:
            # Shouldn't happen if structure is correct, but handle it
            result.append(line)
            i += 1

    return result

def main(heb_file, aram_file):
    # Read both files
    heb_content = read_file(heb_file)
    aram_content = read_file(aram_file)

    # Extract sections
    heb_sections = extract_sections(heb_content)
    aram_sections = extract_sections(aram_content)

    heb_headers = list(heb_sections.keys())
    aram_headers = list(aram_sections.keys())

    if len(heb_headers) != len(aram_headers):
        print(f"ERROR: Different number of sections. Hebrew: {len(heb_headers)}, Aramaic: {len(aram_headers)}")
        print(f"Hebrew sections: {heb_headers}")
        print(f"Aramaic sections: {aram_headers}")
        return

    # Process each section
    merged_content = ['']  # Start with empty line

    for i, heb_header in enumerate(heb_headers):
        aram_header = aram_headers[i]

        heb_lines = heb_sections[heb_header]
        aram_lines = extract_text_lines(aram_sections[aram_header])

        # Validate line counts match
        heb_text_lines = extract_text_lines_from_heb(heb_lines)
        heb_text_count = len(heb_text_lines)
        aram_text_count = len(aram_lines)

        if heb_text_count != aram_text_count:
            print(f"ERROR: Line count mismatch in section {i+1}")
            print(f"  Hebrew section: {heb_header} has {heb_text_count} text lines")
            print(f"  Aramaic section: {aram_header} has {aram_text_count} text lines")
            print(f"  Debug - Hebrew non-empty lines (with verse markers): {len([l for l in heb_lines if l.strip()])}")
            print(f"  Debug - Hebrew verse markers found: {len([l for l in heb_lines if l.strip() and is_verse_marker(l.strip())])}")

            # Show first few text lines from each
            print(f"\n  First 5 Hebrew text lines:")
            for idx, line in enumerate(heb_text_lines[:5]):
                print(f"    {idx+1}: {line[:80]}")
            print(f"\n  First 5 Aramaic text lines:")
            for idx, line in enumerate(aram_lines[:5]):
                print(f"    {idx+1}: {line[:80]}")

            print(f"\n  Last 5 Hebrew text lines:")
            for idx, line in enumerate(heb_text_lines[-5:], start=len(heb_text_lines)-4):
                print(f"    {idx}: {line[:80]}")
            print(f"\n  Last 5 Aramaic text lines:")
            for idx, line in enumerate(aram_lines[-5:], start=len(aram_lines)-4):
                print(f"    {idx}: {line[:80]}")

            print(f"  Script stopped.")
            return

        print(f"Processing section {i+1}: {heb_header} ({heb_text_count} lines)")

        merged_content.append(heb_header)
        merged_content.append('')

        merged_lines = merge_section(heb_lines, aram_lines)
        merged_content.extend(merged_lines)
        merged_content.append('')

    # Write result
    result = '\n'.join(merged_content)
    write_file('result-merged.md', result)
    print("Done! Output written to result-merged.md")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge aram.md content into heb.md structure')
    parser.add_argument('heb_file', help='Path to the Hebrew file (e.g., proc/heb.md)')
    parser.add_argument('aram_file', help='Path to the Aramaic file (e.g., proc/aram.md)')

    args = parser.parse_args()
    main(args.heb_file, args.aram_file)
