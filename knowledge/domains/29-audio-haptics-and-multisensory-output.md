# D29 — Audio Haptics and Multisensory Output

Menghubungkan sound, visual motion dan tactile output melalui measured signals, time contracts dan designed response.

Rumpun: **E — Graphics and Output**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Audio-reactive features tidak otomatis memahami musik; haptic waveform tidak sama across actuators; perceptual effects D32 memerlukan context/human evidence.

Prasyarat: [D03](../../architecture/domain-map.md#d03), [D04](../../architecture/domain-map.md#d04), [D23](../../architecture/domain-map.md#d23).

## Subdomain dan pengetahuan inti

### D29.01 — Audio synthesis dan processing

Oscillators, envelopes, filters dan mixing membuat audio output. Sample rate and amplitude representation menentukan evaluation.

**Model / prosedur.** Generate/control audio using audio clock; envelope attacks/releases avoid clicks.

**Kegagalan.** Visual rAF drives sample-level synthesis; clipping.

**Verifikasi.** Known-frequency waveform, level bounds and discontinuity checks.

### D29.02 — Waveform spectrum dan features

RMS, amplitude peak, spectrum and spectral flux represent different properties. True peak/LUFS need specific algorithms, not RMS relabeling.

**Model / prosedur.** Define window/hop/channel aggregation and calibration.

**Kegagalan.** Mono cancellation, DC counted energy, mislabeled level metrics.

**Verifikasi.** Known tones, silence, impulses, stereo phase cases.

### D29.03 — Onsets rhythm dan mapping

Onsets, beats and tempo are distinct estimates. Mapping visual scale to loudness needs smoothing and bounded response.

**Model / prosedur.** Feature→normalized control→motion evaluator; threshold with hysteresis/refractory as appropriate.

**Kegagalan.** Every peak triggers beat; excessive visual flicker.

**Verifikasi.** Silence/noise/tempo changes, false triggers and review.

### D29.04 — Spatial audio

Position/orientation and acoustics shape perceived audio location. Listener frame must align visual scene.

**Model / prosedur.** Update sources/listener at controlled rate; choose attenuation/spatialization model.

**Kegagalan.** Left/right inversion, source position in wrong unit.

**Verifikasi.** Known source trajectories and listener rotations.

### D29.05 — Haptic waveforms dan actuator limits

Device actuator supports certain frequencies/intensities/time granularity. Software event cannot guarantee identical tactile sensation.

**Model / prosedur.** Map intent to supported envelope/pattern with capability fallback.

**Kegagalan.** Unsupported haptics essential for task; intensity too rapidly repeated.

**Verifikasi.** Capability detection, timing logs and device/user observations.

### D29.06 — Scheduling synchronization dan latency

Audio scheduler and presentation clock may differ. Processing timestamp does not measure acoustic or tactile output time.

**Model / prosedur.** Schedule against audio clock, log mapping, estimate output delays where measurable.

**Kegagalan.** Audio event callback assumed exact speaker onset.

**Verifikasi.** Known synchronized markers, instrumented device observations.

### D29.07 — Multisensory semantics dan adaptation

Output channels should reinforce task meaning. Redundant alternatives support silent devices and users who cannot use a channel.

**Model / prosedur.** State information in accessible visual/text plus optional sound/haptic cues.

**Kegagalan.** Notification meaningful only through sound; sensory overload.

**Verifikasi.** Silent/no-haptic paths, preference controls and context evaluation.

## Contoh kerja dan alasan pemilihan

Contoh audio-reactive particle radius from window RMS. Remove/inspect DC as appropriate; normalize with declared range and smooth time-aware envelope. radius=base+gain·feature is a mapping choice, not physical relationship. Keep radius bounds so silence remains readable and peaks do not obscure labels. If beat synchronization is needed, RMS alone is insufficient.

## Alur implementasi

Define channel purpose; inspect capability; specify signal metrics; align clocks; build bounded mappings; avoid clicks/overload; test silent/fallback modes and actual device output.

## Kriteria penguasaan

Dapat menghasilkan valid audio features, menjelaskan latency boundaries dan membuat mappings yang tetap berguna tanpa sound/haptics.

## Cabang lanjut yang tetap termasuk cakupan

DSP synthesis; spatial acoustics; auditory displays; music information retrieval; tactile rendering; force feedback; vibrotactile design; multimodal timing research.

## Rujukan dan batas bukti

- [S46](../../references/source-map.md#s46)
- [S62](../../references/source-map.md#s62)
- [S63](../../references/source-map.md#s63)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
