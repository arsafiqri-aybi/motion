# D16 — Motion Capture Tracking and Reconstruction

Menghasilkan observations dan reconstructed motion dari sensor, gambar atau video dengan coordinate, time, uncertainty dan provenance yang eksplisit.

Rumpun: **C — Representation and Animation**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Capture adalah pengukuran/estimasi, bukan motion ground truth otomatis. Learned synthesis D15 dan rig retargeting D17 memakai hasil capture dengan batasnya.

Prasyarat: [D02](../../architecture/domain-map.md#d02), [D03](../../architecture/domain-map.md#d03), [D04](../../architecture/domain-map.md#d04).

## Subdomain dan pengetahuan inti

### D16.01 — Acquisition systems

Optical markers, inertial sensors, depth cameras dan markerless images memberikan measurements berbeda. Setiap sensor mempunyai rate, noise, occlusion dan calibration constraints.

**Model / prosedur.** Record raw observations, clock, exposure, units, sensor model dan capture conditions.

**Kegagalan.** Pose confidence diperlakukan akurasi meter; missing marker bernilai zero.

**Verifikasi.** Known geometry/static cases dan documented measurement error.

### D16.02 — Calibration dan frame alignment

Camera intrinsics, extrinsics dan sensor-to-body transforms menentukan mapping observations ke ruang. Calibration drift tidak hilang dengan smoothing.

**Model / prosedur.** Estimate parameters dari known targets; compose transforms with frame labels.

**Kegagalan.** Mirrored coordinates, incorrect scale, moving camera assumed fixed.

**Verifikasi.** Reprojection error serta independent distance/orientation checks.

### D16.03 — Feature tracking dan optical flow

Feature correspondence memperkirakan image displacement. Aperture problem, textureless regions dan occlusion membatasi identifiability.

**Model / prosedur.** Sparse feature tracking atau dense optical flow with temporal consistency checks.

**Kegagalan.** Image motion claimed world velocity tanpa depth/calibration.

**Verifikasi.** Synthetic translations, occlusions, brightness changes dan flow residuals.

### D16.04 — Pose estimation dan reconstruction

2D joint coordinates tidak uniquely menentukan 3D pose. Multiview, depth atau priors menambah constraints dengan assumptions.

**Model / prosedur.** Triangulate calibrated views; enforce correspondence and inspect reprojection.

**Kegagalan.** Anatomical prior hides measurement failure; left/right swaps.

**Verifikasi.** Joint bounds, cross-view consistency, uncertainty and known-pose fixtures.

### D16.05 — Camera motion estimation

Visual object motion tercampur camera motion. Estimating camera requires geometry assumptions and enough reliable features.

**Model / prosedur.** Separate egomotion estimate from residual object motion; reject inconsistent features.

**Kegagalan.** Zoom interpreted translation; planar degeneracy; moving scene bias.

**Verifikasi.** Controlled pan/rotation/zoom cases and independently known camera trajectory.

### D16.06 — Cleaning gap filling dan filtering

Interpolation/filtering memperbaiki usability tetapi menambah synthetic content. Gap length dan dynamics menentukan validity.

**Model / prosedur.** Preserve masks indicating observed/estimated samples; fill short gaps with stated method.

**Kegagalan.** Long missing intervals fabricated as measured motion.

**Verifikasi.** Hold out observed samples, predict gaps, measure errors by gap length.

### D16.07 — Validation dan uncertainty

Capture quality mempunyai spatial, temporal dan identity components. Average residual tidak cukup untuk fast motion/occlusion intervals.

**Model / prosedur.** Report errors by joint, time, condition; preserve original raw and derived versions.

**Kegagalan.** Low reprojection error equated correct 3D scale; timestamps discarded.

**Verifikasi.** Ground-truth subset where available, temporal checks, calibration replay.

## Contoh kerja dan alasan pemilihan

Contoh marker hilang 80ms ketika tangan tertutup. Simpan sample invalid beserta timestamps; jangan menaruh [0,0,0]. Interpolasi boleh menghasilkan estimated trajectory, tetapi bedakan mask estimated. Uji metode dengan menyembunyikan interval lain yang masih memiliki observations. Jika model mengekstrapolasi selama 2 detik, itu berbeda tingkat kepastian dan tidak boleh diwarisi sebagai capture terverifikasi.

## Alur implementasi

Capture raw; calibrate; align clocks/frames; reconstruct; preserve missingness; clean derived stream; validate by condition; export provenance and uncertainty.

## Kriteria penguasaan

Dapat membedakan observations, estimates dan synthetic fills; menguji calibration dan clock alignment.

## Cabang lanjut yang tetap termasuk cakupan

Multiview geometry; SLAM; inertial motion capture; event cameras; markerless reconstruction; differentiable tracking; uncertainty-aware capture; performance capture.

## Rujukan dan batas bukti

- [S31](../../references/source-map.md#s31)
- [S32](../../references/source-map.md#s32)
- [S33](../../references/source-map.md#s33)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
