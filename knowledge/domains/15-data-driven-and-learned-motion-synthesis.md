# D15 — Data Driven and Learned Motion Synthesis

Membangkitkan, memilih atau mengadaptasi gerak menggunakan examples dan models learned dari data.

Rumpun: **B — Motion Models**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Dataset/model availability tidak sama dengan domain coverage. Learned outputs perlu constraints, evaluation, provenance dan deployment checks; capture D16 menghasilkan observations.

Prasyarat: [D01](../../architecture/domain-map.md#d01), [D05](../../architecture/domain-map.md#d05), [D11](../../architecture/domain-map.md#d11), [D16](../../architecture/domain-map.md#d16), [D19](../../architecture/domain-map.md#d19).

## Subdomain dan pengetahuan inti

### D15.01 — Datasets dan representation

Motion data memuat poses, root trajectory, contacts, skeleton/frame conventions dan rate. Representation menentukan what model can learn.

**Model / prosedur.** Normalize units/frames; preserve transform metadata; split by meaningful subject/sequence groups.

**Kegagalan.** Train/test leakage through near-duplicate clips; skeleton mismatch.

**Verifikasi.** Metadata audit, duplicate checks, joint conventions and held-out split integrity.

### D15.02 — Example-based synthesis

Motion clips dapat dipilih/diinterpolasi berdasarkan state, target, style atau similarity. Distance metric menentukan useful match.

**Model / prosedur.** Feature vector of pose/velocity/future trajectory; nearest-neighbor search with calibrated scales.

**Kegagalan.** Foot skating at transitions; metric dominated root position.

**Verifikasi.** Transition continuity, contact preservation, trajectory error.

### D15.03 — Motion graphs dan matching

Graph transitions menghubungkan compatible clip segments. Motion matching memilih samples continuously berdasarkan query cost. Coverage dataset menentukan reachable behavior.

**Model / prosedur.** Build transition candidates with pose/velocity compatibility; evaluate query against dataset features.

**Kegagalan.** Dead-end graph; oscillatory rapid clip switches.

**Verifikasi.** Reachability, transition rate, novel query failure and temporal continuity.

### D15.04 — Statistical dan probabilistic models

Distributions capture variability, tetapi likelihood tidak sama dengan task correctness. Latent state may encode style and motion structure.

**Model / prosedur.** Mixture, autoregressive or latent-variable models with explicit conditioning.

**Kegagalan.** Mean motion looks washed-out; probability calibration ignored.

**Verifikasi.** Held-out predictive error, sample diversity, constraint violation rates.

### D15.05 — Neural generative motion

Learned networks map conditions to pose sequences or dynamics. Diffusion/autoregressive models mempunyai latency dan controllability trade-offs.

**Model / prosedur.** Evaluate text/action/trajectory-conditioned generation; postprocess only with documented effect.

**Kegagalan.** Plausible-looking but impossible contacts; output lengths/rates mismatched.

**Verifikasi.** Contact, joint bounds, task metrics, diverse scenarios and timing.

### D15.06 — Reinforcement learning policies

Policy chooses actions from state to maximize defined reward. Reward shaping, simulated plant dan exploration constrain learned behavior.

**Model / prosedur.** π(a|s); training environment and action limits specified; transfer checked separately.

**Kegagalan.** Reward hacking, unstable unseen states, simulator exploitation.

**Verifikasi.** Perturbed environments, held-out dynamics, failure recovery, real-time inference.

### D15.07 — Evaluation provenance dan deployment

Training sources, licenses, model versions, seeds, preprocessing dan device determine reproducibility. Perceptual quality requires human evidence separate from numerical metrics.

**Model / prosedur.** Record dataset/model hashes and generation settings; benchmark latency and memory on target.

**Kegagalan.** Model demo mistaken full benchmark; licensed data redistributed without basis.

**Verifikasi.** Versioned evaluation sets, performance measurements, constraint tests and documented limitations.

## Contoh kerja dan alasan pemilihan

Contoh locomotion matching uses current pose, velocity, desired future direction dan speed. Normalize feature groups agar unit meter tidak mendominasi angular features. Setelah retrieval, blend dengan pose saat ini dan preserve contact intervals bila memungkinkan. Jika desired motion tidak terdapat pada database, return degraded behavior atau fallback; nearest sample tetap ada secara matematis, tetapi belum tentu sesuai task.

## Alur implementasi

Audit dataset/provenance; choose representation; define task metrics; establish nonlearned baseline; train/select model; test generalization and constraints; measure target runtime; preserve fallback.

## Kriteria penguasaan

Dapat membangun example-based baseline, mendeteksi leakage, serta mengukur contact/task errors terpisah dari perceptual quality.

## Cabang lanjut yang tetap termasuk cakupan

Diffusion motion models; transformers; learned dynamics; physics-informed learning; imitation learning; skill discovery; sim-to-real; controllable motion editing; uncertainty-aware policies.

## Rujukan dan batas bukti

- [S28](../../references/source-map.md#s28)
- [S29](../../references/source-map.md#s29)
- [S30](../../references/source-map.md#s30)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
