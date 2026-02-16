#!/usr/bin/env python3
"""
optimize_images.py — Axiara Image Processor (Layer 3 Execution)

Processes images for the Axiara.id site per brand photography rules:
  1. Converts color photos to grayscale (B&W requirement)
  2. Optionally applies a Crimson (#C41E3A) duotone overlay
  3. Compresses output to WebP format
  4. Generates multiple sizes (375w, 768w, 1440w) for responsive srcset

Usage:
  python3 execution/optimize_images.py \\
    --input src/assets/images/raw/photo.jpg \\
    --output src/assets/images/

  python3 execution/optimize_images.py \\
    --input src/assets/images/raw/photo.jpg \\
    --output src/assets/images/ \\
    --crimson-overlay

  # Batch process all images in a directory:
  python3 execution/optimize_images.py \\
    --input src/assets/images/raw/ \\
    --output src/assets/images/ \\
    --crimson-overlay

Arguments:
  --input           Input image file or directory (required)
  --output          Output directory (required)
  --crimson-overlay Apply Crimson (#C41E3A) duotone overlay (optional)
  --quality         WebP quality 1-100 (default: 80)
  --sizes           Comma-separated widths (default: 375,768,1440)

Source of truth:
  - directives/axiara-brand.md § Photography
    "Black & white only, with optional Crimson color overlay.
     No full-color stock photography. Editorial, documentary aesthetic."

Requires: Pillow (pip install Pillow)
"""

import argparse
import os
import sys

# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------

try:
    from PIL import Image, ImageEnhance, ImageFilter
except ImportError:
    print("[ERROR] Pillow is required but not installed.")
    print("        Install it with: pip install Pillow")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Configuration — from directives/axiara-brand.md
# ---------------------------------------------------------------------------

# Crimson overlay color (brand accent)
CRIMSON = (196, 30, 58)  # #C41E3A

# Default responsive breakpoints matching directives/qa-checklist.md
DEFAULT_SIZES = [375, 768, 1440]

# Default WebP quality (good balance of quality and file size)
DEFAULT_QUALITY = 80

# Supported input formats
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tiff", ".tif", ".bmp", ".webp"}


# ---------------------------------------------------------------------------
# Image Processing Functions
# ---------------------------------------------------------------------------

def to_grayscale(img: Image.Image) -> Image.Image:
    """Convert image to grayscale (B&W).
    
    Brand rule: "Black & white only"
    Source: directives/axiara-brand.md § Photography
    
    Uses luminance conversion (ITU-R 601-2 luma transform) for
    natural-looking B&W results.
    """
    return img.convert("L")


def apply_crimson_overlay(gray_img: Image.Image, opacity: float = 0.25) -> Image.Image:
    """Apply Crimson (#C41E3A) duotone overlay to a grayscale image.
    
    Brand rule: "optional Crimson color overlay"
    Source: directives/axiara-brand.md § Photography
    
    Creates a duotone effect by mapping:
      - Shadows → deep crimson (darker)
      - Highlights → white with crimson tint
    
    Args:
        gray_img: Grayscale PIL Image (mode "L")
        opacity: Overlay intensity 0.0-1.0 (default 0.25 for subtle effect)
    
    Returns:
        RGBA Image with crimson duotone applied
    """
    # Ensure we're working with grayscale
    if gray_img.mode != "L":
        gray_img = gray_img.convert("L")

    # Create the duotone by mapping grayscale values to crimson gradient
    # Shadow color: deep crimson
    shadow = CRIMSON
    # Highlight color: white
    highlight = (255, 255, 255)

    # Build a lookup table for the duotone mapping
    width, height = gray_img.size
    result = Image.new("RGBA", (width, height))
    gray_data = gray_img.load()
    result_data = result.load()

    for y in range(height):
        for x in range(width):
            luma = gray_data[x, y]
            t = luma / 255.0  # 0.0 (shadow) to 1.0 (highlight)

            # Interpolate between shadow and highlight colors
            r = int(shadow[0] * (1 - t) + highlight[0] * t)
            g = int(shadow[1] * (1 - t) + highlight[1] * t)
            b = int(shadow[2] * (1 - t) + highlight[2] * t)

            # Blend the duotone with the original grayscale
            # at the given opacity for a subtle effect
            gray_rgb = (luma, luma, luma)
            r = int(gray_rgb[0] * (1 - opacity) + r * opacity)
            g = int(gray_rgb[1] * (1 - opacity) + g * opacity)
            b = int(gray_rgb[2] * (1 - opacity) + b * opacity)

            result_data[x, y] = (r, g, b, 255)

    return result


def apply_crimson_overlay_fast(gray_img: Image.Image, opacity: float = 0.25) -> Image.Image:
    """Fast version of crimson overlay using PIL blend operations.
    
    Preferred over pixel-by-pixel for large images.
    """
    if gray_img.mode != "L":
        gray_img = gray_img.convert("L")

    # Convert grayscale to RGB
    gray_rgb = Image.merge("RGB", (gray_img, gray_img, gray_img))

    # Create a solid crimson layer
    crimson_layer = Image.new("RGB", gray_img.size, CRIMSON)

    # Blend: multiply the crimson with grayscale for duotone effect
    # Using ImageEnhance for controlled blending
    blended = Image.blend(gray_rgb, crimson_layer, opacity)

    # Restore contrast lost during blending
    enhancer = ImageEnhance.Contrast(blended)
    blended = enhancer.enhance(1.2)

    return blended


def resize_image(img: Image.Image, target_width: int) -> Image.Image:
    """Resize image to target width, maintaining aspect ratio.
    
    Uses LANCZOS resampling for highest quality downscaling.
    Only downscales — if image is smaller than target, returns as-is.
    
    Args:
        img: PIL Image
        target_width: Target width in pixels
    
    Returns:
        Resized PIL Image
    """
    original_width, original_height = img.size

    # Don't upscale
    if original_width <= target_width:
        return img.copy()

    # Calculate proportional height
    ratio = target_width / original_width
    target_height = int(original_height * ratio)

    return img.resize((target_width, target_height), Image.LANCZOS)


def save_webp(img: Image.Image, output_path: str, quality: int = 80) -> int:
    """Save image as WebP with specified quality.
    
    Args:
        img: PIL Image
        output_path: Output file path
        quality: WebP quality 1-100
    
    Returns:
        File size in bytes
    """
    # Ensure RGB mode for WebP (no RGBA unless needed)
    if img.mode == "L":
        img = img.convert("RGB")
    elif img.mode == "RGBA":
        # Check if alpha channel is actually used
        extrema = img.getextrema()
        if extrema[3] == (255, 255):  # All pixels fully opaque
            img = img.convert("RGB")

    img.save(output_path, "WEBP", quality=quality, method=4)
    return os.path.getsize(output_path)


# ---------------------------------------------------------------------------
# Processing Pipeline
# ---------------------------------------------------------------------------

def process_single_image(
    input_path: str,
    output_dir: str,
    crimson_overlay: bool = False,
    quality: int = DEFAULT_QUALITY,
    sizes: list[int] = None,
) -> dict:
    """Process a single image through the full Axiara pipeline.
    
    Pipeline:
      1. Open original image
      2. Convert to grayscale
      3. (Optional) Apply crimson overlay
      4. Generate responsive sizes
      5. Save as WebP
    
    Args:
        input_path: Path to input image
        output_dir: Output directory
        crimson_overlay: Whether to apply crimson duotone
        quality: WebP quality 1-100
        sizes: List of target widths
    
    Returns:
        Dict with processing results
    """
    if sizes is None:
        sizes = DEFAULT_SIZES

    # Extract filename without extension
    basename = os.path.splitext(os.path.basename(input_path))[0]

    # Open image
    img = Image.open(input_path)
    original_size = img.size
    print(f"  Processing: {os.path.basename(input_path)} ({original_size[0]}x{original_size[1]})")

    # Step 1: Convert to grayscale
    gray = to_grayscale(img)

    # Step 2: Apply crimson overlay if requested
    if crimson_overlay:
        processed = apply_crimson_overlay_fast(gray, opacity=0.25)
        suffix = "-crimson"
        print(f"    → Grayscale + Crimson overlay applied")
    else:
        processed = gray.convert("RGB")
        suffix = ""
        print(f"    → Grayscale conversion applied")

    # Step 3: Generate responsive sizes and save as WebP
    results = {
        "input": input_path,
        "original_size": original_size,
        "outputs": [],
    }

    for width in sorted(sizes):
        resized = resize_image(processed, width)
        actual_w, actual_h = resized.size

        # Output filename: {basename}{suffix}-{width}w.webp
        out_filename = f"{basename}{suffix}-{actual_w}w.webp"
        out_path = os.path.join(output_dir, out_filename)

        file_size = save_webp(resized, out_path, quality=quality)
        results["outputs"].append({
            "path": out_path,
            "width": actual_w,
            "height": actual_h,
            "size_bytes": file_size,
        })
        print(f"    → {out_filename} ({actual_w}x{actual_h}, "
              f"{file_size / 1024:.1f}KB)")

    # Also save full-size version
    out_filename = f"{basename}{suffix}-full.webp"
    out_path = os.path.join(output_dir, out_filename)
    file_size = save_webp(processed, out_path, quality=quality)
    results["outputs"].append({
        "path": out_path,
        "width": processed.size[0],
        "height": processed.size[1],
        "size_bytes": file_size,
    })
    print(f"    → {out_filename} ({processed.size[0]}x{processed.size[1]}, "
          f"{file_size / 1024:.1f}KB)")

    return results


def generate_srcset_snippet(results: dict) -> str:
    """Generate an HTML srcset snippet for the processed image.
    
    Returns a ready-to-paste <img> tag with srcset for responsive loading.
    """
    outputs = sorted(results["outputs"], key=lambda o: o["width"])
    # Exclude the "full" size from srcset (it's a fallback)
    sized = [o for o in outputs if not o["path"].endswith("-full.webp")]

    if not sized:
        return ""

    srcset_parts = []
    for o in sized:
        rel_path = o["path"]
        srcset_parts.append(f"{rel_path} {o['width']}w")

    srcset = ",\n             ".join(srcset_parts)
    default_src = sized[-1]["path"]  # Largest size as default

    return (
        f'<img src="{default_src}"\n'
        f'     srcset="{srcset}"\n'
        f'     sizes="(max-width: 375px) 375px,\n'
        f'            (max-width: 768px) 768px,\n'
        f'            1440px"\n'
        f'     alt=""\n'
        f'     loading="lazy">'
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Axiara Image Processor — B&W conversion, "
                    "crimson overlay, WebP compression, responsive sizes.",
        epilog="Example: python3 execution/optimize_images.py "
               "--input src/assets/images/raw/hero.jpg "
               "--output src/assets/images/ --crimson-overlay"
    )
    parser.add_argument(
        "--input", required=True,
        help="Input image file or directory of images"
    )
    parser.add_argument(
        "--output", required=True,
        help="Output directory for processed images"
    )
    parser.add_argument(
        "--crimson-overlay", action="store_true",
        help="Apply Crimson (#C41E3A) duotone overlay"
    )
    parser.add_argument(
        "--quality", type=int, default=DEFAULT_QUALITY,
        help=f"WebP quality 1-100 (default: {DEFAULT_QUALITY})"
    )
    parser.add_argument(
        "--sizes", type=str, default=None,
        help="Comma-separated widths (default: 375,768,1440)"
    )

    args = parser.parse_args()

    # Resolve paths relative to project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    input_path = os.path.join(project_root, args.input)
    output_dir = os.path.join(project_root, args.output)

    # Parse sizes
    sizes = DEFAULT_SIZES
    if args.sizes:
        sizes = [int(s.strip()) for s in args.sizes.split(",")]

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Collect input files
    input_files = []
    if os.path.isfile(input_path):
        input_files.append(input_path)
    elif os.path.isdir(input_path):
        for fname in sorted(os.listdir(input_path)):
            ext = os.path.splitext(fname)[1].lower()
            if ext in SUPPORTED_EXTENSIONS:
                input_files.append(os.path.join(input_path, fname))
    else:
        print(f"[ERROR] Input not found: {input_path}")
        sys.exit(1)

    if not input_files:
        print(f"[ERROR] No supported images found in: {input_path}")
        print(f"        Supported: {', '.join(sorted(SUPPORTED_EXTENSIONS))}")
        sys.exit(1)

    # Process
    print(f"\nAxiara Image Processor")
    print(f"{'=' * 50}")
    print(f"  Input:   {args.input}")
    print(f"  Output:  {args.output}")
    print(f"  Overlay: {'Crimson #C41E3A' if args.crimson_overlay else 'None (pure B&W)'}")
    print(f"  Quality: {args.quality}")
    print(f"  Sizes:   {', '.join(str(s) + 'w' for s in sizes)}")
    print(f"  Files:   {len(input_files)}")
    print(f"{'=' * 50}\n")

    all_results = []
    total_input_size = 0
    total_output_size = 0

    for filepath in input_files:
        total_input_size += os.path.getsize(filepath)
        results = process_single_image(
            input_path=filepath,
            output_dir=output_dir,
            crimson_overlay=args.crimson_overlay,
            quality=args.quality,
            sizes=sizes,
        )
        all_results.append(results)

        for output in results["outputs"]:
            total_output_size += output["size_bytes"]

        # Print srcset snippet
        snippet = generate_srcset_snippet(results)
        if snippet:
            print(f"\n    HTML srcset snippet:")
            for line in snippet.split("\n"):
                print(f"    {line}")
            print()

    # Summary
    print(f"\n{'=' * 50}")
    print(f"  [OK] Processed {len(input_files)} image(s)")
    print(f"  Input total:  {total_input_size / 1024:.1f}KB")
    print(f"  Output total: {total_output_size / 1024:.1f}KB")
    if total_input_size > 0:
        ratio = (1 - total_output_size / total_input_size) * 100
        print(f"  Savings:      {ratio:.1f}%")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
