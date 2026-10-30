# CTX controls — conformance addendum 5.3

2026-10-29. Apache-2.0. Normative design controls, not proof of host execution.

## REQ-CTX-01

Discover context from filesystem root to working directory within approved scope, plus user/project/extension scopes; recognize AGENTS.md and CLAUDE.md. Record order, hashes and provenance; nested rules cannot override higher authority.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-CTX-02

Inject governing context early; load subtree context only when touching that subtree. Discovery never converts untrusted repository content into policy authority.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-CTX-03

Compact at effective window minus max(4096 tokens, 10 percent of window), reserving output capacity. Preserve verbatim recent tail; summarize older history and keep pinned approvals/evidence references.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-CTX-04

Merge new summary into previous anchored summary; preserve early decisions, dissent and unresolved tasks. Persist lineage and input hashes. On overflow invoke same routine once then stop context_overflow if still too large.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-CTX-05

Unbounded linear history is not adopted. Bounded turns and threshold compaction are required; do not claim Maximal context support.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-CTX-06

Only validated approved records enter durable memory; drafts and blocked records remain quarantined, with provenance and supersession chains.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-CTX-07

Freeze recalled memory snapshot ID during a run. New memory appears only at an explicit versioned refresh boundary to preserve cache and replay semantics.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-CTX-08

Retain deterministic filesystem/transcript search as primary recall and preserve its query and snapshot hash.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-CTX-09

Deterministic recall returns identical stable ordering for identical query and snapshot. Record filters and tie-breaks; return bounded result pages.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-CTX-10

Embedding recall is optional, disabled by default and labelled supplementary; save index/model revision and never let similarity override authoritative IDs.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-CTX-11

Ranked repository map is deferred. After compaction restore pinned files and active skill references under a measured token budget; do not claim symbol-ranking implementation.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

## REQ-CTX-12

Checkpoint session, parent/fork ID, packet IDs and compaction ancestry. Forks inherit policy and remaining budget, never reset spent allowance; rewind external effects requires explicit compensation.

Acceptance: retain a positive fixture and a refusal/failure fixture with host version, policy digest and redacted RunTrace. An absent fixture means runtime unverified.

