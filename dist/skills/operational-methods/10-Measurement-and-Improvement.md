# Measured process improvement

SPDX-License-Identifier: Apache-2.0

## Inputs

Require a comparable baseline task, objective, quality/acceptance criteria, measurement owner, sample plan, workflow version, and privacy rules. Use `templates/performance-record.json`.

## Procedure

1. Define the unit of work and outcome before running a comparison. Hold scope and acceptance criteria constant or document adjustments.
2. Measure elapsed cycle time separately from human labor, model/tool compute, waiting, physical testing, and external approvals. Do not subtract work that was simply deferred.
3. Capture quality alongside speed: first-pass acceptance, missing evidence, defect severity, rework hours, reviewer effort, unresolved risks, and downstream failures.
4. Include setup, integration, maintenance, training, licensing, and review costs when estimating economic effect. Label assumptions and distinguish measured from projected values.
5. Use multiple representative runs when feasible. Report sample size, variation, model/tool version, task difficulty, selection bias, and comparability limitations.
6. Derive percentages from recorded denominators; never invent completion percentages or extrapolate one drafting example into an entire R&D program.
7. Use findings to propose a bounded skill or workflow change. Run regression and independent review before accepting it. Keep a rollback baseline.
8. Record lessons and decision history in project memory. A performance claim needs its own evidence ledger and publication approval.

## Outputs and acceptance

Return a baseline/current comparison, measurement definitions, raw observations, quality outcomes, cost assumptions, uncertainty, and a change recommendation. Report improvement only within the tested scope. If no comparable baseline exists, publish observations without claiming quantified savings.
