# motion

Knowledge base **Code-Driven Motion**: pengetahuan untuk merepresentasikan, membangkitkan, menganalisis, menyimulasikan, merender, menyinkronkan dan mengendalikan gerak melalui coding.

Bahasa penjelasan: Indonesia dengan technical terminology English. Repository privat milik `arsafiqri-aybi`. Version **0.1.0**; disusun 2026-10-08.

## Isi

- **40 handbook domain**, mencakup seluruh master map yang disepakati.
- **280 subdomain core** dengan explanation, model/procedure, failure modes dan verification paths.
- **8 deep dives** untuk derivation, implementasi dan hubungan lintas domain.
- **10 application tracks**: web, video, games, character animation, generative systems, simulation, audio/haptics, XR, robotics dan learned motion.
- **49 glossary terms**, diagnosis berdasarkan gejala, directed knowledge graph dengan **141 edges**.
- **90 reference entries** dengan status inspection/candidate/failure yang eksplisit; **9 scoped source claims**.
- Runnable Python references, **35 tests** dan **16 numerical labs** dengan hasil actual tercatat.

Ini berisi pengetahuan nyata, bukan folder kosong. Namun v0.1.0 adalah authored core dengan beberapa derivation/implementations yang lebih dalam, **belum seluruh specialist branches menjadi monograf mendalam atau fully audited scientific encyclopedia**. [Coverage](governance/coverage.json) dan [open gaps](governance/open-gaps.md) mempertahankan target pendalaman tanpa mengklaim selesai palsu.

## Mulai membaca

1. [Master map 40 domain](architecture/domain-map.md).
2. [Panduan knowledge dan deep dives](knowledge/README.md).
3. [Application tracks](tracks/README.md).
4. [Runnable examples](examples/README.md).
5. [Diagnosis gejala](diagnostics/README.md).
6. [Source map](references/source-map.md) dan [evidence policy](governance/evidence-policy.md).

Untuk arah portfolio frontend + high-end motion, mulai dari [Web Frontend and Interaction](tracks/01-web-interaction.md), sambil tetap menjaga seluruh domain sebagai knowledge base bersama. Libraries seperti GSAP, Motion, Three.js, Blender dan WebGPU ditempatkan pada implementation layer; mereka bukan induk ilmu.

## Rumpun pengetahuan

| Rumpun | Domain |
|---|---|
| A — Foundations | D01–D05: mathematics, geometry, time, signals, computation |
| B — Motion Models | D06–D15: interpolation, kinematics, dynamics, simulation, solvers, optimization, control, planning, procedural, learned motion |
| C — Representation and Animation | D16–D19: capture, rigging, character performance, animation composition |
| D — Behavior and Interaction | D20–D23: state/reactivity, input, interaction, synchronization |
| E — Graphics and Output | D24–D31: 2D/3D, GPU, temporal rendering, compositing, audio/haptics, XR, physical actuation |
| F — Human Experience | D32–D34: perception, choreography, accessibility |
| G — Engineering and Production | D35–D38: performance, architecture, assets, tooling/pipelines |
| H — Verification and Delivery | D39–D40: quality engineering, encoding/deployment |

## Struktur

| Path | Fungsi |
|---|---|
| `architecture/` | Stable IDs, domain schema, directed many-to-many graph, tracks |
| `knowledge/domains/` | 40 handbook utama |
| `knowledge/deep-dives/` | Derivations dan cross-domain implementation guides |
| `tracks/` | Jalur belajar sesuai application |
| `references/` | Source registry, inspection scope, claim ledger |
| `governance/` | Coverage, depth/evidence policy, gaps |
| `examples/` | Python algorithms/labs dan unexecuted WGSL example |
| `tests/` | Independent numerical/geometric fixtures |
| `diagnostics/` | Symptom → causes → discriminating checks |
| `scripts/` | Search dan local structural validation |
| `reports/` | Actual scoped verification records |

## Menjalankan

Python 3.10+; standard library, tanpa dependency berbayar.

```bash
python3 scripts/search.py "spring"
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 examples/run_labs.py --output .local-output/labs
```

Atau `make verify` dan `make labs`. Tidak ada automatic deployment atau GitHub workflow yang ditambahkan.

## Status bukti

Core domain/subdomain coverage telah ditulis. Python examples yang diuji mempunyai scope terbatas. Link/schema tests membuktikan struktur, bukan keseluruhan scientific truth. Sebagian besar references masih bibliographic candidates, bukan sumber yang selesai diaudit passage-by-passage.

Browser, GPU shader, learned training/inference, media render/decode, sensor/haptic/XR/robot runtime dan human studies **NOT_RUN**. Lihat [verification report](reports/verification.md). Pendalaman lanjutan menambah derivations, implementations dan evidence pada topic IDs yang sama, dengan [contribution contract](CONTRIBUTING.md).
