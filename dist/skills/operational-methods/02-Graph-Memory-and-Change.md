# Graph-linked memory, retrieval, and change propagation

Mission memory separates protected raw evidence, curated linked wiki pages, versioned outputs, working context and approved identity/preferences. Read the catalogue first, retrieve only relevant pages and preserve source-backed relationships, contradiction records and supersession. Raw inputs are not automatically ground truth.

Expanded procedure: [12-Layered-Wiki-Memory.md](12-Layered-Wiki-Memory.md).

SPDX-License-Identifier: Apache-2.0

## Inputs

Require an approved project namespace, decision owner, sensitivity/retention rules, source records, current baseline, and stable IDs. Use `templates/memory-graph.json`. This compact graph is a companion to, not a replacement for, the larger wiki-memory starter.

## Procedure

1. Store claims, sources, requirements, configurations, tests, tasks, decisions, and documents as separately addressable nodes. Include status, version, owner, timestamps, evidence class, and source references.
2. Store explicit typed relationships. For this utility, a change-propagating edge points from prerequisite to dependent. Set `propagates_change: true` deliberately; a mere association does not imply dependency.
3. Keep raw/untrusted input separate from approved knowledge. Require review before promoting extracted relationships. A plausible model-generated graph is not authoritative.
4. Record corrections as new versions linked to superseded records. Never erase dissent or silently rewrite a decision's original basis.
5. Retrieve approved seed records and bounded related context for a task. Enforce data access before retrieval, omit secrets, and record IDs/versions supplied to the agent.
6. When a baseline item changes, traverse downstream dependencies and produce an impact list: artifact, owner, required recheck, blocking severity, and due date.
7. Mark affected approvals as requiring review. Do not mark impacted work as repaired merely because it was identified. Regenerate only authorized affected artifacts and rerun their acceptance tests.
8. Check for dangling edges, duplicate IDs, stale review dates, conflicting facts, and excessive context. Preserve the difference between proposed changes and approved baselines.

## Local checks

- `python tools/harness_checks.py graph templates/memory-graph.json --seed claim:power --depth 2`
- `python tools/harness_checks.py impact templates/memory-graph.json --seed claim:power`

Graph retrieval returns approved records only; impact traversal also includes draft dependents so work-in-progress is not missed. Neither command writes memory or authorizes access.

## Graph-aware retrieval extension

For a real GraphRAG adapter, add source ingestion, entity/relationship review, indexed retrieval, permission filters, provenance, freshness rules, and evaluation queries. Compare answers against a manually checked benchmark before use. The included graph traversal does not implement semantic embeddings or Microsoft's GraphRAG indexing pipeline. Reference: https://microsoft.github.io/graphrag/.

## Outputs and gate

Return a context manifest, affected-node list, proposed revalidation plan, append-only change record, and approval decision. Reject orphan references, unauthorized context, silent overwrites, or an assertion that dependency detection itself fixed downstream work.


## Shared artifact chain and backward correction

Read skills/operational-methods/15-Shared-Artifact-Chain-and-Correction.md (method 15 in the methods folder). Each harness consumes exact approved revisions, publishes a transactional output manifest, and routes blockers through CorrectionRequest/v1. Preserve the previous baseline, mark dependent artifacts stale, independently review upstream revisions and regenerate the minimal affected closure before promotion. The workflow revisits stages while each pinned revision graph remains acyclic.
