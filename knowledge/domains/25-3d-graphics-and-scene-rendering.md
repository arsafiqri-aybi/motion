# D25 — 3D Graphics and Scene Rendering

Membentuk gambar dari scene spatial dengan cameras, visibility, materials, lights dan rendering algorithms.

Rumpun: **E — Graphics and Output**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

3D rendering tidak otomatis physical simulation. Animation D19 menghasilkan poses; renderer mengevaluasi image formation dengan approximations yang dipilih.

Prasyarat: [D02](../../architecture/domain-map.md#d02), [D24](../../architecture/domain-map.md#d24).

## Subdomain dan pengetahuan inti

### D25.01 — Scene graphs dan transforms

Hierarchical transforms and visibility organize objects. Camera and light objects also have frame conventions. Shared resources differ from shared transform parents.

**Model / prosedur.** Update world transforms in dependency order; distinguish object instance and mesh asset.

**Kegagalan.** Stale parent transform; cloned object shares mutable material unintentionally.

**Verifikasi.** Parent-child fixtures and independent instances.

### D25.02 — Cameras projection dan depth

Perspective maps depth nonlinearly; near/far planes affect clipping and precision. FOV/aspect changes geometry perception.

**Model / prosedur.** Define camera frame, projection convention, near/far and depth range.

**Kegagalan.** Z-fighting, clipping, aspect stale after resize.

**Verifikasi.** Known geometry projection, resize, near-plane crossing.

### D25.03 — Meshes normals dan materials

Geometry, normals, UVs and material model jointly determine appearance. Tangent spaces and nonuniform transforms need correct handling.

**Model / prosedur.** Validate attribute counts; normalize transformed normals; define PBR assumptions explicitly.

**Kegagalan.** Flipped winding, tangent mismatch, textures in wrong color space.

**Verifikasi.** Normal visualization and controlled lighting/material tests.

### D25.04 — Lighting shadows dan transport

Direct lighting, shadows and indirect transport use different algorithms/approximations. Light units and exposure define consistent brightness.

**Model / prosedur.** State light type/intensity, shadow map settings, environment and tone mapping.

**Kegagalan.** Shadow acne, detached shadows, brightness changes after pipeline mix.

**Verifikasi.** Fixed scene with intensity/exposure sweeps and shadow geometry.

### D25.05 — Rasterization ray tracing dan path tracing

Rasterization projects primitives; ray methods sample scene intersections/transport. Quality/cost depend samples, paths, denoising and material complexity.

**Model / prosedur.** Choose algorithm by target; inspect variance and bias separately.

**Kegagalan.** Denoised still looks good but flickers over animation.

**Verifikasi.** Samples-per-pixel convergence plus temporal sequence review.

### D25.06 — Volumes particles dan LOD

Volumes integrate density over paths; particles approximate effects; LOD changes geometry/shading complexity. Transitions can affect motion continuity.

**Model / prosedur.** Define transparency sorting/blending and LOD selection/hysteresis.

**Kegagalan.** Popping, transparent ordering artifacts, particle overdraw.

**Verifikasi.** Camera sweeps, LOD transitions, dense effects and depth boundaries.

### D25.07 — Resources and scene lifecycle

Meshes, materials, textures and render targets own memory. Scene removal must dispose resources according to engine sharing rules.

**Model / prosedur.** Track allocation/ownership; reuse resources; recover device/context loss where supported.

**Kegagalan.** GPU memory leaks; disposing shared texture still in use.

**Verifikasi.** Repeated scene swaps, target resize, loading errors and loss recovery.

## Contoh kerja dan alasan pemilihan

Contoh orbiting camera keeps target fixed while perspective/aspect updated on resize. Compare object-space motion and camera motion independently: identical image displacement does not imply identical world movement. Test near-plane crossing and transparent surfaces while orbiting. For physical plausibility keep lighting/exposure fixed during motion unless the intended camera system changes them.

## Alur implementasi

Define scene/frame conventions; verify camera/static appearance; connect animation; choose lighting/render algorithm; manage resources; profile image/runtime quality across sequence.

## Kriteria penguasaan

Dapat menguji projection/normals/resources, memilih rendering method dan membedakan temporal flicker dari pose error.

## Cabang lanjut yang tetap termasuk cakupan

Global illumination; spectral rendering; participating media; bidirectional transport; real-time ray tracing; virtual geometry; impostors; physically based camera models.

## Rujukan dan batas bukti

- [S02](../../references/source-map.md#s02)
- [S52](../../references/source-map.md#s52)
- [S53](../../references/source-map.md#s53)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
