# Harness chaining, structured handoffs, and parallel work

SPDX-License-Identifier: Apache-2.0

## Inputs

Require a human owner, objective, risk, permissions, available capabilities, definition of done, shared baseline, and resource limits. Use `templates/handoff-packet.json` and the memory graph.

## Procedure

1. Map the objective into work packages with IDs, accountable owners, deliverables, prerequisites, acceptance tests, and authorized tools.
2. Route unknown science through Hypatia; route supported design through Intelligent Engineer; route approved delivery through PM Accelerator. Apply only the phases relevant to the work; record justified skips.
3. Build an acyclic dependency plan. Launch only ready, independent branches within approved concurrency and budget. A safe blocked branch need not stop unrelated work.
4. Give each specialist a spawn contract: parent, scope, exclusions, inputs, output schema, permission limits, maximum depth/children, budget, reviewer, return condition, and memory destination.
5. Pass explicit packets containing schema version, namespace IDs, baseline/configuration hash, producer, input/evidence IDs, deliverables, checks, assumptions, risks, approvals, and next action.
6. At each boundary, check schema and artifact integrity, then independently assess scientific/engineering acceptance and human authority. Reject mismatched baselines or unresolved blocking findings.
7. Return design-sensitive uncertainty as a Research Request Package specifying the affected requirement, unknown, bounds, acceptance threshold, decision consequence, and due date.
8. On a changed prerequisite, pause affected promotion, compute downstream impact, update authorized records, and rerun tests. Never merge conflicting branch outputs silently.
9. Persist the approved result and dissent, revoke temporary access when available, retire the task, and report actual completion or blockage.

## Local check and real adapter boundary

Run `python tools/harness_checks.py gate templates/handoff-packet.json`. A template is intentionally not approvable. The command checks declared record completeness and review separation; it does not verify a reviewer's identity or source truth.

A native application adapter additionally needs authenticated producer/consumer identities, schema validation, access control, artifact-hash verification, replay/idempotency protection, concurrency handling, audit persistence, retries, timeouts, and rollback. Test success, duplicate delivery, stale baseline, partial failure, unauthorized access, and recovery end to end. Do not describe the three SaaS applications as natively integrated before those tests pass.

## Outputs and stops

Return a dependency plan, spawn records, branch results, approved or blocked packets, impact/rework list, and closure record. Stop promotion for missing approval, self-approved consequential work, invalid packet, unresolved blocker, stale configuration, exceeded budget, or missing required tool. Never fabricate an execution record to complete a chain.
