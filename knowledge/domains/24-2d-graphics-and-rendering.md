# D24 — 2D Graphics and Rendering

Mengubah state motion menjadi gambar 2D melalui vector/raster paths, text, layers dan compositing.

Rumpun: **E — Graphics and Output**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Rendering path bukan induk motion generation. DOM/SVG/Canvas dipilih berdasarkan content, accessibility, workload dan editing needs; GPU detail D26.

Prasyarat: [D02](../../architecture/domain-map.md#d02), [D05](../../architecture/domain-map.md#d05), [D19](../../architecture/domain-map.md#d19).

## Subdomain dan pengetahuan inti

### D24.01 — Raster vector dan scene organization

Vector describes geometry; raster stores sampled pixels. Either can be animated. Scene objects need z-order, transform, visibility and ownership.

**Model / prosedur.** Evaluate scene snapshot then render; define coordinate and pixel conventions.

**Kegagalan.** Rendering mutates simulation; object order changes unexpectedly.

**Verifikasi.** Known layered scene, deterministic snapshot and visibility tests.

### D24.02 — DOM CSS dan layout

DOM supports semantic content; animated layout can trigger work beyond one element. Transform/opacity often reduce work but actual compositing must be profiled.

**Model / prosedur.** Prefer clear property ownership; separate geometry reads/writes; keep focus semantics.

**Kegagalan.** Layout thrashing; will-change on everything; offscreen content focusable.

**Verifikasi.** Performance trace, semantic keyboard flow and dynamic layout.

### D24.03 — SVG paths dan vector motion

Paths, strokes, fills, transforms and clipping offer retained vector control. Path length units and morph correspondence require explicit handling.

**Model / prosedur.** Stroke reveal through length/dash properties; evaluate viewBox and local transforms.

**Kegagalan.** Paths resampled mismatched; percentage origin misunderstood.

**Verifikasi.** Endpoint reveal, viewBox scaling, path morph topology.

### D24.04 — Canvas rendering

Immediate-mode renderer redraws content; state and hit-testing remain application responsibilities. CSS size differs backing buffer size.

**Model / prosedur.** Set backing dimensions by target pixel scale, transform coordinates consistently, clear/compose every frame.

**Kegagalan.** Blurry output, double scaling, missing keyboard equivalents.

**Verifikasi.** Known pixel geometry across DPRs, resize and hit-test mapping.

### D24.05 — Typography dan shaping

Text motion must preserve shaping, language direction, line breaking and readability. Grapheme clusters differ from Unicode code points.

**Model / prosedur.** Shape/layout before glyph motion or use browser text semantics; animate groups with language-aware boundaries.

**Kegagalan.** Splitting combining marks/Arabic shaping; line shift during font loading.

**Verifikasi.** Multiple scripts, fallback fonts, copy/accessibility text and loading states.

### D24.06 — Masks clipping filters dan layers

Effects add intermediate surfaces and bounds. Blur shadow and masks can expand rendering footprint and change compositing.

**Model / prosedur.** Track effect bounds and alpha convention; cache only stable layers.

**Kegagalan.** Clipped blur, excessive large offscreen buffers.

**Verifikasi.** Boundary pixels, transparent edges, animated effect extents.

### D24.07 — Sprites raster assets dan batching

Sprites require atlas metadata, sampling rules, frame duration and asset lifecycle. Image sequence timing is not necessarily one frame per display tick.

**Model / prosedur.** Index by animation local time; include padding for filtered atlas sampling.

**Kegagalan.** Atlas bleeding, skipped durations, decode stalls.

**Verifikasi.** Frame timing, texture boundaries, loading failure and memory budget.

## Contoh kerja dan alasan pemilihan

Contoh high-DPI Canvas: CSS viewport 400×300, device scale 2 yields backing 800×600. Apply context scaling once and keep logical geometry/hit testing in CSS pixels. Reset transform appropriately after resize because canvas state resets. Labels essential to task still require semantic DOM representation. Increasing pixel scale improves detail but quadruples pixel workload at scale 2.

## Alur implementasi

Choose rendering path; define scene/value ownership; normalize sizing; render static fixtures; connect evaluator; add effects/text/assets; profile and check semantic alternatives.

## Kriteria penguasaan

Dapat memilih DOM/SVG/Canvas dengan alasan, mengelola high-DPI dan typography, serta menguji animated bounds.

## Cabang lanjut yang tetap termasuk cakupan

Font shaping; vector tessellation; rasterization; signed distance field text; 2D scene graphs; dirty rectangles; sprite packing; retained/immediate hybrid renderers.

## Rujukan dan batas bukti

- [S49](../../references/source-map.md#s49)
- [S50](../../references/source-map.md#s50)
- [S51](../../references/source-map.md#s51)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
