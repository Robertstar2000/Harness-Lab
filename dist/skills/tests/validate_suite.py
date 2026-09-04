from pathlib import Path
import json,re,sys

ROOT=Path(__file__).resolve().parents[1]
EXPECTED={
 'mars-harness-orchestrator','hypatia-science-harness','hyperia-research-synthesis',
 'intelligent-engineer-harness','vibe-engineering-collaboration',
 'ground-truth-gatekeeper','pm-accelerator-harness','mission-memory-steward'
}
errors=[]
found={p.parent.name for p in ROOT.glob('*/SKILL.md')}
if found != EXPECTED: errors.append(f'skill set mismatch: {sorted(found)}')
for p in ROOT.glob('*/SKILL.md'):
    text=p.read_text(encoding='utf-8')
    if not text.startswith('---\n'): errors.append(f'{p}: missing frontmatter')
    for section in ['## Purpose','## Decision loop','## Work-product contract','## Guardrails','## Runtime portability']:
        if section not in text: errors.append(f'{p}: missing {section}')
    if re.search(r'\b(?:TODO|TBD|FIXME)\b',text,re.I): errors.append(f'{p}: placeholder found')
packet=json.loads((ROOT/'examples/moxie-isru/stage-packet.json').read_text())
classes={c['evidence_class'] for c in packet['claims']}
if not {'Observed','Unknown'} <= classes: errors.append('MOXIE packet lacks required evidence classes')
if packet['validation']['status'] not in {'pass','conditional_pass','fail'}: errors.append('invalid gate status')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('PASS: 8 skills, required contracts, and MOXIE evidence packet validated')
