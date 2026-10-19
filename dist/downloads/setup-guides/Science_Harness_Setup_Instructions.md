# Science Harness Setup Instructions

## Required operational methods — V5.2

Download [Operational Methods V5.2](https://mars-harness-lab-v5.tallman-equi-9130.chatgpt.site/downloads/Mars_Harness_Operational_Methods_V5_2.zip). The combined setup ZIP already includes the same files under `operational-methods/`; complete skill/agent suites include them under `skills/operational-methods/`.

1. Load `README.md`, `CAPABILITY_COVERAGE.json`, and the selected role contract along with the original skill and agent instructions.
2. Read methods 01 (bounded reasoning), 02 (graph memory), 03 (outline-driven reports), 05 (experiments/simulation/twins), and 06 (independent challenge).
3. Start with the science question and bounded hypothesis alternatives. Complete a simulation/study template before using a solver, preserve calibration/validation separation, select decision-relevant experiments, and draft the report from its approved TOC.
4. Copy and fill the applicable JSON templates. Do not treat example or template records as completed evidence or authority.
5. With Python 3.10+, run `python -m unittest discover -s tests -v` from the extracted operational-methods directory. Follow its README for individual graph, impact, tree, parts, document, handoff, policy, and hash commands.
6. Test available tools in your chosen runtime with a harmless local example. Attach only approved project data. Document missing capabilities and preserve human approval gates.
7. Record actual tool outputs, versions, unresolved findings, and acceptance results before passing a packet to the next harness.

The procedures are included; native SaaS handoffs, production GraphRAG, CAD/EDA, solvers, telemetry, and permission enforcement still require project-specific implementation and tests. This download update does not deploy those services or alter any installed personal skills.

## Purpose

Set up the Mars Harness Lab science domain so a team can run the scientific method with bounded agents, traceable evidence, human review, and an engineering-ready handoff.

This setup uses the downloadable skills and agents already published with the site.

## Required Downloads

Download these files from the Mars Harness Lab downloads area:

| Item | File | Purpose |
| --- | --- | --- |
| Complete agent suite | `downloads/Mars_Harness_Agents_V5_1_Complete.zip` | All agent souls, instructions, manifests, and license files |
| Complete skill suite | `downloads/Mars_Harness_Skills_V5_1_Complete.zip` | All portable skills and work-product contracts |
| Science skill | `downloads/hypatia-science-harness.zip` | Main science-domain operating procedure |
| Research synthesis skill | `downloads/hyperia-research-synthesis.zip` | Literature review, claim synthesis, and evidence mapping |
| Ground truth skill | `downloads/ground-truth-gatekeeper.zip` | Independent validation and promotion control |
| Mission memory skill | `downloads/mission-memory-steward.zip` | Versioned facts, sources, decisions, and review triggers |
| Ethical specialist skill | `downloads/ethical-specialist-agent-network.zip` | Bounded specialist spawning and ethical supervision |
| Science director agent | `downloads/agents/hypatia-science-director.zip` | Accountable science-domain lead |
| Research synthesist agent | `downloads/agents/hyperia-research-synthesist.zip` | Evidence and source specialist |
| Ground truth agent | `downloads/agents/ground-truth-gatekeeper.zip` | Independent reviewer |
| Memory steward agent | `downloads/agents/mission-memory-steward.zip` | Durable project memory custodian |
| Ethics governor agent | `downloads/agents/ethical-specialist-network-governor.zip` | Delegation and safety controller |

## Recommended Setup Order

1. Create a project folder named `science-harness`.
2. Unzip the complete skill suite into `science-harness/skills`.
3. Unzip the complete agent suite into `science-harness/agents`.
4. Copy the project memory starter into `science-harness/memory`.
5. Open `skills/hypatia-science-harness/SKILL.md` first.
6. Open `agents/hypatia-science-director/INSTRUCTIONS.md` and `SOUL.md`.
7. Load the supporting skills in this order:
   - `hyperia-research-synthesis`
   - `ground-truth-gatekeeper`
   - `mission-memory-steward`
   - `ethical-specialist-agent-network`
8. Assign the human project owner as final authority before any artifact can be promoted.

## Agent Roles

| Role | Agent | Main responsibility |
| --- | --- | --- |
| Domain lead | Hypatia Science Director | Runs the science workflow and owns the Engineering Evidence Package |
| Evidence specialist | Hyperia Research Synthesist | Finds, compares, and traces sources and claims |
| Reviewer | Ground Truth Gatekeeper | Checks facts, provenance, calculations, uncertainty, and promotion readiness |
| Memory steward | Mission Memory Steward | Persists validated facts, decisions, source IDs, and review dates |
| Ethics controller | Ethical Specialist Network Governor | Approves narrow specialist spawning and retires access |

## Phase Configuration

Use the Hypatia Science Harness phases as the control spine:

1. Research question and scope.
2. Evidence discovery and source ledger.
3. Competing hypotheses.
4. Study or experiment design.
5. Data acquisition or simulation plan.
6. Analysis plan and assumptions.
7. Results interpretation.
8. Robustness and uncertainty review.
9. Peer critique and dissent capture.
10. Engineering Evidence Package handoff.

For each phase, require:

- Inputs with source and owner.
- Expected output format.
- Human approval condition.
- Ground truth check.
- Memory write.
- Open questions and blocked claims.

## Minimum Work Products

Produce these artifacts before handoff:

| Work product | Required content |
| --- | --- |
| Claim ledger | Observed, derived, assumed, unknown, and blocked claims |
| Source ledger | Source title, URL or file ID, date accessed, claim supported, and confidence |
| Study plan | Method, variables, units, assumptions, controls, and expected evidence |
| Analysis record | Calculations, code or formulas, data quality notes, and reviewer status |
| Peer critique | Weaknesses, dissent, alternative explanations, and residual uncertainty |
| Engineering Evidence Package | Approved claims, constraints, uncertainties, risks, and open research questions |

## Validation Gates

Do not promote the science package until all of these are true:

- Each important claim has a source or is clearly marked as assumed or unknown.
- Units and time bases are explicit.
- Modeled values are not described as observed results.
- Dissent and uncertainty are recorded.
- Ground Truth Gatekeeper returns pass or conditional pass.
- The human authority approves the handoff.

## Output Handoff

The final output is:

`EngineeringEvidencePackage/v1`

Pass this package to the engineering harness. It should include approved claims, evidence classes, uncertainty, applicability limits, unresolved questions, and the exact research requests that engineering may need to return.

## Quick Start Prompt

Use this prompt with the installed science director:

```text
You are the Hypatia Science Director for this project. Use the Hypatia Science Harness, Hyperia Research Synthesis, Ground Truth Gatekeeper, Mission Memory Steward, and Ethical Specialist Agent Network. Begin with a research charter. Build a claim ledger and source ledger. Mark every claim as observed, derived, assumed, unknown, or blocked. Do not promote work without independent review and human approval. Return an EngineeringEvidencePackage/v1 when ready.
```
