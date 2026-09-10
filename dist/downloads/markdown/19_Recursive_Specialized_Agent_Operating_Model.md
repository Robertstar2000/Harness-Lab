# Recursive Specialized Agent Operating Model

## Purpose

Define the specialized agents required to run the Science, Engineering, and Project Management domains of the Mars Harness. Agents are assignments against durable skill contracts. They may create bounded child agents when parallel work, domain depth, or independent verification is needed.

## Command structure

The Mission Harness Director receives the authorized mission objective. It maintains the shared baseline, routes work among the three domain leads, invokes independent ground-truth review, and sends consequential decisions to the human Mission Authority.

Every spawned agent receives: a unique task ID; one accountable parent; scope and exclusions; authoritative inputs; required tools; a typed output contract; evidence and provenance rules; time, compute, and cost limits; an approval boundary; and a stop or escalation condition. A child may spawn descendants only when its delegation permit says `may_spawn: true`. Maximum default depth is three levels below a domain lead. No child may expand its parent's authority.

## Science domain

### Science Domain Lead

Owns the research question, evidence plan, hypothesis portfolio, scientific baseline, uncertainty register, peer-review response, and Engineering Evidence Package. It may spawn:

1. Research Question and Scope Agent — converts the mission need into answerable questions, variables, boundaries, and success criteria.
2. Literature and Source Intelligence Agent — searches primary sources, records provenance, maps conflicting findings, and maintains the evidence ledger.
3. Hypothesis and Causal Model Agent — creates competing hypotheses, causal graphs, predicted observations, and falsification conditions.
4. Experiment Design Agent — defines controls, factors, sample sizes, instrumentation, procedures, and acceptance thresholds.
5. Simulation and Scientific Modeling Agent — builds mathematical or computational models, runs sensitivities, and labels calibration limits.
6. Data Steward and Statistics Agent — validates datasets, preserves lineage, selects analyses, quantifies uncertainty, and checks reproducibility.
7. Scientific Visualization Agent — produces evidence plots, uncertainty views, experiment workflows, and decision-focused figures without concealing limitations.
8. Independent Scientific Reviewer — challenges methods, calculations, source quality, alternative explanations, and overclaiming; it cannot approve its own work.
9. Science Synthesis and Handoff Agent — assembles findings, unresolved questions, operating envelopes, equations, distributions, and minimum additional tests into the Engineering Evidence Package.

Conditional children include planetary-geology, atmospheric-chemistry, materials-science, radiation, life-sciences, instrumentation, and replication agents.

## Engineering domain

### Engineering Domain Lead

Owns the controlled technical baseline from ConOps through verification and release. It may spawn:

1. ConOps and Stakeholder Needs Agent.
2. Requirements and Traceability Agent.
3. Systems Architecture and Interface Agent.
4. Trade Study and Decision Analysis Agent.
5. Discipline Engineering Coordinator.
6. Modeling, Simulation, and Digital Twin Agent.
7. Safety, Reliability, and FMEA Agent.
8. Verification and Validation Agent.
9. Manufacturing, Integration, and Operations Agent.
10. Configuration and Release Agent.
11. Independent Design Review Agent.

The Discipline Engineering Coordinator creates mechanical, electrical, software, controls, thermal, structures, power, communications, human-factors, or ISRU children as required. When evidence is insufficient, the Engineering Lead creates a Research Request Package for Science. It may not convert an unknown into an assumed requirement without recorded human approval.

## Project Management domain

### Program Domain Lead

Owns authorized scope, integrated execution, performance measurement, governance, and closeout. It may spawn:

1. Charter, Scope, and Governance Agent.
2. WBS and Deliverables Agent.
3. Schedule and Critical Path Agent.
4. Resource and Capacity Agent.
5. Cost and Earned Value Agent.
6. Risk and Opportunity Agent.
7. Quality and Acceptance Agent.
8. Change and Configuration Coordination Agent.
9. Communications and Status Agent.
10. Procurement and Partner Agent.
11. Closure and Lessons Agent.

Program agents coordinate work but cannot approve scientific truth, technical adequacy, or safety risk for the domain authorities.

## Cross-domain controls

- Ground Truth Gatekeeper — independently checks claims, calculations, acceptance criteria, and provenance.
- Mission Memory Steward — maintains append-only facts, decisions, versions, supersession links, review dates, and retrieval context.
- Safety and Ethics Governor — blocks unsafe, unauthorized, privacy-violating, or irreversible external action.
- Integration and Dependency Broker — manages typed handoffs, unresolved interfaces, dependencies, and return loops.
- Human Mission Authority — approves mission intent, residual risk, baselines, resources, external actions, and final release.

## Recursive spawning protocol

1. Prove delegation is necessary and check for an existing capable agent.
2. Create a task packet with scope, inputs, output schema, evidence rules, tools, budget, deadline, risks, and stop conditions.
3. Require the child to acknowledge the contract and declare any further spawning.
4. Return results to the accountable parent and write approved artifacts to shared mission memory.
5. Integrate conflicts at the parent, which remains accountable.
6. Assign independent review to an agent that did not create the work.
7. Promote, return, block, or escalate through the domain lead. Only authorized humans approve consequential execution.

## Default limits

- Maximum recursive depth: domain lead plus three descendant levels.
- Maximum active children per agent: five unless the Mission Harness Director authorizes more.
- No orphan agents; every agent has one accountable parent.
- Permissions can only narrow during delegation.
- No self-approval for consequential work.
- Stop on missing evidence, conflicting baselines, exceeded limits, safety concern, or ambiguous authority.

## Core flow

Mission Authority → Mission Harness Director → Science Evidence Package → Engineering Controlled Baseline → Program Execution Baseline → Verification and Acceptance → Operations Evidence → Science or Engineering update.

