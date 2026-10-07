# Data motion, retargeting, dan evaluation

Menghubungkan D11, D15, D16, D17, D18 dan D37. Ini pipeline knowledge; tidak ada training/inference model atau capture device yang dieksekusi dalam release ini.

## Canonical record

Sequence record should name clock/rate, skeleton hierarchy, rest orientations, joint coordinate conventions, units, root transform, local joint rotations, contacts, observed/estimated mask dan source provenance. If timestamps irregular, preserve them. A fixed array length alone does not prove fixed cadence.

Separate raw capture, cleaned capture, retargeted motion and learned outputs. Each derived asset records source hashes and transformation versions. Smoothed/fill samples jangan diberi measured confidence asli; they are estimates. Capture confidence scores are model outputs unless calibrated against actual error.

## Preprocessing and leakage

Normalize units/frames, handle missingness, map skeleton and resample with antialias considerations. If windows overlap, random window split can place almost identical sequences in train/test. Split by actor/session/action according generalization claim; preserve independent holdout. Feature normalization parameters fitted on training only avoid information leakage.

Augmentation must preserve valid constraints. Mirroring can swap joint identities and semantic actions; time warp alters velocity/acceleration. State exactly which labels/contact annotations updated. Generated augmentation is not more independent measurement data.

## Retargeting problem

Motion on source skeleton is not target end-effector motion automatically. Rest orientation, proportions and root scale differ. A useful objective combines pose similarity, task-space end-effector goals, contact constraints, joint limits and smoothness. Weights require units/scales. Contact feet may force pelvis adjustment; impossible simultaneous constraints should produce residual rather than hidden limb stretch.

Mapping root translation by overall height ratio can preserve approximate stride but does not solve slopes, contact height or limb proportions. Solve target rig within limits and assess world contact velocity. For facial motion, viseme/action mapping and geometry correspondence differ from body skeleton retargeting.

## Motion matching baseline

Define feature vector with current pose/velocity and desired trajectory samples. Normalize feature groups, search dataset, apply transition, preserve phase/contact when appropriate. Evaluate retrieval cost and actual task error separately. Best available match may be poor when query outside dataset coverage; detect and fallback instead of claiming correct behavior.

This baseline helps learned-model evaluation: a complex model should improve stated metrics or expand useful coverage, not only look novel in selected clips. Record latency/memory trade-offs on actual inference target.

## Metrics with meaning

Joint position/rotation errors compare representations. Root trajectory error measures task path. Foot contact velocity/penetration indicate skating/contact issues. Dynamics residual and joint limits measure model/constraint properties. Diversity measures do not guarantee correct task. Perceptual quality requires actual viewers and context, not automatic score called human preference.

Report distributions by condition, not only global mean: fast turns, occlusions, unusual proportions, long sequence, unseen action, low data, target change. For stochastic generation, evaluate multiple seeds and avoid cherry-picking. If metric depends sample rate or normalization, include those settings.

## Deployment audit

Record dataset/model version, preprocessing, conditioning, seeds, generation duration/rate, output representation, postprocess and hardware. Postprocess can improve contacts while hurting task or style; measure before/after. No training reproduction is claimed from paper abstract inspection. Model weights and datasets are external dependencies with their own terms; repository does not redistribute them.

Implement incrementally: canonical dataset validator, planar retargeting fixture, matching baseline, contact diagnostics, then learned integration. Connect new artifacts to topic IDs and update evidence only after actual execution.
