# D38 — Authoring Tools and Production Pipelines

Membuat proses authoring, preview, baking, simulation dan rendering dapat diulang serta ditinjau dengan cepat.

Rumpun: **G — Engineering and Production**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Authoring interfaces mengubah data; runtime evaluator menentukan semantics. Pipeline otomatis perlu inspectable outputs dan failure propagation.

Prasyarat: [D19](../../architecture/domain-map.md#d19), [D36](../../architecture/domain-map.md#d36), [D37](../../architecture/domain-map.md#d37).

## Subdomain dan pengetahuan inti

### D38.01 — Timeline curve dan node editors

Editors expose parameters and relationships. UI representation must match actual evaluation/interpolation.

**Model / prosedur.** Separate authoring data, UI state and evaluated state; preserve units/time.

**Kegagalan.** Curve preview differs render; editor edits hidden duplicate state.

**Verifikasi.** Edit/evaluate round-trip, undo/redo, segment boundaries.

### D38.02 — Scripting automation dan batch authoring

Scripts can generate scenes/clips/assets repeatably. Inputs/config versions must recorded.

**Model / prosedur.** Parameterized idempotent generation with explicit output ownership.

**Kegagalan.** Overwriting source assets, nondeterministic batch order.

**Verifikasi.** Same-input reproducibility and dry/small fixtures.

### D38.03 — Presets parameters dan reusable systems

Presets encode chosen defaults and valid ranges. Meaningful controls avoid exposing internals users cannot interpret.

**Model / prosedur.** Parameter schema, units, bounds, compatibility and exceptions.

**Kegagalan.** Magic names conceal physics; invalid combinations crash.

**Verifikasi.** Extremes, cross-parameter constraints and predictable edits.

### D38.04 — Simulation cache dan baking

Bake turns stateful/complex evaluation into samples. Quality depends cadence/interpolation and which properties captured.

**Model / prosedur.** Record model/version/seed/time grid; preserve source setup separately.

**Kegagalan.** Cache stale after parameter edit; no subframes for blur.

**Verifikasi.** Hash invalidation, trajectory error versus live evaluation.

### D38.05 — Preview iteration dan review

Cheap previews improve iteration but must disclose quality differences. Review notes need time/shot references.

**Model / prosedur.** Same semantics with lower-quality render where feasible; scoped review checklist.

**Kegagalan.** Preview PASS taken final export PASS despite different pipeline.

**Verifikasi.** Representative frames plus playback, final-specific checks.

### D38.06 — Build render queues dan farms

Distributed production needs task IDs, retries and deterministic input bundles. Job completed is different from output verified.

**Model / prosedur.** Content-addressed inputs; bounded retries; verify outputs before publish.

**Kegagalan.** Partial frames accepted; worker version mismatch.

**Verifikasi.** Missing/corrupt outputs, retry idempotence and version audit.

### D38.07 — Collaboration handoff dan provenance

Changes, approvals and creative rationale need durable records. Handoff includes state, artifacts, unresolved gaps and reproduction.

**Model / prosedur.** Version assets/config; retain review decisions with scope and dates.

**Kegagalan.** Inherited status promoted current verification.

**Verifikasi.** Reproduce from handoff, detect changed inputs, preserve open issues.

## Contoh kerja dan alasan pemilihan

Contoh procedural intro generator accepts text/theme/duration/fps. Generated timeline and renders have input hash and version. Preview uses lower resolution but identical timestamps. Final render verifies dimensions/count/PTS and separately reviews layout; preview approval alone is insufficient when font fallback or crop can differ at final settings.

## Alur implementasi

Define input/output contracts; build parameterized authoring; generate preview; record review; bake/cache with fingerprints; render; validate; handoff reproducible bundle.

## Kriteria penguasaan

Dapat membuat repeatable authoring pipeline, cache invalidation dan reviewable outputs without conflating job success with quality.

## Cabang lanjut yang tetap termasuk cakupan

Editor ergonomics; node graph tooling; render farms; pipeline orchestration; asset builds; collaborative editing; content versioning; reproducible media production.

## Rujukan dan batas bukti

- [S34](../../references/source-map.md#s34)
- [S61](../../references/source-map.md#s61)
- [S85](../../references/source-map.md#s85)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
