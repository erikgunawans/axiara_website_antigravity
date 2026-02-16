import os
import re
import sys

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Inject axiara.css if missing
    if 'axiara.css' not in content:
        # Try to insert before </head>, or valid style tag, or tailwind script
        if '</head>' in content:
            content = content.replace('</head>', '<link rel="stylesheet" href="/src/css/axiara.css">\n</head>')
        else:
            print(f"[WARN] Could not insert CSS link in {filepath}")

    # 2. Fix H1 classes (Use .text-hero)
    # Matches <h1 ... class="...">. 
    # Logic: Remove text-Xxl classes, add text-hero.
    def replace_h1_class(match):
        attrs = match.group(1)
        if 'class="' in attrs:
            # Extract class content
            class_match = re.search(r'class="([^"]*)"', attrs)
            if class_match:
                classes = class_match.group(1)
                # Remove conflicting text sizes
                new_classes = re.sub(r'\btext-(2xl|3xl|4xl|5xl|6xl|7xl|8xl|9xl)\b', '', classes)
                # Remove md/lg text sizes on H1 if we want strict text-hero
                new_classes = re.sub(r'\b(md|lg|xl):text-[^\s]+\b', '', new_classes)
                
                # Add text-hero if missing
                if 'text-hero' not in new_classes:
                    new_classes = 'text-hero ' + new_classes
                
                # Clean up spaces
                new_classes = re.sub(r'\s+', ' ', new_classes).strip()
                return f'<h1 {attrs.replace(f'class="{classes}"', f'class="{new_classes}"')}>'
        return match.group(0)

    content = re.sub(r'<h1\s+([^>]+)>', replace_h1_class, content)

    # 3. Fix Grids (Force grid-cols-1 on mobile)
    # Regex to find grid-cols-N where N > 1, NOT prefixed by md/lg/xl, and NOT preceded by grid-cols-1
    # This is complex to do with single regex. 
    # Strategy: Parse class strings. If 'grid-cols-N' (N>1) exists without 'md:', change it to 'grid-cols-1 md:grid-cols-N'
    
    def fix_grid_classes(match):
        prefix = match.group(1)
        classes = match.group(2)
        
        # Split classes
        cls_list = classes.split()
        new_list = []
        has_grid_cols_1 = 'grid-cols-1' in cls_list
        
        for cls in cls_list:
            # Check for naked grid-cols-N (N>1)
            # e.g. grid-cols-2
            m = re.match(r'^grid-cols-([2-9]|1[0-2])$', cls)
            if m:
                # It's a mobile multi-column grid.
                # Transform to: grid-cols-1 md:grid-cols-N
                # But only if grid-cols-1 isn't already there.
                if not has_grid_cols_1:
                    new_list.append('grid-cols-1')
                    new_list.append(f'md:{cls}')
                    has_grid_cols_1 = True # Prevent adding it again
                else:
                    # If grid-cols-1 exists, just make this one md:
                    new_list.append(f'md:{cls}')
            else:
                new_list.append(cls)
        
        return f'{prefix}"{" ".join(new_list)}"'

    content = re.sub(r'(class=)"([^"]*)"', fix_grid_classes, content)

    # 4. Remove rounded classes
    # rounded-full, rounded-lg, etc -> rounded-none (or remove)
    def remove_rounded(match):
        prefix = match.group(1)
        classes = match.group(2)
        # Remove any class starting with rounded- unless it's rounded-none
        new_classes = re.sub(r'\brounded-(?!none)[^\s]+\b', '', classes)
        # Remove naked 'rounded'
        new_classes = re.sub(r'\brounded\b', '', new_classes)
        return f'{prefix}"{re.sub(r"\s+", " ", new_classes).strip()}"'

    content = re.sub(r'(class=)"([^"]*)"', remove_rounded, content)

    # 5. Add prefers-reduced-motion if missing (simple check)
    if 'prefers-reduced-motion' not in content:
        # Insert into existing style block or create new one
        motion_css = """
        <style>
            @media (prefers-reduced-motion: reduce) {
                *, ::before, ::after {
                    animation-duration: 0.01ms !important;
                    animation-iteration-count: 1 !important;
                    transition-duration: 0.01ms !important;
                    scroll-behavior: auto !important;
                }
            }
        </style>
        """
        if '</body>' in content:
            content = content.replace('</body>', motion_css + '\n</body>')

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[FIXED] {filepath}")
    else:
        print(f"[OK] {filepath}")

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for dirpath, _, filenames in os.walk(root_dir):
        if '.gemini' in dirpath or '.git' in dirpath:
            continue
        for filename in filenames:
            if filename.endswith('.html'):
                fix_file(os.path.join(dirpath, filename))

if __name__ == '__main__':
    main()
