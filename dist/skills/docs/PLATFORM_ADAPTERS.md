<!--
Copyright 2026 Mars Harness Lab contributors
SPDX-License-Identifier: Apache-2.0
Complete license text: https://mars-harness-lab-v5.tallman-equi-9130.chatgpt.site/license/
-->
# Platform adapters

## V5.2 operational methods

Load [Operational Methods](../operational-methods/README.md) with the selected skill. Map file reading/writing, model calls, bounded delegation, Python execution, persistent memory, document rendering, CAD/EDA, simulation, and approvals to tools actually available in the current runtime. Record versions and harmless capability checks. Do not infer that a platform name supplies every capability in the table below.

The included Python utility runs locally without network or third-party dependencies. It does not create a model service, graph database, telemetry feed, authenticated SaaS adapter, sandbox, or permissions system. Do not embed secrets in instructions. If execution or another required capability is missing, return a partial/blocked packet and the minimum setup action.

| Capability | Codex | Claude Cowork | Hermes | Grok | Required behavior |
|---|---|---|---|---|---|
| Instructions | SKILL.md | Skill instructions | Agent skill | Skill/plugin | Load role, loop, contract, guardrails |
| Files | Workspace tools | Cowork files | Local/tool layer | Tool layer | Version outputs and preserve provenance |
| Search/browser | Configured web tools | Connected tools | Tool plugins | Web/search tools | Cite source and capture retrieval time |
| Execution | Shell/code tools | Cowork tools | Terminal/tools | Tool execution | Return actual result; never imply a run |
| Memory | Project/library state | Project context | Memory files | Runtime memory | Durable versioned record with review trigger |
| Approval | Product/user gate | User confirmation | Policy/tool gate | Policy/tool gate | Stop before high-impact or irreversible action |

Exact commands differ by runtime and release. Verify current platform documentation before installation. The portable contract is behavioral: observable inputs, tool mappings, outputs, checks, approvals, and durable state.
