# D08 — Dynamics and Physical Modeling

Memilih persamaan yang menjelaskan pengaruh force, inertia, energy, dan material terhadap motion.

Rumpun: **B — Motion Models**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Ini model fisik, bukan jaminan simulated motion tampak benar. Solver D10, collision/contact D09, control D12 dan perceptual plausibility D32 harus dipisahkan.

Prasyarat: [D01](../../architecture/domain-map.md#d01), [D07](../../architecture/domain-map.md#d07).

## Subdomain dan pengetahuan inti

### D08.01 — Newtonian motion

Force mengubah momentum; untuk mass tetap acceleration=force/mass. Gerak dalam inertial frame berbeda dari rotating frame yang memerlukan apparent force terms.

**Model / prosedur.** m x″=ΣF; integrate state position/velocity setelah mass dan initial conditions valid.

**Kegagalan.** Force salah unit, mass nol dipakai sebagai body dinamis.

**Verifikasi.** Free-flight analytic trajectory dan force/mass scaling.

### D08.02 — Rotational dynamics

Moment of inertia berbentuk tensor dan bergantung geometry/frame. Torque tidak cukup dibagi scalar arbitrary pada general 3D rigid body.

**Model / prosedur.** τ=I α+ω×(Iω) dalam body-frame formulation yang sesuai.

**Kegagalan.** World/body inertia tercampur; angular momentum tidak dijaga.

**Verifikasi.** Torque-free rotation dan principal-axis fixtures; energy/momentum drift.

### D08.03 — Energy momentum dan conservation

Conservation adalah invariant model ideal, bukan seluruh simulasi. Drag, damping, contacts inelastic dan external forces mengubah energy atau momentum.

**Model / prosedur.** K=½m v²; spring U=½k x²; conservative system ideal menjaga K+U.

**Kegagalan.** Numerical damping dianggap physical damping; energy rise selalu dianggap bug padahal ada external work.

**Verifikasi.** Energy budget mencatat work, dissipation, dan integration error.

### D08.04 — Springs dan damping

Damped spring membentuk second-order response. Damping ratio mengelompokkan under/critical/overdamped behavior untuk linear fixed-coefficient system.

**Model / prosedur.** m x″+c x′+k(x−target)=0; ωn=√(k/m), ζ=c/(2√km).

**Kegagalan.** k/c diperbesar tanpa memperkecil timestep; target discontinuity mengubah force tajam.

**Verifikasi.** Step response, settling metrics dengan definition, and solver convergence.

### D08.05 — Friction drag dan dissipation

Friction contact dan drag medium berbeda model. Coulomb friction berkaitan normal force; viscous damping proportional velocity.

**Model / prosedur.** Drag linear F=−b v; quadratic F=−½ρCd A norm(v)v; friction bound norm(Ft)≤μFn.

**Kegagalan.** Friction force mempercepat body; static/kinetic friction disamakan.

**Verifikasi.** Force opposes relative motion; parameter/unit sanity dan zero-speed behavior.

### D08.06 — Generalized dynamics

Lagrangian formulation menggunakan generalized coordinates; constraints dan force projection perlu consistent conventions.

**Model / prosedur.** L=T−V; d/dt(∂L/∂qdot)−∂L/∂q=Q. Robotics form M(q)qddot+C+g=τ.

**Kegagalan.** Energy expressions salah frame; constrained DOFs counted twice.

**Verifikasi.** Compare simple pendulum analytic equation and Newtonian formulation.

### D08.07 — Material dan continuum models

Soft-body, cloth dan fluids membutuhkan constitutive assumptions: stress-strain, viscosity, incompressibility, plasticity. Parameter calibrated menentukan meaningful physics.

**Model / prosedur.** Tentukan continuum equations, boundary conditions, discretization dan material regime sebelum solver.

**Kegagalan.** Visual stretch parameter diklaim modulus fisik; incompressibility hanya berdasarkan volume satu frame.

**Verifikasi.** Unit checks, known deformation tests, mesh refinement and parameter sensitivity.

## Contoh kerja dan alasan pemilihan

Contoh spring mass m=1, k=100 memberi ωn=10 rad/s. Critical damping c=20, bukan nilai damping persentase arbitrary. Untuk initial displacement x0 dan zero velocity terhadap target tetap, critical response adalah x(t)=x0(1+10t)e^(−10t). Model ini cocok sebagai oracle numerik. Saat target ikut bergerak, definisikan apakah damping terhadap world velocity atau velocity relatif target; keduanya berbeda.

## Alur implementasi

Nyatakan system boundaries; pilih coordinates/units; daftar forces dan constraints; tetapkan material/parameter assumptions; turunkan invariants; pilih solver; kalibrasi hanya dengan observations yang relevan.

## Kriteria penguasaan

Dapat menurunkan damped spring, menghitung damping ratio, dan mengaudit energy budget. Lab: pisahkan physical damping dari numerical dissipation.

## Cabang lanjut yang tetap termasuk cakupan

Hamiltonian systems; multibody dynamics; constitutive mechanics; viscoelasticity; elastoplasticity; continuum mechanics; fluid dynamics; stochastic dynamics.

## Rujukan dan batas bukti

- [S03](../../references/source-map.md#s03)
- [S15](../../references/source-map.md#s15)
- [S16](../../references/source-map.md#s16)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
