# Paired electrical, PCB, mechanical, and assembly deliverables

SPDX-License-Identifier: Apache-2.0

## Shared rule

Use one approved configuration and stable item IDs across all views. Require requirements, units, interfaces, environment, load limits, standards selected by the responsible engineer, tool/library versions, acceptance tests, and a named release authority. Use `templates/paired-artifacts.json`.

## Electrical/electronic and PCB workflow

1. Build the component and connection records: reference designators, manufacturer part numbers when verified, pins, nets, ratings, protection, footprints, and component quantities.
2. Produce schematics and connector pinout tables from those records. Reconcile diagram occurrences against the bill of materials in both directions.
3. In a real EDA tool, verify symbol-to-footprint and pin-number mappings. Stop if required libraries or footprint evidence are unavailable.
4. Establish board outline, stackup, manufacturing limits, placement, clearance, thermal, power, signal-integrity, isolation, and test-point constraints with the responsible engineer.
5. Place and route the board. Run the actual electrical and design-rule checks; retain logs, waived findings, owner, and rationale. For relevant designs, add independent circuit/thermal/signal-integrity analysis.
6. Reconcile the final netlist, PCB, schematics, BOM, fabrication outputs, assembly drawings, and pick-and-place data against the same revision.
7. Conduct independent design/manufacturing review. Export source files and tool-generated manufacturing artifacts only when authorized. Procurement and fabrication are separate approval actions.

## Mechanical and assembly workflow

1. Create a configuration-controlled assembly tree with item IDs, materials, fasteners, quantities, interfaces, and units.
2. Build parametric solid geometry. Generate wireframes, orthographic views, sections, exploded views, and dimensioned drawings from the same source where tools support it.
3. Record critical dimensions, tolerances, fits, datums, tolerance stacks, and inspection methods. A pretty render cannot substitute for dimensioned engineering data.
4. Reconcile item occurrences and quantities with the parts/assembly list. Check interference, clearances, accessibility, fastening, maintenance, and design-for-manufacture/assembly constraints using appropriate tools.
5. Write ordered assembly instructions with referenced items, orientation, tools, prerequisites, inspection points, and verified torque/process values where applicable. Leave unverified process values explicitly unresolved.
6. Run mesh checks for STL exports, dimensional checks against the model, and independent structural or process validation where required. Mesh integrity alone does not qualify a part.
7. Release the paired model/drawing/BOM/instruction/inspection package under one configuration ID and human engineering approval.

## Local reconciliation

Run `python tools/harness_checks.py pairs templates/paired-artifacts.json`. It checks reference IDs, part identity, and occurrence quantities in supplied records. It is not an ERC, PCB DRC, CAD interference solver, or structural analysis tool.

## Outputs and stops

Return editable sources, derived views, connection/item tables, parts lists, assembly/inspection instructions, actual validator logs, waivers, open risks, and approval. Block for orphan components, quantity mismatches, unsupported footprints, ambiguous units, unverified safety limits, failed critical checks, or unavailable required tools. Preserve draft artifacts without representing them as manufactured, tested, or qualified.
