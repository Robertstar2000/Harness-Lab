"""Apache-2.0. Adversarial local fixtures, no external service calls."""
import json,unittest
from pathlib import Path
from reference_controls import Guard,Blocked,redact,bounded_observation,replay,migrate
C=Path(__file__).parent
class Controls(unittest.TestCase):
 def setUp(self): self.p=json.loads((C/'policy.json').read_text())
 def test_caps(self):
  for field,value,reason in [('max_turns',0,'turn_limit'),('max_tokens',0,'token_limit'),('max_cost_usd',0,'cost_limit'),('wall_seconds',0,'wall_clock_limit')]:
   p=dict(self.p);p[field]=value;g=Guard(p)
   with self.assertRaisesRegex(Blocked,reason):g.begin(0,1,1)
   self.assertEqual(g.termination_reason,reason)
 def test_format_streak(self):
  g=Guard(self.p)
  for i in range(3):g.response(False)
  with self.assertRaisesRegex(Blocked,'format_error_limit'):g.begin(0,1,1)
  g.response(True);g.begin(0,1,1)
 def test_usage_missing(self):
  with self.assertRaisesRegex(Blocked,'usage_unknown'):Guard(self.p).begin(0,None,None)
 def test_frozen_deny_and_parent_intersection(self):
  g=Guard(self.p);self.p['allow_tools'].append('shell')
  self.assertFalse(g.authorize('shell',['shell'])['allowed'])
  p=dict(self.p);g=Guard(p)
  self.assertFalse(g.authorize('shell',[])['allowed']);self.assertTrue(g.authorize('shell',['shell'])['allowed'])
 def test_redact_before_bounding(self):
  text='known-secret sk_live_abc123'
  self.assertNotIn('known-secret',json.dumps(redact({'result':text},['known-secret'])))
  self.assertEqual(redact({'api_key':'anything'})['api_key'],'[REDACTED]')
  o=bounded_observation('a',1,'é'*100,'failure',20)
  self.assertLessEqual(len(o['excerpt'].encode()),20);self.assertTrue(o['truncated']);self.assertEqual(o['exit_status'],1)
 def test_replay_no_side_effects(self):
  trace={'schema_version':'RunTrace/v1','events':[{'kind':'tool_call','call_id':'a'},{'kind':'observation','call_id':'a','result':'recorded'}]}
  self.assertEqual(replay(trace),['recorded'])
  trace['events'].pop(0)
  with self.assertRaisesRegex(ValueError,'orphan'):replay(trace)
 def test_migration_preserves_safety_and_unknown(self):
  s={'schema_version':'old','policy':{'deny':['network']},'custom':{'a':1}}
  n=migrate(s);self.assertEqual(n['policy'],s['policy']);self.assertEqual(n['custom'],s['custom']);self.assertEqual(s['schema_version'],'old')
 def test_invalid_usage(self):
  for value in [float('nan'),float('inf')]:
   with self.assertRaisesRegex(Blocked,'invalid_usage'):Guard(self.p).begin(0,1,value)
 def test_all_requirements(self):
  rows=json.loads((C/'requirements.json').read_text())['requirements'];self.assertEqual(len(rows),97);self.assertEqual(len({r['id'] for r in rows}),97)
  for r in rows:self.assertTrue(r['remediation']);self.assertTrue((C/r['evidence'].split('#')[0]).is_file())
if __name__=='__main__':unittest.main()
