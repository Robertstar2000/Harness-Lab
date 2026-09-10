---
name: intelligent-engineer-harness
description: Run evidence-controlled systems engineering through concept, requirements, architecture, preliminary design, critical design, integration, verification, release, and operational feedback phases.
---

# Intelligent Engineer Harness

## Purpose

Reproduce the Intelligent Engineer Pro pattern: convert an approved evidence package into a traceable, configuration-controlled physical-system baseline and advance it through review gates. Use for multidisciplinary engineering, requirements, trades, DFMA/FMEA, interfaces, verification, and controlled releases. Never use unsupported assumptions as facts or treat AI analysis as physical qualification.

## Inputs

- Approved Engineering Evidence Package and evidence bounds
- Mission need, concept of operations, stakeholders, and authority
- Standards, constraints, interfaces, hazards, resources, and schedule
- Risk classification and required review gates
- Existing baseline, configuration ID, and change history

## Phase workspace rule

Create a separate workspace and baseline for each phase. Lock an approved phase. Later phases may reference but not silently rewrite it. Every revision needs a change request, impact analysis, approval, and supersession links.

## Decision loop

The Intelligent Engineer Systems Director may assign lifecycle agents for requirements, architecture, trades, modeling, safety, verification, manufacturing, configuration, review, reports, and visuals. Its 34-role discipline bench covers the major physical, digital, biological, infrastructure, manufacturing, resource, operations, test, safety, and human-centered engineering fields listed in the Engineering Discipline Agent Catalog. Use the Ethical Specialist Agent Network spawn contract. Children inherit the approved baseline, configuration, permissions, ethics, and stop conditions; the director remains accountable for integration.

Read `../docs/ENGINEERING_DISCIPLINE_AGENT_CATALOG.md` before selecting discipline agents or defining their outputs.

Within each phase: establish baseline → analyze → cross-discipline critique → verify → approve or return → persist. Send missing scientific knowledge to Hypatia as a Research Request Package instead of guessing.

## Application phases

### 0. Intake and evidence readiness

1. Verify evidence approval, provenance, units, bounds, and unresolved items.
2. Quarantine unsupported claims.
3. Define system boundary, owner, risk tier, and definition of done.
4. Create assumptions, interfaces, hazards, and uncertainty registers.
5. Pass evidence readiness before requirements authoring.

Outputs: intake record, evidence crosswalk, initial registers.

### 1. Mission need and concept of operations

1. Define users, scenarios, environments, modes, lifecycle, and off-nominal cases.
2. Identify external systems and mission interfaces.
3. Define measures of effectiveness and thresholds.
4. State logistics, maintenance, autonomy, crew, and communications assumptions.
5. Review with science, operations, safety, and program owners.

Outputs: mission-need statement, ConOps, context model, effectiveness measures.

### 2. Requirements baseline

1. Derive stakeholder, system, subsystem, interface, safety, verification, and operational requirements.
2. Give each a unique ID, rationale, source, owner, priority, verification method, and status.
3. Make requirements singular, measurable, bounded, feasible, and solution-neutral where appropriate.
4. Trace backward to evidence and forward to architecture and verification.
5. Check ambiguity, conflict, orphans, duplicates, and unverifiable language before approval.

Outputs: requirements specification and traceability matrix.

### 3. Functional architecture and alternatives

1. Decompose functions, flows, states, interfaces, failure containment, and control authority.
2. Generate materially different alternatives.
3. Evaluate mass, power, thermal, volume, reliability, maintainability, manufacturability, cost, schedule, autonomy, and safety.
4. Normalize criteria and expose weighting sensitivity.
5. Select through an approved trade record.

Outputs: architecture, interface inventory, trade study, decision record.

### 4. Preliminary design

1. Allocate requirements and budgets to subsystems.
2. Build first-order mass, power, thermal, performance, data, consumables, and reliability models.
3. Define preliminary components, materials, software, controls, sensors, and human interfaces.
4. Perform initial hazard analysis and FMEA.
5. Identify technology and test needs before PDR.

Outputs: preliminary design package, margins, risks, and PDR evidence.

### 5. Critical-design sprints

For each unresolved high-risk area:

1. Frame the question and linked requirements.
2. Assemble required disciplines around one configuration snapshot.
3. Produce calculations, models, drawings, tolerances, interfaces, and test evidence.
4. Run DFMA, detailed FMEA, reliability, fault management, maintainability, and operability analysis.
5. Independently recompute consequential values and resolve conflicts.
6. Issue a Research Request Package if evidence is missing.

Outputs: sprint decision package and closed or escalated blocker.

### 6. Critical design baseline

1. Complete detailed artifacts and interface-control documents.
2. Close or disposition requirements, hazards, risks, waivers, and actions.
3. Freeze BOM, software, drawings, models, and analysis versions.
4. Complete the verification cross-reference matrix.
5. Hold CDR and record approval, conditions, dissent, and residual risk.

Outputs: CDR package and controlled design baseline.

### 7. Build, integration, and verification planning

1. Create procurement, build, inspection, integration, test, and calibration plans.
2. Map each requirement to analysis, inspection, demonstration, test, or similarity.
3. Define articles, facilities, instrumentation, data, criteria, and anomaly handling.
4. Sequence interface tests before full-system tests.
5. Require authorization before procurement or physical work.

Outputs: build package, verification plan, integration sequence.

### 8. Verification, validation, and qualification

1. Execute only authorized procedures.
2. Preserve raw results, configuration, deviations, anomalies, and chain of custody.
3. Compare evidence with requirement criteria.
4. Open corrective action for failures; never average away a critical failure.
5. Distinguish verification, operational validation, environmental qualification, and certification.

Outputs: verification reports, anomalies, compliance matrix.

### 9. Release and operational learning

1. Assemble the as-built/as-tested configuration and release evidence.
2. Confirm approvals, training, spares, maintenance, monitoring, and rollback.
3. Transfer owned work, dependencies, costs, schedule, and criteria to PM Accelerator.
4. Capture operational observations and drift.
5. Feed uncertainty to Hypatia and verified lessons to memory.

Outputs: controlled release, operations baseline, next-phase seed.

## Reports and visual artifacts

Produce phase-appropriate engineering reports and review visuals from the same controlled baseline.

- ConOps report with operational sequence, system-context diagram, mode/state diagram, and off-nominal scenarios.
- Requirements report with traceability matrix, requirement hierarchy, verification-method distribution, and orphan/ambiguity dashboard.
- Architecture and trade-study report with functional-flow diagrams, interface diagrams, weighted decision matrix, sensitivity chart, and budget comparisons.
- Preliminary-design report with system block diagrams, mass/power/thermal budgets, margin charts, risk matrix, and initial FMEA visualization.
- Critical-design report with drawings or model views when supported, interface-control graphics, tolerance stacks, DFMA/FMEA tables, reliability block diagrams, fault trees, and multidisciplinary action matrix.
- Verification report with requirement-to-test matrix, test configuration diagram, pass/fail dashboard, anomaly trend plots, and compliance status.
- Release report with as-built/as-tested configuration tree, open-risk summary, operations concept, maintenance flow, and digital-thread handoff map.

Visuals must be generated from versioned requirements, calculations, models, or test data. Label conceptual, modeled, simulated, and tested content distinctly. Preserve source IDs, configuration IDs, units, dates, and calculation references in the artifact metadata.

## Research Request Package

Include request ID; linked requirement and decision; scientific question; candidate mechanisms; variables and ranges; Mars conditions; requested method; data quality; acceptance limit; due date; owner; and consequence of no answer. Pause only the affected decision path.

## Work-product contract

Return human and machine-readable outputs containing baseline ID, phase, configuration, evidence crosswalk, requirements, interfaces, assumptions, analyses, alternatives, margins, hazards, FMEA/DFMA, risks, decisions, verification matrix, anomalies, reports, visual artifacts, approvals, actions, research requests, next-phase seed, memory write, and supersedes links.

## Guardrails

Never fabricate CAD, simulation, test, certification, or supplier results. Mark estimates and modeled outputs explicitly with calculation references. Require human authorization for physical, financial, safety-critical, regulated, production, credential, or external actions. Never rewrite acceptance criteria after seeing a failed result.

## Runtime portability

Map requirements, modeling, code, CAD/PLM, simulation, documentation, and memory capabilities using `../../docs/PLATFORM_ADAPTERS.md`. Missing tools produce a blocked or partial packet, never simulated completion.
