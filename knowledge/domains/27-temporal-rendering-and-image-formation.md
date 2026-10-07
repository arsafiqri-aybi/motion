# D27 — Temporal Rendering and Image Formation

Menyampling perubahan scene selama exposure dan antarframes untuk menghasilkan image sequence yang sesuai motion serta display target.

Rumpun: **E — Graphics and Output**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Ini image formation, bukan trajectory smoothing. Menambahkan motion blur tidak memperbaiki physics salah; TAA tidak membuktikan temporal continuity.

Prasyarat: [D03](../../architecture/domain-map.md#d03), [D04](../../architecture/domain-map.md#d04), [D25](../../architecture/domain-map.md#d25).

## Subdomain dan pengetahuan inti

### D27.01 — Exposure dan shutter interval

Frame image dapat mengintegrasi scene selama interval exposure. Sample timestamp dan exposure window adalah konsep berbeda.

**Model / prosedur.** Define shutter open/close relative frame; integrate radiance over time with chosen weighting.

**Kegagalan.** One pose blurred screen-space claimed physically exact.

**Verifikasi.** Known moving edge and expected exposure displacement.

### D27.02 — Motion blur dan temporal samples

Motion blur dapat berasal multiple time samples atau approximation velocity buffers. Deformation, camera motion dan occlusion complicate reconstruction.

**Model / prosedur.** Evaluate transforms/geometry at subframe samples; or specify motion-vector approximation limits.

**Kegagalan.** Camera motion omitted; velocity vectors wrong units.

**Verifikasi.** Translation/rotation/deformation fixtures and occlusion crossings.

### D27.03 — Temporal aliasing

Frame sampling dapat membuat wheels apparently reverse or thin features flicker. Exposure blur and sampling change observations, not underlying motion.

**Model / prosedur.** Compare frequency relative frame cadence; increase samples or bandwidth limit when appropriate.

**Kegagalan.** Higher image resolution assumed cures temporal aliasing.

**Verifikasi.** Periodic known motions at multiple rates and exposure settings.

### D27.04 — Temporal accumulation dan antialiasing

TAA combines history with current sample. Reprojection, disocclusion detection and weighting determine ghosting/stability.

**Model / prosedur.** Maintain motion vectors/history; reject invalid history after scene/camera changes.

**Kegagalan.** Trails, history leaking across object IDs, reset omitted.

**Verifikasi.** Camera cuts, moving edges, transparent objects and abrupt lighting.

### D27.05 — Reprojection dan frame interpolation

Reprojection predicts viewpoint changes; frame interpolation synthesizes samples. Neither is equivalent actual evaluated scene at target time in all cases.

**Model / prosedur.** Use depth/motion and validity masks; expose unsupported disocclusions.

**Kegagalan.** Hallucinated surfaces treated actual geometry; latency not counted.

**Verifikasi.** Newly revealed regions, occlusions, thin structures and timestamp correctness.

### D27.06 — Rolling shutter dan acquisition

Image rows may correspond different times. Captured reference distortions can originate acquisition, not object deformation.

**Model / prosedur.** Row-dependent time model matched camera assumptions.

**Kegagalan.** Inferring rigid shape from one distorted fast-motion frame.

**Verifikasi.** Controlled scan/rotation fixture and global-shutter comparison.

### D27.07 — Quality cost dan reproducibility

Sample count, random pattern, denoising and exposure affect time-dependent quality. Seeds and renders need recorded settings.

**Model / prosedur.** Compare variance/bias and temporal consistency at known quality targets.

**Kegagalan.** Nice single frame used to approve sequence; denoiser flicker unnoticed.

**Verifikasi.** Sequence playback, representative cuts, convergence and decoded PTS.

## Contoh kerja dan alasan pemilihan

Contoh object speed 240px/s pada 60fps moves 4px antarframes. Exposure 1/120s gives ideal translation smear 2px; exposure 1/60s gives 4px. Ini conditional ideal calculation, bukan universal camera measurement. Rendering one pose then applying arbitrary blur radius may not match shape/occlusion evolution. Document approximation and compare subframe integration fixture.

## Alur implementasi

Define cadence/exposure; choose temporal rendering method; implement known moving geometry; verify vectors/samples; review disocclusion and cuts; measure runtime/quality; validate encoded sequence.

## Kriteria penguasaan

Dapat menghitung exposure displacement, menjelaskan ghosting dan temporal aliasing, serta membedakan interpolation synthetic dari scene evaluation.

## Cabang lanjut yang tetap termasuk cakupan

Spatiotemporal reconstruction; motion-compensated filtering; temporal superresolution; adaptive time sampling; rolling-shutter inversion; motion-vector generation; temporal denoising.

## Rujukan dan batas bukti

- [S08](../../references/source-map.md#s08)
- [S57](../../references/source-map.md#s57)
- [S58](../../references/source-map.md#s58)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
