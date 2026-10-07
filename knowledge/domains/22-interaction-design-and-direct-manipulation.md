# D22 — Interaction Design and Direct Manipulation

Menentukan mapping yang terasa jelas dan konsisten antara tindakan pengguna, state, dan visual motion.

Rumpun: **D — Behavior and Interaction**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Input engineering D21 menyediakan events; D22 menetapkan feedback, mapping, affordances dan task behavior. Kenyamanan/perception membutuhkan D32/D34.

Prasyarat: [D06](../../architecture/domain-map.md#d06), [D20](../../architecture/domain-map.md#d20), [D21](../../architecture/domain-map.md#d21).

## Subdomain dan pengetahuan inti

### D22.01 — Feedback dan affordances

Press/focus/selection motion menyampaikan status tindakan. Feedback harus cukup cepat dan distinguishable tanpa menghambat task.

**Model / prosedur.** Map idle/hover/pressed/focused/disabled states with semantic equivalents.

**Kegagalan.** Click acknowledgement hanya lewat subtle motion; keyboard focus missing.

**Verifikasi.** Task success, latency observations, keyboard and reduced-motion review.

### D22.02 — Direct manipulation

Object follows intent with predictable coordinate mapping. Visual compliance, constraints dan ownership membuat drag feel berbeda.

**Model / prosedur.** target=initialPose+mappedDisplacement; constrain before/after spring according to desired semantics.

**Kegagalan.** Lag feels disconnected; spring crosses hard boundary.

**Verifikasi.** Input/output trajectory, constraint adherence and release transitions.

### D22.03 — Inertia snapping dan settling

Release motion dapat mengikuti physical or authored model. Snap target selection is interaction policy, not merely damping.

**Model / prosedur.** Choose target based position/velocity/context; settle from current x,v.

**Kegagalan.** High-velocity release snaps opposite intent; repeated snapping oscillates.

**Verifikasi.** Boundary velocities, nearest target ties and interruption.

### D22.04 — Scroll-driven dan view-driven behavior

Scroll progress can drive presentation continuously; trigger events drive timed animations. These are different semantics.

**Model / prosedur.** Compute progress from defined scroll range or use supported timeline; fallback retains content.

**Kegagalan.** Triggered animation lags scroll expectation; division by zero short page.

**Verifikasi.** Forward/back scroll, resize, inactive range and capability fallback.

### D22.05 — Navigation dan shared elements

Motion links before/after views while semantic navigation occurs. Layout measurements, image loading and focus changes affect mapping.

**Model / prosedur.** Capture before/after bounds; transition ownership; complete state/focus regardless animation.

**Kegagalan.** Duplicate element, stale geometry, navigation blocked on failed animation.

**Verifikasi.** Back/forward, rapid navigation, dynamic content and reduced-motion.

### D22.06 — Cursor following dan magnetic mapping

Cursor-following is spatial response; magnetic targets alter perceived mapping. Strength, bounds and input capability determine usability.

**Model / prosedur.** Displacement function with bounded influence radius, decay and keyboard-independent action.

**Kegagalan.** Essential target evades pointer; touch device stuck in hover.

**Verifikasi.** Boundary positions, precision tasks, touch/no-hover and focus.

### D22.07 — UX measurement dan adaptation

Motion quality depends task/audience. Preferences and context may require different trajectories or no spatial animation.

**Model / prosedur.** Define hypothesis and success metrics; compare observed task outcomes.

**Kegagalan.** Generic premium style claimed universally better.

**Verifikasi.** Usability sessions, task errors/time, qualitative review and accessibility.

## Contoh kerja dan alasan pemilihan

Contoh carousel: dragging follows finger directly; release chooses nearest reachable card using position and velocity; settling uses continuous x,v. Arrow key sets same target without needing drag velocity. Reduced-motion switches to immediate/short nonspatial update while keeping selection and focus clear. Test resize mid-drag and interrupt while settling.

## Alur implementasi

Define task/intent; choose feedback mapping; establish constraints; implement direct/control paths; define release/navigation behavior; test full input set; observe users before claiming preference.

## Kriteria penguasaan

Dapat menerangkan motion function per interaction dan menjaga usability di bawah interruption, resize dan reduced motion.

## Cabang lanjut yang tetap termasuk cakupan

FLIP layout transitions; transition choreography; input-to-photon latency; spatial navigation; touch mechanics; interaction accessibility; adaptive feedback.

## Rujukan dan batas bukti

- [S06](../../references/source-map.md#s06)
- [S44](../../references/source-map.md#s44)
- [S45](../../references/source-map.md#s45)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
