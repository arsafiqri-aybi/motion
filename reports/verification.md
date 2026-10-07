# Verification — v0.1.0

## Executed checks

- `python3 -m unittest discover -s tests -v`: **35 tests PASS**. Analytic/geometric fixtures cover interpolation, Bézier x inversion, arc-length approximation/convergence, quaternion handling, critical spring, semi-implicit refinement, RK4, planar FK/IK, low-pass time consistency, alpha composition, spatial neighbors, A* and stale callbacks.
- `python3 examples/run_labs.py --output reports/labs`: **16/16 numerical labs PASS**. Actual values, tolerances, environment and source hash are in [lab-results.json](labs/lab-results.json); [spring trace](labs/spring-trace.csv) records selected trajectory samples.
- Local schema/link validation is executed after final documentation assembly. It checks 40 IDs, 280 core topics, sources, graph endpoints and local links. Machine-readable results are recorded in [structure.json](structure.json).

## Inspection scope

Handbooks contain all seven required core subsections with nonempty models/procedures, failures and verification paths. Source inspection is passage/index scoped; most bibliography remains candidates. Scientific proof is not inferred from content count or link validity.

## NOT_RUN

Browser interaction/layout/accessibility runtime; GPU compile/dispatch/render; sensors/capture calibration; actual audio/haptic output; XR devices; physical robots; learned model training/inference; media render/encode/decode; human perception, preference, usability or comfort studies. WGSL and FFmpeg references are illustrative and not executed.

## Interpretation

PASS is scoped to actual fixtures and environment. Numerical examples are educational subsets. The entire 40-domain scientific space has not been independently audited or tested. Specialist depth remains in [open gaps](../governance/open-gaps.md). No historical PASS claims or prior project material were imported.
