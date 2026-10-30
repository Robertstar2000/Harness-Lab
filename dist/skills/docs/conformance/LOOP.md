# LOOP controls — conformance addendum 5.3

2026-10-29. Apache-2.0. Normative design controls, not proof of host execution.

## REQ-LOOP-01

Use a linear inference → validate → authorize → execute → append observation loop. Append every tool result before the next inference; gate completion independently.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LOOP-02

Keep the linear baseline. Introduce middleware only after documenting at least three independent turn policies and their ordering; denial is final.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LOOP-03

Before every turn and dispatch reserve token/cost allowance; enforce max_turns, max_tokens and max_cost_usd including children and retries. Stop before overspend; unknown usage blocks paid dispatch. Persist termination_reason.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LOOP-04

Enforce stage deadline and per-call cancellation timeout; default 3 consecutive malformed responses, 30 turns, 900 seconds. Reset format-error streak only after schema-valid response. A supervisor must cancel hung calls.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LOOP-05

Batch independent reads; serialize calls sharing a declared writable resource. Keep observation order in call-ID order; dependent operations stay sequential.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LOOP-06

Return errors as observations with call_id, exception_type, redacted message and retryable flag. Bound retries within all original limits; never fabricate success.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LOOP-07

Preserve the existing generate/validate/critique/repair procedure and independent review.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LOOP-08

Require the independent Ground Truth Gatekeeper before stage promotion; the author cannot be the sole approver.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LOOP-09

Persist RunTrace/v1 with input/prompt references, normalized responses, ordered calls, observations, compaction, permission rule IDs, timing, usage and termination. Replay uses recorded responses, never repeats external side effects.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LOOP-10

Interactive adapters may emit ordered text/tool/progress events; accumulate the same final normalized response as nonstreaming. Disconnect does not authorize repeated actions.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

