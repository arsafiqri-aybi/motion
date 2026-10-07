# Glossary

Definisi ringkas; baca linked domain untuk assumptions, equations dan limits.

| Term | Meaning | Domain |
|---|---|---|
| Clock domain | Origin/rate/unit yang memberi meaning timestamp. | [D03](domains/03-time-timing-sampling-and-temporal-systems.md) |
| Delta-time | Elapsed interval pada clock yang ditentukan. | [D03](domains/03-time-timing-sampling-and-temporal-systems.md) |
| Cadence | Jadwal sampling/presentation; tidak otomatis constant. | [D03](domains/03-time-timing-sampling-and-temporal-systems.md) |
| Arc length | Panjang lintasan geometric sampai curve parameter tertentu. | [D02](domains/02-geometry-spatial-representation-and-computational-geometry.md) |
| Local/world frame | Basis ruang relatif objek versus scene. | [D02](domains/02-geometry-spatial-representation-and-computational-geometry.md) |
| Homogeneous coordinate | Representasi untuk affine/projective transforms. | [D02](domains/02-geometry-spatial-representation-and-computational-geometry.md) |
| Quaternion | Representasi rotation empat komponen dengan unit norm. | [D02](domains/02-geometry-spatial-representation-and-computational-geometry.md) |
| C0/C1/C2 | Continuity nilai/first derivative/second derivative pada parameter tertentu. | [D06](domains/06-interpolation-easing-and-transition-models.md) |
| Easing | Mapping progress input ke progress output. | [D06](domains/06-interpolation-easing-and-transition-models.md) |
| Interpolation | Perkiraan values antara data/endpoints dalam ruang tertentu. | [D06](domains/06-interpolation-easing-and-transition-models.md) |
| Kinematics | Deskripsi posisi/velocity tanpa forces penyebab. | [D07](domains/07-kinematics.md) |
| Dynamics | Hubungan forces/torques dengan motion. | [D08](domains/08-dynamics-and-physical-modeling.md) |
| Jacobian | Derivative matrix dari mapping state/task. | [D07](domains/07-kinematics.md) |
| Inverse kinematics | Mencari joint state untuk target task pose. | [D07](domains/07-kinematics.md) |
| Natural frequency | Frequency karakteristik model oscillator linear. | [D08](domains/08-dynamics-and-physical-modeling.md) |
| Damping ratio | Damping relatif critical damping model linear. | [D08](domains/08-dynamics-and-physical-modeling.md) |
| Stiff system | ODE dengan scales yang membatasi explicit timestep. | [D10](domains/10-numerical-methods-and-solvers.md) |
| Residual | Ketidakterpenuhan equations/constraints yang diukur. | [D10](domains/10-numerical-methods-and-solvers.md) |
| Conditioning | Sensitivity solution terhadap perturbations input. | [D10](domains/10-numerical-methods-and-solvers.md) |
| Convergence | Trend approximation menuju solution saat refinement/iterations. | [D10](domains/10-numerical-methods-and-solvers.md) |
| Observability | Kemampuan menentukan state dari outputs di model tertentu. | [D12](domains/12-control-theory-and-feedback-systems.md) |
| Controllability | Kemampuan menggerakkan state melalui allowed inputs pada model tertentu. | [D12](domains/12-control-theory-and-feedback-systems.md) |
| Path/trajectory | Geometric route versus route dengan timing. | [D13](domains/13-motion-planning-and-navigation.md) |
| Configuration space | Ruang kemungkinan state geometric/joint configurations. | [D13](domains/13-motion-planning-and-navigation.md) |
| Motion matching | Pemilihan motion samples menurut feature query. | [D15](domains/15-data-driven-and-learned-motion-synthesis.md) |
| Retargeting | Adaptasi motion pada skeleton/rig/proportions lain. | [D17](domains/17-rigging-articulation-and-deformation-systems.md) |
| Bind pose | Reference configuration untuk deformation mapping. | [D17](domains/17-rigging-articulation-and-deformation-systems.md) |
| Skinning | Mapping joint transforms ke mesh deformation. | [D17](domains/17-rigging-articulation-and-deformation-systems.md) |
| Root motion | Gerak transform root dari animation data. | [D18](domains/18-character-motion-biomechanics-and-performance.md) |
| Additive animation | Layer perubahan relatif reference pose/space. | [D19](domains/19-animation-representation-composition-and-evaluation.md) |
| Statechart | State system dengan hierarchical/parallel semantics. | [D20](domains/20-state-event-and-reactive-motion-architecture.md) |
| Interruption | Perubahan/cancellation ketika motion belum selesai. | [D20](domains/20-state-event-and-reactive-motion-architecture.md) |
| Pointer capture | Routing pointer stream ke target selama lifecycle yang sah. | [D21](domains/21-input-gesture-and-sensor-systems.md) |
| Latency/jitter | Delay versus variation delay. | [D23](domains/23-synchronization-and-distributed-motion-systems.md) |
| Reconciliation | Koreksi predicted state dengan authority. | [D23](domains/23-synchronization-and-distributed-motion-systems.md) |
| Raster/vector | Sampled pixel representation versus geometric description. | [D24](domains/24-2d-graphics-and-rendering.md) |
| Exposure | Interval image integration, berbeda dari frame timestamp. | [D27](domains/27-temporal-rendering-and-image-formation.md) |
| Temporal aliasing | Ambiguity/distortion akibat sampling waktu yang tidak memadai. | [D27](domains/27-temporal-rendering-and-image-formation.md) |
| Premultiplied alpha | Stored RGB telah dikali coverage alpha. | [D28](domains/28-compositing-image-processing-and-visual-effects.md) |
| Working color space | Representation colors ketika operasi dilakukan. | [D28](domains/28-compositing-image-processing-and-visual-effects.md) |
| RMS | Root mean square; bukan otomatis LUFS atau true peak. | [D29](domains/29-audio-haptics-and-multisensory-output.md) |
| Reference space | Basis spatial tracking/render poses dalam XR. | [D30](domains/30-spatial-computing-and-immersive-motion.md) |
| Reduced motion | User preference/alternative presentation untuk mengurangi movement. | [D34](domains/34-accessibility-comfort-and-adaptive-motion.md) |
| Frame budget | Available scheduling interval menurut target, dengan overhead. | [D35](domains/35-runtime-scheduling-and-performance-engineering.md) |
| Determinism | Same specified inputs/environment menghasilkan equivalence yang didefinisikan. | [D36](domains/36-motion-software-architecture-and-systems-engineering.md) |
| Provenance | Catatan asal/version/transformations suatu asset atau claim. | [D37](domains/37-assets-data-models-and-interoperability.md) |
| Baking | Mengubah evaluation menjadi samples/caches yang recorded. | [D38](domains/38-authoring-tools-and-production-pipelines.md) |
| PTS | Presentation timestamp stream sample. | [D40](domains/40-media-delivery-encoding-and-deployment.md) |
| Codec/container | Compression method versus packaging stream/media. | [D40](domains/40-media-delivery-encoding-and-deployment.md) |
