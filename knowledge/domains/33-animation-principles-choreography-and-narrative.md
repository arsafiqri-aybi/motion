# D33 — Animation Principles Choreography and Narrative

Menyusun motion yang menyampaikan maksud, hierarchy, rhythm dan emotion melalui hubungan action, camera, typography dan editing.

Rumpun: **F — Human Experience**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Prinsip animasi adalah desain dan craft; efektivitas spesifik membutuhkan audience/context evaluation. Jangan menjadikan setiap prinsip sebagai efek wajib.

Prasyarat: [D06](../../architecture/domain-map.md#d06), [D19](../../architecture/domain-map.md#d19), [D32](../../architecture/domain-map.md#d32).

## Subdomain dan pengetahuan inti

### D33.01 — Timing spacing dan rhythm

Timing menentukan kapan events terjadi; spacing menentukan displacement antarposes. Rhythm dapat dibangun melalui repeats, contrasts dan pauses.

**Model / prosedur.** Mark beats and holds; evaluate trajectory spacing against intended emphasis.

**Kegagalan.** Constant busy movement; changing duration without adjusting readability.

**Verifikasi.** Playback with task/message review and readable hold durations.

### D33.02 — Anticipation follow-through overlapping action

Preparatory cues and delayed secondary movement can clarify action. Their size/duration depends scale and intent.

**Model / prosedur.** Separate primary action, preparation, settle and secondary response.

**Kegagalan.** Decorative anticipation delays direct UI feedback.

**Verifikasi.** Compare action clarity and response timing across contexts.

### D33.03 — Arcs squash stretch dan exaggeration

Stylization communicates qualities while preserving identity/constraints when required. Volume or shape invariants are design choices.

**Model / prosedur.** Define allowed deformation and path shape; choose exaggeration bounded by message.

**Kegagalan.** Text distortion unreadable; critical task geometry misleading.

**Verifikasi.** Endpoint identity, legibility, constraints and audience review.

### D33.04 — Staging hierarchy dan attention handoff

Motion should make intended focal point available without unnecessary competition. Spatial grouping and timing coordinate information flow.

**Model / prosedur.** Assign one primary emphasis per beat unless deliberate complexity; label this authored heuristic.

**Kegagalan.** Many simultaneous highlights; attention claim without measurement.

**Verifikasi.** Message comprehension and visual review of full sequence.

### D33.05 — Transitions continuity dan editing

Cuts, wipes, morphs and shared elements create relationships between scenes. Continuity can be spatial, temporal, semantic or stylistic.

**Model / prosedur.** Select transition according relationship; preserve orientation and content context.

**Kegagalan.** Transition obscures task, contradictory direction or jump.

**Verifikasi.** Before/after understanding, fast navigation and contextual review.

### D33.06 — Camera motion dan visual narrative

Camera angle/path/scale communicates viewpoint. Object and camera motion interactions affect composition and comfort.

**Model / prosedur.** Plan shot framing, target, path, focus and transitions; inspect projected composition.

**Kegagalan.** Unnecessary orbit, subject cropped during move.

**Verifikasi.** Full shot path, safe areas, subject visibility and viewing context.

### D33.07 — Style systems dan iteration

Reusable motion tokens create coherence but need context-specific overrides. Style should be concrete parameters and rules, not adjectives alone.

**Model / prosedur.** Define timing ranges, easing families, response rules, hierarchy and exceptions.

**Kegagalan.** Every element uses same easing regardless function.

**Verifikasi.** Compare families of states/shots and note purposeful deviations.

## Contoh kerja dan alasan pemilihan

Contoh motion explainer: establish headline, move supporting diagram, hold for reading, highlight relationship, then transition. Timeline allocates motion and stillness according information load. Do not animate all words continuously merely because tool can. A useful specification names focal point, message, entry/hold/exit, path, timing and review criteria.

## Alur implementasi

Extract message/action; write beats; choose motion function; build timing/spacing plan; prototype full sequence; review clarity/comfort; refine tokens and exceptions.

## Kriteria penguasaan

Dapat memberi reason untuk tiap gerak, membuat choreography plan dan menilai full sequence sesuai tujuan.

## Cabang lanjut yang tetap termasuk cakupan

Character acting; cinematography; montage; typography choreography; visual rhetoric; dance-inspired composition; procedural choreography; interactive narrative.

## Rujukan dan batas bukti

- [S72](../../references/source-map.md#s72)
- [S73](../../references/source-map.md#s73)
- [S74](../../references/source-map.md#s74)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
