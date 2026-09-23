---
name: paired-schematic-parts-harness
description: Create, revise, and validate a synchronized schematic plus matching parts or bill-of-materials package for electrical, wiring, fluid, pneumatic, process, control, or assembly systems. Use when Codex must produce a schematic and parts list together, reconcile reference designators and connections, generate a BOM, run ERC/DRC-style checks, select or compare components, or prevent diagram-to-parts drift. Current sourcing, price, availability, standards, and regulated component claims require authoritative verification.
---

<!--
Copyright 2026 Mars Harness Lab contributors
SPDX-License-Identifier: Apache-2.0
Complete license text: https://mars-harness-lab-v5.tallman-equi-9130.chatgpt.site/license/
-->

# Paired Schematic + Parts Harness

## Purpose

Produce one configuration-controlled pair: a schematic that defines topology and a parts dataset that defines every instantiated item. Neither artifact may silently diverge from the other.

## Intake and domain selection

Require system purpose, owner, baseline and requirement IDs, schematic domain, governing standards, interfaces, operating envelope, loads or flows, safety class, environment, units, preferred file formats, sourcing constraints, acceptance criteria, and approval authority.

Select the domain vocabulary before authoring:

- Electrical/electronic: symbols, reference designators, pins, nets, ratings, footprints.
- Wiring/harness: connectors, contacts, cavities, wires, gauges, shields, splices, bundles.
- Fluid/pneumatic/hydraulic: equipment tags, ports, lines, valves, pressure/flow ratings.
- Process/P&ID: equipment, instruments, loops, piping classes, control and safety functions.
- Mechanical/assembly: item numbers, interfaces, fasteners, materials, quantities, and assembly relationships.

## Single-source pairing rule

Create a stable component/item table before or with the diagram. Use the same immutable IDs in both outputs. Every instantiated schematic symbol, equipment tag, connector, or assembly item must resolve to exactly one parts row; every non-consumable parts row must identify its schematic or assembly occurrence.

## Workflow

1. Freeze requirements, interfaces, operating envelope, standards, and acceptance criteria.
2. Define document, configuration, sheet, item, net/line, connector, and interface identifiers.
3. Create the initial parts table with item ID, reference/tag, function, value or specification, tolerance, ratings, material, footprint or form factor, quantity, lifecycle status, approved part or candidate status, alternates, and source evidence.
4. Draw the schematic from the same identifiers. Record ports/pins, direction, net or line IDs, signal/medium, nominal and limit values, protection, and off-sheet references.
5. Cross-probe in both directions: schematic occurrence → parts row and parts row → occurrence count.
6. Run domain checks: ERC/DRC, power/ground, ratings, protection, isolation, derating, and footprint mapping for electrical work; continuity, direction, class, fail state, relief, drains/vents, and instrument loops for fluid/process work; or interface, material, fastener, quantity, and compatibility checks for assemblies.
7. Reconcile quantities, duplicate or missing IDs, orphan rows, unconnected ports, unresolved placeholders, incompatible ratings, and alternate equivalence.
8. Verify current standards, manufacturer data, approved part numbers, lifecycle, price, and availability from authoritative sources when those claims matter. Keep candidate parts distinct from approved selections.
9. Obtain independent technical review and named human approval for consequential release.
10. Export the paired configuration with source files, human-readable views, machine-readable BOM/parts data, validation report, hashes, and supersession links.

## Tool discipline

Prefer native editable schematic and parts formats supported by the available EDA/CAD tool. Preserve library names, versions, symbol/footprint mappings, commands, and validator output. If a native editor is unavailable, provide a machine-readable intermediate representation and mark graphical output as a draft.

Never invent a manufacturer part number, certification, rating, price, availability, or compliance claim. Never infer that visual alignment proves electrical or physical connectivity.

## Engineering integration

Link the pair to Intelligent Engineer requirements, interfaces, hazards, FMEA, verification methods, and configuration baseline. Approved change to topology, rating, interface, or part selection must trigger impact analysis and a new paired revision; never update only one side.

## Work-product contract

Return `SchematicPartsPackage/v1` with objective, domain, owner, risk, requirements, standards, acceptance tests, baseline/configuration IDs, editable source, rendered views, BOM/parts data, bidirectional cross-reference, reconciliation, domain rule checks, review findings, tool/library versions, hashes, assumptions, unknowns, approvals, next action, memory write, and supersedes.

## Guardrails and stop conditions

Stop for missing operating limits, ambiguous connection semantics, incompatible ratings, unresolved safety function, orphan items, quantity mismatch, fabricated sourcing data, missing required library, failed critical rule check, uncontrolled baseline, or absent authority for procurement, fabrication, or hazardous operation. Return `approved`, `conditional`, or `blocked`; never imply release from a polished diagram alone.
