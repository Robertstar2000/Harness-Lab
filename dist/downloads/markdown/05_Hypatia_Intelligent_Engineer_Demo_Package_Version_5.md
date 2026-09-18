<!--
Copyright 2026 Mars Harness Lab contributors
SPDX-License-Identifier: Apache-2.0
Complete license text: https://mars-harness-lab-v5.tallman-equi-9130.chatgpt.site/license/
-->
# Version 5 Demonstration Package for Slides 15–17

Purpose: run a traceable MOXIE scale-up demonstration without confusing proven feasibility with habitat-scale readiness.

## Verified starting evidence

NASA/JPL reports that MOXIE completed 16 oxygen-producing runs, generated 122 grams of oxygen in total, reached 12 grams per hour in its most efficient run and produced oxygen at 98 percent purity or better.

| Claim | Epistemic status | Provenance | Engineering meaning |
|---|---|---|---|
| MOXIE produced oxygen on Mars | Observed | NASA/JPL mission record | Feasibility is established. |
| Sixteen runs produced oxygen | Observed | NASA/JPL mission record | Intermittent operation was demonstrated. |
| Total production was 122 g | Observed | NASA/JPL mission record | Output remained demonstration-scale. |
| Peak efficient rate was 12 g/hour | Observed | NASA/JPL mission record | The result is not a continuous crew-scale duty cycle. |
| Product purity was at least 98 percent | Observed | NASA/JPL mission record | Storage, conditioning and mission interfaces still require engineering. |

Source: https://www.jpl.nasa.gov/images/pia26041-the-sound-of-moxie-at-work-on-mars/

## Case-study question

How should a maintainable Mars ISRU oxygen-production system scale from MOXIE’s demonstrated feasibility to sustained surface operations when duty cycle, stack life, dust, thermal cycling, storage and maintenance remain open?

## Hypatia Pro starting prompt

Investigate the evidence needed to scale Mars oxygen production from MOXIE’s demonstrated results to sustained surface operations. Treat the five NASA/JPL facts above as Observed and preserve their provenance. Do not infer continuous duty cycle, crew-scale output, stack lifetime or habitat readiness from them.

Address atmospheric variability; dust loading and electrostatic behavior; thermal cycling; solid-oxide stack life; materials and seal degradation; contamination; oxygen storage interfaces; maintainability and redundancy. Formulate falsifiable competing hypotheses. Define variables, units, boundary conditions and measurement protocols. Propose simulations and physical experiments. Specify statistical tests and uncertainty treatment. Seek evidence that would refute the preferred hypothesis.

Assign each claim exactly one epistemic status: Observed, Derived, Assumed or Unknown. Record provenance separately as literature, simulation, test or field observation. Run Generate → Validate → Critique → Repair → Approve → Persist for each major generated artifact. Only approved outputs may flow into the Engineering Evidence Package. Preserve failed hypotheses, dissent, negative results and unresolved contradictions.

Deliver an Engineering Evidence Package containing equations, parameter distributions, operating envelopes, confidence levels, assumptions, failure thresholds, unresolved uncertainties, references and the minimum additional experiments required before detailed design.

## Intelligent Engineer Pro starting prompt

Design a maintainable Mars ISRU oxygen-production system using the approved Engineering Evidence Package. Treat uncertainty bounds and unresolved questions as design inputs; never convert them silently into facts.

Generate stakeholder and system requirements; a requirement-to-evidence matrix; architecture alternatives and a scored trade study; preliminary sizing and margins; operating modes; interfaces; maintainability provisions; FMEA; verification methods and acceptance criteria; and design-blocking uncertainties. Every requirement must trace to observed evidence, a derived calculation, an explicit assumption or a mission decision.

Use phase-gated engineering from requirements through controlled release. Preserve configuration state, decisions and dissent. Consequential actions and baseline promotions require human approval. For each design-blocking uncertainty, generate a Research Request Package containing the blocked decision, hypothesis, independent and dependent variables, Mars-relevant boundary conditions, proposed experiment or simulation, minimum detectable effect, acceptance threshold and required evidence quality.

## Current slide contract

- Slide 15 contains verified NASA/JPL starting facts and must retain the feasibility-versus-scale distinction.
- Slide 16 contains illustrative scale-up requirements and verification methods. Replace them with reviewed Intelligent Engineer output before using them as a project baseline.
- Slide 17 contains an illustrative research request focused on solid-oxide stack life. Replace it with the exact reviewed request from a real harness run.

## Demonstration integrity

- Keep epistemic status separate from provenance.
- Never label a simulation as physical validation.
- Preserve uncertainty bounds, negative findings and dissent.
- Show the blocked engineering decision, formal research request, targeted experiment, evidence return, baseline update and verification consequence.


---

## Version 5 demonstration thread

Use the exact slide 15–17 sequence: (1) Hypatia classifies MOXIE evidence and leaves scale, dust, duty cycle, integration, storage, and maintainability open; (2) Intelligent Engineer converts supported evidence into requirements and verification while retaining unresolved items as assumptions; (3) the filter-cleaning blocker becomes a Research Request Package with competing hypotheses, variables, Mars boundary conditions, factorial chamber method, uncertainty analysis, and requirement-derived acceptance limits; (4) reviewed evidence updates the baseline and engineering continues.


---

## Updated demonstration artifacts

The updated deck shows the actual ARES-SOE research bundle, engineering phase files, VibraEngineer CDR excerpt, project-management work products, WBS, and visual outputs. The demonstration target is 592 t of oxygen over 730 days for a 12-person habitat and return-vehicle scenario, with a nominal modeled production rate near 33.8 kg/h and 304 kWe continuous power. These are scenario outputs requiring review, traceability, and qualification.


---

## Corrected conclusion contract

Science concludes that scale-up is plausible but modeled values and degradation remain open. Engineering concludes that system integration, power, traceability, reliability and returned blockers dominate. Project execution concludes that the WBS, estimate basis, risks, change state and approval gates control release.
