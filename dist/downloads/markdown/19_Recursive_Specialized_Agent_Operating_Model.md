# Recursive Specialized Agent Operating Model

## Purpose

Define the specialized agents required to run the Science, Engineering, and Project Management domains of the Mars Harness. Agents are assignments against durable skill contracts. They may create bounded child agents when parallel work, domain depth, or independent verification is needed.

## Command structure

The Mission Harness Director receives the authorized mission objective. It maintains the shared baseline, routes work among the three domain leads, invokes independent ground-truth review, and sends consequential decisions to the human Mission Authority.

Every spawned agent receives: a unique task ID; one accountable parent; scope and exclusions; authoritative inputs; required tools; a typed output contract; evidence and provenance rules; time, compute, and cost limits; an approval boundary; and a stop or escalation condition. A child may spawn descendants only when its delegation permit says `may_spawn: true`. Maximum default depth is three levels below a domain lead. No child may expand its parent's authority.

## Science domain

### Science Domain Lead

Owns the research question, evidence plan, hypothesis portfolio, scientific baseline, uncertainty register, peer-review response, and Engineering Evidence Package. It may spawn:

1. Research Question and Scope Agent — converts the mission need into answerable questions, variables, boundaries, and success criteria.
2. Literature and Source Intelligence Agent — searches primary sources, records provenance, maps conflicting findings, and maintains the evidence ledger.
3. Hypothesis and Causal Model Agent — creates competing hypotheses, causal graphs, predicted observations, and falsification conditions.
4. Experiment Design Agent — defines controls, factors, sample sizes, instrumentation, procedures, and acceptance thresholds.
5. Simulation and Scientific Modeling Agent — builds mathematical or computational models, runs sensitivities, and labels calibration limits.
6. Data Steward and Statistics Agent — validates datasets, preserves lineage, selects analyses, quantifies uncertainty, and checks reproducibility.
7. Scientific Visualization Agent — produces evidence plots, uncertainty views, experiment workflows, and decision-focused figures without concealing limitations.
8. Independent Scientific Reviewer — challenges methods, calculations, source quality, alternative explanations, and overclaiming; it cannot approve its own work.
9. Science Synthesis and Handoff Agent — assembles findings, unresolved questions, operating envelopes, equations, distributions, and minimum additional tests into the Engineering Evidence Package.

Conditional children include planetary-geology, atmospheric-chemistry, materials-science, radiation, life-sciences, instrumentation, and replication agents.

## Engineering domain

### Engineering Domain Lead

Owns the controlled technical baseline from ConOps through verification and release. It may spawn:

1. ConOps and Stakeholder Needs Agent.
2. Requirements and Traceability Agent.
3. Systems Architecture and Interface Agent.
4. Trade Study and Decision Analysis Agent.
5. Discipline Engineering Coordinator.
6. Modeling, Simulation, and Digital Twin Agent.
7. Safety, Reliability, and FMEA Agent.
8. Verification and Validation Agent.
9. Manufacturing, Integration, and Operations Agent.
10. Configuration and Release Agent.
11. Independent Design Review Agent.

The Discipline Engineering Coordinator maintains the following broad engineering bench and activates only the roles required by the work:

12. Systems Engineering Agent — owns technical decomposition, interfaces, budgets, traceability, integration logic, and lifecycle balance.
13. Aerospace and Flight Mechanics Agent — covers aerodynamics, trajectories, flight loads, stability, entry/descent/landing, and atmospheric operations.
14. Propulsion Engineering Agent — covers chemical, electric, nuclear-thermal, fluid-feed, combustion, thrust, performance, and propulsion hazards.
15. Mechanical Engineering Agent — covers mechanisms, machine design, tribology, packaging, tolerances, dynamics, and maintainability.
16. Structural Engineering Agent — covers load paths, stress, fatigue, fracture, vibration, buckling, and structural margins.
17. Civil, Geotechnical, and Construction Agent — covers sites, foundations, regolith mechanics, excavation, roads, structures, utilities, and construction sequencing.
18. Electrical Power Engineering Agent — covers generation, storage, conversion, distribution, protection, grounding, power quality, and load budgets.
19. Electronics and Hardware Engineering Agent — covers analog/digital circuits, boards, components, radiation tolerance, electromagnetic compatibility, and hardware qualification.
20. Embedded Systems and Firmware Agent — covers real-time computing, device drivers, timing, buses, fault handling, and hardware-software integration.
21. RF and Communications Engineering Agent — covers links, antennas, spectrum, networks, latency, coding, navigation signals, and communications reliability.
22. Software, Data, and AI Engineering Agent — covers architecture, data pipelines, models, cybersecurity-aware software, testing, deployment, observability, and model governance.
23. Controls, Guidance, Navigation, and Robotics Agent — covers estimation, control laws, autonomy, motion planning, actuators, sensors, and stability.
24. Thermal Engineering Agent — covers heat loads, conduction, radiation, insulation, thermal control, cryogenics, and operating envelopes.
25. Chemical and Process Engineering Agent — covers reactions, separations, fluids, process control, mass balances, scale-up, ISRU, and chemical hazards.
26. Materials and Metallurgical Engineering Agent — covers material selection, processing, corrosion, wear, radiation effects, degradation, joining, and coupons.
27. Biomedical and Bioengineering Agent — covers physiology, medical devices, biosensors, biomechanics, life support interfaces, biocompatibility, and clinical constraints.
28. Environmental and Life-Support Engineering Agent — covers atmosphere, water, waste, contamination, habitability, closed loops, planetary protection, and environmental monitoring.
29. Nuclear and Radiation Engineering Agent — covers shielding, source terms, dose, reactor interfaces, criticality boundaries, activation, and radiation assurance.
30. Optical, Photonics, and Sensor Engineering Agent — covers imaging, lidar, spectroscopy, illumination, calibration, optical links, and sensor error budgets.
31. Manufacturing and Industrial Engineering Agent — covers process planning, tooling, automation, producibility, capacity, workflow, quality systems, and local manufacturing.
32. Quality, Metrology, and Nondestructive Evaluation Agent — covers inspection, calibration, measurement uncertainty, defects, sampling, NDE, and conformity evidence.
33. Reliability, Maintainability, and Logistics Agent — covers reliability allocation, sparing, repair, prognostics, maintainability demonstrations, and lifecycle support.
34. Safety, Cybersecurity, and Mission Assurance Agent — covers hazards, fault containment, secure architecture, assurance cases, misuse, resilience, and independent risk closure.
35. Human Factors and Habitability Agent — covers workload, ergonomics, displays, procedures, accessibility, team interaction, and human-system validation.
36. Agricultural, Food, and Bioprocess Engineering Agent — covers controlled-environment agriculture, food processing, storage, nutrient loops, and food safety.
37. Mining, Mineral, and Resource Engineering Agent — covers prospecting, excavation, beneficiation, handling, dust, and resource recovery.
38. Petroleum, Drilling, and Subsurface Engineering Agent — covers drilling, wells, subsurface fluids, pressure control, sealing, and geothermal interfaces.
39. Geological, Geospatial, and Survey Engineering Agent — covers terrain models, geodesy, positioning, mapping, remote sensing, and site control.
40. Architectural, Habitat, and Building Systems Engineering Agent — covers habitable layouts, envelopes, egress, utilities, maintainability, and modular construction.
41. Fire Protection Engineering Agent — covers detection, suppression, smoke control, evacuation, and oxygen-enriched hazards.
42. Acoustics and Vibration Engineering Agent — covers noise, vibration, isolation, structural-borne sound, and crew exposure.
43. Marine, Hydraulics, and Fluid Systems Engineering Agent — covers pumps, piping, valves, pressure vessels, fluid networks, and leak control.
44. Mechatronics and Automation Engineering Agent — covers integrated mechanics, electronics, sensing, actuation, robotics cells, and automated commissioning.
45. Test, Instrumentation, and Measurement Engineering Agent — covers sensors, data acquisition, calibration, test rigs, telemetry, and measurement uncertainty.

Each discipline agent produces its applicable design inputs, models, calculations, drawings or interface definitions, assumptions, margins, hazards, verification methods, test evidence, technical report, and visual artifacts. Cross-disciplinary conflicts go to the Systems Engineering Agent and Engineering Domain Lead. When evidence is insufficient, the Engineering Lead creates a Research Request Package for Science. It may not convert an unknown into an assumed requirement without recorded human approval.

## Project Management domain

### Program Domain Lead

Owns authorized scope, integrated execution, performance measurement, governance, and closeout. It may spawn:

1. Charter, Scope, and Governance Agent.
2. WBS and Deliverables Agent.
3. Schedule and Critical Path Agent.
4. Resource and Capacity Agent.
5. Cost and Earned Value Agent.
6. Risk and Opportunity Agent.
7. Quality and Acceptance Agent.
8. Change and Configuration Coordination Agent.
9. Communications and Status Agent.
10. Procurement and Partner Agent.
11. Closure and Lessons Agent.

Program agents coordinate work but cannot approve scientific truth, technical adequacy, or safety risk for the domain authorities.

## Cross-domain controls

- Ground Truth Gatekeeper — independently checks claims, calculations, acceptance criteria, and provenance.
- Mission Memory Steward — maintains append-only facts, decisions, versions, supersession links, review dates, and retrieval context.
- Safety and Ethics Governor — blocks unsafe, unauthorized, privacy-violating, or irreversible external action.
- Integration and Dependency Broker — manages typed handoffs, unresolved interfaces, dependencies, and return loops.
- Human Mission Authority — approves mission intent, residual risk, baselines, resources, external actions, and final release.

## Recursive spawning protocol

1. Prove delegation is necessary and check for an existing capable agent.
2. Create a task packet with scope, inputs, output schema, evidence rules, tools, budget, deadline, risks, and stop conditions.
3. Require the child to acknowledge the contract and declare any further spawning.
4. Return results to the accountable parent and write approved artifacts to shared mission memory.
5. Integrate conflicts at the parent, which remains accountable.
6. Assign independent review to an agent that did not create the work.
7. Promote, return, block, or escalate through the domain lead. Only authorized humans approve consequential execution.

## Default limits

- Maximum recursive depth: domain lead plus three descendant levels.
- Maximum active children per agent: five unless the Mission Harness Director authorizes more.
- No orphan agents; every agent has one accountable parent.
- Permissions can only narrow during delegation.
- No self-approval for consequential work.
- Stop on missing evidence, conflicting baselines, exceeded limits, safety concern, or ambiguous authority.

## Core flow

Mission Authority → Mission Harness Director → Science Evidence Package → Engineering Controlled Baseline → Program Execution Baseline → Verification and Acceptance → Operations Evidence → Science or Engineering update.
