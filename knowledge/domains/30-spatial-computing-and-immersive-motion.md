# D30 — Spatial Computing and Immersive Motion

Menyatukan tracking, spatial anchors, rendering dan input dalam AR/VR/MR experiences dengan coordinate/time contracts yang konsisten.

Rumpun: **E — Graphics and Output**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

XR menambah spatial/display semantics; ia tidak menghapus domains dasar. Comfort perlu target-device dan human evaluation, bukan hanya high fps.

Prasyarat: [D02](../../architecture/domain-map.md#d02), [D03](../../architecture/domain-map.md#d03), [D21](../../architecture/domain-map.md#d21), [D25](../../architecture/domain-map.md#d25), [D27](../../architecture/domain-map.md#d27).

## Subdomain dan pengetahuan inti

### D30.01 — Reference spaces dan anchors

Spatial reference dapat local/floor/world-aligned sesuai platform. Anchors may drift/relocalize; tracked space bukan fixed immutable geometry.

**Model / prosedur.** Tag every pose/reference space and timestamp; handle reference reset.

**Kegagalan.** World content jumps after tracking recovery.

**Verifikasi.** Reference-space changes, origin resets, anchor loss.

### D30.02 — Head hand body gaze tracking

Tracking provides estimates and confidence/validity. Different modalities require permissions and fallback.

**Model / prosedur.** Use pose at requested/predicted frame time with validity checks.

**Kegagalan.** Stale hand pose remains interactive; invalid data silently zero.

**Verifikasi.** Occlusion, tracking loss, capability and reconnect.

### D30.03 — Stereo dan immersive rendering

Per-eye transforms/projection produce spatial perception. Improper scale/interpupillary assumptions distort experience.

**Model / prosedur.** Use platform-provided eye views/projections; correct units and depth.

**Kegagalan.** Mono image duplicated, world scale mismatch.

**Verifikasi.** Known-scale scene, per-eye geometry and resizing/runtime checks.

### D30.04 — Prediction reprojection dan latency

Head prediction/reprojection reduce perceived lag but introduce approximation. Full motion-to-photon includes tracking, rendering and display.

**Model / prosedur.** Match predicted presentation pose; keep timestamps and validity.

**Kegagalan.** CPU frame duration claimed total latency.

**Verifikasi.** Measured device path where possible, fast head motion, disocclusion.

### D30.05 — Locomotion dan interaction spaces

Teleport, continuous locomotion, grabbing and physical movement have different constraints. User boundary and reach matter.

**Model / prosedur.** Align input intent, spatial affordance and movement mode; preserve orientation context.

**Kegagalan.** Virtual movement conflicts real movement or reachable space.

**Verifikasi.** Boundary/reach scenarios, mode switches, reduced-motion options.

### D30.06 — Presence embodiment dan comfort

Presence and comfort are human outcomes. Visual self-motion, acceleration, field of view, conflict and user differences affect response.

**Model / prosedur.** Declare hypotheses/preferences; provide adjustable controls; review representative motion.

**Kegagalan.** Comfort certification from technical profiler alone.

**Verifikasi.** Human evaluation plus technical checks, kept separate.

### D30.07 — Session lifecycle dan degradation

XR sessions can pause/end, lose tracking or change available inputs. Normal app content should recover coherently.

**Model / prosedur.** Explicit enter/pause/resume/end state; dispose/rebuild resources and restore focus.

**Kegagalan.** Orphan loops after session end; content inaccessible outside XR.

**Verifikasi.** Repeated sessions, loss recovery and non-XR fallback.

## Contoh kerja dan alasan pemilihan

Contoh AR object anchored table. Store anchor-relative transform rather than camera-relative offset. On tracking invalid, disable precise placement and preserve last meaningful state with clear status. Reacquisition can alter anchor estimate; apply documented presentation policy while preserving spatial truth. A smoothly hidden jump can still misplace content; measure alignment separately.

## Alur implementasi

Inspect target runtime; define spaces/units; implement static anchored scene; add tracked input; profile stereo/latency; handle loss/session lifecycle; conduct comfort/task review.

## Kriteria penguasaan

Dapat mengaudit reference spaces, valid poses, lifecycle dan latency evidence boundaries.

## Cabang lanjut yang tetap termasuk cakupan

OpenXR/WebXR; SLAM anchors; spatial mapping; hand physics; passthrough composition; foveated rendering; shared XR; embodiment research.

## Rujukan dan batas bukti

- [S64](../../references/source-map.md#s64)
- [S65](../../references/source-map.md#s65)
- [S66](../../references/source-map.md#s66)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
