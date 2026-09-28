# Engineering Harness Setup Instructions

## Purpose

Set up the Mars Harness Lab engineering domain so a team can turn approved evidence into requirements, architectures, models, schematics, verification plans, and a controlled technical baseline.

This setup uses the downloadable skills and agents already published with the site.

## Required Downloads

Download these files from the Mars Harness Lab downloads area:

| Item | File | Purpose |
| --- | --- | --- |
| Complete agent suite | `downloads/Mars_Harness_Agents_V5_1_Complete.zip` | All agent souls, instructions, manifests, and license files |
| Complete skill suite | `downloads/Mars_Harness_Skills_V5_1_Complete.zip` | All portable skills and work-product contracts |
| Engineering skill | `downloads/intelligent-engineer-harness.zip` | Main engineering lifecycle procedure |
| Vibe engineering skill | `downloads/vibe-engineering-collaboration.zip` | Reversible build increments, tests, and rollback |
| 3D modeling skill | `downloads/mars-3d-modeling-harness.zip` | 3D images, editable geometry, STL, mesh checks, and printability |
| Schematic and parts skill | `downloads/paired-schematic-parts-harness.zip` | Schematic/BOM synchronization and rule checks |
| Ground truth skill | `downloads/ground-truth-gatekeeper.zip` | Independent validation and promotion control |
| Mission memory skill | `downloads/mission-memory-steward.zip` | Versioned requirements, configurations, decisions, and review triggers |
| Ethical specialist skill | `downloads/ethical-specialist-agent-network.zip` | Bounded specialist spawning and ethical supervision |
| Systems director agent | `downloads/agents/intelligent-engineer-systems-director.zip` | Accountable engineering-domain lead |
| Vibe engineering agent | `downloads/agents/vibe-engineering-collaboration-lead.zip` | Build-collaboration lead |
| 3D model agent | `downloads/agents/mars-3d-model-engineer.zip` | Geometry and STL specialist |
| Schematic parts agent | `downloads/agents/schematic-parts-configuration-engineer.zip` | Schematic/BOM specialist |
| Ground truth agent | `downloads/agents/ground-truth-gatekeeper.zip` | Independent reviewer |
| Memory steward agent | `downloads/agents/mission-memory-steward.zip` | Durable project memory custodian |
| Ethics governor agent | `downloads/agents/ethical-specialist-network-governor.zip` | Delegation and safety controller |

## Recommended Setup Order

1. Create a project folder named `engineering-harness`.
2. Unzip the complete skill suite into `engineering-harness/skills`.
3. Unzip the complete agent suite into `engineering-harness/agents`.
4. Copy the approved `EngineeringEvidencePackage/v1` from the science harness into `engineering-harness/inputs`.
5. Open `skills/intelligent-engineer-harness/SKILL.md` first.
6. Open `agents/intelligent-engineer-systems-director/INSTRUCTIONS.md` and `SOUL.md`.
7. Load the supporting skills in this order:
   - `vibe-engineering-collaboration`
   - `mars-3d-modeling-harness`
   - `paired-schematic-parts-harness`
   - `ground-truth-gatekeeper`
   - `mission-memory-steward`
   - `ethical-specialist-agent-network`
8. Assign the human technical authority and review board before any baseline can be released.

## Agent Roles

| Role | Agent | Main responsibility |
| --- | --- | --- |
| Domain lead | Intelligent Engineer Systems Director | Owns requirements, architecture, interfaces, design, and release |
| Build lead | Vibe Engineering Collaboration Lead | Runs small, reversible engineering increments with tests |
| Geometry specialist | Mars 3D Model Engineer | Produces geometry packages, STL, dimensions, and mesh evidence |
| Schematic specialist | Schematic and Parts Configuration Engineer | Keeps schematic, BOM, references, quantities, and rule checks synchronized |
| Reviewer | Ground Truth Gatekeeper | Checks evidence, configuration, calculations, and promotion readiness |
| Memory steward | Mission Memory Steward | Persists approved requirements, baselines, decisions, and IDs |
| Ethics controller | Ethical Specialist Network Governor | Approves narrow specialist spawning and retires access |

## Phase Configuration

Use the Intelligent Engineer Harness phases as the control spine:

1. Concept and mission objective.
2. Requirements and constraints.
3. Architecture and interface definition.
4. Trade studies and preliminary design.
5. Critical design and configuration baseline.
6. Artifact branches for geometry, schematic, parts, and software as needed.
7. Verification and validation planning.
8. Integration and test readiness.
9. Release decision and residual risk.
10. Operational feedback and change control.

For each phase, require:

- Input evidence package and baseline version.
- Requirements trace to source claims.
- Configuration ID.
- Acceptance criteria.
- Ground truth review.
- Human technical approval.
- Memory write.

## Minimum Work Products

Produce these artifacts before handoff:

| Work product | Required content |
| --- | --- |
| Requirements baseline | IDs, source evidence, rationale, verification method, owner, and status |
| Architecture record | Subsystems, interfaces, assumptions, constraints, and trade decisions |
| Risk and hazard log | Severity, likelihood, mitigation, verification, residual risk, and owner |
| Geometry package | Editable source, units, dimensions, STL if needed, mesh checks, and printability limits |
| Schematic parts package | Schematic, reference designators, BOM, quantities, ratings, and reconciliation status |
| Verification plan | Tests, analyses, inspections, acceptance thresholds, tools, and evidence records |
| Controlled technical baseline | Approved configuration, decisions, open issues, release state, and rollback path |

## Validation Gates

Do not promote the engineering baseline until all of these are true:

- Every requirement traces to evidence, authority, or an explicitly approved assumption.
- Geometry, schematic, BOM, software, and test records use stable configuration IDs.
- Calculations and modeled outputs are labeled with assumptions and limits.
- Safety, reliability, and compliance claims are reviewed independently.
- Ground Truth Gatekeeper returns pass or conditional pass.
- The human technical authority approves the release or handoff.

## Output Handoff

The final output is:

`ControlledTechnicalBaseline/v1`

Pass this package to the project management harness. It should include requirements, configuration IDs, WBS-ready deliverables, acceptance criteria, verification tasks, risks, dependencies, resources, and unresolved research requests.

If engineering exposes a science blocker, return:

`ResearchRequestPackage/v1`

Send that package back to the science harness with the exact variable, requirement, decision impact, and evidence needed.

## Quick Start Prompt

Use this prompt with the installed engineering director:

```text
You are the Intelligent Engineer Systems Director for this project. Use the Intelligent Engineer Harness, Vibe Engineering Collaboration, Mars 3D Modeling Harness, Paired Schematic + Parts Harness, Ground Truth Gatekeeper, Mission Memory Steward, and Ethical Specialist Agent Network. Start from the approved EngineeringEvidencePackage/v1. Build a requirements baseline, architecture, technical baseline, verification plan, and any required geometry or schematic packages. Do not promote a baseline without independent review and human technical approval. Return a ControlledTechnicalBaseline/v1 when ready.
```

