# NFR controls — conformance addendum 5.3

2026-10-29. Apache-2.0. Normative design controls, not proof of host execution.

## REQ-NFR-01

Replay ordered recorded responses, observations, permissions and compactions against pinned input hashes; external tools disabled. Redacted trace supports control-flow replay, not recovery of withheld secrets.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-NFR-02

Identical query and immutable snapshot produce identical path/offset/ID ordering; reject changed snapshots or label a new search.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-NFR-03

Audit every call, rule decision, hook, spawn, extension, compaction and termination with parent IDs, policy version and rule ID before persistence.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-NFR-04

Redact registered secrets and token/private-key patterns recursively before logs, memory, artifacts or telemetry persist. Reject unsanitizable records. Keep secrets registry outside exports.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-NFR-05

Meter each turn/run/child including retries; reserve worst-case response cost before dispatch. Missing price/usage blocks paid continuation; totals include cached and uncached usage when available.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-NFR-06

Measure resident schema tokens/context budget. Warn above 10 percent and defer unused schemas; record tokenizer and measurement method.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-NFR-07

All model, file, tool and web content remains untrusted data, never control-plane authorization.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-NFR-08

Provider swap requires two adapter fixture suites returning the same normalized schema and passing budget/policy tests; live provider portability remains unverified without actual runs.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-NFR-09

Preserve documented Markdown/JSON state and stable identifiers, retaining original inputs during import.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-NFR-10

Migrations are copy-on-write with schema version, original hash, preserved unknown fields/safety settings and rollback. Round-trip fixtures must pass before replacing state.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-NFR-11

Reference utilities have no general-purpose agent framework dependency. Host dependency inventory is required before runtime-level conformance claims.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-NFR-12

RunTrace events carry trace_id, span_id, parent_span_id, start/end timestamps, event name, status, rule IDs and redacted attributes; mapping supports OTel export but no collector is bundled.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-NFR-13

Malformed output, tool oversize, overflow and host failure produce bounded typed observations/checkpoints and explicit termination. Retry never resets budget or repeats uncertain external writes.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-NFR-14

Date inventories and test evidence; distinguish documentation, local reference tests, live integration and deferred capability. This release does not rescore the independent assessment.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

