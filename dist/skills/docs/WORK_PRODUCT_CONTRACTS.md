<!--
Copyright 2026 Mars Harness Lab contributors
SPDX-License-Identifier: Apache-2.0
Complete license text: https://mars-harness-lab-v5.tallman-equi-9130.chatgpt.site/license/
-->
# Work-product contracts

## V5.2 operational records

Use the templates in [Operational Methods](../operational-methods/README.md) for decision trees, memory/dependency graphs, section contracts, paired artifact records, simulation plans, peer reviews, handoff declarations, risk/budget policy, run manifests, and performance observations. Keep original domain packets; these records supplement rather than replace them. Link each to its approved project/configuration, evidence, actual tool outputs, reviewer, human authority, and memory history.

Record capability state separately as `procedure_available`, `tool_verified`, `executed`, `independently_validated`, or `blocked`. A template, a generated candidate, or a passed record check may never be promoted directly to independently validated. The generic local gate helper checks declared fields only; authenticated adapters and real evidence remain required.

Every stage emits both a brief and a structured packet. Required fields: `packet_version`, `objective`, `stage`, `producer`, `inputs`, `claims`, `evidence`, `assumptions`, `unknowns`, `result`, `acceptance_tests`, `validation`, `approvals`, `owner`, `next_action`, `memory_write`, and `supersedes`.

Evidence classes: **Observed** (direct measurement), **Derived** (reproducible transformation), **Assumed** (declared premise), and **Unknown** (unresolved gap). A critical claim cannot pass solely on Assumed or Unknown evidence.
