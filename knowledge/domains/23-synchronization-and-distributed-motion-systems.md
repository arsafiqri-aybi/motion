# D23 — Synchronization and Distributed Motion Systems

Menyelaraskan motion antarstream, perangkat atau users sambil menangani offset, drift, latency, missingness dan authority.

Rumpun: **D — Behavior and Interaction**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Synchronization tidak hanya start bersamaan. Clock mapping D03, networking semantics, and audio/media rates harus dibedakan dari perceived synchrony D32.

Prasyarat: [D03](../../architecture/domain-map.md#d03), [D04](../../architecture/domain-map.md#d04), [D20](../../architecture/domain-map.md#d20).

## Subdomain dan pengetahuan inti

### D23.01 — Clock offset dan drift

Shared timestamp units tidak menjamin shared origin/rate. Offset dan drift perlu estimator dan uncertainty.

**Model / prosedur.** t_remote≈a t_local+b; calibrate using timestamp exchanges with network-delay assumptions.

**Kegagalan.** RTT/2 claimed exact one-way delay; re-sync causes jump.

**Verifikasi.** Simulated asymmetric delay, drift and discontinuities.

### D23.02 — Buffers dan jitter management

Buffer trades latency for stable presentation. Policy for late/missing data decides behavior.

**Model / prosedur.** Timestamp-ordered queue with target presentation delay, interpolation window and bounded capacity.

**Kegagalan.** Queue grows forever; samples drawn by arrival order.

**Verifikasi.** Bursty arrivals, missing packets, out-of-order data and bounded memory.

### D23.03 — Prediction dan reconciliation

Client prediction reduces perceived input delay; authoritative correction may move state. Correction needs continuity and error bounds.

**Model / prosedur.** Replay pending inputs from authoritative snapshot; smooth presentation separately if appropriate.

**Kegagalan.** Physics state smoothed inconsistent with server; double input application.

**Verifikasi.** Delay/loss fixture, correction residual and replay determinism.

### D23.04 — Deterministic lockstep dan rollback

Lockstep relies consistent simulation/input order. Rollback stores states and replays late inputs. Float and platform differences can break exact sync.

**Model / prosedur.** Hash snapshots; fixed seeds; deterministic event order; checkpoint ring buffer.

**Kegagalan.** Seed shared but RNG call order differs; incompatible engine versions.

**Verifikasi.** Cross-run state hashes, late-input replay and platform comparison.

### D23.05 — Audio visual haptic synchronization

Different streams use own clocks and output latencies. Master clock and correction policy need explicit choice.

**Model / prosedur.** Schedule against chosen master; estimate drift; adjust rate/buffer where supported.

**Kegagalan.** Render timestamp treated actual presentation time.

**Verifikasi.** Known markers, instrumented timestamps and device-level observations.

### D23.06 — Authority consistency dan conflicts

Multiple users editing parameters need ownership/version semantics. Last arrival is not necessarily latest intent.

**Model / prosedur.** Sequence numbers, versioned commands, explicit arbitration, snapshot plus deltas.

**Kegagalan.** Stale packet overrides new goal; feedback loop among peers.

**Verifikasi.** Reordering, reconnect, duplicate command and authority handoff.

### D23.07 — Fault handling dan observability

Disconnect/reconnect and degraded clocks affect continuity. Log time mappings and state age without overclaiming measurement accuracy.

**Model / prosedur.** Bound extrapolation duration; fallback freeze/degrade; rebuild snapshots on reconnect.

**Kegagalan.** Infinite extrapolation, teleport on recovered state.

**Verifikasi.** Long disconnect, stale snapshot, clock reset and measurable recovery.

## Contoh kerja dan alasan pemilihan

Contoh remote object sends 20Hz snapshots while display runs 60Hz. Maintain timestamp buffer and render slightly behind remote latest time to interpolate two states. When future sample absent, bounded extrapolation may be allowed, then freeze/degrade. Choosing 100ms buffer improves availability at expense latency; value is a design example, not universal optimal threshold. Plot state age and correction magnitude during network impairment.

## Alur implementasi

Choose authority/master clock; define timestamp contract; estimate mapping; design buffer/prediction; bound stale behavior; instrument age/drift; test impairment and reconnect.

## Kriteria penguasaan

Dapat membedakan transport latency, clock error, render delay dan perceptual synchrony; reproduce network fixtures.

## Cabang lanjut yang tetap termasuk cakupan

PTP/NTP clock discipline; distributed simulation; collaborative XR; networked physics; media synchronization; rollback netcode; causal consistency; consensus boundaries.

## Rujukan dan batas bukti

- [S46](../../references/source-map.md#s46)
- [S47](../../references/source-map.md#s47)
- [S48](../../references/source-map.md#s48)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
