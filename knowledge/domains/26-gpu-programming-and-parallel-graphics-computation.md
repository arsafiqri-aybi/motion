# D26 — GPU Programming and Parallel Graphics Computation

Mengeksekusi rendering/simulation pada GPU dengan contracts untuk memory, pipelines, parallelism dan precision.

Rumpun: **E — Graphics and Output**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Shader language adalah implementation layer. GPU speed tidak menggantikan model correctness; actual support/limits harus diuji pada target.

Prasyarat: [D05](../../architecture/domain-map.md#d05), [D24](../../architecture/domain-map.md#d24), [D25](../../architecture/domain-map.md#d25).

## Subdomain dan pengetahuan inti

### D26.01 — Pipeline stages

Vertex, fragment dan compute stages mempunyai inputs/outputs dan execution semantics berbeda. Work submission asynchronous terhadap CPU.

**Model / prosedur.** Declare resource bindings, layouts and render/compute passes; respect stage capabilities.

**Kegagalan.** CPU timestamp treated GPU completion; shader interface mismatch.

**Verifikasi.** Minimal known pipeline, validation messages and measured completion where available.

### D26.02 — Buffers textures dan layouts

Alignment, stride, type formats and usage flags determine data interpretation. CPU struct layout must match GPU ABI.

**Model / prosedur.** Use explicit byte offsets/strides and format conversions; bounds based resource dimensions.

**Kegagalan.** Silent corrupt uniforms; index out-of-range.

**Verifikasi.** Known patterns through buffers/textures, boundary indices and layout assertions.

### D26.03 — Parallel work dan races

Work items execute concurrently; ordering absent unless guaranteed synchronization. Atomics provide specific operations, not general sequence determinism.

**Model / prosedur.** Separate phases/passes; use barriers only at supported scope; avoid read/write conflict.

**Kegagalan.** Barrier assumed cross-workgroup; floating reduction nondeterministic.

**Verifikasi.** Small oracle compare, repeated runs and adversarial scheduling inputs.

### D26.04 — Shader math dan precision

Float precision, derivatives and interpolation affect rendered motion. Branch divergence and numeric singularities need handling.

**Model / prosedur.** Guard divisions/normalization; choose precision by scale; handle discontinuous derivatives.

**Kegagalan.** NaN propagates texture coordinates; artifacts at large world positions.

**Verifikasi.** Extreme coordinates, near-zero input, shader debug visualizations.

### D26.05 — Compute-driven motion

GPU can update particles/fields then feed render pipeline. Dataflow and previous/current state ownership determine correctness.

**Model / prosedur.** Ping-pong buffers/textures; dispatch counts rounded with bounds guard.

**Kegagalan.** Last group writes beyond particle count; update in place conflicts neighbors.

**Verifikasi.** Counts not multiple group size, deterministic fixtures and CPU reference.

### D26.06 — Optimization and measurement

Batching/instancing reduce submissions; memory bandwidth, occupancy and overdraw can dominate. GPU timings are device-dependent.

**Model / prosedur.** Measure representative passes; reduce transfers; profile bottleneck before changing algorithms.

**Kegagalan.** Optimizing arithmetic while transfer bound; synchronous readback stalls.

**Verifikasi.** Target-device traces, batch size sweeps, dense/sparse scenes.

### D26.07 — Portability validation dan recovery

API versions/extensions/limits differ; context/device loss needs fallback. Shader translation does not guarantee behavior equivalent.

**Model / prosedur.** Feature detection, validation layer where supported, graceful fallback, resource rebuild.

**Kegagalan.** Unsupported format assumed universal; lost device loop retries indefinitely.

**Verifikasi.** Capability-limited path, resource rebuild, unsupported features.

## Contoh kerja dan alasan pemilihan

Contoh GPU particles: compute pass reads positions/velocities A and writes B; render reads B; next simulation swaps roles. Every invocation checks index<N. Neighbor interactions must read consistent A, not partly updated B. Benchmark simulation, rendering and uploads separately. A tiny system can be slower GPU-bound due overhead, so keep CPU reference for correctness and small workloads.

## Alur implementasi

Establish capabilities/layouts; implement minimal pipeline; verify oracle; define pass synchronization; add realistic workload; profile; support cleanup/loss/fallback.

## Kriteria penguasaan

Dapat membaca GPU data layout, mencegah race/out-of-bounds, dan memisahkan CPU submission dari GPU completion.

## Cabang lanjut yang tetap termasuk cakupan

WGSL/GLSL/HLSL; CUDA-like compute; subgroup operations; indirect draws; bindless resources; GPU BVHs; tiled rendering; GPU fluid simulation.

## Rujukan dan batas bukti

- [S54](../../references/source-map.md#s54)
- [S55](../../references/source-map.md#s55)
- [S56](../../references/source-map.md#s56)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
