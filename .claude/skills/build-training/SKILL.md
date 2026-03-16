---
name: build-training
description: >
  Build the Git Literacy training page from curriculum markdown.
  Use when the user asks to rebuild, regenerate, or update the
  training HTML page, or when curriculum content changes.
---

## Usage

Run the build:

```bash
bash .claude/skills/build-training/scripts/build.sh
```

Or directly:

```bash
python3 .claude/skills/build-training/scripts/build.py
```

## Input / Output

- **Input:** `curriculum/git-literacy-training.md` (curated curriculum with YAML frontmatter)
- **Template:** `.claude/skills/build-training/assets/template.html` (HTML shell with CSS/JS)
- **Output:** `dist/training.html` (self-contained, open in any browser)

## Curriculum conventions

The curriculum file must follow these conventions for the build to parse correctly:

1. **YAML frontmatter** with `title`, `version`, `estimated_time`, `module_count`
2. **Modules** as `### Module N: Title (X minutes)` headings
3. **Check yourself** blocks as `#### Check yourself` followed by `**Q:**`/`**A:**` pairs
4. **Post-module sections** as `## Quick Reference Card`, `## Glossary`, `## Appendix A:...`, `## Appendix B:...`

## Modifying styling

Edit the CSS custom properties in the `:root` block of `assets/template.html`. All colors, fonts, spacing, and sizes are defined there. Class names are semantic (`module`, `check-yourself`, `glossary-term`, etc.) for easy targeting by a design system.

## Adding or removing modules

Edit `curriculum/git-literacy-training.md`:
- Add a new `### Module N: Title (X minutes)` section
- Update the `module_count` in frontmatter
- Re-run the build

## Dependencies

Python 3 stdlib only. No `pip install` needed.
