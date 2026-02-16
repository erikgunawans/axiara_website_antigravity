import os

def propagate_footer():
    # Configuration
    footer_source_path = 'src/components/footer.html'
    target_files = [
        'about.html',
        'careers.html',
        'legal/privacy.html',
        'legal/terms.html'
    ]

    # Read the Golden Master Footer
    try:
        with open(footer_source_path, 'r', encoding='utf-8') as f:
            footer_content = f.read().strip()
    except FileNotFoundError:
        print(f"Error: Source footer file '{footer_source_path}' not found.")
        return

    print(f"Loaded footer source ({len(footer_content)} bytes).")

    # Process each target file
    for file_path in target_files:
        if not os.path.exists(file_path):
            print(f"Skipping {file_path}: File not found.")
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the footer block
        start_marker = '<footer id="axiara-footer"'
        end_marker = '</footer>'

        start_index = content.find(start_marker)
        if start_index == -1:
            print(f"Skipping {file_path}: Footer start marker not found.")
            continue

        # Find the end of the footer block (after the start)
        # We need to find the closing tag corresponding to the footer.
        # Assuming simple structure where </footer> closes the footer.
        end_index = content.find(end_marker, start_index)
        if end_index == -1:
            print(f"Skipping {file_path}: Footer end marker not found.")
            continue

        # Include the markers in replacement?
        # The variables `start_index` points to '<', `end_index` points to '<'.
        # We want to replace everything from `start_index` to `end_index + len(end_marker)`.
        
        replacement_end = end_index + len(end_marker)
        
        new_content = content[:start_index] + footer_content + content[replacement_end:]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated {file_path}.")

if __name__ == "__main__":
    propagate_footer()
