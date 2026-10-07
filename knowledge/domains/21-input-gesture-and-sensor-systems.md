# D21 — Input Gesture and Sensor Systems

Mengubah input perangkat menjadi events/gestures/state estimates dengan timestamps, coordinate frames dan cancellation yang jelas.

Rumpun: **D — Behavior and Interaction**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Acquisition/recognition berbeda dari interaction mapping D22. Input source tidak selalu pointer, dan gestures tidak boleh menghilangkan keyboard semantics.

Prasyarat: [D02](../../architecture/domain-map.md#d02), [D03](../../architecture/domain-map.md#d03), [D04](../../architecture/domain-map.md#d04).

## Subdomain dan pengetahuan inti

### D21.01 — Pointer events dan capture

Mouse/touch/pen dapat dibungkus pointer model tetapi mempunyai capabilities berbeda. Capture menjaga routing saat pointer keluar target; cancellation tetap mungkin.

**Model / prosedur.** Track pointerId, initial position, capture lifecycle and pointercancel.

**Kegagalan.** Drag stuck setelah OS cancels; pointer ownership overwritten.

**Verifikasi.** Outside-target drag, cancellation, multi-pointer and capture-loss cases.

### D21.02 — Coordinate mapping

Event client coordinates tidak selalu sama local geometry coordinates setelah transform, zoom atau scrolling.

**Model / prosedur.** Map client point through inverse relevant transform; distinguish CSS pixels and backing pixels.

**Kegagalan.** High-DPI scale double applied; scroll offset stale.

**Verifikasi.** Known points under scroll/zoom/transformed parent.

### D21.03 — Gesture recognition

Swipe, pinch dan rotate memerlukan thresholds, simultaneity dan ambiguity handling. Early recognition trades responsiveness against false positives.

**Model / prosedur.** State machine possible→recognized/cancelled; derive scale/angle from consistent pointer pair.

**Kegagalan.** Small jitter triggers swipe; recognizer steals native scroll.

**Verifikasi.** Threshold boundaries, slow drag, fast swipe, pointer replacement.

### D21.04 — Velocity estimation

Velocity dari last two samples peka noise dan coalesced events. Temporal window/filter harus mengakui delay dan irregular cadence.

**Model / prosedur.** Weighted fit or finite differences on actual timestamps; handle zero dt.

**Kegagalan.** Release velocity based stale sample; enormous velocity after tiny dt.

**Verifikasi.** Synthetic trajectories with irregular event times and noise.

### D21.05 — Keyboard wheel dan discrete input

Wheel units/modes berbeda; keyboard repeats bukan physical motion samples. Commands perlu semantik dan focus ownership.

**Model / prosedur.** Normalize units cautiously; use intent commands then model motion.

**Kegagalan.** Scroll hijack, repeated key starts competing animations.

**Verifikasi.** Keyboard-only flow, different wheel modes, focus changes.

### D21.06 — Inertial spatial dan fused sensors

Gyro, accelerometer dan orientation estimates memiliki units, frames, drift dan permissions. Gravity and linear acceleration need model separation.

**Model / prosedur.** Calibrate bias; timestamp data; fuse with explicit state/noise model if needed.

**Kegagalan.** Gyro integrated without dt; gravity interpreted translation.

**Verifikasi.** Stationary/known-rotation cases, missing samples, unit/frame conversions.

### D21.07 — Capability permission dan degradation

Sensor availability, browser support dan permission affect path. Capability detection should be behavior-based, with alternative input.

**Model / prosedur.** Detect feature, request only needed access under platform rules, handle denied/unsupported.

**Kegagalan.** Interface blocked without optional sensor; assumed microphone permission.

**Verifikasi.** Denied permission, no device, disconnect, fallback behavior.

## Contoh kerja dan alasan pemilihan

Contoh drag: pointerdown records pointerId/start pose, sets capture; moves update target from local-space displacement; pointerup estimates velocity and releases; pointercancel stops gesture with explicit state cleanup. Native touch scrolling requires touch-action policy appropriate target, not blanket disable page scrolling. Multi-touch introduction must either hand off to pinch or preserve a single-pointer rule.

## Alur implementasi

Define intents; inspect source capabilities; normalize coordinates/time; implement recognizer lifecycle; map events to intent; handle cancellation/permission; test devices and keyboard.

## Kriteria penguasaan

Dapat membangun cancellable drag recognizer, velocity estimation dan coordinate conversion dengan fixtures.

## Cabang lanjut yang tetap termasuk cakupan

Coalesced/predicted events; gesture arbitration; touch ergonomics; gaze input; voice commands; sensor fusion; body tracking; multimodal input.

## Rujukan dan batas bukti

- [S41](../../references/source-map.md#s41)
- [S42](../../references/source-map.md#s42)
- [S43](../../references/source-map.md#s43)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
