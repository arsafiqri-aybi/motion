# D32 — Motion Perception and Human Factors

Menjelaskan hubungan antara stimulus bergerak, perception, attention, task dan individual/context differences.

Rumpun: **F — Human Experience**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Perceptual outcome tidak dapat disimpulkan hanya dari equations atau screenshot. Pisahkan stimulus properties, scientific findings scoped, heuristic design dan actual human observations.

Prasyarat: [D03](../../architecture/domain-map.md#d03), [D04](../../architecture/domain-map.md#d04), [D27](../../architecture/domain-map.md#d27).

## Subdomain dan pengetahuan inti

### D32.01 — Apparent motion dan sampling perception

Discrete images dapat menghasilkan perceived continuous motion atau ambiguity. Frame rate, stimulus structure dan exposure sama-sama relevan.

**Model / prosedur.** Define spatial displacement, cadence, contrast and exposure of stimulus before interpretation.

**Kegagalan.** Universal smoothness threshold based fps alone.

**Verifikasi.** Controlled stimuli/settings and participant observations; technical cadence separately.

### D32.02 — Speed acceleration dan weight impressions

Perceived speed/weight dipengaruhi trajectory, timing, shape dan context. Physical mass cannot generally recovered dari visual acceleration tanpa force information.

**Model / prosedur.** Track stimulus trajectory and explicitly label inferred impression as subjective/conditional.

**Kegagalan.** Slow object called objectively heavy; numeric velocity equated perceived speed.

**Verifikasi.** Controlled parameter comparisons and actual judgments with stated participants.

### D32.03 — Biological motion dan expression

Coordinated joint patterns can convey action/identity/style. Recognition depends stimulus and observer familiarity.

**Model / prosedur.** Compare intact/scrambled point-light patterns when researching biological-motion effects.

**Kegagalan.** Any joint movement claimed human-like; acting judged from one frame.

**Verifikasi.** Full sequences, recognizability tasks and demographic/context limits.

### D32.04 — Attention salience dan tracking

Movement can capture attention but competing cues/goals affect outcome. Design plan is not measured gaze.

**Model / prosedur.** Define target regions/time windows; choose behavioral or eye-tracking measurements appropriate task.

**Kegagalan.** Motion always assumed dominant; invented saliency percentages.

**Verifikasi.** Task success, gaze if measured, competing cue scenarios.

### D32.05 — Temporal rhythm continuity dan causality

Relative timing and sequencing influence grouping and apparent causal relationships. A universal delay threshold is inappropriate across tasks.

**Model / prosedur.** Specify onset/offset relation, object geometry and stimulus parameters.

**Kegagalan.** Fixed milliseconds rule without context; coincidence considered causal proof.

**Verifikasi.** Controlled timing sweep and stated perception task.

### D32.06 — Cognitive load dan predictability

Motion can explain transition or distract from reading/decision. Novelty, density and repeated movement affect demand.

**Model / prosedur.** Form hypothesis tied task; compare comprehension/errors with alternatives.

**Kegagalan.** More movement claimed more engagement without evidence.

**Verifikasi.** Task measures, qualitative observations and repeated-use sessions.

### D32.07 — Crossmodal perception dan variation

Sound/visual/haptic timing can alter interpretation; sensitivity differs by individuals/devices/context.

**Model / prosedur.** Measure channel timing and subjective judgments separately, with actual setup.

**Kegagalan.** Synchrony tolerance assumed universal; device timestamp equated perceived onset.

**Verifikasi.** Participant/device-specific tests and uncertainty reporting.

## Contoh kerja dan alasan pemilihan

Contoh dua cards: satu bergerak cepat lalu berhenti tajam, satu bergerak dengan long deceleration. Reviewer mungkin menilai card kedua lebih berat, tetapi trajectory sendiri tidak mengidentifikasi physical mass. Jika ingin evidence, gunakan controlled comparison dan tanyakan specified perceptual task. Catat desain sebagai heuristic sampai hasil pengguna tersedia.

## Alur implementasi

Define stimulus/task; identify applicable research; preserve population/system limits; separate measurement and inference; evaluate alternatives; record observations and uncertainty.

## Kriteria penguasaan

Dapat membedakan mathematical motion, physical explanation dan perceived impression; merancang evaluasi tanpa invented human outcomes.

## Cabang lanjut yang tetap termasuk cakupan

Psychophysics; ecological perception; eye movements; predictive processing; visual attention; biological motion; temporal cognition; crossmodal integration.

## Rujukan dan batas bukti

- [S69](../../references/source-map.md#s69)
- [S70](../../references/source-map.md#s70)
- [S71](../../references/source-map.md#s71)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
