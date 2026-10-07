# D18 — Character Motion Biomechanics and Performance

Mengorganisasikan gerak articulated agar contact, balance, expression dan performance sesuai tujuan visual atau fisik.

Rumpun: **C — Representation and Animation**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Plausibility visual, anatomical constraints dan validated biomechanics adalah target berbeda. Pengetahuan ini tidak menggantikan diagnosis atau panduan latihan manusia.

Prasyarat: [D07](../../architecture/domain-map.md#d07), [D08](../../architecture/domain-map.md#d08), [D17](../../architecture/domain-map.md#d17), [D19](../../architecture/domain-map.md#d19).

## Subdomain dan pengetahuan inti

### D18.01 — Locomotion dan gait

Walk/run melibatkan phases, support, root progression dan limb coordination. Speed change tidak cukup hanya mempercepat clip jika stride/contact tidak cocok.

**Model / prosedur.** Represent gait phase, stance/swing and root velocity; adapt stride or matching clips.

**Kegagalan.** Foot skating, incorrect phase transitions.

**Verifikasi.** Foot world velocity during stance and traveled distance per cycle.

### D18.02 — Balance dan support

Support region dan center of mass membantu reasoning, tetapi dynamic balance memerlukan momentum/dynamics. Static support condition tidak cukup untuk running.

**Model / prosedur.** For simple quasistatic cases project COM relative support; use dynamics for moving cases.

**Kegagalan.** Static metric claimed universal balance proof.

**Verifikasi.** Static cases, disturbance recovery, dynamic cases evaluated separately.

### D18.03 — Contacts dan environment

Hands/feet berinteraksi surfaces with time-dependent constraints. Contact switching affects continuity and forces.

**Model / prosedur.** Maintain contact metadata; solve limb/root adjustments with feasible constraints.

**Kegagalan.** Limb stretch, feet penetrating slopes, support switches pop.

**Verifikasi.** Contact residual, joint limits, collision and transition continuity.

### D18.04 — Reaching manipulation dan gaze

Task-space goals must coexist with body limits and expressive intent. Gaze involves eyes, head and torso coordination.

**Model / prosedur.** Allocate task priorities; solve IK with joint limits and optional secondary objectives.

**Kegagalan.** All motion concentrated neck; hand target unreachable.

**Verifikasi.** Reachability, eye/head bounds, smooth target changes.

### D18.05 — Facial expression dan lip sync

Speech visemes, facial actions dan emotion controls operate on overlapping channels. Timing/anticipation and coarticulation matter.

**Model / prosedur.** Map phoneme/time cues to blend shape envelopes, preserve explicit uncertainty in alignment.

**Kegagalan.** One phoneme one instant pose; duplicate mouth controllers.

**Verifikasi.** Alignment checks, intelligibility/human review, weight conflicts.

### D18.06 — Secondary motion dan style

Follow-through, accessories dan soft tissue can come from procedural or physics layers. Style intentionally deviates physical model.

**Model / prosedur.** Separate primary action from delayed/overlapping secondary response; clamp only by stated bounds.

**Kegagalan.** Secondary motion distracts message or clips body.

**Verifikasi.** Parameter extremes, silhouettes, contact constraints and editorial review.

### D18.07 — Performance dan evaluation

Expressiveness depends context, rhythm, pose clarity and audience. Numerical metric alone cannot measure convincing acting.

**Model / prosedur.** Define intended action/emotion and review representative sequences plus transitions.

**Kegagalan.** Frame-only judgment; plausible motion claimed universal preference.

**Verifikasi.** Human/context evaluation separate from joint/trajectory metrics.

## Contoh kerja dan alasan pemilihan

Contoh walk clip moves root 1.2m per cycle. Jika runtime menggeser character 2m sambil mempertahankan foot motion clip, foot skating muncul. Root-motion extraction, stride adaptation atau motion matching dapat dipilih. Hitung foot velocity saat stance pada world frame, lalu periksa slopes dan turning. Visual stylization boleh mengubah gait, tetapi deviation harus sengaja.

## Alur implementasi

Tentukan style/task; prepare rig/contact metadata; build primary action; add IK/environment adaptation; add secondary motion; measure contacts/limits; review timing/performance.

## Kriteria penguasaan

Dapat memperbaiki root/stride mismatch, menguji contacts dan memisahkan physical metrics dari expressive judgment.

## Cabang lanjut yang tetap termasuk cakupan

Human motor control; musculoskeletal simulation; physically based characters; crowd animation; animal locomotion; expressive gestures; embodied agents; interaction synthesis.

## Rujukan dan batas bukti

- [S37](../../references/source-map.md#s37)
- [S38](../../references/source-map.md#s38)
- [S31](../../references/source-map.md#s31)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
