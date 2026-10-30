# Build a governed second brain

Copyright 2026 Mars Harness Lab contributors. SPDX-License-Identifier: Apache-2.0.

Updated 2026-10-29. Synthesis of user-supplied reference images; host capabilities require independent validation.

Mission memory is a maintained system of evidence, linked knowledge, working context and outputs. Persistence comes from saved files and explicit reloads. It does not mean unlimited model context, infallible recall or automatic learning.

## Procedure

1. raw/ holds protected source snapshots: papers, images, data, transcripts and notes, with source IDs, hashes and access controls. Preserve originals; correct through new versions. Raw material is evidence, not automatically ground truth. Credentials never enter the public or exportable store.

2. wiki/ holds curated summaries, concepts, entities, decisions and synthesis pages. Each page has a stable ID, one-line summary, source links, evidence class, owner, review date and supersession references. Preserve disagreement rather than silently merging contradictions.

3. wiki/index.md is the catalogue. Read it first, select relevant pages, follow source links and retrieve a bounded context pack. Deterministic IDs and lexical search remain primary; optional embeddings supplement them. One source may update several relevant pages, but there is no fixed page-count target.

4. output/ holds versioned reports, presentations, calculations and other deliverables. Link each artifact back to the claims, sources, checks and approvals that support it; share only an authorized export.

5. ctx/ holds session checkpoints, prompts, templates, tool receipts and task state. mem/ holds approved preferences, goals and project history. Identity and preferences guide presentation; they cannot override policy or evidence. Keep private personal context out of public bundles.

6. Operate four knowledge workflows: ingest sources into quarantine and then approved wiki pages; query index-first and optionally save a useful answer; review contradictions, stale claims, missing references and orphan pages; maintain links and supersession records without silently deleting provenance.

7. For every change append a redacted entry to wiki/log.md: event ID, timestamp, action, changed page IDs, source IDs, reviewer and trace reference. Promote only checked knowledge. A scheduled review is a host configuration option, not a task created by this guide.

8. Use Markdown and JSON so the vault can be read in a normal editor; Obsidian is optional. AGENTS.md or CLAUDE.md may map local workflows where supported. Follow the host instruction hierarchy, scope and trust rules; a repository file never creates credentials, permissions or cross-tool connections.

## Required handoff

Return source IDs, affected packet/page IDs, actual checks, residual uncertainty, owner, next action and a redacted trace reference. Preserve the existing conformance controls and independent approval gates.
