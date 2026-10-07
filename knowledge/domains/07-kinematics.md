# D07 — Kinematics

Mendeskripsikan gerak dan hubungan antarjoint tanpa terlebih dahulu menentukan forces penyebabnya.

Rumpun: **B — Motion Models**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Dynamics D08 menambahkan forces; rigging D17 menambahkan authoring controls; planning D13 menentukan trajectory yang layak.

Prasyarat: [D01](../../architecture/domain-map.md#d01), [D02](../../architecture/domain-map.md#d02), [D03](../../architecture/domain-map.md#d03).

## Subdomain dan pengetahuan inti

### D07.01 — Linear angular kinematics

Translation dan rotation mempunyai velocity berbeda. Angular velocity adalah vector dengan frame tertentu; derivative Euler angles tidak umumnya sama dengan angular velocity.

**Model / prosedur.** x′=v, v′=a; untuk constant angular velocity orientation berkembang melalui rotation exponential.

**Kegagalan.** Degree/radian mismatch; angular derivatives memakai frame salah.

**Verifikasi.** Constant velocity/acceleration analytic fixtures dan rotating basis.

### D07.02 — Articulated chains

Joint transforms dikomposisikan dari root ke leaf. Degrees of freedom dan joint limits menentukan reachable configurations. Parent motion memengaruhi seluruh descendants.

**Model / prosedur.** T_end=T1(q1)T2(q2)…Tn(qn); pisahkan bind transform dan joint update convention.

**Kegagalan.** Wrong multiplication order; root scale mengubah limb length.

**Verifikasi.** Zero pose, one-joint rotations, and known end-effector positions.

### D07.03 — Forward kinematics

FK menghitung pose dari joint coordinates. Ia deterministik untuk chain dan convention yang tetap; general closed loops memerlukan constraint solution tambahan.

**Model / prosedur.** Two-link planar x=L1 cos q1+L2 cos(q1+q2), y=L1 sin q1+L2 sin(q1+q2).

**Kegagalan.** Degree inputs, offset joints, arbitrary hierarchy interpreted as simple chain.

**Verifikasi.** Compare analytic planar formula and matrix implementation.

### D07.04 — Inverse kinematics

IK menemukan joint coordinates untuk target. Solusi dapat banyak, tidak ada, atau singular. Position target saja tidak menetapkan orientation.

**Model / prosedur.** Analytic IK untuk chain sederhana; CCD, FABRIK, Jacobian methods untuk general tasks.

**Kegagalan.** Unreachable targets membuat NaN; elbow flips; ignored joint limits.

**Verifikasi.** Reachable/unreachable cases, residual, joint bounds, temporal continuity.

### D07.05 — Differential kinematics

Jacobian memetakan joint velocity menjadi task-space velocity lokal. Inversion dekat singularity perlu damping atau constrained solve.

**Model / prosedur.** v_task=J(q) qdot; damped inverse Jᵀ(JJᵀ+λ²I)⁻¹ mengurangi amplification.

**Kegagalan.** λ dianggap satu konstanta universal; finite-difference Jacobian tidak membagi perturbation.

**Verifikasi.** Compare analytic/numeric J dan sweep singular configurations.

### D07.06 — Constraints dan contact kinematics

Distance, orientation, attachment dan contact constraints mengurangi degrees of freedom. Contact foot placement berbeda dari physically correct reaction force.

**Model / prosedur.** Constraint C(q)=0; velocity consistency Jc qdot=0 untuk stationary constraint.

**Kegagalan.** Feet locked visually tetapi pelvis trajectory tak feasible.

**Verifikasi.** Position/velocity residual pada support interval dan contact switches.

### D07.07 — Trajectory smoothness

Position continuity tidak cukup untuk actuator atau plausible motion. Velocity, acceleration dan jerk bounds memengaruhi feasibility dan comfort.

**Model / prosedur.** Quintic polynomial dapat memenuhi position/velocity/acceleration endpoint constraints.

**Kegagalan.** Smooth-looking spline melebihi joint speed; no timing feasibility.

**Verifikasi.** Sample derivatives termasuk extrema, bukan hanya keyframes.

## Contoh kerja dan alasan pemilihan

Contoh two-link L1=L2=1. Target (1,1) memiliki elbow-up/down solutions. cos(q2)=(x²+y²−L1²−L2²)/(2L1L2)=0, jadi q2=±π/2. q1=atan2(y,x)−atan2(L2 sin q2,L1+L2 cos q2). Pilih cabang paling dekat pose sebelumnya untuk menghindari flips. Target (3,0) tidak reachable; laporkan residual atau project sesuai policy, jangan menyembunyikan kegagalan.

## Alur implementasi

Definisikan chain/frame/unit; implementasikan FK; verifikasi; pilih IK berdasarkan tugas; tambahkan limits dan continuity; tentukan trajectory timing; ukur residual dan derivative bounds.

## Kriteria penguasaan

Dapat mengimplementasikan planar FK/IK, mengenali singularity dan redundancy, serta memilih branch kontinu. Lab: target bergerak melewati boundary reachable region.

## Cabang lanjut yang tetap termasuk cakupan

Closed-chain kinematics; screw theory; redundant manipulators; task-priority IK; null-space objectives; nonholonomic kinematics; inverse differential kinematics.

## Rujukan dan batas bukti

- [S03](../../references/source-map.md#s03)
- [S14](../../references/source-map.md#s14)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
