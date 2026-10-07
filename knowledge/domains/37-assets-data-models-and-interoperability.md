# D37 — Assets Data Models and Interoperability

Membawa motion data antartools/platform tanpa kehilangan units, hierarchy, timing, interpretation atau provenance.

Rumpun: **G — Engineering and Production**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Format support bukan jaminan fidelity. Importer/exporter perlu subset contracts dan round-trip checks; licenses/provenance tidak boleh ditebak.

Prasyarat: [D02](../../architecture/domain-map.md#d02), [D03](../../architecture/domain-map.md#d03), [D17](../../architecture/domain-map.md#d17), [D19](../../architecture/domain-map.md#d19).

## Subdomain dan pengetahuan inti

### D37.01 — Asset identity dan provenance

Filename bukan immutable identity. Content hash, source, version dan license/usage record mendukung traceability.

**Model / prosedur.** Manifest records ID/path/hash/type/origin/version and actual license metadata.

**Kegagalan.** Renamed asset mistaken new source; rights assumed from downloadable file.

**Verifikasi.** Hash/file existence and provenance fields with unknowns explicit.

### D37.02 — Coordinate units dan schemas

Asset format may define axes/units/rotation order berbeda. Conversion also impacts animation curves, normals and root motion.

**Model / prosedur.** Single normalized internal schema with reversible conversion metadata.

**Kegagalan.** Only static mesh converted while clips remain old frame.

**Verifikasi.** Known static and animated reference geometry round-trip.

### D37.03 — Geometry rigs clips dan media

Geometry, skeleton, animation and audio have linked dependencies. Missing material/font/rig can change interpretation.

**Model / prosedur.** Validate referenced assets and compatibility before runtime.

**Kegagalan.** Clip applied wrong skeleton; font replacement changes choreography.

**Verifikasi.** Dependency closure, joint map and asset-loaded preview.

### D37.04 — Formats import export dan feature subsets

Interchange formats support subsets different from authoring tools. Constraints/drivers may need bake; metadata may be dropped.

**Model / prosedur.** Document supported fields and unsupported features; bake at defined cadence.

**Kegagalan.** Native rig controls assumed exported; successful file parse claimed full fidelity.

**Verifikasi.** Known-feature fixture, bake comparison, unsupported-feature report.

### D37.05 — Compression quantization dan streaming

Compression trade-off depends position/rotation/contact errors. Streaming introduces availability and scheduling constraints.

**Model / prosedur.** Choose per-channel quantization; progressive loading with explicit readiness state.

**Kegagalan.** Root error accumulates, contact slip, stalls at chunk boundary.

**Verifikasi.** Max interval errors, chunk transitions, loss/reconnect.

### D37.06 — Versioning compatibility migration

Schema changes can reinterpret old data. Explicit versions and converters preserve history.

**Model / prosedur.** Read version, validate, migrate deterministically, record original.

**Kegagalan.** Silent reinterpretation, missing default changes trajectory.

**Verifikasi.** Old/new fixtures and round-trip migration expectations.

### D37.07 — Lifecycle integrity dan inventory

Inventory validates actual bytes and metadata, not aesthetic suitability. Caches derived from source should be rebuildable.

**Model / prosedur.** Hash raw assets; validate formats; track derived outputs separately.

**Kegagalan.** Metadata-only check claimed rendered content correct.

**Verifikasi.** Corrupt/missing files, dependency mismatch, decode/render subset checks.

## Contoh kerja dan alasan pemilihan

Contoh import animation in centimeters with y-up into meters z-up. Apply scale/frame conversion consistently to mesh, skeleton translations, root trajectory and normals; rotations require basis conversion. Export, reimport and compare end-effector trajectories, not only static dimensions. If exporter omits constraints, bake evaluated transforms with documented sampling error.

## Alur implementasi

Inventory source/provenance; inspect formats; normalize schemas/units; validate dependencies; import/render fixtures; export round-trip; record compression/migration limits.

## Kriteria penguasaan

Dapat membuktikan animated round-trip fidelity dan mendeteksi asset/reference mismatch tanpa mengklaim unsupported format features.

## Cabang lanjut yang tetap termasuk cakupan

glTF/USD/FBX workflows; animation codecs; skeletal interchange; media metadata; font assets; content-addressed storage; schema evolution; streaming assets.

## Rujukan dan batas bukti

- [S36](../../references/source-map.md#s36)
- [S83](../../references/source-map.md#s83)
- [S84](../../references/source-map.md#s84)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
