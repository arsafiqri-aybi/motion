# D39 — Motion Testing Measurement and Quality Engineering

Menentukan apa yang benar-benar dibuktikan oleh numerical, structural, visual, temporal, performance dan human checks.

Rumpun: **H — Verification and Delivery**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Tidak ada satu test yang membuktikan semua motion quality. Verifier dipilih per property dan hasilnya menyatakan scope/environment.

Prasyarat: [D03](../../architecture/domain-map.md#d03), [D10](../../architecture/domain-map.md#d10), [D34](../../architecture/domain-map.md#d34), [D35](../../architecture/domain-map.md#d35).

## Subdomain dan pengetahuan inti

### D39.01 — Unit property dan model tests

Pure math/models dapat diuji dengan analytic oracle dan invariants. Tests harus mendeteksi meaningful error, bukan menyalin implementation.

**Model / prosedur.** Endpoint/invariant/property checks plus independent formula or solver.

**Kegagalan.** Same bug in test and code; broad tolerances hide failures.

**Verifikasi.** Mutation sanity checks and adversarial boundaries.

### D39.02 — Numerical validation dan convergence

Error trajectory, residual dan conservation trends quantify solver properties. Physical validation membutuhkan external observations/model assumptions.

**Model / prosedur.** Compare refinement and independent reference; distinguish sources of error.

**Kegagalan.** One timestep agreement claimed universal accuracy.

**Verifikasi.** Whole trajectory, stiffness, discontinuity and conditioning cases.

### D39.03 — Temporal visual dan interaction regression

Motion changes between frames, not just frames. Timing, path, lifecycle and input response need sequence tests.

**Model / prosedur.** Sample known times plus replay interactions; compare timestamps and semantic states.

**Kegagalan.** Golden screenshot misses jump at unsampled time.

**Verifikasi.** Continuous/denser checks around events and playback review.

### D39.04 — Determinism compatibility dan replay

Repeated evaluation requires specified environment/versions/equivalence. Bit equality dan perceptual equivalence different guarantees.

**Model / prosedur.** Save seed/events/config; compare outputs with scoped tolerance/hash.

**Kegagalan.** Platform differences ignored; uncontrolled clocks.

**Verifikasi.** Repeated histories and actual target-platform matrix.

### D39.05 — Performance memory dan stress

Quality under load includes latency, tail frames, memory and recovery. Stress fixture must have expected bounds, not just run long.

**Model / prosedur.** Record workload/environment/distributions/peak memory and lifecycle counts.

**Kegagalan.** Only mean FPS; test machine mistaken all devices.

**Verifikasi.** Dense scenes, mount loops, stalls, resource failure.

### D39.06 — Accessibility usability dan perception

Automated checks cover subsets; human task/perception outcomes require participants and protocol.

**Model / prosedur.** Separate technical criterion results, manual review and human studies.

**Kegagalan.** AI review called user testing; reduced motion called full conformance.

**Verifikasi.** Keyboard/preferences, assistive tools, representative participants.

### D39.07 — Instrumentation reporting dan uncertainty

Test reports capture inputs, methods, timestamps, result and limitations. Unknown remains unknown.

**Model / prosedur.** PASS tied property/environment; FAIL reproducer; NOT_RUN reason; measured versus inferred fields.

**Kegagalan.** Entire repo marked verified from link checks.

**Verifikasi.** Report completeness, provenance, and ability to reproduce failure.

## Contoh kerja dan alasan pemilihan

Contoh spring regression uses analytic critical-damping solution and tests timestep refinement. Browser drag test checks event cancellation/final state; screenshot test checks crop; profiler checks frame timing. These are four different results. Bundle them without claiming analytic spring test proves UX comfort or screenshot proves interruption correctness.

## Alur implementasi

List required properties; choose independent verifiers; build fixtures; execute scoped tests; inspect visual/temporal outcomes; fix defects; write evidence and open gaps.

## Kriteria penguasaan

Dapat merancang tests yang membedakan numerical correctness, rendered content, runtime behavior dan human outcomes.

## Cabang lanjut yang tetap termasuk cakupan

Metamorphic testing; property-based generators; perceptual metrics; hardware-in-loop; system identification validation; benchmark design; uncertainty quantification; reproducibility audits.

## Rujukan dan batas bukti

- [S86](../../references/source-map.md#s86)
- [S87](../../references/source-map.md#s87)
- [S88](../../references/source-map.md#s88)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
