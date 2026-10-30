# Rebuild from first principles

Copyright 2026 Mars Harness Lab contributors. SPDX-License-Identifier: Apache-2.0.

Updated 2026-10-29. Synthesis of user-supplied reference images; host capabilities require independent validation.

Before optimizing a familiar design, ask whether its assumptions and components are necessary. Start with the mission outcome and the governing physics, then rebuild a feasible solution. Analogy can suggest candidates; evidence and constraints decide between them.

## Procedure

1. Frame the decision: record the problem, measurable goal, current approach, environment, constraints, source inventory, available tools and permissions. State the decision owner and acceptance checks.

2. Inventory assumptions in assumptions.md. Classify each as a physical law, measured fact, estimate, habit or opinion. Link evidence, date, units, uncertainty and a test or review trigger. Do not label a contested claim a hard fact.

3. Decompose the problem into materials, energy, time, people and money. Identify governing relationships and defensible lower bounds. In SOURCES.md record source, retrieval date, conditions, unit conversions and derivation. An unknown bound stays unknown.

4. Rank the gaps between the current baseline and each feasible bound. Separate physical minimum, manufacturable estimate and delivered lifecycle cost. Compare ratios only for compatible units and boundaries; zero or unknown denominators receive no invented ratio.

5. Rebuild two options: a bold redesign and a conservative alternative. Ask whether a part or process can be removed before improving it. Preserve safety, scientific validity, maintainability and human requirements; eliminating a component is not automatically an improvement.

6. Stress-test both options. Identify first failure, skeptical counterargument, what must be true, sensitive variables and an affordable falsification test. Independently recompute critical numbers and mark checks PASS, FAIL, BLOCKED or UNVERIFIED.

7. Select the best supported option, explain residual uncertainty and specify the first reversible step. Deliver assumptions.md, SOURCES.md, cost-gap.csv, option comparison, risks-and-tests.md and a 30-day plan with owners and gates. Stop the dependent step when a required tool or input is missing.

## Required handoff

Return source IDs, affected packet/page IDs, actual checks, residual uncertainty, owner, next action and a redacted trace reference. Preserve the existing conformance controls and independent approval gates.
