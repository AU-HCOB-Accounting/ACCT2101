"""
Generate click-to-copy HTML pages from IMAGE_PROMPTS.md files.
Run: python generate_copy_pages.py
Creates COPY_PROMPTS.html in each ch* folder.
"""
import re
from pathlib import Path

IMAGES_DIR = Path(__file__).parent

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{chapter_title} — Copy Prompts</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, 'Segoe UI', sans-serif; background: #f5f5f5; padding: 2rem; color: #333; }}
  h1 {{ font-size: 1.4rem; margin-bottom: 1.5rem; color: #1a3a5c; }}
  .card {{ background: #fff; border-radius: 8px; margin-bottom: 1.2rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); overflow: hidden; }}
  .card-header {{ display: flex; justify-content: space-between; align-items: center; padding: 0.8rem 1rem; background: #1a3a5c; color: #fff; }}
  .card-header h3 {{ font-size: 0.95rem; font-weight: 600; }}
  .copy-btn {{ background: #fff; color: #1a3a5c; border: none; padding: 0.4rem 1rem; border-radius: 4px; cursor: pointer; font-size: 0.85rem; font-weight: 600; transition: all 0.2s; }}
  .copy-btn:hover {{ background: #e0e0e0; }}
  .copy-btn.copied {{ background: #4caf50; color: #fff; }}
  .prompt-text {{ padding: 1rem; font-size: 0.85rem; line-height: 1.6; white-space: pre-wrap; font-family: 'Consolas', 'Monaco', monospace; color: #444; max-height: 300px; overflow-y: auto; border-top: 1px solid #eee; }}
  .meta {{ padding: 0.5rem 1rem; font-size: 0.8rem; color: #777; background: #fafafa; border-top: 1px solid #eee; }}
</style>
</head>
<body>
<h1>{chapter_title}</h1>
{cards}
<script>
function copyPrompt(btn, id) {{
  const text = document.getElementById(id).textContent;
  navigator.clipboard.writeText(text).then(() => {{
    btn.textContent = 'Copied!';
    btn.classList.add('copied');
    setTimeout(() => {{ btn.textContent = 'Copy'; btn.classList.remove('copied'); }}, 1500);
  }});
}}
</script>
</body>
</html>
"""

CARD_TEMPLATE = """\
<div class="card">
  <div class="card-header">
    <h3>{title}</h3>
    <button class="copy-btn" onclick="copyPrompt(this, 'prompt-{idx}')">Copy</button>
  </div>
  <div class="meta">{meta}</div>
  <div class="prompt-text" id="prompt-{idx}">{prompt}</div>
</div>"""


def html_escape(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def parse_md(md_text):
    """Parse IMAGE_PROMPTS.md and extract prompt blocks with metadata."""
    prompts = []

    # Match image section headings:
    #   "## Image X:" or "### Image X:" (ch01-07)
    #   "## X. figX-X" (ch08+)
    # Skip sub-headings like "### GPT Prompt:", "### GPT/Gemini Prompt:"
    section_pattern = re.compile(r'^(#{2,3})\s+(.+)$', re.MULTILINE)
    all_headings = list(section_pattern.finditer(md_text))

    # Filter: keep only image-related headings
    section_starts = []
    for m in all_headings:
        h = m.group(2).strip().lower()
        if any(skip in h for skip in ['priority', 'summary table', 'gpt prompt', 'gemini prompt', 'gpt/gemini']):
            continue
        if any(skip in h for skip in ['공통 스타일']):
            continue
        section_starts.append(m)

    for i, match in enumerate(section_starts):
        heading = match.group(2).strip()

        # Get section content until next ## heading
        start = match.end()
        end = section_starts[i + 1].start() if i + 1 < len(section_starts) else len(md_text)
        section = md_text[start:end]

        # Extract prompt: text inside ``` fences
        code_match = re.search(r'```\n?(.*?)```', section, re.DOTALL)
        if code_match:
            prompt = code_match.group(1).strip()
        else:
            # ch08+ style: unfenced prompt after **Prompt:**
            prompt_match = re.search(r'\*\*Prompt:\*\*\s*\n(.*?)(?=\n---|\Z)', section, re.DOTALL)
            if not prompt_match:
                continue
            prompt = prompt_match.group(1).strip()

        # Build a clean title from the heading
        # Remove leading "Image X: " or numbering like "1. "
        title = re.sub(r'^Image\s+\d+:\s*', '', heading)
        title = re.sub(r'^\d+\.\s*', '', title)

        # Extract metadata lines
        meta_parts = []
        for line in section.split('\n'):
            line_s = line.strip()
            for key in ['Filename:', 'File:', 'Used in:', 'Usage:', 'Purpose:', 'Description:']:
                if key.lower() in line_s.lower().replace('*', ''):
                    clean = re.sub(r'\*\*', '', line_s).strip('- ').strip()
                    meta_parts.append(clean)
                    break
        meta = ' | '.join(meta_parts[:2])

        prompts.append({
            'title': title,
            'meta': meta,
            'prompt': prompt,
        })

    return prompts


def generate_html(chapter_dir):
    md_path = chapter_dir / 'IMAGE_PROMPTS.md'
    if not md_path.exists():
        return
    md_text = md_path.read_text(encoding='utf-8')

    title_match = re.match(r'^#\s+(.+)', md_text, re.MULTILINE)
    chapter_title = title_match.group(1).strip() if title_match else chapter_dir.name

    prompts = parse_md(md_text)
    if not prompts:
        print(f"  WARNING: No prompts found in {chapter_dir.name}")
        return

    cards = []
    for i, p in enumerate(prompts):
        cards.append(CARD_TEMPLATE.format(
            title=html_escape(p['title']),
            meta=html_escape(p['meta']),
            prompt=html_escape(p['prompt']),
            idx=i,
        ))

    html = HTML_TEMPLATE.format(
        chapter_title=html_escape(chapter_title),
        cards='\n'.join(cards),
    )

    out_path = chapter_dir / 'COPY_PROMPTS.html'
    out_path.write_text(html, encoding='utf-8')
    print(f"  {chapter_dir.name}: {len(prompts)} prompts -> COPY_PROMPTS.html")


def main():
    dirs = sorted(IMAGES_DIR.glob('ch*'))
    print(f"Found {len(dirs)} chapter folders\n")
    for d in dirs:
        if d.is_dir():
            generate_html(d)
    print("\nDone!")


if __name__ == '__main__':
    main()
