# TOOL controls — conformance addendum 5.3

2026-10-29. Apache-2.0. Normative design controls, not proof of host execution.

## REQ-TOOL-01

Begin with no exposed tools; enable a minimal sandboxed shell only when needed. Each additional tool requires a recorded task failure or capability need, owner and least-privilege rationale.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-TOOL-02

Register name, description, JSON argument schema, resources, timeout, output cap, trust and effect class separately from exposure. Validate arguments before execution.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-TOOL-03

When registered tool inventory exceeds 15, expose catalogue/search metadata only and load permitted schemas on demand; enforce token-budget share.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-TOOL-04

Limit each observation to 16384 UTF-8 bytes by default. Shell results include exit_status, stdout, stderr, truncated and full_artifact_ref; redact full artifact before storage too.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-TOOL-05

Frontier edit adapter uses exact unique substring plus expected file digest. Lower-tier fuzzy matching is optional only with an unambiguous candidate, diff preview and regression fixture.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-TOOL-06

Never edit by line number as the primary contract; stale digest or nonunique match fails without writing and requests a fresh read.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-TOOL-07

Consolidate related actions into typed task-level tools with explicit operation discriminator and per-operation schemas/permissions.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-TOOL-08

Retrieve with rg/glob/traversal and optional parsed symbols; canonical path then offset ordering, fixed snapshot digest and result bound. Similarity retrieval is never the default.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-TOOL-09

Preserve task-level application packet tools rather than mirroring every SaaS endpoint.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-TOOL-10

Declare read/write resources and network destinations per call. Scheduler uses conflicts to serialize writes and keeps approval/mutation dependencies ordered.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-TOOL-11

Embedded code execution is not enabled in the reference utilities. Hosts may batch independent reads only after declaring isolation and resource semantics.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

