# D09 — Physics Simulation Systems

Membangun simulator bodies, contacts dan materials dari model fisik dan discretization yang dipilih.

Rumpun: **B — Motion Models**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

D08 menetapkan persamaan dan material; D10 membahas solver. Simulator perlu menyatakan target: plausibility visual, engineering accuracy, atau interactive response.

Prasyarat: [D02](../../architecture/domain-map.md#d02), [D08](../../architecture/domain-map.md#d08), [D10](../../architecture/domain-map.md#d10).

## Subdomain dan pengetahuan inti

### D09.01 — Particles dan mass-spring systems

Particle state memuat mass, position, velocity, forces. Connectivity springs menentukan system stiffness. Visual point-cloud bukan otomatis physical particle model.

**Model / prosedur.** Accumulate forces dari snapshot state, lalu advance seluruh system; pinned nodes memakai policy mass/integration jelas.

**Kegagalan.** Update order dependency; double-count pair force.

**Verifikasi.** Equal/opposite forces dan center-of-mass pada isolated system.

### D09.02 — Collision detection

Broad phase mencari candidate pairs; narrow phase menentukan contact geometry. Continuous collision detection diperlukan bila object dapat melewati obstacle antarsteps.

**Model / prosedur.** Swept shapes/time-of-impact atau conservative advancement; discrete checks hanya mengamati sample states.

**Kegagalan.** Tunneling, stale bounds, normals flipped.

**Verifikasi.** High-speed thin-wall cases, initial overlaps, and contact normal direction.

### D09.03 — Rigid-body contact

Contact response harus mempertimbangkan relative contact velocity, inertia dan restitution. Constraint solver iteratif memberi approximation dengan residual.

**Model / prosedur.** Normal impulse untuk bodies sederhana menjaga nonpenetration velocity; tangential impulse dibatasi friction cone.

**Kegagalan.** Restitution menambah energy berulang pada resting contact; solver jitter.

**Verifikasi.** Stacking, resting stability, impulse momentum balance, restitution sweeps.

### D09.04 — Soft bodies dan deformables

Surface/volume discretization membawa deformation DOFs. Methods seperti FEM atau position-based systems memiliki compliance dan convergence behavior berbeda.

**Model / prosedur.** Bentuk constraints atau energy dari rest configuration; solve deformation dengan boundary conditions.

**Kegagalan.** Rest state salah, inverted elements, parameter berubah dengan mesh resolution.

**Verifikasi.** Stretch/compression/bending fixtures dan mesh/time-step refinement.

### D09.05 — Cloth hair ropes

Thin structures membutuhkan tensile, bending, collision dan attachment models. Resolution, strand count dan self-collision memengaruhi behavior serta cost.

**Model / prosedur.** Discrete rods/springs/constraints; distinguish stretch stiffness dari bending stiffness.

**Kegagalan.** Overstretch, self-intersection, explosive collision corrections.

**Verifikasi.** Hanging strand, cloth drape, bending response, repeated contact.

### D09.06 — Fluids gases dan granular systems

Eulerian grids dan Lagrangian particles menukar strengths berbeda. Fluids membutuhkan pressure/incompressibility treatment; granular materials bergantung contact/friction.

**Model / prosedur.** Navier–Stokes discretization, SPH, PIC/FLIP/APIC atau discrete element sesuai tujuan.

**Kegagalan.** Volume loss, pressure instability, particle clustering, invalid boundary flux.

**Verifikasi.** Mass/volume checks, hydrostatic cases, divergence residual, refinement.

### D09.07 — Coupling dan simulation staging

Coupled systems bertukar forces, velocity, atau constraints. Update order dan subcycling dapat menambah lag/instability.

**Model / prosedur.** Tentukan explicit/implicit coupling, exchange rate, ownership dan conservation target.

**Kegagalan.** Double integration, delayed force feedback, mismatched units.

**Verifikasi.** Isolated subsystem baselines lalu coupling energy/impulse budget.

## Contoh kerja dan alasan pemilihan

Contoh ball-wall collision: body bergerak ke wall dengan contact normal mengarah menjauhi wall. Untuk static wall, normal component setelah collision adalah −e kali component masuk, 0≤e≤1. Tangential velocity mengikuti friction policy. Bila posisi sample sudah jauh menembus wall, velocity reflection saja tidak mengembalikan waktu collision yang benar. Gunakan time-of-impact atau substeps, lalu bedakan positional correction dari physical impulse.

## Alur implementasi

Tentukan fidelity dan scales; pilih representation; implementasikan isolated model; tambahkan collisions/constraints; ukur stability; refine timestep/resolution; simpan seeds, parameters dan diagnostic trajectories.

## Kriteria penguasaan

Dapat mengukur tunneling, constraint residual, energy drift dan mesh dependence; tidak menyamakan visually plausible dengan physical validation.

## Cabang lanjut yang tetap termasuk cakupan

Fracture; combustion; multiphase fluids; turbulence models; differentiable simulation; adaptive meshing; self-contact; coupled fluid–structure interaction; geophysical simulation.

## Rujukan dan batas bukti

- [S15](../../references/source-map.md#s15)
- [S16](../../references/source-map.md#s16)
- [S17](../../references/source-map.md#s17)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
