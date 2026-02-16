#!/usr/bin/env python3
"""
generate_css.py — Axiara "Darkroom" CSS Kit Generator (Layer 3 Execution)

Generates the complete Axiara CSS file at src/css/axiara.css.
Deterministic: same input → same output, every time.
No external dependencies beyond Python standard library.

Source of truth:
  - docs/agency_9_creative.md (Sections A–E)
  - directives/axiara-brand.md (Non-negotiable brand rules)

Usage:
  python3 execution/generate_css.py

Output:
  src/css/axiara.css
"""

import os
import sys
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Configuration — Design Tokens from directives/axiara-brand.md
# ---------------------------------------------------------------------------

TOKENS = {
    "obsidian":   "#0D0D0D",
    "crimson":    "#C41E3A",
    "white":      "#FFFFFF",
    "silver":     "#A8A8A8",
    "charcoal":   "#1A1A2E",
}

FONTS = {
    "eng":  "'Outfit', sans-serif",           # Structure
    "phil": "'Playfair Display', serif",       # Philosophy / Creativity
    "code": "'JetBrains Mono', monospace",     # Tech Truth
}

# Google Fonts import URL (exact weights from brand directive)
GOOGLE_FONTS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=JetBrains+Mono:wght@300;400&"
    "family=Outfit:wght@300;400;700;900&"
    "family=Playfair+Display:ital,wght@0,400;0,600;1,400&"
    "display=swap"
)

# ---------------------------------------------------------------------------
# CSS Blocks — mirrored from docs/agency_9_creative.md Sections A–E
# ---------------------------------------------------------------------------


def block_a_fonts() -> str:
    """Section A: Google Fonts @import.
    Source: agency_9_creative.md § 3.A "Import Fonts"
    """
    return f"""\
/* ============================================================
   A. GOOGLE FONTS IMPORT
   Source: agency_9_creative.md § 3.A
   Fonts: Outfit (structure), Playfair Display (editorial),
          JetBrains Mono (technical)
   ============================================================ */
@import url('{GOOGLE_FONTS_URL}');
"""


def block_b_variables() -> str:
    """Section B: :root CSS custom properties (Darkroom Variables).
    Source: agency_9_creative.md § 3.B "The Darkroom Variables"
    """
    return f"""\
/* ============================================================
   B. THE "DARKROOM" VARIABLES
   Source: agency_9_creative.md § 3.B
   Non-negotiable palette from directives/axiara-brand.md
   ============================================================ */
:root {{
    /* --- AXIARA CREATIVE PALETTE --- */
    --axiara-obsidian: {TOKENS["obsidian"]};
    --axiara-crimson: {TOKENS["crimson"]};
    --axiara-white: {TOKENS["white"]};
    --axiara-silver: {TOKENS["silver"]};
    --axiara-charcoal: {TOKENS["charcoal"]};

    /* --- TEXTURES --- */
    /* Subtle gradient representing the "Episteme" layer */
    --axiara-gradient: linear-gradient(135deg, {TOKENS["obsidian"]} 0%, {TOKENS["charcoal"]} 100%);

    /* --- GLASS --- */
    --axiara-glass: rgba(26, 26, 46, 0.4);
    --axiara-glass-hover: rgba(26, 26, 46, 0.8);
    --axiara-crimson-glow: rgba(196, 30, 58, 0.05);

    /* --- TYPOGRAPHY --- */
    --font-eng: {FONTS["eng"]};         /* Structure */
    --font-phil: {FONTS["phil"]};       /* Philosophy/Creativity */
    --font-code: {FONTS["code"]};      /* Tech Truth */
}}
"""


def block_c_typography() -> str:
    """Section C: Creative Typography (The "Editorial" Look).
    Source: agency_9_creative.md § 3.C
    Brand rules: directives/axiara-brand.md § Typography (Non-Negotiable)
    """
    return """\
/* ============================================================
   C. CREATIVE TYPOGRAPHY — "THE EDITORIAL LOOK"
   Source: agency_9_creative.md § 3.C
   Brand: directives/axiara-brand.md § Typography
   
   Pairing Outfit (Engineering) with Playfair Display (Philosophy)
   to create a sophisticated, "authored" voice.
   ============================================================ */

/* --- SHARED HEADLINE RULES --- */
h1, h2, h3 {
    color: var(--axiara-white);
    line-height: 1.1;
}

/* H1: The Monolith (Huge, Bold, Structural)
   Font: Outfit 900, uppercase, expanded tracking */
h1 {
    font-family: var(--font-eng);
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* --- HERO H1 SCALING ---
   Mobile: 40px
   Tablet (md, 768px): 56px
   Desktop (lg, 1024px): 72px */
.text-hero {
    font-family: var(--font-eng);
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    line-height: 1.1;
    font-size: 40px; 
}
@media (min-width: 768px) {
    .text-hero {
        font-size: 56px;
    }
}
@media (min-width: 1024px) {
    .text-hero {
        font-size: 72px;
    }
}

/* H2: The Philosopher (Serif, Italic, Emotional)
   Font: Playfair Display 400, italic — the key "Creative Agency" shift */
h2 {
    font-family: var(--font-phil);
    font-weight: 400;
    font-style: italic;
    color: var(--axiara-silver);
}

/* H3: Section Titles
   Font: Outfit 700, white */
h3 {
    font-family: var(--font-eng);
    font-weight: 700;
    color: var(--axiara-white);
}

/* Body Text: High Readability
   Font: Outfit 300, 18px "book" size */
p, body {
    font-family: var(--font-eng);
    font-weight: 300;
    color: var(--axiara-silver);
    font-size: 18px;
}

/* Code / Labels / Badges
   Font: JetBrains Mono 300-400 */
code, .label, .badge {
    font-family: var(--font-code);
    font-weight: 400;
    color: var(--axiara-silver);
}
"""


def block_d_ui_elements() -> str:
    """Section D: UI Elements — "Glass & Wireframe".
    Source: agency_9_creative.md § 3.D
    Brand rules: directives/axiara-brand.md § UI Components
    
    Ghost buttons + frosted glass cards reflecting "Transparent Logic".
    """
    return """\
/* ============================================================
   D. UI ELEMENTS — "GLASS & WIREFRAME"
   Source: agency_9_creative.md § 3.D
   Brand: directives/axiara-brand.md § UI Components
   
   Wireframes and transparency reflecting "Transparent Logic".
   ============================================================ */

/* --- GHOST BUTTONS (The ONLY button style) ---
   Wireframe "Architectural Lines" replacing solid buttons.
   Brand: border-radius 0px ALWAYS ("Knife-edge apex")
   Brand: ALWAYS cursor-pointer on clickable elements */
.button, .btn, button, [role="button"] {
    background: transparent;
    border: 1px solid var(--axiara-white);
    color: var(--axiara-white);
    font-family: var(--font-code);
    border-radius: 0px;  /* Knife-edge apex — NO exceptions */
    text-transform: uppercase;
    letter-spacing: 2px;
    padding: 14px 32px;
    transition: all 0.4s ease;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
}

.button:hover, .btn:hover, button:hover, [role="button"]:hover {
    border-color: var(--axiara-crimson);
    color: var(--axiara-crimson);
    background: var(--axiara-crimson-glow);  /* Faint crimson glow */
}

/* --- FROSTED GLASS CARDS (The ONLY card style) ---
   The "Episteme" layer — floating content with frosted glass.
   Brand: border-LEFT only (crimson), NO top/right/bottom borders */
.glass-card, .column_icon_box, .feature_box {
    background: var(--axiara-glass);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-left: 1px solid var(--axiara-crimson);
    border-top: none;
    border-right: none;
    border-bottom: none;
    border-radius: 0px;  /* Knife-edge apex */
    padding: 40px;
    transition: all 0.4s ease;
}

/* Fallback for browsers without backdrop-filter support */
@supports not (backdrop-filter: blur(12px)) {
    .glass-card, .column_icon_box, .feature_box {
        background: var(--axiara-charcoal);
    }
}

/* Card hover: deeper glass + thicker crimson border */
.glass-card:hover, .column_icon_box:hover, .feature_box:hover {
    background: var(--axiara-glass-hover);
    border-left-width: 4px;
}
"""


def block_e_layout() -> str:
    """Section E: The "Asymmetric Weave" Layout.
    Source: agency_9_creative.md § 3.E
    Brand rules: directives/axiara-brand.md § Asymmetric Image Treatment
    
    Off-grid images + body background texture.
    """
    return """\
/* ============================================================
   E. THE "ASYMMETRIC WEAVE" LAYOUT
   Source: agency_9_creative.md § 3.E
   Brand: directives/axiara-brand.md § Asymmetric Image Treatment
   
   Off-grid image offsets + background texture.
   ============================================================ */

/* --- OFFSET IMAGES ---
   Pushes images slightly off-grid for the "Weave" effect.
   Remove offset on mobile (< 768px) per brand directive. */
.image_wrapper, .img-offset {
    transform: translate(20px, 20px);
    border: 1px solid rgba(255, 255, 255, 0.1);  /* Wireframe box behind image */
    z-index: 1;
}

@media (max-width: 767px) {
    .image_wrapper, .img-offset {
        transform: none;
    }
}

/* --- BODY BACKGROUND ---
   Obsidian base with the cinematic gradient.
   Background-attachment: fixed for subtle parallax. */
body {
    background: var(--axiara-gradient);
    background-attachment: fixed;
    margin: 0;
    padding: 0;
    overflow-x: hidden; /* Prevent horizontal scroll */
}

/* --- WEAVE LINES (Crimson Diagonal Accents) ---
   Large background watermarks using the "Three Diagonal Lines" motif. */
.weave-lines {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

.weave-lines::before,
.weave-lines::after {
    content: '';
    position: absolute;
    width: 1px;
    height: 200%;
    background: linear-gradient(
        to bottom,
        transparent 0%,
        rgba(196, 30, 58, 0.08) 30%,
        rgba(196, 30, 58, 0.08) 70%,
        transparent 100%
    );
    transform: rotate(-35deg);
    transform-origin: top center;
}

.weave-lines::before {
    left: 25%;
    top: -50%;
}

.weave-lines::after {
    left: 65%;
    top: -50%;
}
"""


def block_animations() -> str:
    """Scroll-triggered animations and motion rules.
    Source: directives/axiara-brand.md § Motion Rules (STRICTLY ENFORCED)
    
    ALLOWED: Fade In Up only (0.8–1.2s, ease-out)
    FORBIDDEN: Bounce, elastic, spring, zoom, scale, spin, rotate
    """
    return """\
/* ============================================================
   F. MOTION — FADE IN UP (The ONLY allowed animation)
   Source: directives/axiara-brand.md § Motion Rules
   
   ALLOWED: Fade In Up (translateY 20-30px → 0, opacity 0 → 1)
   FORBIDDEN: Bounce, elastic, spring, zoom, scale, spin, rotate
   ============================================================ */

/* --- SCROLL-TRIGGERED ANIMATION --- */
.fade-in-up {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}

.fade-in-up.visible {
    opacity: 1;
    transform: translateY(0);
}

/* Staggered delays for sibling elements (0.1-0.2s between) */
.fade-in-up.delay-1 { transition-delay: 0.1s; }
.fade-in-up.delay-2 { transition-delay: 0.2s; }
.fade-in-up.delay-3 { transition-delay: 0.3s; }
.fade-in-up.delay-4 { transition-delay: 0.4s; }
.fade-in-up.delay-5 { transition-delay: 0.5s; }

/* --- RESPECT prefers-reduced-motion ---
   Brand directive: prefers-reduced-motion disables ALL animations */
@media (prefers-reduced-motion: reduce) {
    .fade-in-up {
        opacity: 1;
        transform: none;
        transition: none;
    }
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
}
"""


def block_utilities() -> str:
    """Utility classes for common Axiara patterns.
    Derived from brand directive constraints.
    """
    return """\
/* ============================================================
   G. UTILITIES
   Common patterns derived from directives/axiara-brand.md
   ============================================================ */

/* --- GLOBAL BORDER-RADIUS RESET ---
   Brand: 0px on EVERYTHING. No exceptions. "Knife-edge apex" */
*, *::before, *::after {
    border-radius: 0px;
}

/* Ensure images and inputs also get sharp corners */
img, input, textarea, select, video {
    border-radius: 0px;
}

/* --- SKIP-TO-CONTENT (Accessibility) --- */
.skip-to-content {
    position: absolute;
    left: -9999px;
    top: auto;
    width: 1px;
    height: 1px;
    overflow: hidden;
    z-index: 9999;
    background: var(--axiara-obsidian);
    color: var(--axiara-white);
    padding: 14px 32px;
    font-family: var(--font-code);
    text-transform: uppercase;
    letter-spacing: 2px;
    border: 1px solid var(--axiara-crimson);
}

.skip-to-content:focus {
    position: fixed;
    left: 16px;
    top: 16px;
    width: auto;
    height: auto;
    overflow: visible;
}

/* --- FOCUS STATES (Accessibility) ---
   Brand: crimson outline for keyboard nav */
:focus-visible {
    outline: 2px solid var(--axiara-crimson);
    outline-offset: 2px;
}

/* --- SELECTION COLOR --- */
::selection {
    background: var(--axiara-crimson);
    color: var(--axiara-white);
}

/* --- SCROLLBAR STYLING (Webkit) --- */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: var(--axiara-obsidian);
}

::-webkit-scrollbar-thumb {
    background: rgba(168, 168, 168, 0.3);
    border-radius: 0px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--axiara-crimson);
}
"""


# ---------------------------------------------------------------------------
# Assembly & Output
# ---------------------------------------------------------------------------

def generate_css() -> str:
    """Assemble all CSS blocks in order (A through G).
    Deterministic: same output every time.
    """
    header = f"""\
/* ================================================================
   AXIARA "DARKROOM" CSS KIT
   Generated by: execution/generate_css.py
   
   Source of truth:
     - docs/agency_9_creative.md (Visual concept & CSS blocks A–E)
     - directives/axiara-brand.md (Non-negotiable brand constraints)
   
   DO NOT EDIT THIS FILE MANUALLY.
   Re-run the generator to apply changes:
     python3 execution/generate_css.py
   ================================================================ */

"""
    blocks = [
        block_a_fonts(),
        block_b_variables(),
        block_c_typography(),
        block_d_ui_elements(),
        block_e_layout(),
        block_animations(),
        block_utilities(),
    ]

    return header + "\n".join(blocks)


def main():
    """Write the CSS to src/css/axiara.css."""
    # Resolve project root (execution/ lives one level inside the project)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    output_dir = os.path.join(project_root, "src", "css")
    output_file = os.path.join(output_dir, "axiara.css")

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate and write
    css = generate_css()
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(css)

    # Report
    file_size = os.path.getsize(output_file)
    print(f"[OK] Generated: {output_file}")
    print(f"     Size: {file_size:,} bytes")
    print(f"     Blocks: A (Fonts) → B (Variables) → C (Typography) → "
          f"D (UI Elements) → E (Layout) → F (Motion) → G (Utilities)")


if __name__ == "__main__":
    main()
