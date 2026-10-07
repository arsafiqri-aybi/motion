# D40 — Media Delivery Encoding and Deployment

Menyampaikan motion sebagai media atau application yang benar cadence, format, metadata, behavior dan runtime target-nya.

Rumpun: **H — Verification and Delivery**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Encoding success belum membuktikan decoded sequence benar. Deployment tidak sama publishing authorization; repository ini menyediakan knowledge dan examples, bukan layanan live.

Prasyarat: [D03](../../architecture/domain-map.md#d03), [D28](../../architecture/domain-map.md#d28), [D29](../../architecture/domain-map.md#d29), [D37](../../architecture/domain-map.md#d37), [D39](../../architecture/domain-map.md#d39).

## Subdomain dan pengetahuan inti

### D40.01 — Frame sequences dan timestamp contracts

Input sequence filenames/indices, timestamps dan frame rate determine output timing. Audio sample count uses its own clock.

**Model / prosedur.** Define rational cadence, first PTS, frame count, nominal duration and gaps.

**Kegagalan.** Missing frame silently held; 29.97 rounded incorrectly.

**Verifikasi.** Expected frame list and decoded timestamp/count checks.

### D40.02 — Codecs containers dan pixel formats

Codec encodes streams; container packages them. Chroma subsampling, bit depth, alpha and compatibility affect visuals.

**Model / prosedur.** Choose codec/pixel format according target; test actual playback support.

**Kegagalan.** Alpha lost, odd dimensions unsupported, banding.

**Verifikasi.** Decode output, inspect metadata and known color/alpha fixtures.

### D40.03 — Audio video muxing dan sync

Stream timebases, encoder delay and trim offsets affect synchronization. Equal durations alone do not prove aligned events.

**Model / prosedur.** Preserve timestamps; define trim/pad policy; validate markers and drift.

**Kegagalan.** Audio offset at start; resample rate metadata mismatch.

**Verifikasi.** Beginning/middle/end markers and decoded stream lengths.

### D40.04 — Resolution aspect color HDR metadata

Display aspect, sample aspect, primaries, transfer and range must match pipeline. Metadata tags do not turn SDR pixels into HDR.

**Model / prosedur.** Set source conversion and destination metadata consistently.

**Kegagalan.** Stretched video, washed blacks, wrong transfer.

**Verifikasi.** Native resolution/frame inspection and managed target playback.

### D40.05 — Compression quality size dan streaming

Bitrate/quality trade-off depends motion/detail. Streaming segments add buffering and boundary constraints.

**Model / prosedur.** Evaluate target codec/settings across representative sequence and delivery bandwidth.

**Kegagalan.** Static frame chosen bitrate; adaptive switch changes color/cadence.

**Verifikasi.** Fast motion/detail, segment transitions, bandwidth impairment.

### D40.06 — Application packaging deployment dan capabilities

Motion app must initialize assets, detect features, recover failure and support semantic baseline. Bundles/dependencies affect start latency.

**Model / prosedur.** Build reproducibly; version assets; inspect target capability fallback.

**Kegagalan.** Works dev only; unavailable WebGPU hides all content.

**Verifikasi.** Production bundle, offline/missing asset paths, target browser/device.

### D40.07 — Final verification handoff dan maintenance

Release output must be compared expected contract and actual decoded/playback behavior. Retain inputs/scripts/versions for reproduction.

**Model / prosedur.** Decode full stream where relevant; verify PTS/count/dimensions; review sequence and log limitations.

**Kegagalan.** File exists marked delivered; render job success replaces review.

**Verifikasi.** Automated properties plus actual playback/manual review, distinguished.

## Contoh kerja dan alasan pemilihan

Contoh 120-frame sequence at 60fps has nominal coverage 2s. Encode into chosen container, then decode and count frames; inspect PTS rather than trusting filename/encoder log. If audio first cue at 0.5s, verify decoded marker alignment at start and end. Keep original frames/config if compressed export shows artifacts; output quality can be revised without rebuilding model.

## Alur implementasi

Define delivery contract; choose codec/package; generate outputs; decode/validate properties; playback target; inspect sync/color; preserve reproduction/version; release with scoped evidence.

## Kriteria penguasaan

Dapat menghasilkan media dengan explicit timestamps, menjaga color/alpha/sync dan memverifikasi output melalui decode.

## Cabang lanjut yang tetap termasuk cakupan

Adaptive streaming; media containers; video codecs; audio coding; HDR delivery; alpha codecs; app bundles; deployment compatibility; archival masters.

## Rujukan dan batas bukti

- [S61](../../references/source-map.md#s61)
- [S89](../../references/source-map.md#s89)
- [S90](../../references/source-map.md#s90)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
