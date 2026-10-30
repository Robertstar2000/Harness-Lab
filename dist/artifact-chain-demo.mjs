// Apache-2.0. Illustrative state machine only. No live model, storage or approval service.
export function initial(){return {phase:'baseline',revision:1,science:'r1 approved',engineering:'r1 approved; science r1',project:'r1 approved; engineering r1',baseline:'B1 approved',log:'All stages consume pinned approved revisions.'};}
export function transition(state,action){
 const s={...state};
 if(action==='reset')return initial();
 if(action==='detect'&&s.phase==='baseline')return {...s,phase:'blocked',engineering:'r1 historical; dependent work stale',project:'r1 blocked; maintenance assumption unsupported',baseline:'B1 preserved; correction branch C1 open',log:'Project execution opens issue I1. Engineering triage routes a bounded lifetime-evidence request to science. Dependent promotion pauses.'};
 if(action==='revise'&&s.phase==='blocked')return {...s,phase:'review',revision:s.revision+1,science:`r${s.revision+1} draft; supersedes r1 if approved`,log:'A new illustrative science revision awaits independent review. Draft evidence cannot release dependent work.'};
 if(action==='reject'&&s.phase==='review')return {...s,phase:'blocked',science:`r${s.revision} rejected; r1 historical`,log:'Review rejects the draft revision. The issue remains open and the branch stays blocked. No approval or budget is invented.'};
 if(action==='approve'&&s.phase==='review')return {...s,phase:'rebuild',science:`r${s.revision} approved in this simulation`,log:'A simulated independent review accepts the revised science artifact. Engineering and project outputs remain stale until regenerated.'};
 if(action==='rebuild'&&s.phase==='rebuild')return {...s,phase:'ready',engineering:`r2 checked; science r${s.revision}`,project:'r2 checked; engineering r2',log:'Engineering revises the maintenance design. Project execution recomputes affected resources and schedule. All required checks are simulated as passed.'};
 if(action==='promote'&&s.phase==='ready')return {...s,phase:'published',baseline:'B2 approved in this simulation; B1 retained',log:`The coherent B2 manifest pins science r${s.revision}, engineering r2 and project r2. Issue I1 closes with links to the correction and checks. No real system changed.`};
 return {...s,log:'Transition refused: prerequisites are not satisfied. The baseline is unchanged.'};
}
if(typeof document!=='undefined'){
 let state=initial();const ids=['detect','revise','reject','approve','rebuild','promote','reset'];const allowed={baseline:['detect','reset'],blocked:['revise','reset'],review:['reject','approve','reset'],rebuild:['rebuild','reset'],ready:['promote','reset'],published:['reset']};
 function draw(){for(const k of ['science','engineering','project','baseline'])document.getElementById(k+'-state').textContent=state[k];document.getElementById('event-log').textContent=state.log;for(const id of ids)document.getElementById(id).disabled=!allowed[state.phase].includes(id);}
 for(const id of ids)document.getElementById(id).addEventListener('click',()=>{state=transition(state,id);draw();});draw();
}
