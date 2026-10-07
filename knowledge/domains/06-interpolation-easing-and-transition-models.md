# D06 — Interpolation Easing and Transition Models

Menghubungkan nilai atau pose antarwaktu dengan kontrol terhadap bentuk lintasan, continuity, dan interruption.

Rumpun: **B — Motion Models**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Interpolation tidak sama dengan simulasi fisik. Easing mengubah mapping progress; spring integration D08/D10 memiliki state dan velocity.

Prasyarat: [D01](../../architecture/domain-map.md#d01), [D02](../../architecture/domain-map.md#d02), [D03](../../architecture/domain-map.md#d03).

## Subdomain dan pengetahuan inti

### D06.01 — Scalar dan vector interpolation

Lerp menghasilkan garis lurus di value space. Jika progress melampaui [0,1], operasi menjadi extrapolation; clamp adalah kebijakan tambahan.

**Model / prosedur.** lerp(a,b,u)=a+(b−a)u; inverse lerp=(x−a)/(b−a), undefined saat a=b.

**Kegagalan.** Clamp semua values merusak overshoot yang disengaja.

**Verifikasi.** Endpoints, midpoint, extrapolation dan degenerate interval.

### D06.02 — Easing dan cubic Bézier

Easing memetakan progress input ke progress output. CSS cubic Bézier memerlukan inversion x(s)=u sebelum membaca y(s); y(u) langsung bukan evaluasi yang sama.

**Model / prosedur.** Gunakan Newton iteration dengan bracket/bisection fallback; batasi x control points sesuai API.

**Kegagalan.** Solver gagal dekat derivative nol; asumsi seluruh easing monotonic.

**Verifikasi.** Compare evaluator dengan reference sampled curve; uji flat tangent dan endpoint.

### D06.03 — Piecewise dan spline interpolation

Keyframe segments mempunyai continuity berbeda. C0 menjaga nilai; C1 menjaga derivative; C2 menjaga second derivative pada parameter yang sama.

**Model / prosedur.** Hermite segment memakai endpoints dan tangents; tangent unit harus cocok parameterization.

**Kegagalan.** Tangent dihitung per frame tetapi digunakan per detik; spline overshoot menembus constraint.

**Verifikasi.** Ukur boundary position/velocity/acceleration dan value bounds.

### D06.04 — Orientation dan manifold interpolation

Rotations, directions dan poses tidak selalu cocok Euclidean component interpolation. Unit constraints dan rotation topology perlu dijaga.

**Model / prosedur.** Slerp unit quaternions dengan hemisphere correction; dekat dot=1 gunakan normalized lerp.

**Kegagalan.** Quaternion norm drift; interpolation mengambil lintasan panjang.

**Verifikasi.** q dan −q menghasilkan orientation identik; angular steps mendekati expected.

### D06.05 — Morphing dan correspondence

Shape interpolation membutuhkan correspondence yang bermakna. Dua SVG paths atau meshes berbeda topology tidak dapat langsung diblending berdasarkan index arbitrer.

**Model / prosedur.** Resample curves dengan orientation/start-point alignment; mesh morph perlu vertex correspondence.

**Kegagalan.** Twisted morph, vertex mismatch, holes muncul.

**Verifikasi.** Periksa topology, area/winding, self-intersection dan endpoint reconstruction.

### D06.06 — Blending dan property spaces

Weighted blend bergantung value space. Color interpolation, transforms dan additive pose punya semantics berbeda. Weights normalized sesuai model, bukan otomatis untuk semua blend.

**Model / prosedur.** Pose translation dapat weighted sum; rotation perlu rotation-aware blend; additive delta relatif reference pose.

**Kegagalan.** Linear sRGB blend dianggap linear light; matrix blend membuat shear tak sengaja.

**Verifikasi.** Test identity layer, zero weight, weight sum, dan reference-pose consistency.

### D06.07 — Interrupted transitions

Transition baru dimulai dari evaluated current state. Velocity continuity memerlukan initial derivative; duration reset saja hanya memastikan position continuity.

**Model / prosedur.** Simpan x dan v saat interruption; Hermite bridge atau spring dengan initial state dapat mempertahankan derivative.

**Kegagalan.** Rapid toggles membuat snap, accumulated animations, stale completion callbacks.

**Verifikasi.** Interrupt di beberapa progress dan reverse berulang; periksa continuity serta ownership.

## Contoh kerja dan alasan pemilihan

Contoh: panel sedang bergerak dari 0 ke 100px ketika target berubah ke 40px. Membuat animasi baru dari 0 menimbulkan jump. Ambil x_current pada timestamp interruption. Jika gerak lama berkecepatan 200px/s, pilih bridge yang menerima v_current; bridge cubic dengan zero velocity akhir bisa overshoot bila durasi terlalu panjang. Overshoot harus diputuskan berdasarkan ruang UI, bukan dianggap selalu salah.

## Alur implementasi

Tentukan value space; tetapkan parameterization dan boundaries; pilih interpolation; simpan state saat interruption; batasi sesuai constraints; test segment boundaries dan repeated reversal.

## Kriteria penguasaan

Dapat membedakan easing dari path, mengimplementasikan Bézier inversion, serta membuat transition interruption tanpa snap. Lab: bandingkan lerp progress versus critically damped response.

## Cabang lanjut yang tetap termasuk cakupan

Monotone cubic interpolation; spherical splines; dual-quaternion blending; optimal transport morphing; multidimensional blend spaces; perceptual color interpolation.

## Rujukan dan batas bukti

- [S05](../../references/source-map.md#s05)
- [S12](../../references/source-map.md#s12)
- [S13](../../references/source-map.md#s13)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
