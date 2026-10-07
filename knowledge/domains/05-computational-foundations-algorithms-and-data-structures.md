# D05 — Computational Foundations Algorithms and Data Structures

Membuat representasi dan algoritma yang mengubah teori motion menjadi perhitungan efisien, dapat dilacak, dan cukup reproducible.

Rumpun: **A — Foundations**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Pembahasan algoritma umum diarahkan pada workload motion. Tuning frame runtime D35, API architecture D36, dan GPU execution D26 memiliki rincian khusus.

Prasyarat: [D01](../../architecture/domain-map.md#d01).

## Subdomain dan pengetahuan inti

### D05.01 — Numeric representation

Float32 dan Float64 mempunyai precision/range berbeda. Error berulang, cancellation, dan magnitude besar memengaruhi local motion kecil. Precision dipilih menurut unit dan skala scene.

**Model / prosedur.** Machine epsilon adalah properti format, bukan tolerance seluruh problem. Rebase origin atau gunakan local coordinates untuk world besar.

**Kegagalan.** Subtract dua posisi besar yang hampir sama; float equality dipakai untuk convergence.

**Verifikasi.** Uji coordinates dekat nol dan jauh dari origin; compare terhadap higher-precision reference.

### D05.02 — Complexity dan workload

Big-O menjelaskan scaling, tetapi constant cost, cache behavior, dan upload overhead menentukan runtime nyata. Broad-phase yang bagus dapat mengurangi candidate pairs jauh sebelum solver.

**Model / prosedur.** All-pairs particles O(n²); spatial bins sering mengurangi workload lokal, tetapi worst-case tetap padat.

**Kegagalan.** Benchmark hanya n kecil; histogram distribusi scene tidak mewakili worst case.

**Verifikasi.** Scaling sweep n, sparse/dense scenes, cold/warm cache, dan peak allocation.

### D05.03 — Data layout

Array of structures mudah dipakai; structure of arrays dapat menguntungkan vectorized operations. Data ownership dan mutation harus jelas agar render tidak membaca partially updated state.

**Model / prosedur.** Pisahkan x[],y[],vx[],vy[] untuk contiguous per-attribute updates; double-buffer previous/current state jika dibutuhkan.

**Kegagalan.** Allocasi object setiap frame; state/render buffer saling menimpa.

**Verifikasi.** Check layout correctness dengan known fixtures; ukur allocation count dan cache-friendly workload.

### D05.04 — Graphs dan traversal

Scene tree, skeleton hierarchy, dependency graph, dan planning graph punya edge semantics berbeda. Graph evaluator perlu cycle policy, stable order, dan invalidation.

**Model / prosedur.** Kahn/DFS topological sort untuk DAG; BFS shortest path pada unweighted graph; Dijkstra untuk nonnegative costs.

**Kegagalan.** Dijkstra dengan negative weights; shared child dianggap tree unique parent.

**Verifikasi.** Diamond graph, disconnected graph, cycle, repeated node, dan traversal deterministic.

### D05.05 — Spatial structures

Uniform grids, quad/octrees, k-d trees, BVHs memilih trade-off build/update/query. Moving objects dapat memerlukan refit atau rebuild. Struktur terbaik bergantung distribusi data.

**Model / prosedur.** Grid neighbor query radius r harus mengecek cukup cells; BVH bounds refit setelah geometry berubah.

**Kegagalan.** Cell terlalu kecil/besar; stale index; missed neighbors pada batas cell.

**Verifikasi.** Bandingkan semua hits dengan brute force dan uji moving across cell boundaries.

### D05.06 — Caching dan incremental computation

Cache berguna jika key mencakup seluruh dependency yang memengaruhi output. Derived data seperti arc-length LUT invalid bila control points, transform relevan, atau tolerance berubah.

**Model / prosedur.** Cache key dapat memuat content hash, version, model parameters; dirty flags harus propagated secara lengkap.

**Kegagalan.** Cache stale terlihat sebagai easing bug; cache mengubah numerical trajectory tanpa catatan.

**Verifikasi.** Edit satu dependency per fixture dan pastikan hanya caches relevan berubah.

### D05.07 — Parallelism dan reproducibility

Independent jobs dapat berjalan paralel; reductions dan race conditions perlu aturan ordering. Floating-point addition tidak associative sehingga thread order bisa mengubah hasil.

**Model / prosedur.** Pisahkan phases read/update/commit; fixed reduction order memberi replay lebih stabil, tetapi cross-device bit equality tetap perlu dibuktikan.

**Kegagalan.** Concurrent mutation, nondeterministic random stream, atomics dianggap deterministic.

**Verifikasi.** Replay seeds/input berulang; bandingkan single/multithread dan catat numerical tolerance.

## Contoh kerja dan alasan pemilihan

Contoh: 10.000 particles dengan neighbor radius tetap. Brute-force mempunyai sekitar 50 juta unordered pairs. Uniform grid memakai cell width sebanding radius dan mengunjungi cells tetangga, lalu exact distance filter. Pastikan negative coordinates memakai floor, bukan truncation. Performa membaik pada distribusi sparse; semua particles dalam satu cell tetap worst-case kuadratik. Karena itu benchmark harus mencakup cluster padat, bukan hanya titik random merata.

## Alur implementasi

Definisikan workload dan constraints; pilih representation; tulis baseline benar; pilih acceleration; compare hasil dengan oracle; ukur scaling/memory; nyatakan replay guarantees dan limitations.

## Kriteria penguasaan

Dapat memilih struktur data berdasarkan query dan update rate, menunjukkan correctness terhadap baseline, dan mendiagnosis cache invalidation. Latihan: spatial grid yang mendukung particles melewati cell boundaries.

## Cabang lanjut yang tetap termasuk cakupan

SIMD; lock-free structures; task graphs; streaming algorithms; out-of-core computation; interval/exact arithmetic; automatic differentiation data structures; incremental compilation; deterministic parallel reductions.

## Rujukan dan batas bukti

- [S02](../../references/source-map.md#s02)
- [S10](../../references/source-map.md#s10)
- [S11](../../references/source-map.md#s11)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
