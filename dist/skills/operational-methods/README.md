# Mars Harness Operational Methods — V5.2

Copyright 2026 Mars Harness Lab contributors. SPDX-License-Identifier: Apache-2.0.

This pack turns the lab's differentiators into procedures, role assignments, templates, and local checks. It extends the eleven existing skills; it does not install a new SaaS service or grant an agent additional permissions.

## Start here

1. Appoint a human decision owner. Define the objective, scope, risk, available tools, acceptance tests, budget, and stop conditions.
2. Read the applicable method below and its JSON template. Replace all example values; templates are not completed evidence.
3. Load the relevant specialist role from `roles/`. Give it a bounded task and require an independent reviewer for consequential results.
4. Run local checks with Python 3.10 or newer: `python tools/harness_checks.py --help` and `python -m unittest discover -s tests -v` from this directory. No third-party Python dependencies are needed.
5. Execute the actual research, document, CAD/EDA, simulation, or planning task with authorized tools. Preserve real outputs and tool versions.
6. Review the results and pass the approved packet to the next harness. Failed or unavailable checks remain visible and block dependent promotion.

## Method map

| Method | Use it for | Primary owner |
|---|---|---|
| [01 — Bounded reasoning](01-Bounded-Reasoning.md) | Tree of Thoughts, competing hypotheses, trade studies | Domain director |
| [02 — Graph memory and change](02-Graph-Memory-and-Change.md) | Retrieval, provenance, dependencies, change impact | Memory Steward |
| [03 — Outline-driven documents](03-Outline-Driven-Documents.md) | TOC approval, chapter contracts, common facts | Document editor |
| [04 — Paired engineering artifacts](04-Paired-Engineering-Artifacts.md) | Schematics/parts/PCB; geometry/drawings/assembly | Engineering director |
| [05 — Experiments, simulation, and twins](05-Experiments-Simulation-and-Twins.md) | Study design, calibration, uncertainty, next experiments | Science director |
| [06 — Challenge and peer review](06-Challenge-and-Peer-Review.md) | Independent critique, red teams, revisions | Ground Truth Gatekeeper |
| [07 — Handoffs and parallel work](07-Handoffs-and-Parallel-Work.md) | Chaining, return requests, dependency scheduling | Mars Harness Director |
| [08 — Assurance, autonomy, and replay](08-Assurance-Autonomy-and-Replay.md) | Policy checks, resource limits, reproducibility, regression | Assurance specialist |
| [09 — Specialist roles](09-Specialist-Roles.md) | Select bounded roles and prevent self-approval | Network Governor |
| [10 — Measurement and improvement](10-Measurement-and-Improvement.md) | Measure quality, cycle time, effort, and rework | PM director |

## What runs, and what still needs integration

`tools/harness_checks.py` provides local graph retrieval, downstream impact traversal, candidate ranking, paired-parts reconciliation, document-contract checks, declared-policy checks, handoff checks, and file-hash verification. These are deterministic checks of supplied records. Candidate ranking does not call an LLM or generate a reasoning tree. Graph traversal is not a deployed GraphRAG service. A JSON gate check does not authenticate reviewers, verify physical facts, or enforce operating-system permissions.

The ten methods are agent-executable procedures. Real CAD/EDA validation, scientific simulation, fabrication, live digital twins, model routing, secure runtime enforcement, and authenticated cross-application handoffs require their actual tools and project-specific tests. Never substitute a mock result for an unavailable capability. See `CAPABILITY_COVERAGE.json` for precise readiness and ownership.

The tests use synthetic fixtures. They validate utility behavior, not a Mars design, flight readiness, a performance claim, or the three SaaS applications. Physical, regulated, production, financial, publication, and hazardous actions still require explicit human authority.

## Packaging and licensing

Keep this directory together. Individual skill ZIPs include it as a sibling of the skill folder. Complete suites place it under `skills/operational-methods/`. Agent and setup packages include it too. Open the method from your extracted package; do not rely on hidden chat memory. The complete Apache 2.0 license and NOTICE accompany the ZIPs. Third-party tools and sources retain their own licenses.
