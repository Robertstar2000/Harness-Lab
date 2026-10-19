# Graph-linked memory, retrieval, and change propagation

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
