# ORCH controls — conformance addendum 5.3

2026-10-29. Apache-2.0. Normative design controls, not proof of host execution.

## REQ-ORCH-01

Default to single-agent execution. Spawn only for recorded breadth-first work with expected benefit and measured single-agent baseline; independent safety review remains a governance exception with rationale.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-ORCH-02

Parent coordinates isolated workers through bounded typed packets and retains integration accountability.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-ORCH-03

Default depth 3, concurrent workers 3; reserve child budgets from parent before spawn. Completion releases unused reservation, never spent usage.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-ORCH-04

Child permissions are the intersection with parent and charter. Denied capabilities cannot be recovered through another worker.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-ORCH-05

Use in-process tasks where possible; cross-process application handoff uses versioned file packets and explicit acknowledgments, not an asserted live message bus.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-ORCH-06

Declarative fan-out accepts task ID, input reference, budget, permission set and return schema. Validate all rows, bound concurrency and integrate in task-ID order.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-ORCH-07

Swarm and mixture-of-agents are deliberately deferred. Shared mission memory is not a concurrent swarm implementation.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-ORCH-08

Report per-worker and total tokens/cost, comparable single-agent estimate, estimate source and ratio. If baseline is unknown report unknown; never assert the paper’s 15x as a measured Lab result.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-ORCH-09

Agent metadata index declares name, model profile, tools, skills, hooks and permissions. Defaults deny tools; role prose never expands the index policy.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

