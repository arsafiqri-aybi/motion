# D11 — Optimization and Inverse Problems

Mencari parameters, trajectories, atau controls yang memenuhi tujuan dan constraints melalui perhitungan.

Rumpun: **B — Motion Models**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Objective harus mencerminkan tujuan penggunaan. Cost minimum tidak membuktikan motion nyaman atau aman; model fidelity dan feasibility harus diperiksa secara independen.

Prasyarat: [D01](../../architecture/domain-map.md#d01), [D05](../../architecture/domain-map.md#d05), [D07](../../architecture/domain-map.md#d07), [D10](../../architecture/domain-map.md#d10).

## Subdomain dan pengetahuan inti

### D11.01 — Objective dan constraints

Objective memberi ranking solutions; constraints menentukan admissible set. Soft penalty tidak selalu menjamin hard constraint terpenuhi. Units dan scaling memengaruhi importance.

**Model / prosedur.** Minimize J(z) subject to g(z)≤0, h(z)=0; normalize terms memakai meaningful scales.

**Kegagalan.** Weight arbitrary mendominasi cost; collision penalty masih mengizinkan penetration.

**Verifikasi.** Report setiap cost term dan constraint violation secara terpisah.

### D11.02 — Gradients dan automatic differentiation

Gradients menjelaskan local sensitivity; AD menghitung derivative program menurut executed operations, bukan membetulkan discontinuous model.

**Model / prosedur.** Check ∂J/∂zᵢ dengan central finite differences pada perturbation ranges.

**Kegagalan.** Stop-gradient tidak sengaja, nondifferentiable branches, gradient overflow.

**Verifikasi.** Gradient check pada small deterministic fixture dan known analytic function.

### D11.03 — Least squares dan parameter fitting

Fitting motion parameters dari observations membutuhkan residual model dan weighting. Noise/outliers dan identifiability membatasi recovered parameters.

**Model / prosedur.** J=Σwᵢ norm(predictionᵢ−observationᵢ)²; robust losses dapat mengurangi outlier influence.

**Kegagalan.** Fitting trajectory dekat satu regime lalu extrapolate luas.

**Verifikasi.** Held-out trajectories, residual plots, confidence/identifiability analysis.

### D11.04 — Trajectory optimization

Variables dapat berupa samples, spline coefficients, atau controls. Time discretization dan collision checking di antara knots penting.

**Model / prosedur.** Penalize acceleration/jerk, constrain endpoints/dynamics/limits; direct collocation atau shooting.

**Kegagalan.** Smooth knots tetapi collision antarinterval; optimized duration salah dimension.

**Verifikasi.** Densely re-evaluate trajectory dan dynamics residual; independent collision checks.

### D11.05 — Inverse dynamics dan inverse simulation

Inverse problem mencari causes dari motion. Banyak force/parameter combinations dapat memberi observations serupa.

**Model / prosedur.** Given q,qdot,qddot, compute required τ dengan dynamics model; infer parameters with regularization.

**Kegagalan.** Numerical derivatives noise menghasilkan impossible forces.

**Verifikasi.** Synthetic recovery with known truth, noise sweep dan multiple initializations.

### D11.06 — Constrained solvers dan optimality

Local optimum bukan global optimum. Solver convergence perlu primal feasibility, stationarity, dan assumptions yang sesuai.

**Model / prosedur.** Inspect KKT residual ketika formulation mendukung; use bounds and trust regions.

**Kegagalan.** Success flag disamakan feasibility; initial guess menentukan poor branch.

**Verifikasi.** Multi-start, feasibility independent check, termination reason logging.

### D11.07 — Sensitivity dan multi-objective trade-offs

Latency, smoothness, accuracy, energy dan expressiveness dapat konflik. Pareto solutions membantu menjelaskan trade-off tanpa satu score palsu.

**Model / prosedur.** Sweep weights atau constrained objective; perturb measured parameters.

**Kegagalan.** Score tunggal menyembunyikan unacceptable limit violation.

**Verifikasi.** Pareto plot/table serta scenarios at extremes dan nominal.

## Contoh kerja dan alasan pemilihan

Contoh fit spring k,c dari observed positions. Tetapkan mass, initial state, clock dan measurement noise terlebih dahulu. Jika mass tidak diketahui, rasio k/m dan c/m dapat lebih identifiable daripada k,c secara terpisah. Evaluate predicted trajectory dengan solver yang cukup accurate; optimizer tidak boleh sekadar menyesuaikan solver error. Sisihkan sebagian trajectory untuk validasi dan laporkan parameter uncertainty.

## Alur implementasi

Definisikan variables/unit; tetapkan objective/constraints; cek differentiability; pilih solver; scale problem; evaluate residual; restart bila perlu; verify fitted result pada independent fixtures.

## Kriteria penguasaan

Dapat membedakan optimum, feasible dan physically meaningful; memeriksa gradients dan identifiability. Lab: fit noisy damped spring lalu test pada initial displacement berbeda.

## Cabang lanjut yang tetap termasuk cakupan

Optimal transport; Bayesian inverse problems; adjoint methods; mixed-integer planning; differentiable rendering; stochastic optimization; robust optimization; constrained learning.

## Rujukan dan batas bukti

- [S20](../../references/source-map.md#s20)
- [S03](../../references/source-map.md#s03)
- [S21](../../references/source-map.md#s21)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
