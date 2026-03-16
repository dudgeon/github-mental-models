#!/usr/bin/env python3
"""Build the Git Literacy training page from curriculum markdown.

Reads curriculum/git-literacy-training.md and the HTML template,
produces dist/training.html. Python 3 stdlib only — no pip dependencies.
"""

import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
CURRICULUM = os.path.join(REPO_ROOT, "curriculum", "git-literacy-training.md")
TEMPLATE = os.path.join(REPO_ROOT, ".claude", "skills", "build-training", "assets", "template.html")
OUTPUT_DIR = os.path.join(REPO_ROOT, "dist")
OUTPUT = os.path.join(OUTPUT_DIR, "training.html")


# ---------------------------------------------------------------------------
# YAML frontmatter parser (simple key: value)
# ---------------------------------------------------------------------------

def parse_frontmatter(text):
    """Extract YAML frontmatter and return (metadata_dict, remaining_text)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block = text[3:end].strip()
    rest = text[end + 4:].lstrip("\n")
    meta = {}
    for line in block.split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            val = val.strip().strip('"').strip("'")
            meta[key.strip()] = val
    return meta, rest


# ---------------------------------------------------------------------------
# Markdown to HTML converter
# ---------------------------------------------------------------------------

def slugify(text):
    """Convert heading text to a URL-friendly slug."""
    text = re.sub(r'<[^>]+>', '', text)  # strip HTML tags
    text = re.sub(r'\*\*|__|\*|_|`', '', text)  # strip md formatting
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def convert_inline(text):
    """Convert inline markdown (bold, italic, code, links) to HTML."""
    # Inline code first (so backtick content isn't processed further)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    # Bold + italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text


def parse_table(lines):
    """Parse pipe-delimited table lines into an HTML table."""
    if len(lines) < 2:
        return ""
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        rows.append(cells)
    # Row 1 is the separator (|---|---|)
    if len(rows) < 2:
        return ""
    header = rows[0]
    # Find separator row
    sep_idx = 1
    body_rows = rows[sep_idx + 1:]

    html = '<table>\n<thead><tr>'
    for cell in header:
        html += '<th>' + convert_inline(cell) + '</th>'
    html += '</tr></thead>\n<tbody>\n'
    for row in body_rows:
        html += '<tr>'
        for i, cell in enumerate(row):
            # Pad if row has fewer cells than header
            html += '<td>' + convert_inline(cell) + '</td>'
        # Pad missing cells
        for _ in range(len(header) - len(row)):
            html += '<td></td>'
        html += '</tr>\n'
    html += '</tbody></table>\n'
    return html


def md_to_html(text):
    """Convert markdown text to HTML. Handles the subset used in the curriculum."""
    lines = text.split('\n')
    html_parts = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Blank line
        if line.strip() == '':
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^---+\s*$', line):
            html_parts.append('<hr>')
            i += 1
            continue

        # Headings
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            text_content = m.group(2).strip()
            slug = slugify(text_content)
            html_text = convert_inline(text_content)
            html_parts.append(f'<h{level} id="{slug}">{html_text}</h{level}>')
            i += 1
            continue

        # Table (starts with |)
        if line.strip().startswith('|'):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i])
                i += 1
            html_parts.append(parse_table(table_lines))
            continue

        # Blockquote
        if line.strip().startswith('>'):
            bq_lines = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                bq_lines.append(re.sub(r'^>\s?', '', lines[i].strip()))
                i += 1
            bq_content = md_to_html('\n'.join(bq_lines))
            html_parts.append(f'<blockquote>{bq_content}</blockquote>')
            continue

        # Fenced code block
        if line.strip().startswith('```'):
            lang = line.strip()[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1  # skip closing ```
            code_text = '\n'.join(code_lines)
            code_text = code_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            html_parts.append(f'<pre><code>{code_text}</code></pre>')
            continue

        # Ordered list
        if re.match(r'^\s*\d+\.\s', line):
            items = []
            while i < len(lines) and re.match(r'^\s*\d+\.\s', lines[i]):
                item_text = re.sub(r'^\s*\d+\.\s+', '', lines[i])
                i += 1
                # Continuation lines (indented, not a new list item or blank)
                while i < len(lines) and lines[i].strip() and not re.match(r'^\s*\d+\.\s', lines[i]) and not re.match(r'^\s*[-*]\s', lines[i]) and not lines[i].strip().startswith('#') and not lines[i].strip().startswith('|') and not lines[i].strip().startswith('>'):
                    item_text += ' ' + lines[i].strip()
                    i += 1
                items.append(convert_inline(item_text))
            html = '<ol>\n'
            for item in items:
                html += f'<li>{item}</li>\n'
            html += '</ol>\n'
            html_parts.append(html)
            continue

        # Unordered list
        if re.match(r'^\s*[-*]\s', line):
            items = []
            while i < len(lines) and re.match(r'^\s*[-*]\s', lines[i]):
                item_text = re.sub(r'^\s*[-*]\s+', '', lines[i])
                i += 1
                # Continuation lines
                while i < len(lines) and lines[i].strip() and not re.match(r'^\s*[-*]\s', lines[i]) and not re.match(r'^\s*\d+\.\s', lines[i]) and not lines[i].strip().startswith('#') and not lines[i].strip().startswith('|') and not lines[i].strip().startswith('>'):
                    item_text += ' ' + lines[i].strip()
                    i += 1
                items.append(convert_inline(item_text))
            html = '<ul>\n'
            for item in items:
                html += f'<li>{item}</li>\n'
            html += '</ul>\n'
            html_parts.append(html)
            continue

        # Paragraph (collect consecutive non-blank lines that aren't special)
        para_lines = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^#{1,6}\s', lines[i]) and not lines[i].strip().startswith('|') and not lines[i].strip().startswith('>') and not lines[i].strip().startswith('```') and not re.match(r'^---+\s*$', lines[i]) and not re.match(r'^\s*[-*]\s', lines[i]) and not re.match(r'^\s*\d+\.\s', lines[i]):
            para_lines.append(lines[i].strip())
            i += 1
        if para_lines:
            html_parts.append(f'<p>{convert_inline(" ".join(para_lines))}</p>')
            continue

        # Fallback: skip line
        i += 1

    return '\n'.join(html_parts)


# ---------------------------------------------------------------------------
# Structure parser: extract modules, sections, check-yourself blocks
# ---------------------------------------------------------------------------

def extract_check_yourself(html):
    """Extract check-yourself sections from HTML and replace with styled blocks.

    Looks for <h4> with 'check yourself' followed by Q/A pairs.
    Returns the modified HTML.
    """
    # Find #### Check yourself sections
    pattern = r'<h4 id="check-yourself[^"]*">Check yourself</h4>\s*(.*?)(?=<h[234]|$)'

    def replace_check(match):
        content = match.group(1)
        # Try two patterns:
        # 1. Q and A on separate <p> tags
        qa_pairs = re.findall(
            r'<p><strong>Q:</strong>\s*(.*?)</p>\s*<p><strong>A:</strong>\s*(.*?)</p>',
            content, re.DOTALL
        )
        # 2. Q and A on the same <p> tag
        if not qa_pairs:
            qa_pairs = re.findall(
                r'<strong>Q:</strong>\s*(.*?)\s*<strong>A:</strong>\s*(.*?)(?=<strong>Q:</strong>|</p>)',
                content, re.DOTALL
            )
        if not qa_pairs:
            return match.group(0)

        block = '<div class="check-yourself">\n<h4>Check yourself</h4>\n'
        for q, a in qa_pairs:
            block += '<div class="qa-pair">\n'
            block += f'<p class="question">Q: {q}</p>\n'
            block += f'<div class="answer"><p>{a}</p></div>\n'
            block += '<button class="reveal-btn">Show answer</button>\n'
            block += '</div>\n'
        block += '</div>\n'
        return block

    return re.sub(pattern, replace_check, html, flags=re.DOTALL)


def parse_modules(md_text):
    """Parse module sections from markdown. Returns list of dicts and remaining sections."""
    # Split by ### Module N: headings
    module_pattern = r'^### (Module \d+:.+?)$'
    parts = re.split(module_pattern, md_text, flags=re.MULTILINE)

    modules = []
    other_sections = {}

    # parts[0] is content before first module
    pre_modules = parts[0]

    i = 1
    while i < len(parts) - 1:
        title = parts[i].strip()
        body = parts[i + 1]

        # Extract time estimate from title
        time_match = re.search(r'\((\d+)\s*minutes?\)', title)
        time_est = time_match.group(0) if time_match else ''

        # Extract module number
        num_match = re.match(r'Module (\d+)', title)
        num = int(num_match.group(1)) if num_match else 0

        modules.append({
            'number': num,
            'title': title,
            'time': time_est,
            'body_md': body.strip(),
        })
        i += 2

    return pre_modules, modules


def parse_post_modules(md_text):
    """Extract post-module sections (Quick Reference, Glossary, Appendices)."""
    sections = {}
    # Split by ## headings
    parts = re.split(r'^(## .+)$', md_text, flags=re.MULTILINE)
    i = 1
    while i < len(parts) - 1:
        heading = parts[i].strip()
        body = parts[i + 1].strip()
        sections[heading] = body
        i += 2
    return sections


# ---------------------------------------------------------------------------
# HTML assembly
# ---------------------------------------------------------------------------

def build_nav(modules):
    """Generate sidebar navigation HTML."""
    items = []
    for mod in modules:
        slug = slugify(mod['title'])
        label = mod['title']
        # Shorten for nav: "Module N: Short Title"
        short = re.sub(r'\s*\(\d+\s*minutes?\)', '', label)
        items.append(
            f'<li><a href="#{slug}">'
            f'<span class="nav-check" data-section-id="{slug}">&#10003;</span>'
            f'{short}</a></li>'
        )
    return '\n'.join(items)


def build_module_html(mod):
    """Convert a module dict to HTML."""
    slug = slugify(mod['title'])
    title_html = convert_inline(mod['title'])
    time_badge = f'<span class="module-time">{mod["time"]}</span>' if mod['time'] else ''

    body_html = md_to_html(mod['body_md'])
    body_html = extract_check_yourself(body_html)

    # Make check-yourself heading IDs unique per module
    body_html = re.sub(
        r'id="check-yourself"',
        f'id="check-yourself-{mod["number"]}"',
        body_html
    )

    return (
        f'<section class="module" id="{slug}">\n'
        f'<h3>{title_html}{time_badge}</h3>\n'
        f'{body_html}\n'
        f'</section>\n'
    )


def build():
    """Main build function."""
    # Read inputs
    with open(CURRICULUM, 'r', encoding='utf-8') as f:
        curriculum_text = f.read()
    with open(TEMPLATE, 'r', encoding='utf-8') as f:
        template = f.read()

    # Parse frontmatter
    meta, md_body = parse_frontmatter(curriculum_text)
    title = meta.get('title', 'Git Literacy Training')

    # Split into Part 1 (requirements) and Part 2 (lessons)
    # We only render Part 2 + appendices in the training page
    part2_marker = '## Part 2: Lesson Plan'
    part2_idx = md_body.find(part2_marker)
    if part2_idx == -1:
        print("ERROR: Could not find '## Part 2: Lesson Plan' in curriculum", file=sys.stderr)
        sys.exit(1)

    lesson_text = md_body[part2_idx:]

    # Find where modules end and reference sections begin
    # Split at the first ## after modules (Quick Reference, Glossary, etc.)
    # Modules use ### headings, post-module sections use ## headings
    post_module_markers = ['## Quick Reference', '## Glossary', '## Appendix']
    split_idx = len(lesson_text)
    for marker in post_module_markers:
        idx = lesson_text.find(marker)
        if idx != -1 and idx < split_idx:
            split_idx = idx

    module_text = lesson_text[:split_idx]
    post_text = lesson_text[split_idx:]

    # Parse modules
    pre_modules_md, modules = parse_modules(module_text)

    # Build intro (Part 2 intro before Module 1)
    # Find "### How to Use This Training" section
    intro_html = ''
    how_to_match = re.search(r'### How to Use This Training.*?(?=### Module|\Z)', pre_modules_md, re.DOTALL)
    if how_to_match:
        intro_html = md_to_html(how_to_match.group(0))

    # Build module HTML
    modules_html = intro_html + '\n'
    for mod in modules:
        modules_html += build_module_html(mod)

    # Build post-module sections
    post_html = md_to_html(post_text)

    # Build nav
    nav_html = build_nav(modules)

    # Assemble
    content_html = modules_html + '\n' + post_html

    output = template.replace('{{TITLE}}', title)
    output = output.replace('{{SHORT_TITLE}}', 'Git Literacy')
    output = output.replace('{{SUBTITLE}}', 'For Product Managers')
    output = output.replace('{{NAV_ITEMS}}', nav_html)
    output = output.replace('{{CONTENT}}', content_html)

    # Write output
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"Built: {OUTPUT}")
    print(f"  Modules: {len(modules)}")
    print(f"  Title: {title}")


if __name__ == '__main__':
    build()
