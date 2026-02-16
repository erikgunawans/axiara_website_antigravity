#!/usr/bin/env python3
"""
generate_page_shell.py — Axiara Page Shell Generator (Layer 3 Execution)

Generates a standard HTML page shell for the Axiara.id site with all
required brand elements pre-wired.

Usage:
  python3 execution/generate_page_shell.py \\
    --title "NTRJ Episteme — Axiara" \\
    --slug "episteme" \\
    --output "src/pages/technology/episteme.html" \\
    --desc "Episteme: Axiara's knowledge governance engine."

Arguments:
  --title   Page <title> tag text (required)
  --slug    URL slug / page identifier (required)
  --output  Output filepath relative to project root (required)
  --desc    Meta description text (optional, defaults to title)

Source of truth:
  - directives/build-page.md (Standard Page Structure)
  - directives/axiara-brand.md (Visual rules)
  - docs/agency_9_creative.md (CSS kit)

No external dependencies beyond Python standard library.
"""

import argparse
import os
import sys


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Google Fonts URL — exact weights from directives/axiara-brand.md
GOOGLE_FONTS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=JetBrains+Mono:wght@300;400&"
    "family=Outfit:wght@300;400;700;900&"
    "family=Playfair+Display:ital,wght@0,400;0,600;1,400&"
    "display=swap"
)

# Tailwind CSS CDN (latest v3 via Play CDN for development)
TAILWIND_CDN = "https://cdn.tailwindcss.com"

# Lucide Icons CDN
LUCIDE_CDN = "https://unpkg.com/lucide@latest"

# Component file paths (relative to project root)
NAVBAR_PATH = "src/components/navbar.html"
FOOTER_PATH = "src/components/footer.html"

# CSS path (relative from the HTML page — will be computed dynamically)
CSS_FILE = "src/css/axiara.css"


# ---------------------------------------------------------------------------
# Default Inline Components
# Used when src/components/navbar.html or footer.html don't exist yet.
# ---------------------------------------------------------------------------

DEFAULT_NAVBAR = """\
    <!-- Navbar — replace with src/components/navbar.html when ready -->
    <nav class="fixed top-4 left-4 right-4 z-50 flex items-center justify-between px-8 py-4"
         style="background: rgba(13, 13, 13, 0.85); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);">
        
        <!-- Logo -->
        <a href="/" class="flex items-center gap-3 no-underline">
            <span style="font-family: var(--font-eng); font-weight: 900; font-size: 1.25rem;
                         color: var(--axiara-white); text-transform: uppercase; letter-spacing: 0.1em;">
                AXIARA
            </span>
        </a>

        <!-- Nav Links -->
        <div class="hidden md:flex items-center gap-8">
            <a href="/src/pages/services/e2e-transformation.html"
               style="font-family: var(--font-code); font-size: 0.75rem; color: var(--axiara-silver);
                      text-transform: uppercase; letter-spacing: 2px; text-decoration: none;
                      transition: color 0.3s ease;">
                Services
            </a>
            <a href="/src/pages/technology/aksara-vector-core.html"
               style="font-family: var(--font-code); font-size: 0.75rem; color: var(--axiara-silver);
                      text-transform: uppercase; letter-spacing: 2px; text-decoration: none;
                      transition: color 0.3s ease;">
                Technology
            </a>
            <a href="/src/pages/industries/telco.html"
               style="font-family: var(--font-code); font-size: 0.75rem; color: var(--axiara-silver);
                      text-transform: uppercase; letter-spacing: 2px; text-decoration: none;
                      transition: color 0.3s ease;">
                Industries
            </a>
            <a href="/src/pages/compliance/iso-42001.html"
               style="font-family: var(--font-code); font-size: 0.75rem; color: var(--axiara-silver);
                      text-transform: uppercase; letter-spacing: 2px; text-decoration: none;
                      transition: color 0.3s ease;">
                Compliance
            </a>
            <a href="#contact" class="btn"
               style="font-size: 0.75rem; padding: 10px 24px;">
                Contact
            </a>
        </div>
    </nav>"""

DEFAULT_FOOTER = """\
    <!-- Footer — replace with src/components/footer.html when ready -->
    <footer class="w-full py-16 px-8" style="border-top: 1px solid rgba(255,255,255,0.05);">
        <div class="max-w-7xl mx-auto">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-12 mb-12">

                <!-- Brand -->
                <div>
                    <span style="font-family: var(--font-eng); font-weight: 900; font-size: 1.25rem;
                                 color: var(--axiara-white); text-transform: uppercase; letter-spacing: 0.1em;">
                        AXIARA
                    </span>
                    <p class="mt-4" style="font-size: 14px; line-height: 1.8;">
                        Sovereign AI Governance.<br>
                        End-to-End Transformation.
                    </p>
                </div>

                <!-- Navigation -->
                <div>
                    <h3 style="font-family: var(--font-code); font-size: 0.7rem; color: var(--axiara-crimson);
                               text-transform: uppercase; letter-spacing: 3px; margin-bottom: 1.5rem;">
                        Navigation
                    </h3>
                    <ul class="space-y-3 list-none p-0">
                        <li><a href="/" style="font-family: var(--font-eng); font-size: 14px;
                               color: var(--axiara-silver); text-decoration: none;">Home</a></li>
                        <li><a href="/about" style="font-family: var(--font-eng); font-size: 14px;
                               color: var(--axiara-silver); text-decoration: none;">About</a></li>
                        <li><a href="#contact" style="font-family: var(--font-eng); font-size: 14px;
                               color: var(--axiara-silver); text-decoration: none;">Contact</a></li>
                    </ul>
                </div>

                <!-- Legal -->
                <div>
                    <h3 style="font-family: var(--font-code); font-size: 0.7rem; color: var(--axiara-crimson);
                               text-transform: uppercase; letter-spacing: 3px; margin-bottom: 1.5rem;">
                        Legal
                    </h3>
                    <p style="font-size: 14px; color: var(--axiara-silver);">
                        PT Axiara Teknologi Indonesia
                    </p>
                </div>
            </div>

            <!-- Bottom Bar -->
            <div class="pt-8" style="border-top: 1px solid rgba(255,255,255,0.05);">
                <p style="font-family: var(--font-code); font-size: 0.7rem; color: rgba(168,168,168,0.5);
                          text-transform: uppercase; letter-spacing: 2px; text-align: center;">
                    &copy; 2026 Axiara. All rights reserved.
                </p>
            </div>
        </div>
    </footer>"""


# ---------------------------------------------------------------------------
# Template
# ---------------------------------------------------------------------------

PAGE_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{meta_desc}">
    <title>{title}</title>

    <!-- A. Google Fonts — Outfit, Playfair Display, JetBrains Mono -->
    <!-- Source: directives/axiara-brand.md § Typography -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="{google_fonts_url}" rel="stylesheet">

    <!-- Tailwind CSS (Play CDN for development) -->
    <script src="{tailwind_cdn}"></script>

    <!-- Axiara "Darkroom" CSS Kit -->
    <!-- Generated by: execution/generate_css.py -->
    <link rel="stylesheet" href="{css_path}">
</head>
<body>
    <!-- Skip-to-content link (Accessibility) -->
    <!-- Source: directives/qa-checklist.md § Accessibility -->
    <a href="#content" class="skip-to-content">Skip to content</a>

    <!-- Weave Lines (Crimson diagonal watermarks) -->
    <!-- Source: agency_9_creative.md § 3.E -->
    <div class="weave-lines" aria-hidden="true"></div>

    <!-- ============================================================
         NAVBAR
         ============================================================ -->
{navbar}

    <!-- ============================================================
         MAIN CONTENT
         Page: {slug}
         ============================================================ -->
    <main id="content" class="relative z-10 pt-24">

        <!-- Hero Section -->
        <section class="min-h-screen flex items-center justify-center px-8">
            <div class="max-w-5xl mx-auto text-center">
                <h1 class="fade-in-up text-5xl md:text-7xl mb-6">
                    {title_h1}
                </h1>
                <h2 class="fade-in-up delay-1 text-xl md:text-2xl mb-10">
                    <!-- Subheadline — source from Manual -->
                </h2>
                <a href="#learn-more" class="btn fade-in-up delay-2">
                    Explore
                </a>
            </div>
        </section>

        <!-- Content Sections -->
        <!-- Add sections here. Each should use:
             - .fade-in-up class for scroll animation
             - .glass-card for content cards
             - .btn for all buttons
             Pull content from the Manual section mapped in
             directives/content-source.md -->

        <section id="learn-more" class="py-24 px-8">
            <div class="max-w-7xl mx-auto">
                <!-- Section content goes here -->
            </div>
        </section>

    </main>

    <!-- ============================================================
         FOOTER
         ============================================================ -->
{footer}

    <!-- ============================================================
         SCRIPTS
         ============================================================ -->

    <!-- Lucide Icons -->
    <!-- Source: directives/axiara-brand.md § Icons -->
    <script src="{lucide_cdn}"></script>
    <script>lucide.createIcons();</script>

    <!-- Scroll-triggered Fade-In-Up Animation (IntersectionObserver) -->
    <!-- Source: directives/axiara-brand.md § Motion Rules -->
    <!-- ALLOWED: Fade In Up only (0.8-1.2s, ease-out) -->
    <!-- FORBIDDEN: Bounce, elastic, spring, zoom, scale, spin, rotate -->
    <script>
        (function() {{
            'use strict';

            // Respect prefers-reduced-motion
            var prefersReducedMotion = window.matchMedia(
                '(prefers-reduced-motion: reduce)'
            ).matches;

            if (prefersReducedMotion) {{
                // Make all fade-in-up elements immediately visible
                document.querySelectorAll('.fade-in-up').forEach(function(el) {{
                    el.classList.add('visible');
                }});
                return;
            }}

            // IntersectionObserver for scroll-triggered animations
            var observer = new IntersectionObserver(function(entries) {{
                entries.forEach(function(entry) {{
                    if (entry.isIntersecting) {{
                        entry.target.classList.add('visible');
                        observer.unobserve(entry.target);
                    }}
                }});
            }}, {{
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            }});

            // Observe all .fade-in-up elements
            document.querySelectorAll('.fade-in-up').forEach(function(el) {{
                observer.observe(el);
            }});
        }})();
    </script>

</body>
</html>
"""


# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------

def resolve_project_root() -> str:
    """Resolve the project root (one level up from execution/)."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(script_dir)


def compute_relative_css_path(output_path: str, project_root: str) -> str:
    """Compute the relative path from the output HTML file to axiara.css.
    
    Example:
      output: src/pages/technology/episteme.html
      css:    src/css/axiara.css
      result: ../../css/axiara.css
    """
    output_abs = os.path.join(project_root, output_path)
    css_abs = os.path.join(project_root, CSS_FILE)
    output_dir = os.path.dirname(output_abs)
    return os.path.relpath(css_abs, output_dir)


def load_component(filepath: str, project_root: str, default: str) -> str:
    """Load an HTML component file, or return the default inline version.
    
    Args:
        filepath: Relative path to the component file
        project_root: Absolute path to the project root
        default: Default inline HTML to use if file doesn't exist
    
    Returns:
        The component HTML string
    """
    abs_path = os.path.join(project_root, filepath)
    if os.path.isfile(abs_path):
        with open(abs_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
        if content:
            # Indent to match template nesting
            return content
        print(f"  [WARN] {filepath} exists but is empty, using default")
    else:
        print(f"  [INFO] {filepath} not found, using inline default")
    return default


def slug_to_h1(slug: str) -> str:
    """Convert a URL slug to a display-friendly H1 text.
    
    Examples:
      "episteme" -> "EPISTEME"
      "aksara-vector-core" -> "AKSARA VECTOR CORE"
      "e2e-transformation" -> "E2E TRANSFORMATION"
    
    Note: H1 is uppercase per brand directive (Outfit 900 uppercase).
    """
    return slug.replace("-", " ").upper()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate an Axiara page shell (Layer 3 Execution).",
        epilog="Example: python3 execution/generate_page_shell.py "
               '--title "NTRJ Episteme — Axiara" '
               '--slug "episteme" '
               '--output "src/pages/technology/episteme.html"'
    )
    parser.add_argument(
        "--title", required=True,
        help='Page <title> text, e.g. "NTRJ Episteme — Axiara"'
    )
    parser.add_argument(
        "--slug", required=True,
        help='URL slug / page identifier, e.g. "episteme"'
    )
    parser.add_argument(
        "--output", required=True,
        help='Output filepath relative to project root, '
             'e.g. "src/pages/technology/episteme.html"'
    )
    parser.add_argument(
        "--desc", default=None,
        help="Meta description text (optional, defaults to title)"
    )

    args = parser.parse_args()
    project_root = resolve_project_root()

    # Resolve values
    meta_desc = args.desc if args.desc else args.title
    css_path = compute_relative_css_path(args.output, project_root)
    title_h1 = slug_to_h1(args.slug)

    # Load or use default components
    print(f"Generating page shell: {args.output}")
    navbar = load_component(NAVBAR_PATH, project_root, DEFAULT_NAVBAR)
    footer = load_component(FOOTER_PATH, project_root, DEFAULT_FOOTER)

    # Render template
    html = PAGE_TEMPLATE.format(
        title=args.title,
        meta_desc=meta_desc,
        google_fonts_url=GOOGLE_FONTS_URL,
        tailwind_cdn=TAILWIND_CDN,
        css_path=css_path,
        slug=args.slug,
        title_h1=title_h1,
        navbar=navbar,
        footer=footer,
        lucide_cdn=LUCIDE_CDN,
    )

    # Write output
    output_abs = os.path.join(project_root, args.output)
    os.makedirs(os.path.dirname(output_abs), exist_ok=True)

    with open(output_abs, "w", encoding="utf-8") as f:
        f.write(html)

    file_size = os.path.getsize(output_abs)
    print(f"[OK] Generated: {output_abs}")
    print(f"     Size: {file_size:,} bytes")
    print(f"     Title: {args.title}")
    print(f"     H1: {title_h1}")
    print(f"     CSS path: {css_path}")
    print(f"     Slug: {args.slug}")


if __name__ == "__main__":
    main()
