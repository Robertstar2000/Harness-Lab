---
name: pm-accelerator-harness
description: Run the HMAP-style project lifecycle from intake and proposal through planning, agentic task execution, monitoring, change propagation, review readiness, and evidence-based closure.
---

<!--
Copyright 2026 Mars Harness Lab contributors
SPDX-License-Identifier: Apache-2.0
Complete license text: https://mars-harness-lab-v5.tallman-equi-9130.chatgpt.site/license/
-->

# PM Accelerator Harness

## Purpose

Reproduce the Project Management Accelerator pattern: convert an approved technical baseline into executable work, coordinate non-physical deliverables, manage change across the document set, and close work using evidence. Use for charters, plans, WBS, schedules, resources, budgets, risks, dashboards, notifications, and controlled change. Do not independently authorize engineering, safety, procurement, or operations decisions.

## Inputs

- Approved objective and technical baseline
- Sponsor, project manager, decision rights, stakeholders, and team roles
- Deliverables, constraints, assumptions, dependencies, dates, and budget limits
- Acceptance criteria, review calendar, communication rules, and risk tolerance
- Existing plans, documents, actuals, changes, and lessons

## Application modes

- `Plan`: Plan Agent → Context Memory → Human Alignment → Approved Documents.
- `Execute`: Doer Agent → Tools/Retrieval Agent → Tester Agent.
- `Change`: Change Agent → Surgical Revision → QA Agent.

## Decision loop

The PM Accelerator Program Director may assign Charter/Stakeholder/Governance, WBS/Schedule/Critical Path, Cost/Resource/Procurement, Risk/Issue/Change Control, Execution, QA/Testing, Status/Dashboard/Communications, and Closure/Lessons agents. Use the Ethical Specialist Agent Network spawn contract. Children inherit authorization, budget, data, ethics, change-control, and stop limits; they cannot authorize their own work or conceal adverse status.

Plan or revise → validate dependencies and authority → execute bounded work → test acceptance criteria → repair or escalate → approve → persist. Status must be derived from work-product evidence rather than optimism.

## Application phases

### 1. Intake and project framing

1. Define problem, outcome, sponsor, manager, beneficiaries, exclusions, and success measures.
2. Select project type, lifecycle, risk tier, governance, and required documents.
3. Identify legal, safety, technical, financial, data, and external dependencies.
4. Load authoritative context into wiki-style memory.
5. Approve intake before proposal generation.

Outputs: intake record, context inventory, governance profile.

### 2. Proposal and charter

1. Generate mission case, alternatives, benefits, costs, risks, and recommendation.
2. Define scope, objectives, deliverables, milestones, budget envelope, and authority.
3. Identify assumptions requiring validation and decisions requiring approvers.
4. Critique feasibility against the technical baseline.
5. Obtain sponsor approval and persist the charter.

Outputs: proposal, charter, approval record.

### 3. Integrated planning

1. Decompose deliverables into a unique, non-duplicated WBS.
2. Give each work package an owner, inputs, outputs, effort, duration, dependencies, acceptance tests, and evidence.
3. Build network logic, milestones, critical path, float, calendars, and gates.
4. Estimate labor, facilities, equipment, materials, procurement, reserves, and cash flow.
5. Establish risk, issue, assumption, decision, change, communication, quality, configuration, and verification plans.
6. Run resource-leveling and what-if scenarios before baseline approval.

Outputs: integrated plan and approved scope/cost/schedule baseline.

### 4. Work authorization and readiness

1. Confirm predecessor completion, inputs, tools, permissions, and owner availability.
2. Verify measurable acceptance criteria.
3. Flag external, hazardous, financial, or physical actions for human authorization.
4. Issue context-rich notifications when work becomes ready.
5. Record authorization, start conditions, and planned evidence.

Outputs: authorized queue and readiness record.

### 5. Agentic task execution

1. Doer Agent creates the non-physical deliverable from the approved work package.
2. Tools Agent supplies only current project context and approved sources.
3. Tester Agent checks completeness, accuracy, traceability, consistency, and acceptance criteria.
4. Repair within the configured iteration budget; default maximum is 20 cycles.
5. Escalate blocked dependencies, conflicting authority, unavailable evidence, or repeated failure.

Outputs: deliverable, test record, evidence, and escalation if needed.

### 6. Monitoring and control

1. Collect actual dates, effort, cost, evidence, risks, issues, and forecasts.
2. Calculate milestones and variance from approved baselines.
3. Update Gantt, Kanban, workload, cost, risk, milestone, and verification views from common records.
4. Forecast completion with confidence and data age.
5. Prevent subjective percent-complete from overriding deliverable evidence.

Outputs: status, forecast, dashboards, corrective actions.

### 7. Integrated change management

1. Record trigger, requester, rationale, urgency, and affected baseline items.
2. Change Agent finds impacted requirements, design, WBS, schedule, cost, risks, tests, documents, and approvals.
3. Run what-if analysis before commitment.
4. Apply minimal revisions while preserving history and supersession links.
5. QA Agent checks cross-document consistency; repair within a maximum of 50 cycles.
6. Obtain change-authority approval and rebaseline only approved dimensions.

Outputs: change request, impact analysis, decision, revised baseline, QA report.

### 8. Review and decision readiness

1. Assemble evidence for the gate.
2. Verify actions, risk acceptance, ownership, and technical approvals.
3. Separate facts, forecasts, assumptions, and unresolved issues.
4. Record decisions, conditions, dissent, and follow-up owners.
5. Block promotion when evidence or authority is missing.

Outputs: review package and gate decision.

### 9. Closure and learning

1. Confirm deliverable acceptance and requirement/verification closure.
2. Reconcile cost, schedule, contracts, assets, data, access, and obligations.
3. Capture evidence-based lessons with applicability limits.
4. Archive the final baseline and write wiki-memory records.
5. Transfer unresolved work to operations or a follow-on project with ownership.

Outputs: closure report, archive manifest, lessons, transition record.

## Reports and visual artifacts

Generate management reports and visual controls directly from the approved project records.

- Intake and charter reports with stakeholder map, objective hierarchy, governance/RACI chart, and benefits map.
- Integrated project plan with WBS tree, network diagram, Gantt chart, milestone roadmap, resource histogram, cost profile, and risk heat map.
- Work-authorization package with ready/not-ready dashboard, dependency view, owner queue, and acceptance-evidence checklist.
- Execution report with Kanban view, deliverable status, iteration/test history, blocked-work aging, and workload heat map.
- Status and forecast report with schedule/cost variance, milestone trend, critical path, risk exposure, verification burndown, and forecast confidence.
- Change package with impact map, before/after baseline comparison, what-if charts, document impact matrix, and approval status.
- Review and closure reports with decision dashboard, action-aging chart, acceptance matrix, lessons map, and transition checklist.

All dashboards and charts must be reproducible from the same WBS, schedule, cost, risk, verification, and decision records used in the report. Show data date, baseline version, forecast assumptions, and confidence. Do not use invented percentages or visually imply progress without evidence.

## Work-product contract

Every plan item includes unique ID, parent WBS ID, deliverable, accountable owner, contributors, dependencies, planned and actual dates, effort, cost, acceptance criteria, verification evidence, status, confidence, risks, issues, decisions, approvals, linked reports, linked visual artifacts, and memory records.

## PM Accelerator code adapter

The reviewed `backup-2026-09-22` application implements sequential HMAP document locking, manual or automatic Gemini generation, a current in-memory project copy during automatic runs, retry and rate-limit controls, compacted first-document plus immediately previous approved-document context, WBS/plan parsing, and project tracking, testing, workload, team, document, revision, notification, and change views.

Preserve native `Project`, `Document`, `Task`, `Sprint`, `Milestone`, `Resource`, notification, and phase-data IDs. The reviewed tracking source implements four model stages—Extractor, QA, Scheduler, QA—even though interface copy says six-agent synthesis. Add formal authorization/readiness, Doer/Tools/Tester evidence, complete cross-baseline impact analysis, independent review, and closure packets around native records; do not claim those extensions already ran merely because an application status changed.

## Guardrails

Treat speed claims as concept-generation estimates unless supported by measured project data. Do not notify people, change shared systems, authorize work, spend funds, or contact external parties without authority. Do not close work from narrative assurance. Preserve the original baseline and decision history.

## Runtime portability

Map planning, document creation, retrieval, scheduling, notifications, collaboration, dashboards, and memory using `../../docs/PLATFORM_ADAPTERS.md`. When integrations are absent, provide exportable artifacts and disclose the limitation instead of claiming synchronization.
