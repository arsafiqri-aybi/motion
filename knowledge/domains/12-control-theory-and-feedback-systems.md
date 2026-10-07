# D12 — Control Theory and Feedback Systems

Mengatur motion berdasarkan reference, estimated state, dan feedback agar tracking atau stabilization sesuai constraints.

Rumpun: **B — Motion Models**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Controller mengendalikan model/plant; animation evaluator saja tidak selalu plant. Physical deployment membutuhkan D31 dan verifikasi hardware, bukan menyalin UI spring parameters.

Prasyarat: [D01](../../architecture/domain-map.md#d01), [D08](../../architecture/domain-map.md#d08), [D10](../../architecture/domain-map.md#d10).

## Subdomain dan pengetahuan inti

### D12.01 — Feedforward dan feedback

Feedforward menggunakan reference/model; feedback mengoreksi error observed. Keduanya dapat digabung, tetapi measurement delay mengubah closed-loop dynamics.

**Model / prosedur.** u=u_ff+K(reference−estimate); jelaskan sign, units dan available state.

**Kegagalan.** Gain sign salah; controller correction memperbesar error.

**Verifikasi.** Step/disturbance response dan measurement-delay sweep.

### D12.02 — PID dan saturation

Integral mengurangi steady-state error tetapi dapat wind up saat actuator saturated. Derivative peka terhadap noise dan setpoint kick.

**Model / prosedur.** u=Kp e+Ki∫e dt+Kd e′; use anti-windup and filtered derivative.

**Kegagalan.** Integral accumulates during pause, derivative divided wrong dt.

**Verifikasi.** Saturate plant, release saturation, observe recovery and overshoot.

### D12.03 — State-space models

State harus cukup untuk prediction berikutnya. Linear model lokal punya validity region; discretization bergantung sample period.

**Model / prosedur.** xdot=Ax+Bu, y=Cx+Du; discrete model x_next=Ad x+Bd u.

**Kegagalan.** Reuse discrete gains at different timestep without review.

**Verifikasi.** Model prediction versus observed/reference state across operating range.

### D12.04 — Stability observability controllability

Stability membatasi response perturbations. State tidak observable dari measurements tertentu; actuator tidak dapat mengontrol semua modes.

**Model / prosedur.** Eigenvalue analysis untuk linear models; rank tests untuk controllability/observability under assumptions.

**Kegagalan.** Stable poles dianggap robust terhadap arbitrary delay/nonlinearity.

**Verifikasi.** Perturb initial conditions, inspect modes, and validate model assumptions.

### D12.05 — Estimation dan system identification

Controller memakai estimated state; noise, drift dan missing measurements perlu explicit handling. Identification memerlukan excitation yang informative.

**Model / prosedur.** Fit model dari input/output; Kalman-like estimator combines prediction and observations.

**Kegagalan.** Measurement interpreted as truth; unexcited parameters claimed identified.

**Verifikasi.** Prediction residual, held-out input sequences, missing sensor response.

### D12.06 — Optimal robust dan predictive control

LQR/MPC memilih actions menurut model/cost. MPC dapat mengatasi constraints tetapi membutuhkan timely solve dan fallback. Robust control mempertimbangkan specified uncertainty.

**Model / prosedur.** Receding horizon: estimate, solve constrained horizon, execute first action, repeat.

**Kegagalan.** Missed deadline, infeasible optimization, incorrect uncertainty bounds.

**Verifikasi.** Constraint/solve-time statistics, fault injection, safe fallback behavior.

### D12.07 — Tracking dan disturbance rejection

Reference trajectory punya derivatives dan feasibility. High gain dapat improve tracking tetapi amplify noise atau excite unmodeled dynamics.

**Model / prosedur.** Track position/velocity with feedforward acceleration when valid; low-pass reference if necessary.

**Kegagalan.** Following unreachable trajectory; tuning only no-disturbance case.

**Verifikasi.** Steady-state/transient error, disturbance recovery, bandwidth and actuator effort.

## Contoh kerja dan alasan pemilihan

Contoh virtual camera tracking target with PD force: a=Kp(target−x)+Kd(v_target−v). Gains memiliki unit 1/s² dan 1/s. Untuk target tetap, pilih Kp=ω² dan Kd=2ζω dalam model acceleration command. Ketika camera collision blocks motion, integral tambahan dapat wind up; jangan tambahkan I hanya untuk terlihat lengkap. Ukur error dan overshoot dengan targets bergerak serta delayed input.

## Alur implementasi

Definisikan plant/state/reference; identifikasi rates/delays; pilih controller; enforce action limits; instrument errors/actions; test disturbances; add fallback; validate hardware separately if applicable.

## Kriteria penguasaan

Dapat menurunkan simple PD, menangani saturation dan delay, membedakan simulation stability dari control stability.

## Cabang lanjut yang tetap termasuk cakupan

Nonlinear control; Lyapunov methods; passivity; adaptive control; robust control; hybrid control; distributed control; learning-based control.

## Rujukan dan batas bukti

- [S03](../../references/source-map.md#s03)
- [S22](../../references/source-map.md#s22)
- [S23](../../references/source-map.md#s23)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
