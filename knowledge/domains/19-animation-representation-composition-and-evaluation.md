# D19 — Animation Representation Composition and Evaluation

Menyimpan, mengevaluasi, dan menggabungkan gerak menjadi pose/property state yang konsisten sepanjang timeline.

Rumpun: **C — Representation and Animation**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Composition describes runtime semantics; tools D38 author data, reactive behavior D20 memilih transitions, rendering D24/D25 menampilkan hasil.

Prasyarat: [D02](../../architecture/domain-map.md#d02), [D03](../../architecture/domain-map.md#d03), [D06](../../architecture/domain-map.md#d06).

## Subdomain dan pengetahuan inti

### D19.01 — Curves tracks dan clips

Track mengubah satu attribute; clip mengelompokkan tracks beserta time domain. Missing channels perlu default/base policy.

**Model / prosedur.** Evaluate segment per time using declared interpolation and extrapolation.

**Kegagalan.** Time units mismatch, missing keys become zero.

**Verifikasi.** Endpoints, missing channels, duplicate timestamps, out-of-range time.

### D19.02 — Sequencing dan orchestration

Sequence defines relative timing, overlaps dan completion behavior. Stagger can be based index, space or other explicit order.

**Model / prosedur.** Timeline node resolves local start/duration; total duration derived from child intervals.

**Kegagalan.** Object order changes visual choreography; stale calculated durations.

**Verifikasi.** Permutation fixture, overlaps, nested playback rates.

### D19.03 — Layering dan masks

Layers own sets of channels/joints. Masking determines influence; property replacement order and additive composition berbeda.

**Model / prosedur.** Establish base pose, evaluate layers, apply masks/weights in explicit order.

**Kegagalan.** Lower layer unexpectedly overrides hand control; multiple writers.

**Verifikasi.** Isolated layers then pairwise/full-stack combinations.

### D19.04 — Blend trees dan state transitions

Blend inputs may be speed/direction; transition chooses how to mix clips over time. Matching phase avoids abrupt gait changes.

**Model / prosedur.** Blend-space weights based documented parameters; preserve phase/contact where needed.

**Kegagalan.** Weight sums wrong; rapid state toggles create discontinuity.

**Verifikasi.** Corner points, interior, parameter jumps and repeated transitions.

### D19.05 — Additive animation

Additive delta is relative reference pose/space. Rotation delta composition is not ordinary component addition.

**Model / prosedur.** ΔT=T_pose T_ref⁻¹ under chosen convention; apply weighted delta with appropriate rotation math.

**Kegagalan.** Wrong reference frame, duplicate root displacement.

**Verifikasi.** Identity delta, full delta, zero weight, reference change.

### D19.06 — Evaluation caching dan compression

Compression reduces size at cost of error. Track-specific error metric must match position/rotation/perception relevance.

**Model / prosedur.** Key reduction and quantization with bounds; cache evaluated data using full dependencies.

**Kegagalan.** Compressed angles wrap incorrectly; stale cached pose.

**Verifikasi.** Maximum error across intervals, contact-critical frames, cache invalidation.

### D19.07 — Ownership events dan lifecycle

Animation events and callbacks have time-crossing semantics. Seek, reverse and cancellation require defined event policy and cleanup.

**Model / prosedur.** One owner per property or explicit composition; generation token rejects stale completions.

**Kegagalan.** Event fired twice after seek; unmounted target callback.

**Verifikasi.** Forward/reverse/seek/cancel histories, resource cleanup and final state.

## Contoh kerja dan alasan pemilihan

Contoh walking lower-body clip plus upper-body pointing. Mask pointing to torso/arm, maintain locomotion root from base. Additive breathing layer uses known reference pose; full-body replacement would erase walk. At transition to idle, decide whether pointer action persists or fades. Record policy and test repeated navigation/state changes rather than only smooth forward playback.

## Alur implementasi

Define channel schema/base pose; normalize time; implement pure evaluator; add composition; define event policy; compress with error bounds; test layered and interrupted playback.

## Kriteria penguasaan

Dapat membangun clip evaluator, masks, additive layers dan phase-aware transitions; membuktikan lifecycle cleanup.

## Cabang lanjut yang tetap termasuk cakupan

Nonlinear animation; pose graphs; blend-space interpolation; motion compression; animation streaming; motion matching integration; multirate animation evaluation.

## Rujukan dan batas bukti

- [S05](../../references/source-map.md#s05)
- [S34](../../references/source-map.md#s34)
- [S36](../../references/source-map.md#s36)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
