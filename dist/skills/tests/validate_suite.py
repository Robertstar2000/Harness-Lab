from pathlib import Path
import json,re,sys

ROOT=Path(__file__).resolve().parents[1]
EXPECTED={
 'mars-harness-orchestrator','hypatia-science-harness','hyperia-research-synthesis',
 'intelligent-engineer-harness','vibe-engineering-collaboration',
 'ground-truth-gatekeeper','pm-accelerator-harness','mission-memory-steward',
 'ethical-specialist-agent-network'
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
phase_minimums={
 'hypatia-science-harness':10,
 'intelligent-engineer-harness':10,
 'pm-accelerator-harness':9,
}
for skill,minimum in phase_minimums.items():
    text=(ROOT/skill/'SKILL.md').read_text(encoding='utf-8')
    phases=len(re.findall(r'^###\s+(?:Phase\s+)?\d+[.\s—-]',text,re.M))
    if phases < minimum: errors.append(f'{skill}: expected at least {minimum} application phases, found {phases}')
packet=json.loads((ROOT/'examples/moxie-isru/stage-packet.json').read_text())
classes={c['evidence_class'] for c in packet['claims']}
if not {'Observed','Unknown'} <= classes: errors.append('MOXIE packet lacks required evidence classes')
if packet['validation']['status'] not in {'pass','conditional_pass','fail'}: errors.append('invalid gate status')
wiki=json.loads((ROOT/'examples/wiki-memory/project-wiki-memory-starter.json').read_text())
if wiki.get('schema_version') != '1.0.0': errors.append('wiki memory schema version missing')
entity_ids={e['id'] for e in wiki.get('entities',[])}
if len(entity_ids) != len(wiki.get('entities',[])): errors.append('duplicate wiki entity IDs')
claim_ids={c['id'] for c in wiki.get('claims',[])}
if len(claim_ids) != len(wiki.get('claims',[])): errors.append('duplicate wiki claim IDs')
for claim in wiki.get('claims',[]):
    if claim.get('evidence_class') not in {'Observed','Derived','Assumed','Unknown'}:
        errors.append(f"invalid evidence class: {claim.get('id')}")
for rel in wiki.get('relationships',[]):
    if rel.get('from') not in entity_ids or rel.get('to') not in entity_ids:
        errors.append(f'invalid wiki relationship: {rel}')
for key in ['agents','agent_runs','spawn_events','ethics_reviews']:
    if key not in wiki: errors.append(f'wiki memory lacks {key}')
if not all(a.get('ethics_required') for a in wiki.get('agents',[])):
    errors.append('all agents must require ethics')
engineering=next((a for a in wiki.get('agents',[]) if a.get('id')=='agent:engineering-director'),{})
if engineering.get('discipline_agent_count',0) < 30:
    errors.append('engineering agent bench is not multidisciplinary enough')
if len(engineering.get('specialties',[])) != engineering.get('discipline_agent_count'):
    errors.append('engineering discipline count does not match specialties')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('PASS: 9 skills, application phases, MOXIE packet, ethical agents, and wiki memory validated')
