# D03 — Time Timing Sampling and Temporal Systems

Menentukan arti waktu, progress, dan cadence agar motion konsisten saat dijalankan, di-seek, diperlambat, dirender offline, atau dikendalikan input.

Rumpun: **A — Foundations**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Domain ini menetapkan clock dan mapping temporal. Scheduling compute D35; synchronization antarstream D23; exposure sampling D27. Wall-clock calendar tidak otomatis cocok menjadi simulation clock.

Prasyarat: [D01](../../architecture/domain-map.md#d01), [D05](../../architecture/domain-map.md#d05).

## Subdomain dan pengetahuan inti

### D03.01 — Clock domains dan time origins

Clock display, audio, media, network, dan simulation bisa memiliki origin dan rate berbeda. Monotonic clock cocok mengukur interval; wall clock dapat meloncat setelah penyesuaian waktu.

**Model / prosedur.** Timestamp harus membawa clock_id dan unit. Mapping awal dapat berupa tB=a tA+b dengan rate a dan offset b.

**Kegagalan.** Mengurangi timestamps dari clock berbeda; hidden-tab pause dianggap waktu aktif pengguna.

**Verifikasi.** Uji clock jump, pause/resume, dan perubahan playback rate dengan expected semantic state.

### D03.02 — Timeline mapping

Timeline progress berasal dari clock maupun scroll/gesture. Animation local time berbeda dari timeline time dan iteration progress. Fill behavior menentukan nilai di luar active interval.

**Model / prosedur.** Untuk duration d>0, local=(timeline−start)·rate; progress=clamp(local/d,0,1) hanya untuk animasi sekali tanpa delay/loop.

**Kegagalan.** Formula sederhana dipakai untuk repeats, negative rates, inactive timelines, atau d=0.

**Verifikasi.** Fixture boundary sebelum start, tepat start/end, reversal, zero duration, dan inactive source.

### D03.03 — Delta-time dan integration cadence

Δt mengukur elapsed time, tetapi simulasi bisa memakai timestep tetap. Display fps dan simulation Hz tidak harus sama. Batas catch-up diperlukan setelah stall panjang.

**Model / prosedur.** Accumulator+=elapsed; selama accumulator≥h jalankan step(h); render dapat interpolate previous/current menggunakan accumulator/h.

**Kegagalan.** Spiral of death, dropped time tanpa catatan, variable-step instability.

**Verifikasi.** Uji display 30/60/120Hz dan stall; ukur hasil state serta jumlah steps.

### D03.04 — Frame sampling dan timestamp arithmetic

Frame n pada constant rational fps p/q mempunyai t=n q/p. Evaluasi langsung dari index mencegah akumulasi roundoff repeated addition. Jumlah frame dan durasi stream memiliki convention.

**Model / prosedur.** Untuk N frames, last sample=(N−1)/fps dan nominal coverage=N/fps; keduanya jangan disamakan.

**Kegagalan.** Frame terakhir keliru dianggap seluruh durasi; 29.97 dibulatkan padahal target 30000/1001.

**Verifikasi.** Periksa rational arithmetic, expected count, first/last PTS, dan coverage semantics.

### D03.05 — Seeking reverse dan determinism

Pure animation evaluator F(t) mudah di-seek. Stateful simulation membutuhkan replay, checkpoint, atau solusi analitik. Reverse playback bukan berarti menegasikan Δt pada dissipative solver.

**Model / prosedur.** Pisahkan evaluate(time) dari advance(dt); simpan checkpoints berisi state, seed, model parameters dan time.

**Kegagalan.** Seek mengubah state lama dua kali; reverse physics tidak stabil; cache dianggap deterministic lintas arsitektur.

**Verifikasi.** Seek ke t dari beberapa histori; bandingkan dengan baseline replay dan nyatakan tolerance.

### D03.06 — Time remapping dan continuity

Mengubah playback rate atau time-warp mengubah velocity dan acceleration visual. Derivative chain rule diperlukan untuk memahami dampak easing waktu.

**Model / prosedur.** x(t)=p(u(t)); x′=p′(u)u′; x″=p″(u)(u′)²+p′(u)u″.

**Kegagalan.** Progress continuous tetapi velocity meloncat; rate berubah dengan reset origin sehingga posisi jump.

**Verifikasi.** Ukur position dan finite-difference velocity tepat sebelum/sesudah remap boundary.

### D03.07 — Latency jitter dan temporal contracts

Average delay berbeda dari variation delay. Motion system membutuhkan kebijakan data terlambat: discard, interpolate, predict, atau rewind. Temporal contract menghubungkan input age dan output deadline.

**Model / prosedur.** Catat acquisition, processing, submission, presentation timestamps jika tersedia; end-to-end latency tidak sama dengan compute time.

**Kegagalan.** FPS tinggi dianggap responsiveness rendah latency; clock offset salah dianggap network lag.

**Verifikasi.** Inject known delays/jitter dan periksa queue growth, stale-data handling, serta event order.

## Contoh kerja dan alasan pemilihan

Contoh: animasi 2 detik dirender 60fps memakai 120 samples pada t=n/60 untuk n=0…119. Nilai endpoint t=2 tidak termasuk sample terakhir, tetapi nominal coverage adalah 2 detik. Jika frame final harus menampilkan progress tepat 1, jadwalkan hold atau atur sampling convention secara eksplisit; jangan diam-diam mengubah duration. Untuk preview 120Hz, evaluasi F(t) yang sama, sehingga trajectory tidak bergantung fps.

## Alur implementasi

Tetapkan clock IDs/unit; definisikan duration/progress semantics; pisahkan evaluation dan advancing; pilih sampling; tulis pause/seek/reverse behavior; verifikasi timestamps dan boundary conditions.

## Kriteria penguasaan

Dapat mengonversi clock dengan kontrak, menjelaskan fixed-step accumulator, merender rational cadence tanpa drift, dan menguji seek. Latihan: jalankan timeline yang sama dengan timestamps tidak teratur.

## Cabang lanjut yang tetap termasuk cakupan

Multirate systems; event-driven simulation; continuous-time state estimation; clock discipline; timecode/drop-frame notation; temporal databases; deterministic rollback; timestamp uncertainty.

## Rujukan dan batas bukti

- [S05](../../references/source-map.md#s05)
- [S06](../../references/source-map.md#s06)
- [S07](../../references/source-map.md#s07)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
