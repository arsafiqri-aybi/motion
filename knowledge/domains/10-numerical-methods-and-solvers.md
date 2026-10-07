# D10 — Numerical Methods and Solvers

Mengaproksimasi persamaan motion pada komputer dengan batas stability, accuracy, cost, dan convergence yang jelas.

Rumpun: **B — Motion Models**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Solver sukses menjalankan iteration belum membuktikan model benar. Model D08 dan validation D39 memberi pertanyaan terpisah.

Prasyarat: [D01](../../architecture/domain-map.md#d01), [D05](../../architecture/domain-map.md#d05), [D08](../../architecture/domain-map.md#d08).

## Subdomain dan pengetahuan inti

### D10.01 — Explicit integration

Forward Euler murah tetapi dapat menambah energy pada oscillator. Semi-implicit Euler memperbarui velocity lalu position dan mempunyai sifat berbeda.

**Model / prosedur.** Euler x_next=x+h v; v_next=v+h a(x,v). Semi-implicit memakai v_next pada update x.

**Kegagalan.** Semua metode diberi label Euler; fixed dt terlalu besar.

**Verifikasi.** Compare analytic oscillator, energy behavior, dan convergence saat h dibagi dua.

### D10.02 — Higher-order integration

RK methods mengevaluasi derivative beberapa kali. Order tinggi membantu smooth ODE, tetapi collision discontinuities dan stiffness dapat membatasi manfaatnya.

**Model / prosedur.** RK4 menggunakan empat derivative stages; local/global error order berlaku dengan assumptions smoothness.

**Kegagalan.** Force side effects di stage; collision impulse diterapkan berkali-kali.

**Verifikasi.** Smooth analytic ODE convergence plus event/discontinuity fixtures.

### D10.03 — Implicit dan stiff systems

Stiffness dapat memaksa explicit step sangat kecil. Implicit methods membutuhkan nonlinear solve dan tolerance; stable tidak berarti accurate.

**Model / prosedur.** Backward Euler y_next=y+h f(y_next), diselesaikan via Newton atau other solver.

**Kegagalan.** Newton converges ke unsuitable branch; terlalu banyak numerical damping.

**Verifikasi.** Residual, iteration counts, step refinement, dan comparison independent method.

### D10.04 — Constraint solvers

Iterative solving menghasilkan residual yang bergantung iterations, timestep, ordering dan conditioning. Position projection bukan identik impulse dynamics.

**Model / prosedur.** Gauss–Seidel/Jacobi, projected methods, XPBD compliance conventions sesuai formulation.

**Kegagalan.** Stiffness berubah saat fps berubah; warm-start cache stale.

**Verifikasi.** Sweep dt/iterations, constraint error, resting stability, and ordering sensitivity.

### D10.05 — Linear algebra dan conditioning

Sistem Ax=b yang ill-conditioned memperbesar perturbations. Sparse structure dan preconditioner memengaruhi cost dan convergence.

**Model / prosedur.** Direct factorization atau iterative CG untuk SPD; method assumptions diperiksa sebelum pemakaian.

**Kegagalan.** CG pada indefinite matrix; stopping berdasarkan iterations tanpa residual.

**Verifikasi.** Compute norm(Ax−b), compare reference solve, perturb b sedikit.

### D10.06 — Adaptive step dan error control

Adaptive integrator mengubah h berdasarkan error estimate. Event detection diperlukan agar collision atau switch terjadi pada waktu tepat.

**Model / prosedur.** Embedded RK estimate menentukan accept/reject dan next step; min/max h serta event bracketing eksplisit.

**Kegagalan.** Tolerance salah unit; rejected step mengubah RNG/state permanent.

**Verifikasi.** Accepted/rejected history, event-time accuracy, reproducibility.

### D10.07 — Verification dan error budgets

Discretization, truncation, rounding, solver residual dan model mismatch adalah sumber error berbeda. Refinement membuktikan trend numerik pada problem tertentu.

**Model / prosedur.** Compare h,h/2,h/4; estimate observed order saat asymptotic regime tercapai.

**Kegagalan.** Single PASS dekat sample endpoint; numerical agreement dianggap physical truth.

**Verifikasi.** Entire trajectory error, invariant drift, pathological inputs dan finite-output guards.

## Contoh kerja dan alasan pemilihan

Contoh x′=−x, x(0)=1 mempunyai solusi e^(−t). Euler x_next=x(1−h). Dengan h=0.1 dan 0.05, bandingkan error pada t=1 dan seluruh trajectory. Error semestinya turun kira-kira sesuai first-order behavior ketika h cukup kecil. Untuk x′=−1000x, langkah 0.1 tidak stable; menaikkan precision tidak memperbaiki timestep yang salah. Stability region dan accuracy target harus dipisahkan.

## Alur implementasi

Tetapkan ODE/constraints; buat analytic/reference cases; pilih solver assumptions; set unit-aware tolerances; instrument residual/iterations; run refinement; bound execution; document convergence limitations.

## Kriteria penguasaan

Dapat memilih integration method berdasarkan stiffness dan invariants, membaca residual, serta menolak hasil nonfinite. Lab: error-convergence table untuk Euler versus RK4.

## Cabang lanjut yang tetap termasuk cakupan

Symplectic integration; geometric integration; DAE solvers; multigrid; FEM/FVM discretization; Krylov methods; adaptive PDE solvers; interval verification.

## Rujukan dan batas bukti

- [S18](../../references/source-map.md#s18)
- [S19](../../references/source-map.md#s19)
- [S07](../../references/source-map.md#s07)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
