"""Apache-2.0. Local reference controls; NOT a sandbox or production loop."""
import copy, hashlib, json, re, math

class Blocked(RuntimeError): pass

def redact(value, secrets=()):
    if isinstance(value, dict):
        return {k: ('[REDACTED]' if re.search(r'password|secret|authorization|api[_-]?key|token$',k,re.I) else redact(v,secrets)) for k,v in value.items()}
    if isinstance(value, list): return [redact(v,secrets) for v in value]
    if not isinstance(value,str): return value
    for s in sorted(filter(None,secrets),key=len,reverse=True): value=value.replace(s,'[REDACTED]')
    value=re.sub(r'-----BEGIN [^-]*PRIVATE KEY-----.*?-----END [^-]*PRIVATE KEY-----','[REDACTED PRIVATE KEY]',value,flags=re.S)
    return re.sub(r'\b(?:sk_live_|sk_test_|rk_live_|github_pat_|ghp_)[A-Za-z0-9_]+','[REDACTED]',value)

def bounded_observation(call_id, exit_status, stdout, stderr, limit=16384, secrets=()):
    if limit<1: raise ValueError('positive byte limit required')
    raw=json.dumps(redact({'stdout':stdout,'stderr':stderr},secrets),ensure_ascii=False)
    data=raw.encode(); excerpt=data[:limit].decode('utf-8',errors='ignore')
    return dict(call_id=call_id,exit_status=exit_status,stdout=redact(stdout,secrets).encode()[:limit//2].decode('utf-8',errors='ignore'),stderr=redact(stderr,secrets).encode()[:limit//2].decode('utf-8',errors='ignore'),excerpt=excerpt,truncated=len(data)>limit,full_artifact_sha256=hashlib.sha256(data).hexdigest())

class Guard:
    def __init__(self,policy,start=0):
        self._policy=copy.deepcopy(policy); self.start=start
        self.turns=self.tokens=self.cost=self.errors=0; self.termination_reason=None
    def begin(self,now,reserve_tokens,reserve_cost):
        p=self._policy
        if not math.isfinite(now) or any(v is not None and (not isinstance(v,(int,float)) or not math.isfinite(v)) for v in (reserve_tokens,reserve_cost)):
            self.termination_reason='invalid_usage'; raise Blocked('invalid_usage')
        reason=('wall_clock_limit' if now-self.start>=p['wall_seconds'] else
                'format_error_limit' if self.errors>=p['max_format_errors'] else
                'turn_limit' if self.turns>=p['max_turns'] else
                'usage_unknown' if reserve_tokens is None or reserve_cost is None else
                'token_limit' if self.tokens+reserve_tokens>p['max_tokens'] else
                'cost_limit' if self.cost+reserve_cost>p['max_cost_usd'] else None)
        if reason: self.termination_reason=reason; raise Blocked(reason)
        if reserve_tokens<0 or reserve_cost<0: raise ValueError('negative reservation')
        self.turns+=1; self.tokens+=reserve_tokens; self.cost+=reserve_cost
        # Conservative reservations remain charged; never undercount missing usage.
    def authorize(self,tool,parent_allow=()):
        p=self._policy
        allowed=tool in p['allow_tools'] and tool in parent_allow and tool not in p['deny_tools']
        return {'allowed':allowed,'rule_id':p['rule_id'],'policy_version':p['version']}
    def response(self,valid): self.errors=0 if valid else self.errors+1

def replay(trace):
    if trace['schema_version']!='RunTrace/v1': raise ValueError('unsupported trace')
    seen=set(); observations=[]
    for e in trace['events']:
        if e['kind']=='tool_call':
            if e['call_id'] in seen: raise ValueError('duplicate call')
            seen.add(e['call_id'])
        elif e['kind']=='observation':
            if e['call_id'] not in seen: raise ValueError('orphan observation')
            observations.append(e['result']);seen.remove(e['call_id'])
    if seen: raise ValueError('missing observations')
    return observations # never invokes tools

def migrate(state):
    result=copy.deepcopy(state); result['schema_version']='mars-state/1.1'
    result['migration']={'from':state['schema_version'],'original_sha256':hashlib.sha256(json.dumps(state,sort_keys=True).encode()).hexdigest()}
    return result
