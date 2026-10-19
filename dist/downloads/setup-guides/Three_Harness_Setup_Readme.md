# Three Harness Setup Readme

## Required operational methods — V5.2

Download [Operational Methods V5.2](https://mars-harness-lab-v5.tallman-equi-9130.chatgpt.site/downloads/Mars_Harness_Operational_Methods_V5_2.zip). The combined setup ZIP already includes the same files under `operational-methods/`; complete skill/agent suites include them under `skills/operational-methods/`.

1. Load `README.md`, `CAPABILITY_COVERAGE.json`, and the selected role contract along with the original skill and agent instructions.
2. Read methods 01–10 as applicable to the current domain and task.
3. Use the same operational-method version and shared baseline across the three domains. Keep independent branches bounded, preserve explicit packets and review separation, and treat unavailable integrations as blocked rather than successful.
4. Copy and fill the applicable JSON templates. Do not treat example or template records as completed evidence or authority.
5. With Python 3.10+, run `python -m unittest discover -s tests -v` from the extracted operational-methods directory. Follow its README for individual graph, impact, tree, parts, document, handoff, policy, and hash commands.
6. Test available tools in your chosen runtime with a harmless local example. Attach only approved project data. Document missing capabilities and preserve human approval gates.
7. Record actual tool outputs, versions, unresolved findings, and acceptance results before passing a packet to the next harness.

The procedures are included; native SaaS handoffs, production GraphRAG, CAD/EDA, solvers, telemetry, and permission enforcement still require project-specific implementation and tests. This download update does not deploy those services or alter any installed personal skills.

## Purpose

This package gives a visitor the setup instructions for all three Mars Harness Lab domains:

- Science Harness.
- Engineering Harness.
- Project Management Harness.

Each guide explains which published skills and agents to download, how to load them, what work products to create, and which validation gates must pass before handoff.

## Recommended Use

1. Start with the science harness and produce `EngineeringEvidencePackage/v1`.
2. Pass that approved package to the engineering harness and produce `ControlledTechnicalBaseline/v1`.
3. Pass that approved baseline to the project management harness and produce `ProjectExecutionPacket/v1`.
4. Use Mars Harness Director, Ground Truth Gatekeeper, Mission Memory Steward, and Ethical Specialist Agent Network across all three domains.
5. Preserve human authority at every promotion gate.

## Included Guides

| Guide | Domain |
| --- | --- |
| `Science_Harness_Setup_Instructions.md` | Scientific discovery and evidence package |
| `Engineering_Harness_Setup_Instructions.md` | Engineering design and technical baseline |
| `Project_Management_Harness_Setup_Instructions.md` | Work authorization, execution, and closure |

## Core Chain

```text
Science Harness
  -> EngineeringEvidencePackage/v1
Engineering Harness
  -> ControlledTechnicalBaseline/v1
Project Management Harness
  -> ProjectExecutionPacket/v1
```

Blocked claims, unresolved variables, operational observations, and approved changes can move upstream through typed request packets. No domain should rely on hidden chat state as the source of truth.
