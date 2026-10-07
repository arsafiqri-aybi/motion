# D04 — Signal Processing and Reconstruction

Mengubah samples menjadi informasi gerak yang dapat digunakan, dengan perhatian terhadap noise, aliasing, filtering, dan delay.

Rumpun: **A — Foundations**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Signal processing memperkirakan atau membentuk sinyal. Ia tidak membuktikan sensor benar atau gerak manusia aman; capture calibration D16, control D12, perception D32 memberikan batas tambahan.

Prasyarat: [D01](../../architecture/domain-map.md#d01), [D03](../../architecture/domain-map.md#d03).

## Subdomain dan pengetahuan inti

### D04.01 — Sampling dan aliasing

Sinyal band-limited ideal dapat direkonstruksi jika sampling rate melebihi dua kali frekuensi tertinggi. Sinyal nyata perlu anti-alias filtering; gerak tajam tidak benar-benar band-limited.

**Model / prosedur.** Sinus f dan f+k fs dapat memberi sample indistinguishable. Gunakan low-pass sebelum downsampling.

**Kegagalan.** Menghaluskan setelah aliasing dianggap memulihkan detail asli; irregular samples diperlakukan seragam.

**Verifikasi.** Sample sinus di bawah/atas Nyquist dan compare apparent frequency; uji prefilter sebelum decimation.

### D04.02 — Convolution dan filters

Filter linear time-invariant menggabungkan samples melalui impulse response. FIR mudah mengontrol finite support; IIR menggunakan state feedback dan perlu stability assessment.

**Model / prosedur.** y[n]=Σh[k]x[n−k]; first-order low-pass y[n]=αx[n]+(1−α)y[n−1].

**Kegagalan.** Filter initialization spike; coefficients untuk sampling rate lain; overflow atau unstable poles.

**Verifikasi.** Impulse/step response, steady-state gain, noise suppression, dan output finite pada input bounded.

### D04.03 — Frequency analysis

Spectrum mengungkap periodicity dan bandwidth, tetapi finite windows menyebabkan leakage. FFT bin width bukan selalu frequency-resolution kemampuan membedakan dua sinyal.

**Model / prosedur.** Δf=fs/N. Terapkan window, catat normalization, sampling rate, dan apakah magnitude power atau amplitude.

**Kegagalan.** FFT index dipakai sebagai Hz; DC dianggap beat; zero padding dianggap informasi baru.

**Verifikasi.** Known-frequency sine dengan amplitudo diketahui; periksa dominant bins, leakage, dan reconstruction.

### D04.04 — Differentiation dan smoothing trajectories

Numerical derivative memperbesar high-frequency noise. Smoothing sebelum derivative mengurangi noise dengan trade-off lag dan detail. Central differences membutuhkan samples masa depan.

**Model / prosedur.** v[n]≈(x[n+1]−x[n−1])/(2h); acceleration memperbesar noise lagi. Local polynomial fitting dapat menghasilkan derivative halus.

**Kegagalan.** Derivative tidak membagi dt; causal preview memakai future samples tanpa mengakui latency.

**Verifikasi.** Trajectory analitik plus noise terkontrol; ukur derivative error dan group delay.

### D04.05 — Resampling dan interpolation

Resampling mengubah sample grid, sehingga timestamps dan boundary behavior penting. Linear interpolation murah tetapi bukan ideal reconstruction untuk seluruh bandwidth.

**Model / prosedur.** Upsampling melalui reconstruction lalu sampling grid baru; downsampling perlu antialias low-pass.

**Kegagalan.** Samples hilang diisi sebagai nol; repeated resampling menyebabkan blur; clock drift tidak diperbaiki.

**Verifikasi.** Bandingkan resampled waveform dengan analytic oracle dan ukur end-to-end timing drift.

### D04.06 — Correlation dan feature detection

Cross-correlation mencari similarity terhadap lag; tidak otomatis membuktikan causality. Peak/onset/beat berbeda jenis event. Threshold dan refractory period menentukan false positives.

**Model / prosedur.** Rxy[k]=Σx[n]y[n+k] untuk convention yang dinyatakan; normalize jika membandingkan amplitudo berbeda.

**Kegagalan.** Salah sign lag; amplitude bias; peak energi diklaim beat musikal universal.

**Verifikasi.** Shift sinyal diketahui dan recover lag; uji silence, noise, double peaks, dan tempo changes.

### D04.07 — State estimation dan uncertainty

Filter dapat menggabungkan prediction model dan noisy measurement. Measurement covariance harus berdimensi benar; asumsi Gaussian/linear membatasi interpretasi.

**Model / prosedur.** Kalman predict/update memakai model state transition, process noise Q, measurement noise R; gain menentukan trade-off.

**Kegagalan.** Covariance tuning tanpa unit; estimate diperlakukan ground truth; missing data dianggap zero.

**Verifikasi.** Synthetic system dengan noise known; periksa residuals, covariance consistency, dan missing-measurement behavior.

## Contoh kerja dan alasan pemilihan

Contoh: cursor tracker noisy pada 120Hz. Gunakan causal low-pass dengan α=1−exp(−Δt/τ) dan τ=0.04s. Pada Δt≈0.00833s, α≈0.188. Ini menjaga time constant saat sampling berubah. Filtering mengurangi noise tetapi menambah delay; jangan mengklaim output lebih akurat tanpa ground truth. Untuk drag yang harus terasa dekat input, ukur spatial lag pada kecepatan representative dan pertimbangkan adaptive filtering.

## Alur implementasi

Deklarasikan source clock dan rate; inspeksi missingness/noise; pilih causal/noncausal mode; tentukan bandwidth; implementasikan boundaries; ukur noise, delay, dan error; simpan raw input untuk diagnosis.

## Kriteria penguasaan

Dapat menjelaskan aliasing, filter delay, FFT normalization, dan uncertainty. Latihan: bandingkan moving average dengan time-aware exponential filter pada irregular timestamps.

## Cabang lanjut yang tetap termasuk cakupan

Wavelets; multiresolution analysis; spectral estimation; Wiener filtering; adaptive filters; sensor fusion; nonlinear filtering; optical-flow regularization; change-point detection; system identification.

## Rujukan dan batas bukti

- [S01](../../references/source-map.md#s01)
- [S08](../../references/source-map.md#s08)
- [S09](../../references/source-map.md#s09)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
