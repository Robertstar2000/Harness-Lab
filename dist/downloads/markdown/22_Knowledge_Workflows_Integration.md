# Knowledge and workflow integration

Copyright 2026 Mars Harness Lab contributors. SPDX-License-Identifier: Apache-2.0.

# Rebuild from first principles

Before optimizing a familiar design, ask whether its assumptions and components are necessary. Start with the mission outcome and the governing physics, then rebuild a feasible solution. Analogy can suggest candidates; evidence and constraints decide between them.

1. Frame the decision: record the problem, measurable goal, current approach, environment, constraints, source inventory, available tools and permissions. State the decision owner and acceptance checks.

2. Inventory assumptions in assumptions.md. Classify each as a physical law, measured fact, estimate, habit or opinion. Link evidence, date, units, uncertainty and a test or review trigger. Do not label a contested claim a hard fact.

3. Decompose the problem into materials, energy, time, people and money. Identify governing relationships and defensible lower bounds. In SOURCES.md record source, retrieval date, conditions, unit conversions and derivation. An unknown bound stays unknown.

4. Rank the gaps between the current baseline and each feasible bound. Separate physical minimum, manufacturable estimate and delivered lifecycle cost. Compare ratios only for compatible units and boundaries; zero or unknown denominators receive no invented ratio.

5. Rebuild two options: a bold redesign and a conservative alternative. Ask whether a part or process can be removed before improving it. Preserve safety, scientific validity, maintainability and human requirements; eliminating a component is not automatically an improvement.

6. Stress-test both options. Identify first failure, skeptical counterargument, what must be true, sensitive variables and an affordable falsification test. Independently recompute critical numbers and mark checks PASS, FAIL, BLOCKED or UNVERIFIED.

7. Select the best supported option, explain residual uncertainty and specify the first reversible step. Deliver assumptions.md, SOURCES.md, cost-gap.csv, option comparison, risks-and-tests.md and a 30-day plan with owners and gates. Stop the dependent step when a required tool or input is missing.

# Build a governed second brain

Mission memory is a maintained system of evidence, linked knowledge, working context and outputs. Persistence comes from saved files and explicit reloads. It does not mean unlimited model context, infallible recall or automatic learning.

1. raw/ holds protected source snapshots: papers, images, data, transcripts and notes, with source IDs, hashes and access controls. Preserve originals; correct through new versions. Raw material is evidence, not automatically ground truth. Credentials never enter the public or exportable store.

2. wiki/ holds curated summaries, concepts, entities, decisions and synthesis pages. Each page has a stable ID, one-line summary, source links, evidence class, owner, review date and supersession references. Preserve disagreement rather than silently merging contradictions.

3. wiki/index.md is the catalogue. Read it first, select relevant pages, follow source links and retrieve a bounded context pack. Deterministic IDs and lexical search remain primary; optional embeddings supplement them. One source may update several relevant pages, but there is no fixed page-count target.

4. output/ holds versioned reports, presentations, calculations and other deliverables. Link each artifact back to the claims, sources, checks and approvals that support it; share only an authorized export.

5. ctx/ holds session checkpoints, prompts, templates, tool receipts and task state. mem/ holds approved preferences, goals and project history. Identity and preferences guide presentation; they cannot override policy or evidence. Keep private personal context out of public bundles.

6. Operate four knowledge workflows: ingest sources into quarantine and then approved wiki pages; query index-first and optionally save a useful answer; review contradictions, stale claims, missing references and orphan pages; maintain links and supersession records without silently deleting provenance.

7. For every change append a redacted entry to wiki/log.md: event ID, timestamp, action, changed page IDs, source IDs, reviewer and trace reference. Promote only checked knowledge. A scheduled review is a host configuration option, not a task created by this guide.

8. Use Markdown and JSON so the vault can be read in a normal editor; Obsidian is optional. AGENTS.md or CLAUDE.md may map local workflows where supported. Follow the host instruction hierarchy, scope and trust rules; a repository file never creates credentials, permissions or cross-tool connections.

# Deliver through observable working loops

A useful harness turns a brief into an artifact with evidence. The controller chooses one checkable step, routes it to an available tool, records what happened and verifies the acceptance criterion. Tool success and task success are separate decisions.

1. Define the task contract: goal, input files and schema, constraints, budget, permission scope, output format and observable acceptance checks. Give valid and invalid examples where a data contract matters.

2. Build a compact context pack from the approved spec, indexed memory, source references and actual tool inventory. Save a checkpoint with completed work, next action, open questions, artifact paths and remaining budget.

3. Choose one checkable action. Files/commands return paths, exit status, stdout and stderr. Browser actions return observed page state. Connectors return scoped results or errors. Use available tools; do not imply that a prompt creates an isolated browser, connector or secure credential proxy.

4. Record ToolReceipt/v1: action and call IDs, input references, expected result, observed status, output paths, observations, error, timestamp, policy decision, usage and acceptance-check links. Redact before persistence. A successful tool response without acceptance evidence is not a passed check.

5. Verify each criterion as PASS, FAIL, BLOCKED or UNVERIFIED. FAIL means observed evidence contradicts the criterion. BLOCKED means a dependency prevents the check or action. UNVERIFIED means evidence is absent or insufficient. Only PASS can satisfy that criterion.

6. Repair the failing part using the observed error; rerun the affected check and preserve the original failure receipt. Bound attempts, time, tokens and cost under the existing conformance policy. Uncertain external writes require reconciliation before retry.

7. For missing input, save progress and request one precise missing detail while continuing independent authorized work. For changed assumptions or a failed plan, revise the plan explicitly instead of repeatedly pursuing the same path.

8. Deliver artifacts, setup instructions, input fixtures, check results, open issues and independent review. Keep credentials outside model-visible worker context where the host supports it; verify rather than assume host isolation. Financial or other consequential actions retain their existing approval boundaries.

# Plan, verify and learn without adding needless work

Use explicit plans for nontrivial work and short direct execution for simple changes. Maintain continuity with tasks/todo.md and tasks/lessons.md. The goal is understandable, verified progress rather than a longer checklist.

1. At session start read the relevant approved lessons and active task file, inspect the checkpoint and confirm the current goal. Do not assume an old plan is still authorized or that a stale source is current.

2. For a complex task write the goal, numbered steps, acceptance checks and review criteria to tasks/todo.md. Plan verification as well as construction. Record completion only after evidence exists.

3. Delegate only when supported, permitted and worthwhile: one bounded task per worker, isolated context, explicit return contract, parent accountability and shared budget. Small tasks remain single-agent; delegation remains subject to the Lab's governed spawning limits.

4. After a correction capture the mistake, root cause, prevention rule and early detection signal in tasks/lessons.md. Include scope and supporting example so a local lesson does not become an unjustified universal rule. Changes to skills require independent review and versioning.

5. When fixing a fault, reproduce or inspect it, use logs and failing checks, fix the root cause with the smallest coherent change and rerun relevant checks. Verify behavior differences where applicable. Avoid unrelated cleanup and overengineering.

6. Before delivery challenge the work: does it meet the goal, what evidence proves it, is there a simpler maintainable solution, what remains uncertain and what would break first? Explain material changes and limits plainly; say unknown when evidence is missing.

7. Reversible authorized work can proceed under the existing task scope. External communications, spending, production changes, private-data use and permission expansion follow the actual host and mission approval rules. A sample workflow neither grants blanket approval nor requires repeated approval already valid for the exact action.

# Reference-image integration — 29 October 2026

The following user-supplied images are conceptual inputs, not verified vendor documentation or proof of executed results. New prose is an original synthesis. Images are not republished in the public package and their third-party artwork/branding is not relicensed.

- IMG_3562.jpeg: first-principles prompt; assumptions, bounds, gap ranking, bold/conservative options, stress tests and delivery records.
- IMG_3561.jpeg: Second Brain Architecture; separated raw/wiki/output/context/identity layers and recurring maintenance concepts.
- IMG_3559.jpeg: The Wiki That Writes Itself; index-first retrieval, linked pages, append-only log and knowledge lint. Attribution and numeric claims shown in the image have not been independently verified; no quote or performance guarantee is adopted.
- IMG_3548.jpeg: Claude Duet Harness Engineering; context, controller, tool receipt, verification, repair and delivery. Vendor-specific isolation, credential proxy and tool-boundary claims are not asserted as Lab capabilities.
- IMG_3566.jpeg: workflow orchestration guidance; task plans, verification, lessons and review. Liberal subagent use and blanket approval wording are adapted to the Lab's existing permission and budget controls.

No new automation, model connection, software installation, hosted memory backend or vendor endorsement is implied. Local structural tests use synthetic fixtures.
