# D28 — Compositing Image Processing and Visual Effects

Menggabungkan serta memproses image layers dengan contracts untuk color, alpha, coordinates dan temporal behavior.

Rumpun: **E — Graphics and Output**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Compositing tidak boleh menyembunyikan wrong data assumptions. Color management D40 menentukan delivery; temporal processing D27 menentukan history effects.

Prasyarat: [D04](../../architecture/domain-map.md#d04), [D24](../../architecture/domain-map.md#d24), [D25](../../architecture/domain-map.md#d25).

## Subdomain dan pengetahuan inti

### D28.01 — Alpha dan layer composition

Straight dan premultiplied alpha menyimpan colors berbeda. Composite order noncommutative; transparent RGB can affect filtering.

**Model / prosedur.** Premultiplied over: C=Ca+Cb(1−αa), α=αa+αb(1−αa); colors already multiplied.

**Kegagalan.** Dark/light halos from mixing conventions.

**Verifikasi.** Transparent-edge fixtures and analytically known layer results.

### D28.02 — Color spaces dan transfer functions

Encoded RGB tidak umumnya proportional light. Operations linear-light versus display-encoded memberi results berbeda. Color primaries juga harus diketahui.

**Model / prosedur.** Decode transfer, convert primaries if required, process, encode output; metadata retained.

**Kegagalan.** sRGB arithmetic labeled physically correct; double gamma conversion.

**Verifikasi.** Gray ramps, reference patches and controlled blending comparisons.

### D28.03 — Masks clipping dan matte quality

Matte represents coverage/selection; antialias and feather affect edge. Moving matte needs alignment over time.

**Model / prosedur.** Keep matte coordinate/time grid aligned with image; define invert/threshold/feather.

**Kegagalan.** Edges swim, matte offset, clipping blur beyond bounds.

**Verifikasi.** Edge movement, thin features, subpixel motion and layer alignment.

### D28.04 — Keying rotoscoping dan tracking

Keying estimates foreground separation; rotoscoping authoring and tracking can assist but errors accumulate.

**Model / prosedur.** Separate track/matte provenance; inspect occlusion and spill suppression.

**Kegagalan.** Tracking confidence assumed correct matte; temporal jitter.

**Verifikasi.** Difficult edges, motion blur, occlusions and representative playback.

### D28.05 — Filtering warping dan displacement

Spatial filters and geometric warps change frequency/bounds. Resampling method and edge behavior affect quality.

**Model / prosedur.** Define kernel, sampling coordinates, wrap/clamp and inverse mapping.

**Kegagalan.** Forward warp holes, repeated resampling blur, aliasing.

**Verifikasi.** Checkerboards, moving grids and boundary behavior.

### D28.06 — Postprocessing glow blur grading

Effects have radiometric and editorial semantics. Glow/blur consumes bandwidth and can alter contrast/readability.

**Model / prosedur.** Process bright contribution with chosen space/threshold; preserve unclipped intermediate range where needed.

**Kegagalan.** Clipped highlights, excessive luminance flicker, oversized buffers.

**Verifikasi.** Dynamic brightness cases, bounds, text legibility and cost.

### D28.07 — Temporal compositing dan pipeline order

Temporal filters, exposure, grading and composite order can affect flicker and alpha correctness. Ordering should be documented and versioned.

**Model / prosedur.** Compare stage outputs; keep timestamps and alpha/color contracts each interface.

**Kegagalan.** Different preview/export pipeline; footage misaligned by one frame.

**Verifikasi.** Stage-by-stage regression, known markers and final decode.

## Contoh kerja dan alasan pemilihan

Contoh red foreground with alpha 0.5 over blue background. In premultiplied representation foreground color is (0.5,0,0), not (1,0,0). Applying premultiplied formula to straight RGB produces too-bright edge. Choose working color space before interpreting numerical result. A static correct edge is insufficient: scale/rotate the layer to exercise filtering during motion.

## Alur implementasi

Inventory image/color/alpha contracts; normalize; compose static oracle; add warps/effects; inspect intermediate stages; playback moving edges; compare preview/export pipeline.

## Kriteria penguasaan

Dapat mendiagnosis alpha halos, color-space errors, bounds clipping dan temporal matte instability.

## Cabang lanjut yang tetap termasuk cakupan

Deep compositing; optical-flow retiming; HDR compositing; chromatic effects; procedural VFX; volumetric compositing; color transforms; film pipelines.

## Rujukan dan batas bukti

- [S59](../../references/source-map.md#s59)
- [S60](../../references/source-map.md#s60)
- [S61](../../references/source-map.md#s61)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
