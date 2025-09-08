# Copilot Instructions for Promptmakers Blog Dist

## Project Overview
This project is a static blog site, with all distributable files located in the `dist/` directory. The site is designed for accessibility and is deployed using Netlify (see `netlify.toml`).

## Key Files and Structure
- `dist/` — Main output directory for the static site (HTML, CSS, images, etc.)
- `update_accessibility.py` — Python script for batch accessibility updates to HTML files
- `ACCESSIBILITY_UPDATE_SUMMARY.md` — Documents accessibility improvements and conventions
- `netlify.toml` — Netlify deployment configuration

## Accessibility Automation
- Use `update_accessibility.py` to update all "Read More" and related links for accessibility. This script:
  - Adds `aria-label` and visually hidden `<span class="sr-only">` to links
  - Updates homepage, blog index, and individual blog post pages
- The `.sr-only` CSS class is defined in `/dist/_astro/index.CGi0OF9J.css` for screen-reader-only content

## Developer Workflow
- **Accessibility updates:** Run `update_accessibility.py` after adding or modifying articles to ensure all links are accessible
- **Deployment:** Netlify auto-publishes from the `dist/` directory; all routes are redirected to `index.html` for SPA behavior
- **No build scripts or package managers** are present in this distribution folder; all content is static except for the Python script

## Project Conventions
- All article links use descriptive `aria-label` and a hidden span for screen readers
- Accessibility changes are summarized in `ACCESSIBILITY_UPDATE_SUMMARY.md` with before/after code samples
- All static assets (HTML, CSS, images) are under `dist/`

## Example: Accessible Link Pattern
```html
<a href="/blog/advanced-prompt-engineering-techniques" class="read-more" aria-label="Read full article: Advanced Prompt Engineering Techniques: Beyond the Basics">
  Read More
  <span class="sr-only">: Advanced Prompt Engineering Techniques: Beyond the Basics</span>
  <svg>...</svg>
</a>
```

## References
- See `ACCESSIBILITY_UPDATE_SUMMARY.md` for details on accessibility improvements and compliance
- See `update_accessibility.py` for automation logic and patterns

---
For any new automation or accessibility features, follow the patterns in `update_accessibility.py` and document changes in `ACCESSIBILITY_UPDATE_SUMMARY.md`.
