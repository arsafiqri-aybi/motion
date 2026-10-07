# Master map — 40 domain

Arsitektur disepakati dalam percakapan 2026-10-08. Domain adalah organizational unit, bukan klaim taxonomy universal. Setiap handbook mempunyai tujuh subdomain tertulis, contoh kerja, workflow, failure modes, checks, dan advanced scope.

## D01

[Mathematical Foundations for Motion](../knowledge/domains/01-mathematical-foundations-for-motion.md) — A — Foundations

Bahasa kuantitatif untuk merepresentasikan perubahan. Gerak yang dapat diprogram membutuhkan besaran, hubungan antarbesaran, dan asumsi yang memungkinkan perhitungan serta pembuktian.

## D02

[Geometry Spatial Representation and Computational Geometry](../knowledge/domains/02-geometry-spatial-representation-and-computational-geometry.md) — A — Foundations

Menetapkan bentuk, orientasi, posisi, dan query spasial yang dipakai animasi, rendering, simulasi, serta planning.

## D03

[Time Timing Sampling and Temporal Systems](../knowledge/domains/03-time-timing-sampling-and-temporal-systems.md) — A — Foundations

Menentukan arti waktu, progress, dan cadence agar motion konsisten saat dijalankan, di-seek, diperlambat, dirender offline, atau dikendalikan input.

## D04

[Signal Processing and Reconstruction](../knowledge/domains/04-signal-processing-and-reconstruction.md) — A — Foundations

Mengubah samples menjadi informasi gerak yang dapat digunakan, dengan perhatian terhadap noise, aliasing, filtering, dan delay.

## D05

[Computational Foundations Algorithms and Data Structures](../knowledge/domains/05-computational-foundations-algorithms-and-data-structures.md) — A — Foundations

Membuat representasi dan algoritma yang mengubah teori motion menjadi perhitungan efisien, dapat dilacak, dan cukup reproducible.

## D06

[Interpolation Easing and Transition Models](../knowledge/domains/06-interpolation-easing-and-transition-models.md) — B — Motion Models

Menghubungkan nilai atau pose antarwaktu dengan kontrol terhadap bentuk lintasan, continuity, dan interruption.

## D07

[Kinematics](../knowledge/domains/07-kinematics.md) — B — Motion Models

Mendeskripsikan gerak dan hubungan antarjoint tanpa terlebih dahulu menentukan forces penyebabnya.

## D08

[Dynamics and Physical Modeling](../knowledge/domains/08-dynamics-and-physical-modeling.md) — B — Motion Models

Memilih persamaan yang menjelaskan pengaruh force, inertia, energy, dan material terhadap motion.

## D09

[Physics Simulation Systems](../knowledge/domains/09-physics-simulation-systems.md) — B — Motion Models

Membangun simulator bodies, contacts dan materials dari model fisik dan discretization yang dipilih.

## D10

[Numerical Methods and Solvers](../knowledge/domains/10-numerical-methods-and-solvers.md) — B — Motion Models

Mengaproksimasi persamaan motion pada komputer dengan batas stability, accuracy, cost, dan convergence yang jelas.

## D11

[Optimization and Inverse Problems](../knowledge/domains/11-optimization-and-inverse-problems.md) — B — Motion Models

Mencari parameters, trajectories, atau controls yang memenuhi tujuan dan constraints melalui perhitungan.

## D12

[Control Theory and Feedback Systems](../knowledge/domains/12-control-theory-and-feedback-systems.md) — B — Motion Models

Mengatur motion berdasarkan reference, estimated state, dan feedback agar tracking atau stabilization sesuai constraints.

## D13

[Motion Planning and Navigation](../knowledge/domains/13-motion-planning-and-navigation.md) — B — Motion Models

Menentukan jalur dan timing yang dapat mencapai tujuan sambil menghormati obstacles, kinematic limits, serta interaksi agen.

## D14

[Procedural Generative and Emergent Motion](../knowledge/domains/14-procedural-generative-and-emergent-motion.md) — B — Motion Models

Menghasilkan gerak melalui rules, fields, randomness, dan interactions yang dapat direproduksi serta diarahkan secara kreatif.

## D15

[Data Driven and Learned Motion Synthesis](../knowledge/domains/15-data-driven-and-learned-motion-synthesis.md) — B — Motion Models

Membangkitkan, memilih atau mengadaptasi gerak menggunakan examples dan models learned dari data.

## D16

[Motion Capture Tracking and Reconstruction](../knowledge/domains/16-motion-capture-tracking-and-reconstruction.md) — C — Representation and Animation

Menghasilkan observations dan reconstructed motion dari sensor, gambar atau video dengan coordinate, time, uncertainty dan provenance yang eksplisit.

## D17

[Rigging Articulation and Deformation Systems](../knowledge/domains/17-rigging-articulation-and-deformation-systems.md) — C — Representation and Animation

Membangun kontrol dan representasi deformasi yang menghubungkan motion parameters dengan bentuk yang dirender.

## D18

[Character Motion Biomechanics and Performance](../knowledge/domains/18-character-motion-biomechanics-and-performance.md) — C — Representation and Animation

Mengorganisasikan gerak articulated agar contact, balance, expression dan performance sesuai tujuan visual atau fisik.

## D19

[Animation Representation Composition and Evaluation](../knowledge/domains/19-animation-representation-composition-and-evaluation.md) — C — Representation and Animation

Menyimpan, mengevaluasi, dan menggabungkan gerak menjadi pose/property state yang konsisten sepanjang timeline.

## D20

[State Event and Reactive Motion Architecture](../knowledge/domains/20-state-event-and-reactive-motion-architecture.md) — D — Behavior and Interaction

Membuat motion menjadi respons sistem yang predictable terhadap state, events, asynchronous work, dan interruptions.

## D21

[Input Gesture and Sensor Systems](../knowledge/domains/21-input-gesture-and-sensor-systems.md) — D — Behavior and Interaction

Mengubah input perangkat menjadi events/gestures/state estimates dengan timestamps, coordinate frames dan cancellation yang jelas.

## D22

[Interaction Design and Direct Manipulation](../knowledge/domains/22-interaction-design-and-direct-manipulation.md) — D — Behavior and Interaction

Menentukan mapping yang terasa jelas dan konsisten antara tindakan pengguna, state, dan visual motion.

## D23

[Synchronization and Distributed Motion Systems](../knowledge/domains/23-synchronization-and-distributed-motion-systems.md) — D — Behavior and Interaction

Menyelaraskan motion antarstream, perangkat atau users sambil menangani offset, drift, latency, missingness dan authority.

## D24

[2D Graphics and Rendering](../knowledge/domains/24-2d-graphics-and-rendering.md) — E — Graphics and Output

Mengubah state motion menjadi gambar 2D melalui vector/raster paths, text, layers dan compositing.

## D25

[3D Graphics and Scene Rendering](../knowledge/domains/25-3d-graphics-and-scene-rendering.md) — E — Graphics and Output

Membentuk gambar dari scene spatial dengan cameras, visibility, materials, lights dan rendering algorithms.

## D26

[GPU Programming and Parallel Graphics Computation](../knowledge/domains/26-gpu-programming-and-parallel-graphics-computation.md) — E — Graphics and Output

Mengeksekusi rendering/simulation pada GPU dengan contracts untuk memory, pipelines, parallelism dan precision.

## D27

[Temporal Rendering and Image Formation](../knowledge/domains/27-temporal-rendering-and-image-formation.md) — E — Graphics and Output

Menyampling perubahan scene selama exposure dan antarframes untuk menghasilkan image sequence yang sesuai motion serta display target.

## D28

[Compositing Image Processing and Visual Effects](../knowledge/domains/28-compositing-image-processing-and-visual-effects.md) — E — Graphics and Output

Menggabungkan serta memproses image layers dengan contracts untuk color, alpha, coordinates dan temporal behavior.

## D29

[Audio Haptics and Multisensory Output](../knowledge/domains/29-audio-haptics-and-multisensory-output.md) — E — Graphics and Output

Menghubungkan sound, visual motion dan tactile output melalui measured signals, time contracts dan designed response.

## D30

[Spatial Computing and Immersive Motion](../knowledge/domains/30-spatial-computing-and-immersive-motion.md) — E — Graphics and Output

Menyatukan tracking, spatial anchors, rendering dan input dalam AR/VR/MR experiences dengan coordinate/time contracts yang konsisten.

## D31

[Robotics Mechatronics and Physical Actuation](../knowledge/domains/31-robotics-mechatronics-and-physical-actuation.md) — E — Graphics and Output

Menghubungkan motion models, planning dan control dengan actuators, sensors serta physical operating limits.

## D32

[Motion Perception and Human Factors](../knowledge/domains/32-motion-perception-and-human-factors.md) — F — Human Experience

Menjelaskan hubungan antara stimulus bergerak, perception, attention, task dan individual/context differences.

## D33

[Animation Principles Choreography and Narrative](../knowledge/domains/33-animation-principles-choreography-and-narrative.md) — F — Human Experience

Menyusun motion yang menyampaikan maksud, hierarchy, rhythm dan emotion melalui hubungan action, camera, typography dan editing.

## D34

[Accessibility Comfort and Adaptive Motion](../knowledge/domains/34-accessibility-comfort-and-adaptive-motion.md) — F — Human Experience

Menjaga informasi dan task tetap dapat digunakan ketika motion dikurangi, dihentikan atau diganti, serta ketika device/context berbeda.

## D35

[Runtime Scheduling and Performance Engineering](../knowledge/domains/35-runtime-scheduling-and-performance-engineering.md) — G — Engineering and Production

Menjalankan motion dengan response dan resource use sesuai target tanpa mengubah model atau task semantics diam-diam.

## D36

[Motion Software Architecture and Systems Engineering](../knowledge/domains/36-motion-software-architecture-and-systems-engineering.md) — G — Engineering and Production

Mengorganisasikan motion code dengan contracts, ownership, reproducibility dan integration boundaries yang dapat dipelihara.

## D37

[Assets Data Models and Interoperability](../knowledge/domains/37-assets-data-models-and-interoperability.md) — G — Engineering and Production

Membawa motion data antartools/platform tanpa kehilangan units, hierarchy, timing, interpretation atau provenance.

## D38

[Authoring Tools and Production Pipelines](../knowledge/domains/38-authoring-tools-and-production-pipelines.md) — G — Engineering and Production

Membuat proses authoring, preview, baking, simulation dan rendering dapat diulang serta ditinjau dengan cepat.

## D39

[Motion Testing Measurement and Quality Engineering](../knowledge/domains/39-motion-testing-measurement-and-quality-engineering.md) — H — Verification and Delivery

Menentukan apa yang benar-benar dibuktikan oleh numerical, structural, visual, temporal, performance dan human checks.

## D40

[Media Delivery Encoding and Deployment](../knowledge/domains/40-media-delivery-encoding-and-deployment.md) — H — Verification and Delivery

Menyampaikan motion sebagai media atau application yang benar cadence, format, metadata, behavior dan runtime target-nya.
