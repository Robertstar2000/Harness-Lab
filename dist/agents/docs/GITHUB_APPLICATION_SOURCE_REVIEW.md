<!--
Copyright 2026 Mars Harness Lab contributors
SPDX-License-Identifier: Apache-2.0
-->

# GitHub Source Review — Three Mars Harness SaaS Applications

Reviewed 23 September 2026 for the public `Robertstar2000` repositories. Hypatia Pro and Intelligent Engineer Pro were assessed on `backup-2026-09-22`, because those branches contain the complete current application trees while their `main` branches are sparse following secret-removal work. PM Accelerator was also assessed on its complete `backup-2026-09-22` branch.

This is a source-architecture review, not a security certification or production-readiness approval.

## Source baselines

| Application | Reviewed source | Product pattern |
|---|---|---|
| Hypatia Pro | [backup-2026-09-22](https://github.com/Robertstar2000/Hypatia-Pro/tree/backup-2026-09-22) | Ten-step scientific discovery, data/simulation, review, and publication workflow |
| Intelligent Engineer Pro | [backup-2026-09-22](https://github.com/Robertstar2000/Intelligent-Engineer-Pro/tree/backup-2026-09-22) | Vibe Engineering Partner with phase locking, sprints, reviews, risks, compliance, and exports |
| Project Management Accelerator | [backup-2026-09-22](https://github.com/Robertstar2000/project-management-accelerator/tree/backup-2026-09-22) | HMAP document planning, approved-step context, tracking synthesis, controls, and closure tools |

## 1. Hypatia Pro

### Runtime and persistence

- React 19 + TypeScript + Vite frontend; Express 5 server.
- Google GenAI/Gemini generation, including grounded literature retrieval.
- Dexie/IndexedDB for browser data, with Firestore and Better-SQLite3 integration present in the source set.
- Chart.js, KaTeX, Marked, JSZip, and XLSX for analysis, publication, visualization, and export.

### Control flow observed in code and design files

1. Initialize authentication/API-key guard and restore the latest experiment.
2. Formulate a testable research question under a JSON schema.
3. Choose manual forensic control or agentic reconstruction.
4. Execute steps 2–10: literature review, competing hypotheses, method, data plan, acquisition/simulation, analysis, conclusion, skeptical review, and publication.
5. Require a human `Verify Node` before phase advancement.
6. In the generated-code path, run standalone JavaScript in a sandboxed Web Worker and bound debugger repair attempts at 25.
7. Run CSV/data QA and structured multi-role analysis before interpretation.
8. Export experiment state and results as JSON or ZIP.

### Mars Harness extension

The Mars Harness adds explicit `Observed/Derived/Assumed/Unknown` claim classes, immutable evidence packets, independent promotion review, durable cross-application memory, and a typed `EngineeringEvidencePackage`. These are architectural controls around the application; they must not be represented as native application behavior unless implemented and tested.

## 2. Intelligent Engineer Pro / Vibe Engineering Partner

### Runtime and persistence

- React 19 + TypeScript + Vite + Tailwind; Express 5 backend.
- Gemini text and image generation with retry wrapper and a frontend service bridge to backend-oriented AI functions.
- Firebase/Firestore, SQLite, and local state patterns appear in the reviewed source.
- Versioned phase and sprint outputs, risk/resource/task models, compliance traceability, analytics, change management, and export services.

### Control flow observed in code and design files

1. Create a project from a name, mode, requirements, constraints, compliance choices, and up to three engineering disciplines.
2. Use seven product phases: Requirements, Preliminary Design, Critical Design, Testing, Launch, Operation, and Improvement.
3. Lock future phases; carry approved prior-phase outputs into the next generation context.
4. Use multi-document workflows in Requirements, Preliminary Design, and Testing.
5. In Critical Design, generate a preliminary specification and sprint list; require DFMA/FMEA; accept sprint outputs and merge them into a controlled phase output.
6. Require a human design-review checklist before finalizing an in-review phase.
7. Store versioned outputs and support risk, task, collaboration, compliance, artifact, and project export views.

### Mars Harness extension

The ten-stage engineering harness wraps and refines the seven UI phases: evidence readiness and ConOps precede requirements; architecture and preliminary design refine the design phases; critical sprints and controlled CDR map into Critical Design; build/V&V planning plus verification map into Testing; release and operational learning span Launch, Operation, and Improvement. Native IDs and approved records remain intact. Two bounded artifact branches now attach here: `GeometryPackage/v1` for model-derived images and validated STL delivery, and `SchematicPartsPackage/v1` for a synchronized schematic plus BOM/parts configuration.

## 3. Project Management Accelerator

### Runtime and persistence

- React 19 + TypeScript + Vite + Tailwind; Express 5 server.
- Gemini generation through `@google/genai`, with retry, compacted context, JSON schemas, and rate-limit delays.
- Firebase, SQLite, localStorage/session state, and `BroadcastChannel` same-browser synchronization patterns.
- JSZip exports, authentication utilities, revision control, tracking, testing, workload, document, team, and dashboard views.

### Control flow observed in code and design files

1. Create a project and required HMAP document set; add conditional RFP/contract documents for subcontracted scope.
2. Unlock a document only after the immediately preceding document is `Approved`.
3. Generate manually or iterate documents automatically with an in-memory current project copy.
4. Build prompt context from the compacted first document and compacted immediately preceding approved document; compact every new result in a second AI call.
5. When planning is approved, transform the WBS/detailed plan into structured tasks, milestones, dependencies, and sprints.
6. Run the reviewed tracking workflow as four model stages: Extractor → QA → Scheduler → QA, each using a structured schema where applicable.
7. Populate Gantt/Kanban-style tracking, workload, testing, team, document, revision, notification, and change-control views.

The current UI copy calls the tracking action a “6-Agent Synthesis Workflow,” but the reviewed `trackingDataAgentWorkflow.ts` implements four stages. Architecture documentation should follow the executable source and treat the label as interface copy.

### Mars Harness extension

The PM harness adds a formal nine-phase lifecycle, typed work authorization, evidence-derived status, bounded Doer/Tools/Tester repair, complete change-impact propagation, independent gate review, and closure/transition packets. The application’s current document and tracking records are inputs to those controls, not proof that every harness gate ran.

## 4. Cross-application chain

The reviewed repositories implement three separate applications; the source review did not identify a shared cross-repository packet bus. The Mars Harness therefore specifies an integration layer:

1. Hypatia exports `EngineeringEvidencePackage/v1`.
2. Intelligent Engineer imports evidence and returns either `ResearchRequestPackage/v1` or `ControlledTechnicalBaseline/v1`.
3. PM Accelerator imports the controlled baseline and emits `ProjectExecutionPacket/v1` plus execution evidence.
4. Operational observations return to Hypatia; anomalies and approved changes return to engineering.
5. Ground Truth, ethics, human authority, and Mission Memory gate and version every promotion.

Implement this chain with explicit APIs or signed export/import packets, schema validation, stable IDs, configuration hashes, idempotent writes, access control, audit events, and replay-safe state transitions. Until that adapter exists and is tested, the chain is an architectural contract rather than a claim of native live integration.
