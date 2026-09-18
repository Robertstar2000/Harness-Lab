<!--
Copyright 2026 Mars Harness Lab contributors
SPDX-License-Identifier: Apache-2.0
Complete license text: https://mars-harness-lab-v5.tallman-equi-9130.chatgpt.site/license/
-->
# Engineering Discipline Agent Catalog

Use this catalog to select the smallest multidisciplinary team that can cover the approved scope. The Systems Engineering Agent maintains the integrated technical baseline; discipline agents own their analyses but do not unilaterally change cross-domain requirements or interfaces.

| Agent | Scope | Typical reports and visual artifacts |
|---|---|---|
| Systems Engineering | Decomposition, interfaces, budgets, traceability, lifecycle balance | System model, interface map, requirements trace, margin dashboard |
| Aerospace and Flight Mechanics | Aerodynamics, trajectories, EDL, stability, flight loads | Trajectory report, flight envelope, load plots |
| Propulsion Engineering | Propulsion cycles, feed systems, thrust, performance, hazards | Performance model, P&ID, operating map |
| Mechanical Engineering | Mechanisms, machines, tolerances, tribology, packaging | Design report, tolerance stack, mechanism views |
| Structural Engineering | Loads, stress, fatigue, fracture, vibration, buckling | FEA report, load paths, margin and mode plots |
| Civil, Geotechnical, and Construction | Sites, foundations, soil/regolith, excavation, utilities | Site plan, foundation report, construction sequence |
| Electrical Power Engineering | Generation, storage, conversion, distribution, protection | One-line diagram, load/energy budget, fault study |
| Electronics and Hardware | Analog/digital circuits, boards, EMC, radiation tolerance | Schematics, PCB records, derating and EMC reports |
| Embedded Systems and Firmware | Real-time software, buses, timing, fault handling | State diagrams, timing analysis, interface tests |
| RF and Communications | Links, antennas, spectrum, networks, navigation signals | Link budget, coverage map, spectrum plan |
| Software, Data, and AI | Architecture, pipelines, models, testing, deployment, governance | Architecture, data lineage, test and model cards |
| Controls, GNC, and Robotics | Estimation, control, autonomy, planning, actuators, sensors | Control model, state flow, stability and Monte Carlo plots |
| Thermal Engineering | Heat transfer, insulation, cryogenics, thermal control | Thermal model, heat-flow diagram, temperature margins |
| Chemical and Process Engineering | Reactions, separations, fluids, scale-up, ISRU | Mass/energy balance, PFD/P&ID, process envelope |
| Materials and Metallurgical | Selection, processing, corrosion, wear, joining, degradation | Selection matrix, property plots, coupon/test plan |
| Biomedical and Bioengineering | Physiology, devices, biosensors, biomechanics, biocompatibility | Hazard/benefit report, physiological model, validation plan |
| Environmental and Life Support | Air, water, waste, contamination, closed loops | ECLSS balance, flow diagram, contamination map |
| Nuclear and Radiation | Shielding, dose, source terms, reactor interfaces | Dose map, shielding trade, radiation assurance case |
| Optical, Photonics, and Sensors | Imaging, lidar, spectroscopy, calibration, optical links | Optical budget, field-of-view layout, calibration report |
| Manufacturing and Industrial | Process planning, tooling, producibility, capacity, workflow | Process flow, line balance, capacity and quality plan |
| Quality, Metrology, and NDE | Inspection, calibration, uncertainty, sampling, defect detection | Control plan, measurement analysis, NDE coverage map |
| Reliability, Maintainability, and Logistics | Reliability allocation, repair, sparing, prognostics | Reliability block diagram, maintenance flow, spares model |
| Safety, Cybersecurity, and Mission Assurance | Hazards, secure design, fault containment, assurance | Hazard tree, threat model, assurance case, risk matrix |
| Human Factors and Habitability | Workload, ergonomics, displays, procedures, accessibility | Task analysis, workspace layout, human-system test plan |
| Agricultural, Food, and Bioprocess Engineering | Controlled-environment agriculture, crop systems, food processing, storage, nutrient loops | Farm system model, crop schedule, food mass balance, HACCP plan |
| Mining, Mineral, and Resource Engineering | Prospecting, excavation, beneficiation, material handling, dust, resource recovery | Mine plan, process flow, resource model, equipment utilization chart |
| Petroleum, Drilling, and Subsurface Engineering | Drilling, wells, subsurface fluids, pressure control, sealing, geothermal interfaces | Well plan, pressure model, drilling program, barrier diagram |
| Geological, Geospatial, and Survey Engineering | Terrain models, geodesy, positioning, mapping, remote sensing, site control | GIS layers, survey-control plan, terrain and hazard maps |
| Architectural, Habitat, and Building Systems Engineering | Habitable layouts, envelopes, egress, utilities, maintainability, modular construction | Habitat plan, building-system diagrams, code/criteria matrix |
| Fire Protection Engineering | Detection, suppression, smoke control, evacuation, oxygen-enriched hazards | Fire-hazard analysis, zone map, suppression and egress plan |
| Acoustics and Vibration Engineering | Noise, vibration, isolation, structural-borne sound, crew exposure | Spectra, modal plots, isolation design, exposure assessment |
| Marine, Hydraulics, and Fluid Systems Engineering | Pumps, piping, valves, pressure vessels, fluid networks, leak control | Hydraulic model, P&ID, pressure-drop and transient report |
| Mechatronics and Automation Engineering | Integrated mechanics, electronics, sensing, actuation, automation cells | Functional architecture, I/O map, sequence diagram, commissioning plan |
| Test, Instrumentation, and Measurement Engineering | Sensors, DAQ, calibration, test rigs, telemetry, uncertainty budgets | Instrumentation plan, channel list, calibration chain, test-data report |

## Discipline work-product contract

Each assigned agent returns applicable inputs, governing requirements and standards, assumptions, methods, models, calculations, units, margins, interfaces, hazards, failure modes, uncertainty, decisions requested, verification methods, test evidence, configuration identifiers, technical report, visual artifacts, open issues, and a machine-readable handoff packet.

The agent must identify adjacent disciplines affected by its work. Conflicts are resolved through systems engineering, configuration control, independent review, and named human authority where consequential.
