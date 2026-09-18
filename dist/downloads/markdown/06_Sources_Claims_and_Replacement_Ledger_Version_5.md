<!--
Copyright 2026 Mars Harness Lab contributors
SPDX-License-Identifier: Apache-2.0
Complete license text: https://mars-harness-lab-v5.tallman-equi-9130.chatgpt.site/license/
-->
# Sources, Claims and Replacement Ledger

Purpose: identify the authority, status, provenance and replacement state of presentation claims.

## Primary project sources

- Bob J Mills, “The AI Path to Mars,” supplied Safari webarchive: `9755c3bfec1c898947b240937f902e73e6a35f9e.webarchive` (`file_0000000008ec81f5ab560b257bb47abd`).
- NASA/JPL, “The Sound of MOXIE at Work on Mars,” 6 September 2023: https://www.jpl.nasa.gov/images/pia26041-the-sound-of-moxie-at-work-on-mars/
- Mars Society 2026 convention information: https://www.marssociety.org/
- Hypatia Pro: https://github.com/Robertstar2000/Hypatia-Pro
- Intelligent Engineer Pro: https://github.com/Robertstar2000/Intelligent-Engineer-Pro
- Initial presentation design record summarized in `13_Detailed_Initial_Chat_Summary_and_Restored_Concepts.md`.

## Evidence model

Epistemic status and provenance answer different questions and must remain separate.

| Field | Allowed values | Question answered |
|---|---|---|
| Epistemic status | Observed; Derived; Assumed; Unknown | What kind of knowledge claim is this? |
| Provenance | Literature; simulation; physical test; field observation; mission decision | Where did the claim or obligation come from? |
| Gate state | Draft; challenged; approved; blocked; released | May the work product move forward? |

## Claim classes

- Architectural claims describe the proposed Mars Harness and must be presented as design recommendations.
- Product workflow claims must be checked against the current repositories before the conference.
- Mars environmental or ISRU claims require primary scientific or agency sources.
- Quantitative claims require units, boundary conditions, uncertainty where available, epistemic status and provenance.
- Claims about “the harness” must distinguish orchestration, instructions, tools, context, memory, specialist agents, validation and approval from replaceable models.
- Platform portability means the work-product contract can be implemented on multiple runtimes; it does not claim identical behavior across vendors.
- Human-role claims must preserve mission direction, values, accountability, risk acceptance and release authority. Consequential actions require human approval.

## Case-study replacement state

| Slide | Current state | Required replacement | Acceptance check |
|---:|---|---|---|
| 15 | Verified NASA/JPL MOXIE starting facts | Optional reviewed Hypatia evidence expansion | Every added finding has status, provenance, units and bounds. |
| 16 | Illustrative scale-up requirements | Reviewed Intelligent Engineer baseline | IDs, evidence links, assumptions, configuration and V&V methods are present. |
| 17 | Illustrative stack-life research request | Actual reviewed Research Request Package | Blocked decision, variables, boundary conditions and acceptance threshold are explicit. |

## Integrity rules

- Never fake certainty or imply that MOXIE demonstrated habitat-scale readiness.
- Keep Observed, Derived, Assumed and Unknown explicit.
- Keep provenance distinct from epistemic status.
- Treat failed hypotheses, dissent and negative findings as useful evidence.
- Let science refuse premature engineering certainty.
- Let engineering return precise unresolved questions to science.
- Preserve model and vendor independence.
- Persist evidence, provenance, configuration state, decisions, dissent, tests and lessons learned in mission memory.
- Require human approval for consequential actions and baseline release.


---

## Version 5 claim controls

The deck explicitly distinguishes **literature**, **modeled**, **empirical**, and **open** claims. MOXIE figures shown on slide 15—16 runs, 122 g total oxygen, and ≥98% purity—remain empirical NASA results. Settlement-scale production, dust life, duty cycle, storage integration, and maintenance intervals are not promoted to fact. Slides 16–17 are marked illustrative and must be replaced by reviewed harness outputs before being treated as a qualified design baseline.


---

## Scaled-MOXIE scenario claims

Treat the original MOXIE performance as empirical NASA evidence. Treat 304 kWe, 592 t, 585 t return allocation, 7.4 t crew allocation, 33.8 kg/h, the proposed architecture, costs, schedules, and reliability claims as modeled or assumed until their calculations and sources are independently reviewed. The phrase “an approach in hours” describes concept-package generation, not physical qualification.


---

## Corrected scenario labeling

The deck now labels 304 kWe and 592 t as modeled outputs, identifies the 585 t and 7.4 t bars as modeled oxygen allocation in tonnes, and identifies ≥98% purity as demonstrated at MOXIE scale. Speaker notes include the 592,000 kg ÷ 17,520 h = 33.79 kg/h calculation and the 7,400 kg ÷ (12 × 730) = 0.845 kg/person/day calculation.
