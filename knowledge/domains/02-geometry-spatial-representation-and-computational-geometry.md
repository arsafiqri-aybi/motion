# D02 — Geometry Spatial Representation and Computational Geometry

Menetapkan bentuk, orientasi, posisi, dan query spasial yang dipakai animasi, rendering, simulasi, serta planning.

Rumpun: **A — Foundations**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Geometri memberikan representasi ruang. Gerak articulated dibahas D07/D17, physical response D09, dan visibility/rendering D25. Konvensi handedness dan matrix layout selalu dinyatakan.

Prasyarat: [D01](../../architecture/domain-map.md#d01), [D05](../../architecture/domain-map.md#d05).

## Subdomain dan pengetahuan inti

### D02.01 — Frames dan coordinate conventions

Vector posisi bermakna hanya dengan frame dan unit. Local frame objek, world frame, camera frame, clip space, dan screen space mempunyai fungsi berbeda. Screen y-down tidak sama dengan world y-up.

**Model / prosedur.** Tuliskan transform T_world_local. Untuk column vectors, p_world=T_world_local p_local; composition diterapkan dari kanan ke kiri.

**Kegagalan.** Mencampur row/column convention atau handedness; koordinat sensor dipakai sebagai screen coordinate.

**Verifikasi.** Transform known basis vectors dan origin; round-trip dengan inverse harus memulihkan point.

### D02.02 — Affine dan projective transforms

Translation, rotation, scale, shear membentuk affine transformations. Perspective membutuhkan homogeneous division. Point dan direction berbeda pada homogeneous coordinate terakhir.

**Model / prosedur.** Point [x,y,z,1], direction [x,y,z,0]. Normal dengan nonuniform scale memakai inverse transpose linear transform.

**Kegagalan.** Normal diperlakukan seperti position; pembagian oleh w dekat nol; urutan transform dianggap komutatif.

**Verifikasi.** Uji plane normal tetap tegak lurus tangent setelah transform dan compare dua urutan transform.

### D02.03 — Rotations dan quaternions

Euler angles mudah dibaca tetapi memiliki singular configurations. Unit quaternion mewakili rotation, dengan q dan −q menyatakan orientation sama. Rotation interpolation memerlukan convention dan hemisphere handling.

**Model / prosedur.** Untuk shortest-path slerp, jika dot(q0,q1)<0 balik salah satu quaternion. Normalisasi setelah akumulasi numerik.

**Kegagalan.** Long-path rotation, gimbal lock, drift norm; komponen quaternion di-lerp tanpa normalisasi.

**Verifikasi.** Uji orthonormal rotation matrix, determinant≈1, q/−q equivalence, dan 180-degree edge cases.

### D02.04 — Curves dan arc-length parameterization

Parameter u pada Bézier tidak umumnya sebanding dengan jarak. Constant-speed path motion perlu mapping jarak ke parameter melalui integral panjang kurva atau lookup table.

**Model / prosedur.** Cubic B(u)=(1−u)³P0+3(1−u)²uP1+3(1−u)u²P2+u³P3. s(u)=∫norm(B′(u))du.

**Kegagalan.** Equal Δu menghasilkan speed naik-turun; cusp membuat tangent tidak terdefinisi.

**Verifikasi.** Bandingkan jarak successive samples sebelum/sesudah arc-length mapping; ukur approximation error.

### D02.05 — Topology meshes dan surfaces

Connectivity menentukan deformasi dan traversal; geometry positions menentukan bentuk saat ini. Duplicate vertices untuk UV seams dapat menimbulkan adjacency berbeda dari visual surface.

**Model / prosedur.** Mesh memuat vertices dan indices; manifoldness, winding, boundary edges, serta self-intersection merupakan properti terpisah.

**Kegagalan.** Inverted faces, cracked seams, nonmanifold assumptions; topology berubah tanpa memperbarui skinning.

**Verifikasi.** Periksa edge incidence, degenerate triangles, winding consistency, dan deformasi seam.

### D02.06 — Spatial queries dan acceleration structures

Intersection dan distance queries mendukung picking, collisions, dan visibility. Broad phase menyaring kandidat; narrow phase memberi hasil geometris lebih presisi.

**Model / prosedur.** AABB overlap per axis; BVH membagi primitive bounds; ray intersection menghasilkan t pada parameterisasi ray yang dinyatakan.

**Kegagalan.** Bounds usang setelah motion; tunneling jika hanya memeriksa posisi akhir; epsilon salah skala.

**Verifikasi.** Bandingkan accelerated query dengan brute-force oracle pada scene kecil dan moving bounds.

### D02.07 — Geometric predicates dan constraints

Near-collinear atau near-coplanar inputs membuat sign computation rapuh. Constraint seperti jarak, sudut, dan attachment merupakan hubungan ruang sebelum menjadi masalah solver.

**Model / prosedur.** Orientation predicate memakai determinant; robust predicates atau higher precision diperlukan saat sign menentukan topology.

**Kegagalan.** Tolerance menyatukan dua fitur berbeda; solver convergence dianggap membuktikan geometry valid.

**Verifikasi.** Uji adversarial hampir collinear, skala sangat kecil/besar, dan constraint residual.

## Contoh kerja dan alasan pemilihan

Contoh: kamera mengikuti lintasan Bézier. Buat samples (u,s), normalisasi s menjadi progress, cari dua samples yang mengapit desired distance, lalu interpolasikan u. Position=B(u). Arah kamera dari tangent B′(u), tetapi up vector perlu aturan anti-flip ketika tangent mendekati up. Panjang kurva berubah jika control point diedit, sehingga tabel perlu dibangun ulang. Tujuan constant-speed harus diuji dalam world distance, bukan berdasarkan curve parameter.

## Alur implementasi

Deklarasikan frame/unit; pilih representasi; buat transform chain; tentukan geometry query; cache hanya data dengan invalidation jelas; uji edge geometry; hubungkan geometry dengan time dan state evaluator.

## Kriteria penguasaan

Dapat menjelaskan perbedaan point/direction/normal, mengomposisi dan membalik transform, membangun arc-length LUT, serta menguji query terhadap brute-force. Latihan: animate parent scale nonuniform dan pertahankan normal benar.

## Cabang lanjut yang tetap termasuk cakupan

NURBS; subdivision surfaces; signed distance fields; constructive solid geometry; geometric algebra; geodesics; mesh repair; remeshing; robust exact predicates; configuration-space geometry.

## Rujukan dan batas bukti

- [S02](../../references/source-map.md#s02)
- [S03](../../references/source-map.md#s03)
- [S04](../../references/source-map.md#s04)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
