# Deliver through observable working loops

Copyright 2026 Mars Harness Lab contributors. SPDX-License-Identifier: Apache-2.0.

Updated 2026-10-29. Synthesis of user-supplied reference images; host capabilities require independent validation.

A useful harness turns a brief into an artifact with evidence. The controller chooses one checkable step, routes it to an available tool, records what happened and verifies the acceptance criterion. Tool success and task success are separate decisions.

## Procedure

1. Define the task contract: goal, input files and schema, constraints, budget, permission scope, output format and observable acceptance checks. Give valid and invalid examples where a data contract matters.

2. Build a compact context pack from the approved spec, indexed memory, source references and actual tool inventory. Save a checkpoint with completed work, next action, open questions, artifact paths and remaining budget.

3. Choose one checkable action. Files/commands return paths, exit status, stdout and stderr. Browser actions return observed page state. Connectors return scoped results or errors. Use available tools; do not imply that a prompt creates an isolated browser, connector or secure credential proxy.

4. Record ToolReceipt/v1: action and call IDs, input references, expected result, observed status, output paths, observations, error, timestamp, policy decision, usage and acceptance-check links. Redact before persistence. A successful tool response without acceptance evidence is not a passed check.

5. Verify each criterion as PASS, FAIL, BLOCKED or UNVERIFIED. FAIL means observed evidence contradicts the criterion. BLOCKED means a dependency prevents the check or action. UNVERIFIED means evidence is absent or insufficient. Only PASS can satisfy that criterion.

6. Repair the failing part using the observed error; rerun the affected check and preserve the original failure receipt. Bound attempts, time, tokens and cost under the existing conformance policy. Uncertain external writes require reconciliation before retry.

7. For missing input, save progress and request one precise missing detail while continuing independent authorized work. For changed assumptions or a failed plan, revise the plan explicitly instead of repeatedly pursuing the same path.

8. Deliver artifacts, setup instructions, input fixtures, check results, open issues and independent review. Keep credentials outside model-visible worker context where the host supports it; verify rather than assume host isolation. Financial or other consequential actions retain their existing approval boundaries.

## Required handoff

Return source IDs, affected packet/page IDs, actual checks, residual uncertainty, owner, next action and a redacted trace reference. Preserve the existing conformance controls and independent approval gates.
