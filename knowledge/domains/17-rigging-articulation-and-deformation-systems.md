# D17 — Rigging Articulation and Deformation Systems

Membangun kontrol dan representasi deformasi yang menghubungkan motion parameters dengan bentuk yang dirender.

Rumpun: **C — Representation and Animation**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Rig bukan hanya skeleton. Controls, deformation, constraints, bind state dan evaluation order harus dibedakan; kinematics D07 memberi solver mathematical layer.

Prasyarat: [D02](../../architecture/domain-map.md#d02), [D07](../../architecture/domain-map.md#d07), [D19](../../architecture/domain-map.md#d19).

## Subdomain dan pengetahuan inti

### D17.01 — Skeleton dan bind spaces

Joint hierarchy, rest/bind pose dan inverse bind matrices menentukan deformation. Imported conventions perlu disamakan sebelum animation diterapkan.

**Model / prosedur.** Skin transform joint_world·inverse_bind dengan mesh/world convention yang dinyatakan.

**Kegagalan.** Double transforms, root mismatch, bind pose not identity.

**Verifikasi.** Mesh unchanged at bind pose and single-joint controlled rotations.

### D17.02 — Control rigs dan drivers

Author-facing controls dapat berbeda dari deformation skeleton. Driver dependencies perlu order dan cycle detection.

**Model / prosedur.** Map control parameters to joint transforms with constraints/expressions.

**Kegagalan.** Cyclic drivers, mixed local/world control semantics.

**Verifikasi.** Neutral pose, control ranges, dependency invalidation and cycle fixture.

### D17.03 — Skinning dan weights

Linear blend skinning menggabungkan bone transforms; dual quaternions memiliki behavior berbeda untuk rigid transforms. Weights and correspondence affect deformation.

**Model / prosedur.** p′=Σwᵢ Mᵢp, typically Σwᵢ=1 for standard LBS; prune/normalize as specified.

**Kegagalan.** Collapsing twist, candy-wrapper artifacts, unweighted vertices.

**Verifikasi.** Weight sums, joint extremes, twist cases and seam continuity.

### D17.04 — Blend shapes dan correctives

Morph targets mengubah geometry relatif base. Corrective shapes memperbaiki poses tertentu; parameter combination dapat interact nonlinearly.

**Model / prosedur.** p′=p_base+ΣwᵢΔpᵢ; conditional correctives driven by pose descriptors.

**Kegagalan.** Double-applied deltas; vertex ordering mismatch.

**Verifikasi.** Base at all-zero weights, endpoint targets, combinations and topology checks.

### D17.05 — Constraints dan procedural controls

Aim, parent, distance dan IK constraints mengevaluasi relationships yang mungkin conflicting. Priority/blend semantics perlu eksplisit.

**Model / prosedur.** Solve or evaluate constraints in defined order; expose residual when target infeasible.

**Kegagalan.** Pop at constraint activation; overconstrained chain.

**Verifikasi.** Toggle/weight sweep, impossible targets, continuity at switches.

### D17.06 — Retargeting dan proportions

Mapping motion antar skeleton requires naming, rest orientation, scale dan contact treatment. Same joint rotation tidak selalu menghasilkan same reach.

**Model / prosedur.** Align rest frames; map chain goals; solve target skeleton IK and root adjustment.

**Kegagalan.** Foot sliding, arm penetration, scale-normalized trajectory lost.

**Verifikasi.** End-effector/task errors, contact preservation, body intersections.

### D17.07 — Deformation beyond bones

Curves, lattices, cages, muscle-inspired systems dan cloth rigs memiliki representations sendiri. Modifier order changes result.

**Model / prosedur.** State rest geometry and deformation stack; invalidation follows topology/version changes.

**Kegagalan.** Modifier stack noncommutative ignored; dynamic simulation applied twice.

**Verifikasi.** Single-stage baselines and full-stack endpoint regression.

## Contoh kerja dan alasan pemilihan

Contoh elbow dengan dua skinning bones: test rest pose sebelum menjalankan animation. Jika bind pose telah mendistort mesh, masalahnya bukan easing. Twist forearm dapat collapse pada LBS; compare dual-quaternion atau corrective shape pada fixture yang sama. Jangan menganggap satu metode selalu terbaik: nonuniform scale handling dan engine support membatasi pilihan.

## Alur implementasi

Normalize assets/frame; verify bind state; build skeleton/control mapping; add deformation; test extreme poses; define retargeting; export bake when runtime lacks controls.

## Kriteria penguasaan

Dapat mendiagnosis bind-transform errors, weight artifacts dan constraint pops; retarget dengan task/contact checks.

## Cabang lanjut yang tetap termasuk cakupan

Muscle systems; pose-space deformation; dual-quaternion skinning; facial action controls; spline IK; autorigging; cage deformation; differentiable rigs.

## Rujukan dan batas bukti

- [S34](../../references/source-map.md#s34)
- [S35](../../references/source-map.md#s35)
- [S36](../../references/source-map.md#s36)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
