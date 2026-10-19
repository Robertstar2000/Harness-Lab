# Multistage virtual challenge and independent peer critique

SPDX-License-Identifier: Apache-2.0

## Inputs

Require the artifact and baseline, evidence/data, method, rubric, acceptance criteria, author, independent reviewer, risk tier, and a review budget. Use `templates/review-record.json`.

## Procedure

1. Separate author and reviewer roles. Give the reviewer raw artifacts, scope, and acceptance criteria; do not supply a desired verdict or conceal adverse results.
2. Round one: challenge source provenance, unsupported claims, assumptions, units, calculations, methodology, and coverage of requirements.
3. Round two: propose counterexamples, failure scenarios, boundary tests, alternative explanations, and interface mismatches. Execute relevant tests with authorized tools when available.
4. Round three: assess reproducibility, safety, privacy, practical implementation, manufacturability, human factors, and operational consequences.
5. Classify findings as blocking, major, or minor with evidence, affected record IDs, required action, owner, and disposition. Preserve dissent and uncertainty even when the majority agrees.
6. Return findings to the author. Record each response as accepted/fixed, disputed with evidence, deferred with named authority, or unresolved. Never rewrite the original criticism to make it disappear.
7. Recheck the revised artifact and rerun affected tests. Use another reviewer or a different method/model for high-impact work when possible, while acknowledging correlated model failures.
8. Stop after the declared maximum rounds or budget. Escalate unresolved blockers to a human; repeated debate must not manufacture approval.

## Outputs and acceptance

Return an issue/response matrix, actual test evidence, configuration reviewed, independent disposition, unresolved risks, and human approval where required. A model vote or self-evaluation is not scientific proof. A virtual review is not equivalent to external journal peer review, regulated sign-off, physical testing, or certification.

## Multi-model extension

Record each reviewer's model/version, prompt/task, evidence exposure, and independence limitations. Prefer diversity of evidence and checking method over simply increasing the number of similar agents. Any disagreement affecting acceptance remains visible at the gate.
