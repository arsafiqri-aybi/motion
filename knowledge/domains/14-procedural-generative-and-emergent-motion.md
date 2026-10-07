# D14 — Procedural Generative and Emergent Motion

Menghasilkan gerak melalui rules, fields, randomness, dan interactions yang dapat direproduksi serta diarahkan secara kreatif.

Rumpun: **B — Motion Models**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Procedural bukan otomatis physically plausible atau learned. Domain 15 menangani models fitted/trained dari data; generative visual control tetap memerlukan D33.

Prasyarat: [D01](../../architecture/domain-map.md#d01), [D03](../../architecture/domain-map.md#d03), [D04](../../architecture/domain-map.md#d04), [D05](../../architecture/domain-map.md#d05).

## Subdomain dan pengetahuan inti

### D14.01 — Oscillators dan periodic systems

Periodic signals menjadi basis pulsing, orbital motion, waves, dan rhythmic coordination. Frequency dan phase harus berbasis waktu.

**Model / prosedur.** x=A sin(ωt+φ); combine frequencies for beats; phase accumulator update ωΔt.

**Kegagalan.** Frame-based increments; discontinuity at phase reset.

**Verifikasi.** Repeatability, period, amplitude dan fps invariance.

### D14.02 — Randomness dan coherent noise

White randomness berubah independen; coherent noise menghubungkan nearby coordinates. Seed, space/time scale, distribution dan correlation menentukan character motion.

**Model / prosedur.** Evaluate noise(x·scale,t·speed); use independent RNG streams per entity.

**Kegagalan.** Every frame reseed; changing iteration order changes all particles.

**Verifikasi.** Deterministic replay, statistics, spatial/temporal correlation.

### D14.03 — Fields dan flow

Vector field mengarahkan velocity/force di ruang. Field dapat time-dependent dan punya singularities/boundary behavior.

**Model / prosedur.** dx/dt=F(x,t); curl-derived field can produce divergence-free construction under assumptions.

**Kegagalan.** Field scale mislabeled speed; singular attraction explodes.

**Verifikasi.** Known flow trajectories, divergence check, boundary tests.

### D14.04 — Rule systems dan grammars

Local rules, rewrite grammars dan state transitions menentukan procedural structure. Rule priority dan termination penting.

**Model / prosedur.** L-systems generate structures; grammar expansion bounded by depth/resource budgets.

**Kegagalan.** Exponential growth, contradictory rules, unintended infinite recursion.

**Verifikasi.** Rule fixtures, termination limits, count-growth analysis.

### D14.05 — Agents flocking dan swarms

Separation/alignment/cohesion membentuk group behavior. Neighborhood, acceleration limits dan integration mengubah emergence.

**Model / prosedur.** Compute forces from shared snapshot; neighbor radius and weights explicit; enforce action limits.

**Kegagalan.** Sequential update bias; all-pairs cost; density collapse.

**Verifikasi.** Order independence, collision rate, bounded speed and dense scenes.

### D14.06 — Cellular systems dan reaction diffusion

Local update rules dapat menghasilkan complex patterns. Discrete grid/time assumptions menentukan stability dan anisotropy.

**Model / prosedur.** Cellular automata use synchronous transitions; reaction-diffusion integrates coupled PDE discretization.

**Kegagalan.** In-place updates change rule semantics; unstable diffusion timestep.

**Verifikasi.** Symmetry, boundary modes, known simple patterns, refinement.

### D14.07 — Art direction dan parameter spaces

Generative richness harus dikendalikan agar mendukung purpose. Parameter ranges, presets dan sensitivity menjaga usable exploration.

**Model / prosedur.** Expose frequency, density, correlation, force gains; annotate valid combinations.

**Kegagalan.** Random result claimed universally pleasing; knobs duplicate same effect.

**Verifikasi.** Seed sweeps, parameter extremes, constraints and human review.

## Contoh kerja dan alasan pemilihan

Contoh flocking: snapshot seluruh positions/velocities, query neighbors via grid, hitung three steering terms, batasi acceleration, lalu integrate seluruh agents. Gunakan seed per agent agar menambah satu agent tidak mengubah RNG semua yang lain. Masukkan asymmetric obstacles untuk menguji robustness; pola cantik pada scene kosong belum membuktikan navigation reliable.

## Alur implementasi

Definisikan generative rules/state; specify randomness; constrain rates/limits; implement snapshot update; instrument behavior; expose meaningful parameters; evaluate many seeds plus adversarial scenes.

## Kriteria penguasaan

Dapat mereproduksi generative motion, menjelaskan emergence dari rules, dan memisahkan field model dari numerical integration.

## Cabang lanjut yang tetap termasuk cakupan

Chaos; nonlinear oscillators; attractors; fractals; self-organization; complex adaptive systems; procedural ecosystems; evolutionary search; generative choreography.

## Rujukan dan batas bukti

- [S25](../../references/source-map.md#s25)
- [S26](../../references/source-map.md#s26)
- [S27](../../references/source-map.md#s27)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
