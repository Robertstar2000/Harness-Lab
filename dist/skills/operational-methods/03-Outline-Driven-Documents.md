# Outline-driven documents and cross-document consistency

SPDX-License-Identifier: Apache-2.0

## Inputs

Require audience, purpose, deliverable format, length limits, approved baseline, source policy, and reviewer. Use `templates/document-plan.json` and the project memory graph.

## Procedure

1. Propose one table of contents. Give every chapter a stable section ID, purpose, content description, required questions, sources, expected tables/figures, dependencies, and acceptance criteria.
2. Obtain approval for the outline before long-form drafting. Record changes as outline revisions instead of allowing chapters to quietly change the document's scope.
3. Establish a canonical fact ledger: names, numbers, units, dates, definitions, assumptions, requirements, and evidence classes. Reference fact IDs instead of copying uncontrolled variants.
4. For each ready section, retrieve only its approved sources and relevant memory. Draft from its content contract; distinguish evidence from interpretation and cite sources.
5. Draft independent sections in parallel only after shared definitions and facts are fixed. Wait for prerequisite results before writing dependent conclusions.
6. Review each section for coverage, unsupported assertions, traceability, units, and open questions. Return an issue record to its author; do not invent missing material to fill the outline.
7. Assemble chapters in approved order. Reconcile terminology, numeric values, headings, cross-references, figure/table numbering, captions, citations, and duplicate passages.
8. Render the requested final format with an appropriate document or presentation tool. Inspect pagination, tables, figure labels, accessibility, and working links. A text check alone does not validate rendered layout.
9. Publish or share only with the required authority. Archive the approved document, outline, fact ledger, source manifest, review responses, and versions.

## Local check

Run `python tools/harness_checks.py document templates/document-plan.json`. It checks section dependencies, IDs, source references, and exact shared-fact values/units declared in the plan. It does not read a PDF or prove that the prose cites a source correctly. An agent/editor must check the actual generated document against the plan.

## Outputs and acceptance

Return the TOC, section contracts, chapter artifacts, common-fact ledger, coverage report, consistency findings, rendered deliverable, and approval. Block release for missing required sections, unresolved conflicting facts, unsupported conclusions, or unreviewed scope changes.
