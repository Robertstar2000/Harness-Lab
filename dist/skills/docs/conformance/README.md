# Conformance remediation 5.3

2026-10-29. Apache-2.0.

All 97 assessment entries are tracked in requirements.json. The original 9 Exceeds / 9 Meets / 49 Partially meets / 9 Does not meet / 21 Unverified grades are historical and have not been independently rescored. This addendum addresses all findings as explicit controls or deliberate feature deferrals. It does not establish full runtime conformance.

Read the nine subsystem control documents, policy.json, reference_controls.py and test_reference_controls.py. These local reference utilities demonstrate selected mechanisms; they are not an operating-system sandbox, production agent loop, live provider adapter, ACP/MCP server or telemetry collector.

Before mission execution the Director records host versions and capability probes. Gatekeeper blocks stages lacking required enforcement (budgets, deadline cancellation, policy, isolation, redaction). The Memory Steward persists redacted RunTrace/v1 and pinned summary lineage only. The Council retains independent denial authority. Existing stricter safety and human authority rules take precedence.

Run `python -m unittest discover -s dist/skills/docs/conformance -p 'test_*.py'` from the repository. Each production adapter must additionally demonstrate pre-tool denial, hung-call cancellation, real usage reservation, subprocess isolation, event normalization, checkpoint recovery and provider swap. Missing evidence stays unverified; no prompt instruction substitutes for enforcement.

Optional features explicitly deferred: ACP exposure/hosting, A2A mesh, marketplace plugin installer, embedding recall, ranked repository map, multi-cache dialects, swarm, agent-as-model endpoint, live meta-harness API, MDM transport and telemetry collector. These remain adoption decisions, not implemented features.
