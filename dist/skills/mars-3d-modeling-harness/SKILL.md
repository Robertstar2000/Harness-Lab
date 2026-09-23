---
name: mars-3d-modeling-harness
description: Create traceable 3D concept images, parametric geometry, and validated STL deliverables for engineering design, prototyping, visualization, or additive manufacturing. Use when Codex must generate or revise a 3D model, render orthographic or isometric views, export `.stl`, assess mesh integrity or printability, or package geometry for an Intelligent Engineer design phase. Do not use a generated image as proof of geometry or a mesh as proof of structural adequacy.
---

<!--
Copyright 2026 Mars Harness Lab contributors
SPDX-License-Identifier: Apache-2.0
Complete license text: https://mars-harness-lab-v5.tallman-equi-9130.chatgpt.site/license/
-->

# Mars 3D Modeling Harness

## Purpose

Turn approved geometry requirements into versioned 3D source, derived images, and an STL package whose units, dimensions, configuration, and validation state are explicit.

## Intake and mode

Require purpose, owner, baseline and requirement IDs, coordinate system, units, critical dimensions, tolerances, material or process assumptions, interfaces, intended printer or manufacturing method, risk tier, and acceptance criteria. Record missing decision-critical values as `Unknown`.

Select one mode:

- `concept-view`: visual exploration only; no claim of dimensional fidelity.
- `dimensioned-model`: parametric or editable geometry with declared dimensions and interfaces.
- `print-ready-stl`: dimensioned source plus triangulated export and mesh/printability checks.

## Workflow

1. Freeze the geometry brief and acceptance criteria.
2. Establish origin, axes, orientation, units, naming, and configuration ID.
3. Build simple editable primitives first; prefer parametric source such as OpenSCAD, FreeCAD, Blender geometry scripts, or the available CAD-native format.
4. Encode dimensions and tolerances in the source or a paired dimension table. Never rely on STL to preserve units or design intent.
5. Generate isometric and orthographic images from the same geometry when tools allow. If an image generator produces a concept view, label it `conceptual-not-derived-from-model`.
6. Export STL from the controlled source. Record assumed STL units, tessellation settings, axis convention, and source hash.
7. Validate the mesh: parseability, closed/manifold topology, outward normals, nonzero volume, degenerate or duplicate triangles, self-intersections where detectable, bounding box, and connected bodies.
8. Validate use-specific constraints: minimum wall thickness, clearances, fits, overhangs, unsupported spans, build orientation, support access, drainage or powder escape, and printer envelope where applicable.
9. Compare critical dimensions and interfaces with the approved brief. Use an independent check for consequential geometry.
10. Package source, STL, images, dimensions, assumptions, validation record, known limitations, checksum, approval status, and rollback/supersession links.

## Tool discipline

Use the best available geometry/CAD tool and deterministic validators. Keep editable source beside derived files. Preserve commands, versions, parameters, and export settings. If required tooling is unavailable, return a blocked or partial package instead of inventing a model or validation result.

Image generation may support concept communication, materials, or scene context, but it must not establish measurements, topology, tolerances, fit, mass, strength, manufacturability, or STL validity.

## Engineering integration

Link every model to Intelligent Engineer requirements, interfaces, phase baseline, and configuration. During preliminary design, permit conceptual geometry and trade views. During critical design, require explicit dimensions, tolerances, materials, interface control, DFMA input, and independent review. Manufacturing or printing requires named human authorization.

## Work-product contract

Return `GeometryPackage/v1` with objective, owner, risk tier, requirements, acceptance tests, baseline/configuration IDs, coordinate system, units, dimensions, tolerances, materials/process assumptions, editable source, STL, derived images, hashes, mesh metrics, dimensional and printability checks, tool versions, evidence status, assumptions, unknowns, approvals, next action, memory write, and supersedes.

## Guardrails and stop conditions

Never claim that a render is CAD, an STL is dimensionally self-describing, a watertight mesh is manufacturable, or a printed part is structurally qualified. Stop for ambiguous units, missing critical dimensions, incompatible interfaces, unsafe intended use, unavailable required validator, failed manifold or dimensional checks, uncontrolled source, or absent authorization for consequential fabrication.
