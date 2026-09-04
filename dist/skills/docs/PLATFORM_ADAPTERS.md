# Platform adapters

| Capability | Codex | Claude Cowork | Hermes | Grok | Required behavior |
|---|---|---|---|---|---|
| Instructions | SKILL.md | Skill instructions | Agent skill | Skill/plugin | Load role, loop, contract, guardrails |
| Files | Workspace tools | Cowork files | Local/tool layer | Tool layer | Version outputs and preserve provenance |
| Search/browser | Configured web tools | Connected tools | Tool plugins | Web/search tools | Cite source and capture retrieval time |
| Execution | Shell/code tools | Cowork tools | Terminal/tools | Tool execution | Return actual result; never imply a run |
| Memory | Project/library state | Project context | Memory files | Runtime memory | Durable versioned record with review trigger |
| Approval | Product/user gate | User confirmation | Policy/tool gate | Policy/tool gate | Stop before high-impact or irreversible action |

Exact commands differ by runtime and release. Verify current platform documentation before installation. The portable contract is behavioral: observable inputs, tool mappings, outputs, checks, approvals, and durable state.
