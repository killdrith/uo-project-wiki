from pathlib import Path
import re, html, json, os

root = Path(__file__).parent
out = root / 'docs'
out.mkdir(exist_ok=True)
source = root / 'handoff-public.txt'
if not source.exists():
    imported = (Path(os.environ['PAPERCLIP_RUN_SCRATCH_DIR']) / 'handoff.txt').read_text(encoding='utf-8-sig')
    imported = re.sub(r'(?m)^C:\\Users\\.*$', '[Original local export path omitted]', imported)
    source.write_text(imported, encoding='utf-8')
raw = source.read_text(encoding='utf-8-sig')
parts = re.split(r'(?m)^(\d+)\. ([A-Z][^\n]+)\n', raw)
assert len(parts) == 55, 'Expected all 18 handoff sections'
pages = []
for i in range(1, len(parts), 3):
    n, title, body = parts[i:i+3]
    body = body.replace('END OF HANDOFF', '').strip()
    pages.append(dict(slug=f'topic-{n}', title=title.capitalize(), body=body, source=f'Handoff section {n}'))
pages.insert(0, dict(slug='index', title='UO project wiki', source='Editorial overview of the September 28, 2026 handoff', body='''A different game with the visual style and much of the movement and combat feel of original Ultima Online.

This wiki starts from the architecture and design handoff. It records intentions, recommendations, and questions; it is not an approved game specification.

START HERE:
  - Vision and user answers: topics 1 and 2.
  - Platform options and customization: topics 4 and 5.
  - Progression, creatures, and combat: topics 6 through 8.
  - Art, visibility, and world: topics 9 through 12.
  - Performance and persistence: topics 13 and 14.
  - Open decisions and source trail: topics 16 and 18.

STATUS KEY:
  - User intention: an explicitly expressed preference, not necessarily a finalized design.
  - Working recommendation: the prior assistant's judgment, subject to validation.
  - Exploration: an idea considered to understand boundaries, not selected scope.
  - Unresolved: a decision or technical claim still requiring work.

CURRENT DIRECTION:
ModernUO with ClassicUO is the leading recommendation, not a final selection. A dedicated downloadable client is acceptable. Most encounters should involve fewer than ten players. A connected passive tree is an interest; its rules remain open.

IMPLEMENTATION STATUS:
The handoff reports no completed server setup, benchmark, game implementation, or final platform selection in that conversation. Work in the separate Testing conversation is unknown. This wiki does not imply that those activities have happened.

PROVENANCE:
Source: UO-Project-Paperclip-Handoff.txt, prepared September 28, 2026, summarizing discussions from September 16 through 28. Technical claims are imported historical research, not freshly verified findings. The original local export path is omitted from this publication package. The attached original remains on the Paperclip task.

MAINTAINING THIS WIKI:
Edit the topic text files and run build_wiki.py with Python 3. New decisions should record the decision maker, date, status, and supporting evidence. A future approved design document supersedes conflicting exploratory notes. Topic 17 preserves the original suggested organization as historical context.'''))
content = out / 'content'
content.mkdir(exist_ok=True)
# Preserve editable content; subsequent builds use the text files as their authority.
for p in pages:
    f = content / (p['slug'] + '.txt')
    if f.exists(): p['body'] = f.read_text(encoding='utf-8')
    else: f.write_text(p['body'] + '\n', encoding='utf-8')

def inline(s):
    return re.sub(r'https://[^\s<>]+', lambda m: '<a href="'+m[0]+'">'+m[0]+'</a>', html.escape(s))

def render(body):
    blocks=[]
    for block in re.split(r'\n\s*\n', body):
        lines=block.splitlines()
        if all(x.strip().startswith('- ') for x in lines):
            blocks.append('<ul>'+''.join('<li>'+inline(x.strip()[2:])+'</li>' for x in lines)+'</ul>')
        else:
            blocks.append('<p>'+ '<br>'.join(inline(x) for x in lines)+'</p>')
    return '\n'.join(blocks)

for p in pages:
    nav=''.join(f'<a href="{q["slug"]}.html"'+(' aria-current="page"' if p==q else '')+'>'+html.escape(q['title'])+'</a>' for q in pages)
    doc=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(p['title'])} · UO project</title><link rel="stylesheet" href="style.css"></head><body><a class="skip" href="#main">Skip to content</a><header><a href="index.html">UO PROJECT <span>Working knowledge</span></a></header><div class="layout"><aside><label for="search">Search the wiki</label><input id="search" type="search" placeholder="Combat, saves, progression…"><p id="search-status" role="status"></p><nav aria-label="Wiki topics">{nav}</nav></aside><main id="main"><p class="eyebrow">DESIGN & ARCHITECTURE / SEPTEMBER 2026</p><h1>{html.escape(p['title'])}</h1><div class="notice">Working notes · Preferences, recommendations, and exploration retain their original status. Technical research requires version-specific verification.</div><article>{render(p['body'])}</article><footer>{html.escape(p['source'])} · Imported September 28, 2026<br><a href="content/{p['slug']}.txt">Read editable source</a> · <a href="topic-18.html">Research references</a></footer></main></div><script src="search-data.js"></script><script src="search.js"></script></body></html>'''
    (out / (p['slug']+'.html')).write_text(doc, encoding='utf-8')
(out/'search-data.js').write_text('const wikiSearch = '+json.dumps({p['slug']+'.html':p['title']+' '+p['body'] for p in pages})+';', encoding='utf-8')
(out/'.nojekyll').touch()
print(f'Built {len(pages)} pages; all 18 source sections retained.')
