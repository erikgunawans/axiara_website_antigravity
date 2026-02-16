# DIRECTIVE: Deploy Axiara Website (BeTheme / Static)

> **Objective**: Prepare and deploy the Axiara static website (HTML/Tailwind).
> **Note**: While titled "BeTheme", this project is a custom static build. This guide covers deploying the HTML artifacts. If WordPress integration is required later, a separate migration phase is needed.

## 1. Pre-Deployment Optimization

Before deploying, run the full optimization suite to ensure performance and brand compliance.

### 1.1 Regenerate CSS
Ensure the latest `axiara.css` is built from the source config.

```bash
python3 execution/generate_css.py
```

### 1.2 Optimize Images
Convert all assets to WebP and apply B&W treatment where necessary.

```bash
python3 execution/optimize_images.py
```

### 1.3 Validate Codebase
Run the strict HTML validator to catch any regressions, broken links, or A11Y issues.

```bash
# Validates all HTML files in the project
python3 execution/validate_html.py .
```

> **CRITICAL**: Do NOT deploy if any `FAIL` results appear. `WARN` items must be reviewed.

---

## 2. Packaging for Deployment

### 2.1 Clean Junk Files
Remove local development artifacts (`.DS_Store`, `.git`, `.gemini`, `.tmp`) before packaging.

```bash
# Example clean command (use with caution)
find . -name ".DS_Store" -delete
rm -rf .tmp .gemini
```

### 2.2 Create Archive
Zip the project root (excluding sensitive/dev files) for upload.

```bash
zip -r axiara-deploy-v1.zip . -x "*.git*" -x "*.gemini*" -x "*.tmp*" -x "execution/*" -x "directives/*" -x "docs/*"
```

> **Note**: You may exclude `execution/`, `directives/`, and `docs/` if the server only needs the runtime site (`index.html`, `src/`, `contact.html`, etc.).

---

## 3. Server Deployment

### Option A: Static Host (Netlify / Vercel)
1.  Drag & drop the `axiara-deploy-v1.zip` (or link GitHub repo).
2.  Set **Publish Directory** to `./` (root).
3.  Ensure asset paths are relative or configured correctly.

### Option B: cPanel / FTP (Standard Shared Hosting)
1.  Upload `axiara-deploy-v1.zip` to `public_html`.
2.  Extract the zip.
3.  Ensure `index.html` is in the root of `public_html`.

### Option C: WordPress / BeTheme Integration
*(If the goal is to use this design within WordPress)*
This requires a **Theme Migration** phase:
1.  Create a Child Theme for BeTheme.
2.  Port `axiara.css` to the theme's stylesheet.
3.  Convert HTML pages to PHP templates (`page-services.php`, etc.).
4.  OR use BeTheme's "Custom HTML" blocks to paste section code.

---

## 4. Post-Deployment Verification

Visit the live URL and verify:

- [ ] **Home Page**: Hero animation plays?
- [ ] **Navigation**: Links work? Mobile menu opens?
- [ ] **Assets**: Images load? (Check console for 404s).
- [ ] **Forms**: Contact form submission works? (Static forms may need a backend handler like Formspree or Netlify Forms).
- [ ] **SSL**: HTTPS lock icon present?
