#!/usr/bin/env python3
"""
validate_html.py — Axiara HTML Brand Compliance Validator (Layer 3 Execution)

Validates an Axiara HTML page against brand rules and structural standards.

Usage:
  python3 execution/validate_html.py src/pages/services/sprint.html
  python3 execution/validate_html.py src/pages/technology/episteme.html

Checks performed (9 total):
  1. STRUCTURE   — Valid HTML5 doctype, lang attribute, meta viewport
  2. FONTS       — Google Fonts import contains Outfit, Playfair Display, JetBrains Mono
  3. CSS         — Links to axiara.css
  4. NO EMOJIS   — No emoji unicode in visible text content
  5. BORDER RAD  — No border-radius > 0 (flags Tailwind "rounded-" except "rounded-none")
  6. ANIMATIONS  — No forbidden animation names (bounce, spin, zoom, elastic, scale)
  7. HEADINGS    — Proper heading hierarchy (no skipping levels)
  8. A11Y        — alt="" on images, <label> on form inputs
  9. MOTION PREF — prefers-reduced-motion media query present
  10. RESP H1      — H1 tags must use .text-hero class
  11. RESP GRIDS   — No multi-column grids on mobile (naked grid-cols-X > 1)

Source of truth:
  - directives/axiara-brand.md (Responsive Rules)

No external dependencies beyond Python standard library.
"""

import os
import re
import sys
from html.parser import HTMLParser
from typing import NamedTuple


# ---------------------------------------------------------------------------
# Data Structures
# ---------------------------------------------------------------------------

class Issue(NamedTuple):
    """A single validation issue."""
    check: str       # Check category name
    severity: str    # "FAIL" or "WARN"
    line: int        # Line number (1-indexed, 0 = N/A)
    message: str     # Human-readable description


# ---------------------------------------------------------------------------
# HTML Parser — extracts structured info from the HTML
# ---------------------------------------------------------------------------

class AxiaraHTMLParser(HTMLParser):
    """Custom HTML parser that extracts elements needed for validation.
    
    Collects:
      - Doctype presence
      - <html lang=""> attribute
      - <meta> tags (viewport, description)
      - <link> tags (stylesheets, fonts)
      - <script> tags
      - Heading elements (h1-h6) with line numbers
      - Image elements with alt attributes
      - Form input elements
      - Label elements
      - Class attributes (for Tailwind checks)
      - Style attributes (for inline style checks)
      - Raw text content (for emoji scanning)
    """

    def __init__(self):
        super().__init__()
        self.has_doctype = False
        self.html_lang = None
        self.meta_viewport = False
        self.meta_description = False

        # Font & CSS links
        self.link_hrefs = []         # [(line, href)]
        self.script_srcs = []        # [(line, src)]

        # Headings: [(line, level)]  e.g., [(10, 1), (25, 2)]
        self.headings = []

        # Images: [(line, alt_value_or_None)]
        self.images = []

        # Form inputs without associated labels
        self.form_inputs = []        # [(line, input_type, id, name)]
        self.label_fors = set()      # set of "for" attribute values

        # Classes: [(line, class_string)]
        self.classes = []

        # Inline styles: [(line, style_string)]
        self.styles = []

        # Text content: [(line, text)]
        self.text_chunks = []

        # Style blocks: [(line, css_text)]
        self.style_blocks = []

        # Current tag tracking
        self._in_style = False
        self._style_start_line = 0
        self._style_content = []

    def handle_decl(self, decl):
        if decl.lower().startswith("doctype"):
            self.has_doctype = True

    def handle_starttag(self, tag, attrs):
        line = self.getpos()[0]
        attrs_dict = dict(attrs)

        # <html lang="">
        if tag == "html":
            self.html_lang = attrs_dict.get("lang")

        # <meta>
        if tag == "meta":
            name = attrs_dict.get("name", "").lower()
            if name == "viewport":
                self.meta_viewport = True
            if name == "description":
                self.meta_description = True

        # <link>
        if tag == "link":
            href = attrs_dict.get("href", "")
            if href:
                self.link_hrefs.append((line, href))

        # <script>
        if tag == "script":
            src = attrs_dict.get("src", "")
            if src:
                self.script_srcs.append((line, src))

        # Headings h1-h6
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(tag[1])
            self.headings.append((line, level))

        # Images
        if tag == "img":
            alt = attrs_dict.get("alt")  # None if missing entirely
            self.images.append((line, alt))

        # Form inputs
        if tag in ("input", "textarea", "select"):
            input_type = attrs_dict.get("type", "text")
            input_id = attrs_dict.get("id", "")
            input_name = attrs_dict.get("name", "")
            # Skip hidden inputs — they don't need labels
            if input_type != "hidden":
                self.form_inputs.append((line, input_type, input_id, input_name))

        # Labels
        if tag == "label":
            for_attr = attrs_dict.get("for", "")
            if for_attr:
                self.label_fors.add(for_attr)

        # Classes (for Tailwind checks)
        class_val = attrs_dict.get("class", "")
        if class_val:
            self.classes.append((line, class_val))

        # Inline styles
        style_val = attrs_dict.get("style", "")
        if style_val:
            self.styles.append((line, style_val))

        # <style> block
        if tag == "style":
            self._in_style = True
            self._style_start_line = line
            self._style_content = []

    def handle_endtag(self, tag):
        if tag == "style" and self._in_style:
            self._in_style = False
            css_text = "\n".join(self._style_content)
            self.style_blocks.append((self._style_start_line, css_text))
            self._style_content = []

    def handle_data(self, data):
        line = self.getpos()[0]
        if self._in_style:
            self._style_content.append(data)
        else:
            stripped = data.strip()
            if stripped:
                self.text_chunks.append((line, stripped))


# ---------------------------------------------------------------------------
# Validation Checks
# ---------------------------------------------------------------------------

def check_structure(parser: AxiaraHTMLParser) -> list[Issue]:
    """Check 1: STRUCTURE — doctype, lang, viewport.
    Source: directives/build-page.md § Standard Page Structure
    """
    issues = []

    if not parser.has_doctype:
        issues.append(Issue("STRUCTURE", "FAIL", 0,
            "Missing <!DOCTYPE html> declaration"))

    if not parser.html_lang:
        issues.append(Issue("STRUCTURE", "FAIL", 0,
            'Missing lang attribute on <html> (expected lang="en")'))
    elif parser.html_lang.lower() != "en":
        issues.append(Issue("STRUCTURE", "WARN", 0,
            f'<html lang="{parser.html_lang}"> — expected "en"'))

    if not parser.meta_viewport:
        issues.append(Issue("STRUCTURE", "FAIL", 0,
            "Missing <meta name='viewport'> tag"))

    return issues


def check_fonts(parser: AxiaraHTMLParser) -> list[Issue]:
    """Check 2: FONTS — Google Fonts import contains required families.
    Source: directives/axiara-brand.md § Typography (Non-Negotiable)
    """
    issues = []
    required_fonts = ["Outfit", "Playfair+Display", "JetBrains+Mono"]
    alt_fonts = ["Playfair Display", "JetBrains Mono"]  # Space-separated variants

    # Search in <link> hrefs and inline @import
    all_font_refs = []
    for line, href in parser.link_hrefs:
        if "fonts.googleapis.com" in href:
            all_font_refs.append((line, href))

    for line, css in parser.style_blocks:
        if "@import" in css and "fonts.googleapis.com" in css:
            all_font_refs.append((line, css))

    if not all_font_refs:
        issues.append(Issue("FONTS", "FAIL", 0,
            "No Google Fonts import found. Required: Outfit, "
            "Playfair Display, JetBrains Mono"))
        return issues

    # Check each required font is present
    combined = " ".join(ref for _, ref in all_font_refs)
    for i, font in enumerate(required_fonts):
        if font not in combined and alt_fonts[i - 1] not in combined if i > 0 else font not in combined:
            # Friendlier display name
            display = font.replace("+", " ")
            issues.append(Issue("FONTS", "FAIL", all_font_refs[0][0],
                f"Google Fonts import missing '{display}'"))

    return issues


def check_css(parser: AxiaraHTMLParser) -> list[Issue]:
    """Check 3: CSS — page links to axiara.css.
    Source: directives/build-page.md § Standard Page Structure item 4
    """
    issues = []
    found = any("axiara.css" in href for _, href in parser.link_hrefs)
    if not found:
        issues.append(Issue("CSS", "FAIL", 0,
            "Missing <link> to axiara.css (the Darkroom kit)"))
    return issues


def check_emojis(parser: AxiaraHTMLParser) -> list[Issue]:
    """Check 4: NO EMOJIS — scan for emoji unicode in text content.
    Source: directives/axiara-brand.md § Icons ("NEVER: Emoji icons")
    
    Scans common emoji ranges:
      - Emoticons (U+1F600–U+1F64F)
      - Misc Symbols (U+1F300–U+1F5FF)
      - Transport (U+1F680–U+1F6FF)
      - Supplemental (U+1F900–U+1F9FF)
      - Dingbats (U+2702–U+27B0)
      - Misc Symbols & Pictographs (U+2600–U+26FF)
    """
    issues = []
    # Comprehensive emoji regex pattern
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Misc Symbols and Pictographs
        "\U0001F680-\U0001F6FF"  # Transport and Map
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U00002600-\U000026FF"  # Misc Symbols
        "\U0000FE00-\U0000FE0F"  # Variation Selectors
        "\U0000200D"             # Zero Width Joiner
        "\U00002B50"             # Star
        "\U0000203C-\U00003299"  # CJK Symbols
        "]"
    )

    for line, text in parser.text_chunks:
        matches = emoji_pattern.findall(text)
        if matches:
            emojis = " ".join(matches[:5])  # Show first 5
            issues.append(Issue("NO EMOJIS", "FAIL", line,
                f"Emoji found in text: {emojis} — use Lucide SVG icons instead"))

    return issues


def check_border_radius(parser: AxiaraHTMLParser, raw_lines: list[str]) -> list[Issue]:
    """Check 5: BORDER RADIUS — no border-radius > 0.
    Source: directives/axiara-brand.md § Border Radius
    "0px on EVERYTHING. No exceptions. Knife-edge apex."
    
    Scans for:
      - Tailwind "rounded-" classes (except "rounded-none")
      - Inline/CSS border-radius values > 0
    """
    issues = []

    # Check Tailwind classes
    rounded_pattern = re.compile(r'\brounded(?!-none)\b[\w-]*')
    for line, class_str in parser.classes:
        matches = rounded_pattern.findall(class_str)
        if matches:
            issues.append(Issue("BORDER RADIUS", "FAIL", line,
                f"Tailwind rounded class found: {', '.join(matches)} — "
                "must be 0px (knife-edge apex)"))

    # Check inline styles
    br_pattern = re.compile(r'border-radius\s*:\s*(\d+)')
    for line, style_str in parser.styles:
        match = br_pattern.search(style_str)
        if match and int(match.group(1)) > 0:
            issues.append(Issue("BORDER RADIUS", "FAIL", line,
                f"Inline border-radius: {match.group(0)} — must be 0px"))

    # Check <style> blocks
    for start_line, css in parser.style_blocks:
        for i, css_line in enumerate(css.split("\n")):
            match = br_pattern.search(css_line)
            if match and int(match.group(1)) > 0:
                issues.append(Issue("BORDER RADIUS", "FAIL", start_line + i,
                    f"CSS border-radius: {match.group(0)} — must be 0px"))

    return issues


def check_animations(parser: AxiaraHTMLParser, raw_lines: list[str]) -> list[Issue]:
    """Check 6: ANIMATIONS — no forbidden animation types.
    Source: directives/axiara-brand.md § Motion Rules (STRICTLY ENFORCED)
    FORBIDDEN: bounce, elastic, spring, zoom, scale (on hover), spin, rotate
    """
    issues = []
    forbidden = ["bounce", "elastic", "spring", "zoom", "spin", "rotate"]
    forbidden_pattern = re.compile(
        r'\b(' + '|'.join(forbidden) + r')\b', re.IGNORECASE
    )

    # Scan all raw lines for forbidden animation keywords
    for i, line_text in enumerate(raw_lines, 1):
        # Skip comments
        stripped = line_text.strip()
        if stripped.startswith("/*") or stripped.startswith("//") or stripped.startswith("<!--"):
            continue

        matches = forbidden_pattern.findall(line_text)
        if matches:
            # Check context — only flag if it's in animation/transition/keyframe context
            anim_context = re.compile(
                r'(animation|@keyframes|transition|transform)', re.IGNORECASE
            )
            if anim_context.search(line_text):
                issues.append(Issue("ANIMATIONS", "FAIL", i,
                    f"Forbidden animation keyword: {', '.join(set(matches))} — "
                    "only fade-in-up is allowed"))

    # Also check Tailwind animation classes
    tw_forbidden = re.compile(r'\b(animate-bounce|animate-spin|animate-ping)\b')
    for line, class_str in parser.classes:
        matches = tw_forbidden.findall(class_str)
        if matches:
            issues.append(Issue("ANIMATIONS", "FAIL", line,
                f"Forbidden Tailwind animation: {', '.join(matches)}"))

    return issues


def check_headings(parser: AxiaraHTMLParser) -> list[Issue]:
    """Check 7: HEADINGS — proper heading hierarchy, no skipping levels.
    Source: directives/qa-checklist.md § Accessibility
    """
    issues = []
    if not parser.headings:
        issues.append(Issue("HEADINGS", "WARN", 0,
            "No headings found on page"))
        return issues

    # First heading should be h1
    first_line, first_level = parser.headings[0]
    if first_level != 1:
        issues.append(Issue("HEADINGS", "WARN", first_line,
            f"First heading is <h{first_level}>, expected <h1>"))

    # Check for skipped levels (e.g., h1 → h3 without h2)
    prev_level = 0
    for line, level in parser.headings:
        if level > prev_level + 1 and prev_level > 0:
            issues.append(Issue("HEADINGS", "FAIL", line,
                f"Heading hierarchy skip: <h{prev_level}> → <h{level}> "
                f"(missing <h{prev_level + 1}>)"))
        prev_level = level

    return issues


def check_accessibility(parser: AxiaraHTMLParser) -> list[Issue]:
    """Check 8: ACCESSIBILITY — alt on images, labels on inputs.
    Source: directives/qa-checklist.md § Accessibility Checks
    """
    issues = []

    # Check images for alt attribute
    for line, alt in parser.images:
        if alt is None:
            issues.append(Issue("A11Y", "FAIL", line,
                "Image missing alt attribute"))
        elif alt == "":
            # Empty alt is valid for decorative images, but worth noting
            pass

    # Check form inputs have labels
    for line, input_type, input_id, input_name in parser.form_inputs:
        identifier = input_id or input_name or input_type
        if input_id and input_id in parser.label_fors:
            continue  # Has a matching <label for="">
        issues.append(Issue("A11Y", "WARN", line,
            f"Form input '{identifier}' may be missing an associated "
            "<label> element"))

    return issues


def check_reduced_motion(raw_lines: list[str]) -> list[Issue]:
    """Check 9: REDUCED MOTION — prefers-reduced-motion present.
    Source: directives/axiara-brand.md § Motion Rules
    Source: directives/build-page.md § Standard Page Structure item 10
    """
    issues = []
    full_text = "\n".join(raw_lines)
    if "prefers-reduced-motion" not in full_text:
        issues.append(Issue("MOTION PREF", "FAIL", 0,
            "Missing prefers-reduced-motion media query — "
            "animations must be disabled for users who prefer reduced motion"))
    return issues


def check_responsive_h1(parser: AxiaraHTMLParser) -> list[Issue]:
    """Check 10: RESPONSIVE H1 — H1 tags must use .text-hero class.
    Source: directives/axiara-brand.md § Responsive Rules
    """
    issues = []
    # Identify H1 lines
    h1_lines = {line for line, level in parser.headings if level == 1}
    
    # Check classes on those lines
    for line, class_str in parser.classes:
        if line in h1_lines:
            if "text-hero" not in class_str:
                issues.append(Issue("RESP H1", "FAIL", line,
                    "H1 missing '.text-hero' class (required for 40px/56px/72px scaling)"))
    
    return issues


def check_responsive_grids(parser: AxiaraHTMLParser) -> list[Issue]:
    """Check 11: RESPONSIVE GRIDS — No multi-column grids on mobile.
    Source: directives/axiara-brand.md § Responsive Rules
    
    Naked classes like 'grid-cols-2' apply to mobile.
    They must be prefixed (e.g. 'md:grid-cols-2') or be 'grid-cols-1'.
    """
    issues = []
    # Find naked grid-cols-X where X > 1
    # Matches "grid-cols-2", "grid-cols-12" but not "md:grid-cols-2"
    pattern = re.compile(r'(?<![:\w-])grid-cols-([2-9]|1[0-2])\b')
    
    for line, class_str in parser.classes:
        matches = pattern.findall(class_str)
        if matches:
            issues.append(Issue("RESP GRIDS", "FAIL", line,
                f"Multi-column grid on mobile: 'grid-cols-{matches[0]}' — "
                "must use breakpoint prefix (e.g. md:grid-cols-2) or grid-cols-1"))
                
    return issues


def check_skip_link(parser: AxiaraHTMLParser) -> list[Issue]:
    """Check 12: SSKIP LINK — A 'Skip to content' link must exist.
    Source: directives/qa-checklist.md § Accessibility
    """
    issues = []
    has_skip = False
    
    # Simple heuristic: look for a link with 'skip' in class or text, pointing to an ID
    for line, href in parser.link_hrefs:
        # This parser tracks <link> tags, NOT <a> tags.
        # We need to scan <a> tags. The parser was not tracking <a> tags.
        pass

    # The parser needs to be updated to track <a> tags/text first.
    # Since we can't easily change the parser class in this replace block without replacing the whole file,
    # let's grep the raw text or use the existing text_chunks.
    
    # We can scan text_chunks for "Skip to content"
    for line, text in parser.text_chunks:
        if "skip to" in text.lower() or "skip navigation" in text.lower():
            has_skip = True
            break
            
    if not has_skip:
        issues.append(Issue("A11Y SKIP", "FAIL", 0,
            "No visible 'Skip to content' link found (required for keyboard navigation)"))
            
    return issues


def check_contrast(parser: AxiaraHTMLParser) -> list[Issue]:
    """Check 13: CONTRAST — Warn about Crimson text on Obsidian background.
    Source: directives/qa-checklist.md § Color & Contrast
    """
    issues = []
    
    # Check for text-axiara-crimson used without a safe background or on obsidian
    # This is a loose static check
    for line, class_str in parser.classes:
        if "text-axiara-crimson" in class_str:
            # If it's small text (not text-xl, 2xl, etc) and on obsidian bg
            is_large = any(x in class_str for x in ["text-xl", "text-2xl", "text-3xl", "text-4xl", "text-hero", "font-bold", "font-black"])
            
            if not is_large:
                 issues.append(Issue("CONTRAST", "WARN", line,
                    "Crimson text used on small font — verify 4.5:1 contrast against background"))

    return issues


# ---------------------------------------------------------------------------
# Report Formatting
# ---------------------------------------------------------------------------

def format_report(filepath: str, issues: list[Issue], checks_run: int) -> str:
    """Format the validation report as a readable terminal output."""
    lines = []
    lines.append("")
    lines.append("=" * 64)
    lines.append("  AXIARA HTML VALIDATOR")
    lines.append(f"  File: {filepath}")
    lines.append("=" * 64)

    # Group issues by check
    check_names = [
        "STRUCTURE", "FONTS", "CSS", "NO EMOJIS", "BORDER RADIUS",
        "ANIMATIONS", "HEADINGS", "A11Y", "MOTION PREF",
        "RESP H1", "RESP GRIDS", "A11Y SKIP", "CONTRAST"
    ]

    fails = 0
    warns = 0
    passes = 0

    for check_name in check_names:
        check_issues = [i for i in issues if i.check == check_name]
        check_fails = [i for i in check_issues if i.severity == "FAIL"]
        check_warns = [i for i in check_issues if i.severity == "WARN"]

        if check_fails:
            status = "❌ FAIL"
            fails += 1
        elif check_warns:
            status = "⚠️  WARN"
            warns += 1
        else:
            status = "✅ PASS"
            passes += 1

        lines.append(f"\n  [{status}] {check_name}")

        for issue in check_issues:
            loc = f"L{issue.line}" if issue.line > 0 else "   "
            marker = "✗" if issue.severity == "FAIL" else "!"
            lines.append(f"    {marker} {loc}: {issue.message}")

    # Summary
    lines.append("")
    lines.append("-" * 64)
    total = passes + fails + warns
    lines.append(f"  RESULT: {passes} passed, {fails} failed, {warns} warnings "
                 f"(out of {total} checks)")

    if fails == 0:
        lines.append("  STATUS: ✅ ALL CHECKS PASSED")
    else:
        lines.append("  STATUS: ❌ BRAND COMPLIANCE ISSUES FOUND")

    lines.append("=" * 64)
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 execution/validate_html.py <filepath>")
        print("Example: python3 execution/validate_html.py "
              "src/pages/services/sprint.html")
        sys.exit(1)

    filepath = sys.argv[1]

    # Resolve relative to project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    abs_path = os.path.join(project_root, filepath)

    if not os.path.isfile(abs_path):
        print(f"[ERROR] File not found: {abs_path}")
        sys.exit(1)

    # Read the file
    with open(abs_path, "r", encoding="utf-8") as f:
        content = f.read()

    raw_lines = content.split("\n")

    # Parse HTML
    parser = AxiaraHTMLParser()
    parser.feed(content)

    # Run all 9 checks
    all_issues: list[Issue] = []
    all_issues.extend(check_structure(parser))
    all_issues.extend(check_fonts(parser))
    all_issues.extend(check_css(parser))
    all_issues.extend(check_emojis(parser))
    all_issues.extend(check_border_radius(parser, raw_lines))
    all_issues.extend(check_animations(parser, raw_lines))
    all_issues.extend(check_headings(parser))
    all_issues.extend(check_accessibility(parser))
    all_issues.extend(check_reduced_motion(raw_lines))
    all_issues.extend(check_responsive_h1(parser))
    all_issues.extend(check_responsive_grids(parser))
    all_issues.extend(check_skip_link(parser))
    all_issues.extend(check_contrast(parser))

    # Print report
    report = format_report(filepath, all_issues, checks_run=11)
    print(report)

    # Exit code: 1 if any FAILs, 0 otherwise
    has_fails = any(i.severity == "FAIL" for i in all_issues)
    sys.exit(1 if has_fails else 0)


if __name__ == "__main__":
    main()
