# D36 — Motion Software Architecture and Systems Engineering

Mengorganisasikan motion code dengan contracts, ownership, reproducibility dan integration boundaries yang dapat dipelihara.

Rumpun: **G — Engineering and Production**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Architecture mengikuti kebutuhan nyata; tidak semua prototype membutuhkan ECS/plugin framework. Engineering depth diukur dari correctness dan maintainability, bukan jumlah abstractions.

Prasyarat: [D05](../../architecture/domain-map.md#d05), [D19](../../architecture/domain-map.md#d19), [D20](../../architecture/domain-map.md#d20).

## Subdomain dan pengetahuan inti

### D36.01 — Model behavior rendering separation

Motion models, interaction goals dan presentation depend berbeda. Separation memungkinkan headless testing and alternate renderers.

**Model / prosedur.** Input→intent/state→model evaluator→scene snapshot→renderer.

**Kegagalan.** Renderer changes physics state; UI lifecycle owns global solver.

**Verifikasi.** Headless model fixtures and alternate rendering adapters.

### D36.02 — Ownership lifecycle dan resources

Transform, loop, listeners, buffers dan assets mempunyai owner dan lifetime. Shared ownership requires explicit reference/disposal rules.

**Model / prosedur.** Create/use/dispose contracts; property arbitration; immutable snapshots where practical.

**Kegagalan.** Multiple writers, memory leak, disposed shared texture.

**Verifikasi.** Repeated mounts/scenes, dispose idempotence and no post-dispose effects.

### D36.03 — Entity component dan scene architecture

ECS suits many similar entities; scene graph suits hierarchy. Hybrid is possible with clear sync boundaries.

**Model / prosedur.** Choose data layout/query patterns; keep transform hierarchy consistent.

**Kegagalan.** Premature ECS hides simple behavior; duplicate state systems diverge.

**Verifikasi.** Scale workload and scene/physics consistency tests.

### D36.04 — APIs plugins dan contracts

Extensions need typed/schema interfaces, units and versioning. Capability discovery determines what adapter really supports.

**Model / prosedur.** Validate inputs, name versions, document effects and errors.

**Kegagalan.** Accept malformed data; plugin claims all formats.

**Verifikasi.** Contract fixtures, incompatible versions and unsupported operation.

### D36.05 — Deterministic evaluation replay dan snapshots

Reproducibility requires inputs, seed, clock semantics, versions and model parameters. Stateful simulations need checkpoints.

**Model / prosedur.** Record event log/snapshots; compare outputs under defined equivalence.

**Kegagalan.** Seed-only reproducibility claim; hidden system clock dependencies.

**Verifikasi.** Replay histories, checkpoint recovery, platform tolerance checks.

### D36.06 — Error recovery dan degradation

Failures must preserve coherent task state. Visual failure should not silently change source truth.

**Model / prosedur.** Define recoverable errors, bounded retries, fallback renderer/motion, observability.

**Kegagalan.** Infinite retries or quietly missing important content.

**Verifikasi.** Resource load failure, device loss, invalid model state.

### D36.07 — Integration documentation dan maintenance

Motion integrates routing, layout, assets, sensors and deployment. Changes need versioned contracts and migration guidance.

**Model / prosedur.** Record dependencies and rationale; update schema/examples together.

**Kegagalan.** Library upgrade changes timing unnoticed.

**Verifikasi.** Integration matrix and migration/regression fixtures.

## Contoh kerja dan alasan pemilihan

Contoh pure spring module advances {x,v} using dt/target/parameters; controller chooses target; renderer draws current x. Headless tests can compare analytic oracle without browser. UI teardown cancels loop/listeners but does not mutate historical simulation fixtures. A shared clock service prevents each component inventing incompatible time origins.

## Alur implementasi

Identify modules/state owners; define contracts; implement minimal path; add adapters; test headless/integration; document lifecycle; version changes and migrations.

## Kriteria penguasaan

Dapat menjaga single ownership, headless correctness, replay dan bounded recovery; memilih architecture sesuai workload.

## Cabang lanjut yang tetap termasuk cakupan

Data-oriented design; component systems; actor architecture; service boundaries; plugin ABI; observability; deterministic engines; fault-tolerant render systems.

## Rujukan dan batas bukti

- [S80](../../references/source-map.md#s80)
- [S81](../../references/source-map.md#s81)
- [S82](../../references/source-map.md#s82)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
