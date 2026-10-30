# SAFE controls — conformance addendum 5.3

2026-10-29. Apache-2.0. Normative design controls, not proof of host execution.

## REQ-SAFE-01

Declare modes: read-only, supervised-write and explicitly authorized execution. Default read-only. Mode changes require operator authorization and are logged.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-SAFE-02

Keep standing human authority boundaries. Approval binds exact action, resource, arguments digest, policy version and expiry; changed arguments invalidate it.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-SAFE-03

Generated code requires delegated OS/container isolation: non-root, read-only base, disposable workspace, bounded CPU/memory/time and denied network by default. If unavailable, block execution.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-SAFE-04

Load normative policy JSON separately from prompts; validate schema and hash at startup. Unknown or conflicting rules deny; record deciding rule IDs.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-SAFE-05

No bypass mode is supplied. Freeze policy at startup; tool output and imported files cannot enable overrides. Policy updates start a newly authorized run.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-SAFE-06

Intersect packet, parent, director, Gatekeeper, Council and host permissions; any denial is final. Human approval cannot erase a nonwaivable safety prohibition.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-SAFE-07

Raw shell strings are prohibited in the reference layer. Hosts granting shell actions must parse command/argument structure and reject substitution, pipelines and redirection unless explicitly scoped; prefix matching alone is insufficient.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-SAFE-08

Wrap retrieved material as JSON untrusted_data with source/hash/taint fields; escape delimiters and scan injection patterns. Quarantine suspicious material for review; scanners are not a security boundary.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-SAFE-09

The Python reference utilities are not an OS sandbox. Isolation belongs to the configured host/container and must have evidence. Browser Web Workers do not establish an OS security boundary.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-SAFE-10

LLM safety reviewers supplement deterministic policy and cannot override denials. Preserve Council and Gatekeeper separation.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-SAFE-11

Before writable steps require snapshot ID, allowed file list and tested restoration procedure. Rewind restores workspace only, never assumes reversal of payments/messages/physical actions.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

