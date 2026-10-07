# D20 — State Event and Reactive Motion Architecture

Membuat motion menjadi respons sistem yang predictable terhadap state, events, asynchronous work, dan interruptions.

Rumpun: **D — Behavior and Interaction**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

State architecture bukan motion model. Ia memilih goals dan lifecycle; evaluator D19 dan solver D10 menjalankan perubahan.

Prasyarat: [D05](../../architecture/domain-map.md#d05), [D19](../../architecture/domain-map.md#d19).

## Subdomain dan pengetahuan inti

### D20.01 — Finite-state machines

Explicit states membatasi valid transitions. Animation phase dan business state dapat berbeda; completed animation tidak selalu berarti task success.

**Model / prosedur.** Transition table state×event→next state plus side effects; reject invalid events.

**Kegagalan.** Implicit booleans allow impossible combinations.

**Verifikasi.** Enumerate transitions, invalid events, terminal states and invariants.

### D20.02 — Statecharts dan hierarchy

Hierarchy mengurangi duplicate transitions; parallel regions represent concurrent behavior. Entry/exit actions need deterministic semantics.

**Model / prosedur.** Parent/child active states with event priority and history policy.

**Kegagalan.** Parent exit forgets child animation cleanup.

**Verifikasi.** Nested transitions, simultaneous events and exit cleanup.

### D20.03 — Signals dan reactive graphs

Derived motion values depend on sources; batching prevents intermediate inconsistent outputs. Cycles need rejection or explicit iterative semantics.

**Model / prosedur.** Dirty propagation, topological evaluation, one commit after transaction.

**Kegagalan.** Glitches, repeated work, hidden cycle.

**Verifikasi.** Diamond graph, batched changes, cycle fixture and consistent snapshots.

### D20.04 — Interruption cancellation dan stale work

Cancel is lifecycle operation, not merely hide output. Pending async completions must not overwrite newer state.

**Model / prosedur.** Generation/version token; completion accepted only when owner/token current.

**Kegagalan.** Old transition callback restores wrong visibility.

**Verifikasi.** Rapid toggle, delayed completion and target removal tests.

### D20.05 — Concurrency dan event ordering

Multiple input/network/animation events require priority and ordering policy. Wall-clock arrival order may differ logical sequence.

**Model / prosedur.** Queue events with source sequence/time; arbitrate ownership before output mutation.

**Kegagalan.** Two loops update same transform; nondeterministic event race.

**Verifikasi.** Permute independent events, reproduce conflict histories.

### D20.06 — Observers dan resource lifecycle

Listeners, timers, observers and animation instances retain resources. Unmount/dispose must end ownership and subscriptions.

**Model / prosedur.** Create/dispose symmetry, cancellation on teardown, weak ownership where useful.

**Kegagalan.** Memory leaks and duplicate handlers after remount.

**Verifikasi.** Mount/unmount repeated, count resources, trigger events post-disposal.

### D20.07 — Reactive goals versus presentation

Desired state differs from intermediate visual state. Store goals separately, derive motion, report interaction affordance promptly.

**Model / prosedur.** goal state→motion controller→presented state; preserve semantic accessibility while animating.

**Kegagalan.** Slow visual exit delays actual disabled state; hidden target stays focusable.

**Verifikasi.** Keyboard/focus tests and state checks during intermediate motion.

## Contoh kerja dan alasan pemilihan

Contoh drawer states closed/opening/open/closing. OPEN during closing retargets from current pose; a previous close-completion token must be ignored. Escape updates desired closed state immediately, and focus policy follows semantic state. Visual spring can continue while pointer interaction is disabled. Test event sequences such as OPEN,CLOSE,OPEN before any animation finishes.

## Alur implementasi

Define semantic states; map valid events; separate desired/presented state; define ownership; add cancellation tokens; instrument transitions; replay adversarial histories.

## Kriteria penguasaan

Dapat merancang event histories tanpa impossible states dan membuktikan cleanup serta stale-callback rejection.

## Cabang lanjut yang tetap termasuk cakupan

Actor models; event sourcing; distributed statecharts; functional reactive programming; hybrid systems; transactional reactive evaluation.

## Rujukan dan batas bukti

- [S39](../../references/source-map.md#s39)
- [S40](../../references/source-map.md#s40)
- [S05](../../references/source-map.md#s05)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
