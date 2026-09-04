# Work-product contracts

Every stage emits both a brief and a structured packet. Required fields: `packet_version`, `objective`, `stage`, `producer`, `inputs`, `claims`, `evidence`, `assumptions`, `unknowns`, `result`, `acceptance_tests`, `validation`, `approvals`, `owner`, `next_action`, `memory_write`, and `supersedes`.

Evidence classes: **Observed** (direct measurement), **Derived** (reproducible transformation), **Assumed** (declared premise), and **Unknown** (unresolved gap). A critical claim cannot pass solely on Assumed or Unknown evidence.
