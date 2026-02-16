#!/usr/bin/env python3
import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Inject Skip Link & Main ID
    # -----------------------------------------------------------
    if 'Skip to content' not in content:
        # Find body start
        if '<body' in content:
            # Insert skip link after opening body tag
            skip_link = '\n    <a href="#main-content" class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 bg-axiara-crimson text-white px-4 py-2 z-50 font-code text-sm">Skip to content</a>'
            content = re.sub(r'(<body[^>]*>)', r'\1' + skip_link, content, count=1)
            
            # Add id="main-content" to <main> if likely wrapper, or first <section> or <header> after navbar
            # If <main id="..."> already exists, good.
            if 'id="main-content"' not in content:
                if '<main' in content:
                    content = content.replace('<main', '<main id="main-content"', 1)
                else:
                    # Try to find the first non-navbar header/section
                    # Navbar often in <div id="navbar-placeholder"> or similar.
                    # We want the content after that.
                    
                    # Pattern: <header ...> (Home hero) or <section ...> (Inner hero)
                    # We will add id="main-content" to the first <header> or <section> that appears AFTER the navbar placeholder
                    
                    parts = content.split('navbar-placeholder')
                    if len(parts) > 1:
                        # Scan the second part
                        pre_nav = parts[0] + 'navbar-placeholder'
                        post_nav = parts[1]
                        
                        # Replace first header or section in post_nav
                        new_post_nav = re.sub(r'(<(header|section))', r'\1 id="main-content"', post_nav, count=1)
                        content = pre_nav + new_post_nav
                    else:
                        # Fallback: just put it on the first header/section found
                        content = re.sub(r'(<(header|section))', r'\1 id="main-content"', content, count=1)

    # 2. Fix Low Contrast (Crimson on Small Text)
    # -----------------------------------------------------------
    # Pattern: text-xs ... text-axiara-crimson -> text-xs ... text-axiara-silver
    # We want to keep the crimson color for Hover or Large text, but separate it from small text static.
    
    # Regex to find class strings containing both text-xs/text-sm AND text-axiara-crimson
    # We will replace text-axiara-crimson with text-axiara-silver in those specific combos
    
    def repl_contrast(match):
        attrs = match.group(2)
        if 'class="' in attrs:
            class_match = re.search(r'class="([^"]*)"', attrs)
            if class_match:
                classes = class_match.group(1)
                
                # Check for small text + crimson
                is_small = 'text-xs' in classes or 'text-sm' in classes
                is_crimson = 'text-axiara-crimson' in classes
                is_hover = 'hover:text-axiara-crimson' in classes
                
                # If it has crimson as a base color (not just hover) and is small
                if is_small and is_crimson and not 'font-bold' in classes and not 'font-black' in classes:
                    # Replace base crimson with silver
                    print(f"  [Replacing Contrast] {classes} -> Silver")
                    # Rebuild classes safely
                    cls_list = classes.split()
                    final_list = []
                    for c in cls_list:
                        if c == 'text-axiara-crimson':
                            final_list.append('text-axiara-silver')
                        else:
                            final_list.append(c)
                    new_classes = ' '.join(final_list)
                    
                    new_attrs = attrs.replace(f'class="{classes}"', f'class="{new_classes}"')
                    return f'<{match.group(2)} {new_attrs}>'
        
        return match.group(0)

    # Apply to all tags
    content = re.sub(r'<(\w+)\s+([^>]+)>', repl_contrast, content)

    # 3. Ensure HTML Lang="en"
    # -----------------------------------------------------------
    content = re.sub(r'<html(?![^>]*lang=)[^>]*>', '<html lang="en">', content)
    content = re.sub(r'<html\s+lang="[^"]*"\s*>', '<html lang="en">', content)

    # 4. Ensure Prefers Reduced Motion
    # -----------------------------------------------------------
    if 'prefers-reduced-motion' not in content:
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
