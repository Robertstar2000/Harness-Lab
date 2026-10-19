# Experiments, simulation validation, and digital-twin readiness

SPDX-License-Identifier: Apache-2.0

## Inputs

Require the research question, decision that results will inform, competing hypotheses, baseline, validity envelope, data rights, risk, tools, units, and approval authority. Use `templates/simulation-plan.json`.

## Study and simulation procedure

1. State hypotheses, expected observations, falsification criteria, controls, variables, sampling, and preregistered analysis/acceptance rules.
2. Select the least complex model adequate for the question. Record equations, parameters, boundary conditions, solver, numerical tolerances, units, software versions, assumptions, and excluded physics.
3. Verify the implementation with unit tests, analytic or benchmark cases, conservation checks where applicable, and mesh/time-step or solver convergence checks.
4. Separate calibration data from validation data. Document measurement error and fit parameters only on the declared calibration set; retain an independent holdout when appropriate.
5. Execute using a real solver or computation tool. Record inputs, code/data hashes, seed, actual outputs, residuals, failures, and execution logs. Never describe an unrun model as a completed simulation.
6. Challenge sensitivity, boundary conditions, alternative models, uncertainty propagation, and off-nominal conditions. Report model discrepancy separately from numerical error and measurement uncertainty.
7. Compare predictions with independent observations and predefined error bounds. Limit conclusions to the validated envelope; mark extrapolation clearly.
8. Submit methods, data, calculations, limitations, and reproducibility materials to an independent reviewer. Return unresolved design blockers as bounded research requests.

## Digital-twin extension

A live twin additionally requires a verified asset/configuration identity, authorized telemetry, time synchronization, sensor quality checks, calibration version, data-latency limits, drift detection, operating envelope, and safe fallback when data are stale or missing. Start read-only. Model updates and any control actuation need separate approvals, rollback, and safety validation. An offline simulation is not a live twin.

## Choosing the next experiment

1. List decision-sensitive unknowns and candidate tests.
2. Estimate plausible outcomes and how each could change the decision; document probabilities and evidence for them.
3. Where justified, compare expected decision benefit with experiment cost, elapsed time, and risk. Otherwise use a clearly labeled uncertainty-reduction heuristic rather than claiming a calculated monetary value of information.
4. Select a bounded test, define a stopping rule, and revisit the estimate after the result. Do not optimize for producing a favorable finding.

## Outputs and stops

Return study protocol, simulation/validation plan, actual execution manifest, data-quality record, uncertainty report, review responses, and next-test recommendation. Block for unavailable solver or data, failed convergence, data leakage between fit/test sets, unbounded extrapolation, unsafe testing, or missing consent/authority. Physical experiments, regulated decisions, and control actions require domain-appropriate review.
