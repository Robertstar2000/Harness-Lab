# Three Harness Setup Readme

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

