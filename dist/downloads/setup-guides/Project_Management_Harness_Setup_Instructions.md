# Project Management Harness Setup Instructions

## Required operational methods — V5.2

Download [Operational Methods V5.2](https://mars-harness-lab-v5.tallman-equi-9130.chatgpt.site/downloads/Mars_Harness_Operational_Methods_V5_2.zip). The combined setup ZIP already includes the same files under `operational-methods/`; complete skill/agent suites include them under `skills/operational-methods/`.

1. Load `README.md`, `CAPABILITY_COVERAGE.json`, and the selected role contract along with the original skill and agent instructions.
2. Read methods 02 (change impact), 03 (planning documents), 07 (dependencies/handoffs), 08 (policy/replay), and 10 (measurement).
3. Build outline-controlled planning documents and evidence-linked work packages. Route changed prerequisites to affected owners, respect authorization and resource limits, and measure elapsed time, human effort, review, rework, cost, and quality against a comparable baseline.
4. Copy and fill the applicable JSON templates. Do not treat example or template records as completed evidence or authority.
5. With Python 3.10+, run `python -m unittest discover -s tests -v` from the extracted operational-methods directory. Follow its README for individual graph, impact, tree, parts, document, handoff, policy, and hash commands.
6. Test available tools in your chosen runtime with a harmless local example. Attach only approved project data. Document missing capabilities and preserve human approval gates.
7. Record actual tool outputs, versions, unresolved findings, and acceptance results before passing a packet to the next harness.

The procedures are included; native SaaS handoffs, production GraphRAG, CAD/EDA, solvers, telemetry, and permission enforcement still require project-specific implementation and tests. This download update does not deploy those services or alter any installed personal skills.

## Purpose

Set up the Mars Harness Lab project management domain so a team can turn an approved technical baseline into authorized work, schedule, resources, risk control, execution evidence, change control, and closure.

This setup uses the downloadable skills and agents already published with the site.

## Required Downloads

Download these files from the Mars Harness Lab downloads area:

| Item | File | Purpose |
| --- | --- | --- |
| Complete agent suite | `downloads/Mars_Harness_Agents_V5_1_Complete.zip` | All agent souls, instructions, manifests, and license files |
| Complete skill suite | `downloads/Mars_Harness_Skills_V5_1_Complete.zip` | All portable skills and work-product contracts |
| PM skill | `downloads/pm-accelerator-harness.zip` | Main project management operating procedure |
| Mission memory skill | `downloads/mission-memory-steward.zip` | Versioned plans, decisions, risks, changes, and lessons |
| Ground truth skill | `downloads/ground-truth-gatekeeper.zip` | Independent validation and promotion control |
| Ethical specialist skill | `downloads/ethical-specialist-agent-network.zip` | Bounded specialist spawning and ethical supervision |
| PM director agent | `downloads/agents/pm-accelerator-program-director.zip` | Accountable project-domain lead |
| Memory steward agent | `downloads/agents/mission-memory-steward.zip` | Durable project memory custodian |
| Ground truth agent | `downloads/agents/ground-truth-gatekeeper.zip` | Independent reviewer |
| Ethics governor agent | `downloads/agents/ethical-specialist-network-governor.zip` | Delegation and safety controller |
| Mars harness director agent | `downloads/agents/mars-harness-director.zip` | Cross-domain routing and final integration |

## Recommended Setup Order

1. Create a project folder named `project-management-harness`.
2. Unzip the complete skill suite into `project-management-harness/skills`.
3. Unzip the complete agent suite into `project-management-harness/agents`.
4. Copy the approved `ControlledTechnicalBaseline/v1` from the engineering harness into `project-management-harness/inputs`.
5. Open `skills/pm-accelerator-harness/SKILL.md` first.
6. Open `agents/pm-accelerator-program-director/INSTRUCTIONS.md` and `SOUL.md`.
7. Load the supporting skills in this order:
   - `mission-memory-steward`
   - `ground-truth-gatekeeper`
   - `ethical-specialist-agent-network`
   - `mars-harness-orchestrator`
8. Assign the human sponsor, project owner, and technical authority before any work is authorized.

## Agent Roles

| Role | Agent | Main responsibility |
| --- | --- | --- |
| Domain lead | PM Accelerator Program Director | Owns charter, WBS, schedule, resources, execution, change, and closure |
| Cross-domain lead | Mars Harness Director | Routes approved packets across science, engineering, and project domains |
| Reviewer | Ground Truth Gatekeeper | Checks readiness, evidence, acceptance status, and closure claims |
| Memory steward | Mission Memory Steward | Persists plans, owners, decisions, changes, actuals, and lessons |
| Ethics controller | Ethical Specialist Network Governor | Approves narrow specialist spawning and retires access |

## Phase Configuration

Use the PM Accelerator Harness phases as the control spine:

1. Intake and project charter.
2. Scope, stakeholders, and governance.
3. WBS and deliverable decomposition.
4. Schedule, dependencies, and critical path.
5. Cost, resource, procurement, and staffing plan.
6. Risk, issue, assumption, and decision log.
7. Execution tracking and acceptance evidence.
8. Change control and impact propagation.
9. Closure, transition, lessons, and archive.

For each phase, require:

- Approved technical baseline input.
- Owner and authority.
- Acceptance criteria.
- Dependency and risk record.
- Evidence required for completion.
- Ground truth review.
- Memory write.

## Minimum Work Products

Produce these artifacts before execution:

| Work product | Required content |
| --- | --- |
| Project charter | Purpose, scope, authority, success criteria, constraints, and governance |
| WBS | Deliverables, work packages, owners, acceptance criteria, and baseline links |
| Schedule | Dependencies, milestones, critical path, resource assumptions, and float |
| Resource plan | People, tools, facilities, procurement needs, and capacity limits |
| RAID log | Risks, assumptions, issues, decisions, owners, triggers, and status |
| Execution tracker | Tasks, status, actuals, blockers, test evidence, and acceptance records |
| Change log | Change request, affected baselines, cost/schedule/risk impact, and approvals |
| Closure packet | Delivered scope, evidence, exceptions, lessons, transition, and archive state |

## Validation Gates

Do not authorize execution or closure until all of these are true:

- Work packages trace to the approved technical baseline.
- Each task has an owner, acceptance criteria, and evidence requirement.
- Dependencies and blockers are visible.
- Risks, assumptions, issues, and decisions have owners and review dates.
- Changes propagate back to technical and science baselines when needed.
- Ground Truth Gatekeeper returns pass or conditional pass.
- The human sponsor or project authority approves execution or closure.

## Output Handoff

The core output is:

`ProjectExecutionPacket/v1`

Use this package to authorize and track work. It should include WBS, schedule, resources, cost model, RAID records, acceptance criteria, execution evidence, change records, and closure state.

If project execution reveals a technical or science blocker, send a typed change or research request back upstream through the Mars Harness Director.

## Quick Start Prompt

Use this prompt with the installed PM director:

```text
You are the PM Accelerator Program Director for this project. Use the PM Accelerator Harness, Mission Memory Steward, Ground Truth Gatekeeper, Ethical Specialist Agent Network, and Mars Harness Orchestrator. Start from the approved ControlledTechnicalBaseline/v1. Build the charter, WBS, schedule, resource plan, RAID log, execution tracker, change log, and closure packet. Do not authorize work or close work without independent review and human approval. Return a ProjectExecutionPacket/v1 and keep upstream change requests explicit.
```
