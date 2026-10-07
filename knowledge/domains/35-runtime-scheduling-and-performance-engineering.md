# D35 — Runtime Scheduling and Performance Engineering

Menjalankan motion dengan response dan resource use sesuai target tanpa mengubah model atau task semantics diam-diam.

Rumpun: **G — Engineering and Production**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Performance target harus menyebut device/workload/refresh rate. Average FPS tidak membuktikan deadline, input latency, atau smoothness semua frames.

Prasyarat: [D03](../../architecture/domain-map.md#d03), [D05](../../architecture/domain-map.md#d05), [D26](../../architecture/domain-map.md#d26).

## Subdomain dan pengetahuan inti

### D35.01 — Animation loop dan scheduling

Rendering clock and simulation clock berbeda. Browser callback timing bukan guaranteed fixed frequency. Work lifecycle menentukan apakah loop perlu aktif.

**Model / prosedur.** Use elapsed timestamps, fixed-step where needed, pause/offscreen policy.

**Kegagalan.** New loop every interaction; hidden-tab stall integrated unbounded.

**Verifikasi.** Single loop ownership, pause/resume, irregular frame times.

### D35.02 — Frame budgets dan distributions

Budget 1000/refreshHz ms adalah interval theoretical, bukan seluruh CPU time available. Tail frame times sering menjelaskan jank lebih baik mean FPS.

**Model / prosedur.** Report median/p95/p99/max frame intervals with measurement setup.

**Kegagalan.** Averaging hides isolated long stalls; CPU/GPU overlapped times summed incorrectly.

**Verifikasi.** Representative interactions, load spikes, refresh variability.

### D35.03 — Layout paint composite

DOM changes can trigger style/layout/paint/composite work. Effect cost depends geometry and engine, not property name alone.

**Model / prosedur.** Batch reads then writes; profile actual rendering pipeline.

**Kegagalan.** Repeated layout reads after writes; huge blur layers.

**Verifikasi.** Trace layout/paint events and compare controlled change.

### D35.04 — CPU GPU memory dan transfer

Bottleneck dapat computation, bandwidth, submission, readback atau synchronization. Resource lifetime affects peaks/leaks.

**Model / prosedur.** Time stages with appropriate CPU/GPU instrumentation and memory accounting.

**Kegagalan.** Async submission time claimed GPU execution.

**Verifikasi.** Large/small workload sweeps and repeated resource churn.

### D35.05 — Allocation garbage collection dan reuse

Frequent allocations can introduce pauses; pooling can retain excessive memory. Reuse chosen from measured behavior.

**Model / prosedur.** Preallocate bounded buffers; release ownership; avoid mutation conflicts.

**Kegagalan.** Unbounded pools; reuse corrupts active data.

**Verifikasi.** Allocation trace, peak memory, long session stability.

### D35.06 — Workers batching caching dan quality tiers

Parallelism and batching add overhead and data-transfer constraints. Adaptive quality should preserve essential task information.

**Model / prosedur.** Move separable computation; batch updates; expose tier policy with hysteresis.

**Kegagalan.** Quality oscillates each frame; worker output stale.

**Verifikasi.** Low capability, transfer cost, tier transitions and stale data.

### D35.07 — Profiling experiments dan regression

Optimize measured bottleneck, keeping correctness baseline. Benchmarks must record versions and environment.

**Model / prosedur.** Profile→hypothesis→controlled change→same workload compare.

**Kegagalan.** Claimed faster from single run; changed scene invalidates comparison.

**Verifikasi.** Repeat enough for variability, report distributions and correctness regression.

## Contoh kerja dan alasan pemilihan

Contoh 120Hz target has nominal 8.33ms presentation interval. A 7ms average CPU task does not guarantee fit: other work, GPU, input processing dan occasional 20ms allocations can miss frames. Measure representative distributions and identify which stage dominates. Reducing particles is a valid quality adaptation only if it preserves intended information and keeps transitions stable.

## Alur implementasi

Define targets/environment; establish correctness baseline; instrument stages; profile representative workloads; optimize bottleneck; test memory/lifecycle; document quality policy.

## Kriteria penguasaan

Dapat melaporkan measured frame distributions, mendiagnosis layout/GPU/GC, dan menjaga behavior setelah optimization.

## Cabang lanjut yang tetap termasuk cakupan

Real-time scheduling; browser pipelines; heterogeneous compute; performance modeling; energy/thermal constraints; memory allocators; scalable simulation; latency measurement.

## Rujukan dan batas bukti

- [S07](../../references/source-map.md#s07)
- [S78](../../references/source-map.md#s78)
- [S79](../../references/source-map.md#s79)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
