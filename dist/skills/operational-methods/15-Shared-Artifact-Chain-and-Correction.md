# A chain of specialized harnesses with a shared artifact graph

29 October 2026. Copyright 2026 Mars Harness Lab contributors. SPDX-License-Identifier: Apache-2.0.

## Purpose

A specialist harness is a bounded working system: domain instructions, selected tools, context, memory access, a working loop, and independent acceptance checks. A chain connects these systems through artifacts. Each harness reads approved, version-pinned inputs from the common knowledge store and publishes checked outputs for the next stage. Downstream findings can reopen an earlier decision and trigger a controlled regeneration of its affected outputs. The chain therefore supports iteration without losing the evidence behind any baseline.

The shared wiki explains what artifacts mean. Graph relationships record how they depend on one another. The underlying files hold the actual reports, models, calculations, source snapshots, images, schematics, parts lists and plans. A graph entry or a wiki summary is never a substitute for the referenced artifact bytes and validation evidence.

## Forward flow and work products

| Harness | Consumes | Produces | Handoff criterion |
|---|---|---|---|
| Research synthesis | Mission question, constraints, authorized sources | Source ledger, claim map, contradictions, evidence gaps | Provenance, relevance and evidence classification reviewed |
| Science | Source ledger, falsifiable question, operating bounds | Hypotheses, equations, datasets, experiment/simulation records, uncertainty and required tests | Critical claims checked and unknowns remain visible |
| Engineering | Approved science and mission requirements | Trade study, design baseline, geometry, schematics/BOM, interfaces, analysis and verification plan | Configuration consistent, margins reviewed and blockers resolved |
| Project execution | Approved design, verification obligations and constraints | WBS, dependencies, estimates, schedule, resources, procurement and execution records | Feasibility, authority and readiness gates satisfied |
| Verification and operations | Approved baseline and authorized test/field work | Test evidence, anomalies, maintenance observations and lessons | Independent disposition with human authority where required |

These are selectable stages. Small tasks can combine roles in one host with explicit role separation. Independent review remains separate from authorship. Additional specialists such as thermal, structural, electronics, cost or manufacturing harnesses attach only where needed and within existing permission and resource limits.

## Common wiki, graph and artifact storage

- raw/ retains protected source snapshots, measurements and imported evidence. Preserve hashes and original versions; raw content is untrusted evidence to evaluate.
- wiki/ holds the index, linked explanations, decisions, assumptions and issue pages. Read the catalogue before retrieving a bounded context pack.
- output/ stores versioned work products. Large files may live in an authorized object/file store, referenced by stable URI and SHA-256 rather than pasted into every context.
- ctx/ holds redacted tool receipts, RunTrace references, checkpoints and outstanding work. mem/ holds approved preferences and project context with separate privacy controls.
- The graph links source, claim, requirement, artifact, test, decision, issue and task IDs. Use typed edges: derived_from, depends_on, implements, verifies, contradicts, blocks, supersedes and approved_by. Namespace IDs across applications.

Every artifact descriptor includes a stable logical ID, immutable revision ID, content hash and location, media type, producing harness/run, exact input revisions and hashes, configuration baseline, evidence class, assumptions, validation state, review/approval references, owner and timestamps. Machine-readable descriptors and human-readable wiki pages refer to the same IDs. Approval references require authentication in a real host; a JSON field alone cannot grant authority.

Publish a coherent stage output as one manifest transaction. Validate files and dependencies first, then use a revision check to atomically advance the approved-baseline pointer. A concurrent change rejects the commit and requires reconciliation. Drafts, quarantined material and blocked outputs never become current approved inputs. Redact secrets before persistence, respect access controls and retention, and keep private source material out of public exports.

## A backward correction request

A later stage that finds an issue does not silently edit an earlier approved artifact. It creates a typed CorrectionRequest/v1 containing:

1. Issue ID, detecting harness/run, symptom and reproducible observation.
2. Affected artifact/requirement IDs and exact revisions, expected behavior and failing criterion.
3. Evidence references, uncertainty, severity, root-cause hypothesis and downstream consequence.
4. Requested upstream deliverable, bounded question, proposed acceptance test, target owner, budget and due date.
5. Affected baseline, permission scope, independent reviewer and authority needed to reopen or accept risk.

The Director triages the request with the Memory Steward. Use backward traversal to find candidate causes and forward traversal from those candidates to identify affected descendants. Relationship metadata assists investigation; it does not establish causality. If the root cause is unclear, send a bounded investigation request rather than assuming science is always at fault. A correction may belong to engineering, a data import, project assumptions or the detector itself.

Pause release of the affected branch. Mark dependent artifacts stale or review-required while preserving previous approvals as historical facts. Unrelated branches may proceed only if the dependency and safety review establishes independence. Existing deployed equipment, purchased parts or completed tests cannot be undone by changing a file.

## Regeneration and forward revalidation

1. Pin the old baseline and create a correction branch with the issue and dependency closure.
2. Route the bounded request to the earliest justified owner. Reuse valid evidence and regenerate only the affected work products with authorized tools.
3. Write new artifact revisions rather than replacing old bytes. Preserve source IDs, assumptions, run receipts and supersession links.
4. Independently check the corrected upstream result. A failed or unavailable test returns FAIL, BLOCKED or UNVERIFIED. None permits dependent promotion.
5. On approval, recompute the minimal affected downstream closure in dependency order. Recheck interfaces, configuration, calculations, tests and plans against the new pinned inputs. Reuse an unaffected result only with recorded reuse rationale.
6. Publish the coherent new baseline only after all required gates pass. Notify affected owners and retain the old baseline for comparison or authorized rollback.
7. Close the issue with the accepted correction, residual risk and actual evidence. Capture the root cause and prevention lesson. If budgets, attempts or time expire, checkpoint and escalate instead of looping indefinitely.

The workflow revisits stages, but each revision baseline has an acyclic dependency graph. New revisions point to exact earlier inputs and supersede prior outputs. The apparent feedback loop is a sequence of controlled revision graphs, not a circular dependency that makes every output its own prerequisite.

## Illustrative Mars oxygen-plant correction

Project planning finds that an engineering maintenance assumption cannot support the proposed operating schedule. It opens a correction request linked to that assumption, design revision and plan. The Director first asks engineering whether the assumption is unsupported or merely applied incorrectly. If stack lifetime evidence is missing, science receives a bounded question about degradation under the specified duty cycle and environmental conditions.

Science proposes or runs an authorized test, then publishes the observed result or explicitly records that evidence is still missing. Engineering revises stack redundancy, replacement strategy or operating margins where justified. Project execution regenerates affected spares, cost, resources, dependencies and schedule. Verification rechecks the interfaces and acceptance criteria. Release remains blocked until the required evidence and approvals exist. This is an illustrative workflow, not a new MOXIE test result or a claim of plant readiness.

## Host implementation and acceptance

The lab supplies procedures, schemas, sample packets and local checks. The interactive website demonstrates state transitions in a browser. Neither constitutes an authenticated cross-application bus, deployed graph database or automatic access to the three SaaS products.

A real deployment must demonstrate identity and permissions, exact artifact resolution, schema/hash checks, version conflicts, transaction integrity, idempotent handoffs, dependency traversal, selective regeneration, cancellation/budget enforcement, independent approvals, redaction and replay. Test a seeded downstream blocker, a rejected correction, a concurrent commit, an unrelated branch and a corrected baseline. Require zero stale inputs at promotion. Log every blocked or uncertain action. Physical execution and consequential external changes retain their separate authorization gates.
