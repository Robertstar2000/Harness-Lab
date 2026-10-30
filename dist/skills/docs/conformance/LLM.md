# LLM controls — conformance addendum 5.3

2026-10-29. Apache-2.0. Normative design controls, not proof of host execution.

## REQ-LLM-01

Use one complete(messages, tools, limits) interface returning text, tool_calls with stable IDs, finish_reason and usage; provider wire formats stay inside adapters.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LLM-02

No foundation model ships here. Use generic normalized adapter with explicit capability negotiation; reject unsupported features instead of silently weakening controls.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LLM-03

Per-model profile must declare provider/model revision, reasoning effort mapping, context limit, tokenizer, cache dialect/breakpoints, edit format and quirk flags. Unknown settings remain unsupported until probed.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LLM-04

Freeze static instructions and tool catalogue prefix per run; append changing state after a stable cache boundary. Report cached/uncached tokens separately when available; never invent cache savings.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LLM-05

Model routing is opt-in. Record chosen model, reason and quality evidence; default to operator-selected model. Cheaper summaries still pass evidence and retention checks.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LLM-06

Policy is machine-readable configuration enforced before dispatch; prompts explain rationale and cannot grant permissions.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LLM-07

Maintain a versioned prompt variant matrix: default generic, provider revision, observed failure fixture, gated change and regression result. No speculative model-specific tweaks.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LLM-08

Reference control utilities use the Python standard library and no agent framework. Host framework independence remains unverified until dependency inventory is supplied.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LLM-09

Normalize provider streaming deltas into text, tool-call IDs and arguments; reject duplicate or orphan IDs. Validate completed arguments before permission evaluation.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-LLM-10

Simultaneous cache dialect emission is deliberately not adopted. A profile selects one provider dialect; local inference prefix normalization needs fixture tests.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

