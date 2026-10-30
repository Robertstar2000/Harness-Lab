# INT controls — conformance addendum 5.3

2026-10-29. Apache-2.0. Normative design controls, not proof of host execution.

## REQ-INT-01

ACP server exposure is deliberately deferred: mission chain uses typed packets rather than editor protocol. No ACP conformance claimed; require version negotiation, auth/trust, session and cancellation fixtures before adoption.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-INT-02

ACP peer hosting is deferred; no network peer is treated as interchangeable until policy, cancellation, isolation and usage mappings are tested.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-INT-03

A2A mesh is explicitly not adopted. Revisit only for a demonstrated cross-vendor requirement; internal coordination stays simple.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-INT-04

Preserve in-process coordination and typed packets; do not add ACP/A2A for internal calls.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-INT-05

Discovery checks configured own and neighbouring skill roots including .agents/skills, .claude/skills and .codex/skills within authorized scope. Deduplicate by canonical path/hash, show collisions, never execute on discovery.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-INT-06

Import documented public formats only; namespace source IDs, preserve settings and safety rules. Unsupported safety setting blocks import; never silently drop it. Export original plus mapped data and migration report.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-INT-07

Own hook vocabulary is mars-hooks/v1: pre_tool, post_tool, stop. Adapter records host event name, semantic differences and version; no fabricated universal host mapping.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-INT-08

Publish skill index with suite version, source, license, content hashes, declared dependencies, trust tier and review evidence. Hashes prove integrity, not publisher trust.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-INT-09

Importable Python reference-control module is supplied for local checks only. Agent-as-model endpoint and hosted SDK are deferred and not claimed.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-INT-10

Meta-harness remains a packet orchestration contract; every imported stage must reapply policy, evidence, redaction, usage and approval gates. No running cross-app API is claimed.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-INT-11

Managed policy may be delivered as read-only versioned JSON by an administrator; verify expected digest before use. MDM transport and central administration service are deferred and not claimed.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

