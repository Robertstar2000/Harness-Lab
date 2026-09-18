<!--
Copyright 2026 Mars Harness Lab contributors
SPDX-License-Identifier: Apache-2.0
Complete license text: https://mars-harness-lab-v5.tallman-equi-9130.chatgpt.site/license/
-->
# Work-product contracts

Every stage emits both a brief and a structured packet. Required fields: `packet_version`, `objective`, `stage`, `producer`, `inputs`, `claims`, `evidence`, `assumptions`, `unknowns`, `result`, `acceptance_tests`, `validation`, `approvals`, `owner`, `next_action`, `memory_write`, and `supersedes`.

Evidence classes: **Observed** (direct measurement), **Derived** (reproducible transformation), **Assumed** (declared premise), and **Unknown** (unresolved gap). A critical claim cannot pass solely on Assumed or Unknown evidence.
