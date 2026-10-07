# Diagnosis berdasarkan gejala

Mulai dari observable symptom, reproducer, lalu isolate layer. Mengganti easing untuk semua masalah akan menyembunyikan clock, geometry atau ownership errors. Domain references resolve melalui [master map](../architecture/domain-map.md).

| Gejala | Kandidat penyebab | Cara membedakan | Domain |
|---|---|---|---|
| Speed berubah pada refresh rate berbeda | Increment per frame, fixed alpha filter | Replay trajectory pada timestamps sama dengan display rates berbeda | D03, D04 |
| Spring meledak | dt unit salah, stiff step, force sign, invalid mass | Unit audit, analytic oracle, h refinement | D08, D10 |
| Overshoot tak diinginkan | Underdamping atau incompatible incoming velocity | Measure x/v and damping ratio; inspect target policy | D06, D08 |
| Snap saat retarget | New animation starts from old origin | Log current x/v and new initial state | D06, D20 |
| Final visibility salah setelah rapid toggle | Stale callback, multiple owners | Event token history and accepted completion log | D20 |
| Object speed tidak rata di Bézier | u dianggap jarak | Equal-u spacing versus arc-length mapping | D02 |
| Camera flip di path | Tangent/up singularity, rotation discontinuity | Visualize basis, tangent norm and dot(up,tangent) | D02, D25 |
| Quaternion taking long path | Hemisphere mismatch | q and −q fixture, dot sign | D06 |
| IK elbow tiba-tiba flip | Branch selection/history missing | Compare branches and previous pose | D07 |
| IK target tidak tercapai | Unreachable geometry, limits, conflicting tasks | Residual plus reach/limit checks | D07, D13 |
| Mesh distorted at rest | Inverse bind/frame mismatch | Neutral pose and one-joint fixture | D17 |
| Skin twist collapse | LBS geometry limitation, weights | Weight audit and controlled twist comparison | D17 |
| Feet skating | Root/stride mismatch, contact phase | World foot velocity during stance | D18 |
| Body penetrates thin wall | Discrete detection tunneling | High-speed swept collision fixture | D09 |
| Resting objects jitter | Contact bias/restitution/iterations | Resting fixture, energy budget, solver sweep | D09, D10 |
| Fluid changes with resolution | Discretization/model parameter scaling | Mesh/timestep refinement with fixed physical parameters | D09, D10 |
| Drag remains active after interruption | pointercancel/capture loss ignored | Cancel stream and inspect lifecycle | D21 |
| Drag offset under transformed parent | Frame conversion/DPR mismatch | Known client/local points under transforms | D02, D21 |
| Noisy release inertia | Velocity estimated tiny/stale dt | Known noisy/irregular trajectory oracle | D04, D21 |
| Scroll animation behavior ambiguous | Trigger semantics versus progress semantics | Reverse/seek scroll and inspect intended mapping | D03, D22 |
| Remote object warps | Clock/buffer/prediction error | State age, clock mapping, correction residual | D23 |
| Audio sync drifts | Clock-rate mismatch, resampling, encoder delay | Markers at beginning/middle/end and clock records | D23, D40 |
| Text breaks when animated | Grapheme/shaping/font load assumptions | Multiple scripts and actual shaping/layout | D24 |
| Blurry Canvas or wrong picking | Backing/CSS pixel scale mismatch | Size/DPR/hit-test fixture | D24 |
| Alpha edges dark/light | Straight/premultiplied mismatch | Known compositing oracle plus transformed edge | D28 |
| Ghost trails | Invalid temporal history/reprojection | Camera cuts, disocclusion, object ID changes | D27 |
| GPU last particles corrupt | Dispatch bounds or stride mismatch | N=63,64,65 and known data layouts | D26 |
| GPU results vary by run | Data race, reduction order | CPU oracle, fixed inputs, multiple dispatch runs | D26 |
| High average FPS but visible jank | Tail frames, scheduling, GC | Frame interval distribution and trace | D35 |
| Memory grows after navigation | Undisposed resources/listeners | Repeated mount/unmount counts and peak memory | D35, D36 |
| Reduced-motion doesn't stop background | Preference only applied CSS | Inspect JS/Canvas/GPU ownership paths | D34 |
| Hidden exit content keyboard-focusable | Semantic state not coordinated | Focus traversal during interrupted exit | D20, D34 |
| Learned motion fails unseen action | Data coverage, representation, leakage | Independent holdout and baseline comparison | D15 |
| Export differs preview | Pipeline/font/color/cadence mismatch | Compare input hashes, stages and decoded properties | D38, D40 |

## Reproducer record

Record input/config/version, unit/frame/time contract, exact event history, expected property, observed symptom, interval/region, evidence captured, suspected causes and discriminating checks. Keep original inputs. A visual impression belongs in observation; physical/root cause requires additional evidence.

## Verification after fix

Re-run affected verifier and dependent integration checks. Do not widen tolerance to hide a defect. Do not re-run unrelated expensive checks without changed dependency or unresolved concern. If failure is target-device-specific, preserve that target evidence and keep other environments separate.
