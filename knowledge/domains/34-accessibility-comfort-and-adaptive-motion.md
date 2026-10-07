# D34 — Accessibility Comfort and Adaptive Motion

Menjaga informasi dan task tetap dapat digunakan ketika motion dikurangi, dihentikan atau diganti, serta ketika device/context berbeda.

Rumpun: **F — Human Experience**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Accessibility bukan satu checkbox reduced motion. WCAG checks, user comfort, assistive technology dan contextual usability merupakan evidences berbeda.

Prasyarat: [D20](../../architecture/domain-map.md#d20), [D21](../../architecture/domain-map.md#d21), [D22](../../architecture/domain-map.md#d22), [D32](../../architecture/domain-map.md#d32).

## Subdomain dan pengetahuan inti

### D34.01 — Reduced-motion preferences

System preference provides user intent but no-preference tidak membuktikan comfort. Adapt specific motion functions rather than remove semantic information.

**Model / prosedur.** Detect preference when platform supports; provide user setting where useful; respond changes.

**Kegagalan.** CSS changed but JS still moves; essential info disappears.

**Verifikasi.** Initial preference, live changes, all implementation paths.

### D34.02 — Pause stop hide dan user control

Continuing movement can interfere reading/tasks. Applicable requirements depend content and trigger; user controls must work during animation.

**Model / prosedur.** Define controllable moving content, stop behavior, persistence and focus.

**Kegagalan.** Pause button itself animates inaccessible; restart overwrites preference.

**Verifikasi.** Keyboard operation and stop state across navigation/remount.

### D34.03 — Flashing flicker dan motion sensitivity

Flashing and large visual self-motion have different concerns. Pixel-level metrics do not fully predict individual comfort.

**Model / prosedur.** Evaluate actual sequence with appropriate standard criteria; avoid inferred medical guarantees.

**Kegagalan.** Reduced translation considered removes all flicker; still-frame audit.

**Verifikasi.** Full sequence checks and actual preference/comfort feedback.

### D34.04 — Keyboard focus dan assistive technology

Semantic visibility, focusability and announcement must match interaction state through motion. Visual offscreen isn't automatically inaccessible.

**Model / prosedur.** Manage focus, inert/hidden state as appropriate, avoid duplicates in transitions.

**Kegagalan.** Hidden exit element remains focusable; changing DOM loses focus.

**Verifikasi.** Keyboard traversal, screen-reader behavior and interrupted transitions.

### D34.05 — Information alternatives

Motion can encode direction/progress/state. Provide meaningful text/static cues when movement unavailable or imperceptible.

**Model / prosedur.** Map each communicated fact to accessible alternative; maintain task completion.

**Kegagalan.** Animation-only instructions or invisible status changes.

**Verifikasi.** No-animation/no-sound paths with task-level verification.

### D34.06 — Responsive capability adaptation

Viewport, input, performance and sensor support affect suitable motion. Adapt cost and layout while preserving user control.

**Model / prosedur.** Feature/capability detection, bounded quality tiers, baseline content.

**Kegagalan.** Lower-end device removes essential state; media query overgeneralized device identity.

**Verifikasi.** Small viewport, touch/no-hover, low capability and disconnect.

### D34.07 — Evaluation and evidence boundaries

Automated audit and synthetic fixtures can verify limited technical properties, not full accessibility or comfort for everyone.

**Model / prosedur.** Record criterion, test setup, outcome and open human review.

**Kegagalan.** Technical PASS promoted universal accessibility certification.

**Verifikasi.** Manual interaction plus automated checks and representative users.

## Contoh kerja dan alasan pemilihan

Contoh navigation shared-element move becomes short opacity change or immediate state update under reduced-motion preference. Focus still moves to appropriate heading; loading state remains textually available. Preference change mid-animation cancels/retargets cleanly. Verify CSS, JS, Canvas and shader paths separately, because one media query cannot control all renderers.

## Alur implementasi

Inventory motion functions/information; choose reduced alternatives; implement controls and semantic lifecycle; evaluate applicable criteria; test input/preferences; record human review limits.

## Kriteria penguasaan

Dapat membangun reduced-motion path tanpa kehilangan informasi dan menguji focus/controls selama interruptions.

## Cabang lanjut yang tetap termasuk cakupan

Assistive technology testing; inclusive interaction; motion sensitivity research; caption/sound alternatives; user personalization; adaptive rendering; accessibility standards interpretation.

## Rujukan dan batas bukti

- [S75](../../references/source-map.md#s75)
- [S76](../../references/source-map.md#s76)
- [S77](../../references/source-map.md#s77)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
