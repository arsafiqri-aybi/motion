# D13 — Motion Planning and Navigation

Menentukan jalur dan timing yang dapat mencapai tujuan sambil menghormati obstacles, kinematic limits, serta interaksi agen.

Rumpun: **B — Motion Models**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Path adalah geometri; trajectory juga mencakup timing. Planner success harus diverifikasi pada representation dan physical bounds yang dipakai runtime.

Prasyarat: [D02](../../architecture/domain-map.md#d02), [D05](../../architecture/domain-map.md#d05), [D07](../../architecture/domain-map.md#d07), [D11](../../architecture/domain-map.md#d11).

## Subdomain dan pengetahuan inti

### D13.01 — Configuration space

Obstacles dalam workspace harus diterjemahkan menjadi forbidden configurations. Shape, orientation dan articulated geometry menentukan collision.

**Model / prosedur.** Point robot dengan radius r dapat memakai obstacle inflation bila assumptions planar/circular sesuai.

**Kegagalan.** Center point clear tetapi body collision; orientation ignored.

**Verifikasi.** Full-body collision check terhadap path samples dan segments.

### D13.02 — Graph search

A*/Dijkstra mencari path pada graph, bukan seluruh ruang kontinu. Heuristic properties menentukan optimality guarantees pada assumptions tertentu.

**Model / prosedur.** A* memakai f=g+h; admissible h tidak overestimate remaining cost.

**Kegagalan.** Negative edge costs, heuristic salah units, disconnected endpoints.

**Verifikasi.** Compare small cases dengan exhaustive/Dijkstra oracle.

### D13.03 — Sampling-based planning

PRM/RRT keluarga mengeksplorasi configuration space melalui samples. Resolution collision checking menentukan missed obstacles.

**Model / prosedur.** Sample configuration, connect/extend, validate edges; seed and stopping budget recorded.

**Kegagalan.** Planner sample nodes safe tetapi edges unsafe.

**Verifikasi.** Narrow passages, disconnected space, reproducible seed sweeps.

### D13.04 — Local navigation dan steering

Local responses cepat tetapi bisa local minima atau oscillation. Global plan dan local collision handling harus punya reconciliation.

**Model / prosedur.** Seek/avoid/arrive rules; potential fields or velocity-space methods with specified constraints.

**Kegagalan.** Agents stuck symmetric configuration; summed forces violate limits.

**Verifikasi.** Deadlocks, corners, opposing streams, bounded speed/acceleration.

### D13.05 — Trajectory generation

Geometric path diberi time law yang memenuhi velocity, acceleration dan jerk limits. Smooth path tidak menjamin feasible timing.

**Model / prosedur.** Piecewise trapezoidal/S-curve profile atau constrained time parameterization.

**Kegagalan.** Abrupt corners demand infinite acceleration; endpoints omit required velocity.

**Verifikasi.** Derivative bounds and timing consistency across path joins.

### D13.06 — Multi-agent coordination

Agent intentions, priorities dan communication affect shared space. Collision-free individual paths dapat conflict saat times overlap.

**Model / prosedur.** Space-time reservation, reciprocal avoidance, centralized planning sesuai workload.

**Kegagalan.** Shared targets deadlock; priority starvation; stale peer state.

**Verifikasi.** Dense crossings, communication delay and fairness criteria.

### D13.07 — Online replanning dan uncertainty

Scene dapat berubah setelah planning. Replanning perlu state continuity dan bounded reaction latency. Uncertain obstacles require margins matched assumptions.

**Model / prosedur.** Validate upcoming horizon; recompute or emergency fallback when invalidated.

**Kegagalan.** Teleport to new path, velocity jump, infinite replanning loop.

**Verifikasi.** Moving obstacles, target changes, planner timeouts, path handoff residual.

## Contoh kerja dan alasan pemilihan

Contoh robot disk radius 0.2m di corridor. Inflate planar obstacles 0.2m lalu plan centerline; ini benar hanya untuk disk dengan orientation-independent footprint. Setelah path ditemukan, tambahkan timing dan collision check continuous segments. Jika robot sebenarnya rectangle, inflation disk dapat terlalu konservatif atau tidak cukup; configuration-space representation harus berubah.

## Alur implementasi

Pilih configuration representation; specify collision model; build planner; verify edges; parameterize time; connect controller; handle invalidation; test narrow passages and replanning.

## Kriteria penguasaan

Dapat membedakan path/trajectory, menjelaskan graph heuristic assumptions, dan memverifikasi swept collision.

## Cabang lanjut yang tetap termasuk cakupan

Kinodynamic planning; nonholonomic planning; belief-space planning; task-and-motion planning; navigation under uncertainty; swarm coordination; optimization-based planning.

## Rujukan dan batas bukti

- [S03](../../references/source-map.md#s03)
- [S14](../../references/source-map.md#s14)
- [S24](../../references/source-map.md#s24)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
