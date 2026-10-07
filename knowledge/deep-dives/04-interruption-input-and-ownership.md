# Interruption, input, dan single ownership

Menghubungkan D06, D19, D20, D21, D22 dan D34. Tujuan: interaction remains coherent meskipun commands datang lebih cepat daripada animation selesai.

## Semantic state versus presented state

Desired drawer state `closed` berbeda dari progress visual menuju closed. Interaction/focus semantics tidak selalu harus menunggu settle. Jika close diminta, tentukan kapan background dan drawer menerima input; visual transparency alone does not set accessibility tree. Simpan desired state sebagai source of truth, presented pose sebagai evaluator output.

## Stale completion

History OPEN→CLOSE→OPEN menghasilkan tiga transitions overlapping secara temporal. First open completion dan close completion bisa tiba setelah final open. Generation tokens membuat completion berlaku hanya untuk transition current. Token bukan source clock; ia logical version.

`TransitionOwner` menunjukkan request increments generation, complete checks equality. Test stale callback rejects old token. Full system juga harus cancel resources, remove listeners dan decide event delivery. Logical guard tidak membuktikan browser event implementation sudah benar.

## Continuous handoff

Ketika ownership berubah dari drag ke settling, current x dan estimated v adalah initial conditions. Position target alone can preserve x continuity but drop derivative. Gunakan model yang menerima velocity bila purpose membutuhkannya. Jika direct drag sudah constrained, releasing spring outside bounds memerlukan consistent constraint policy.

Velocity estimate harus memakai timestamp asli dan cukup window, dengan zero-dt/stale-sample handling. Average dari samples irregular tanpa timestamps bias. Aggressive smoothing dapat feel delayed; tuning harus tied input-to-output trajectory and task.

## Pointer lifecycle

Track one pointerId or explicit multi-pointer ownership. Pointer capture keeps routing but pointercancel/lost capture tetap harus ditangani. Browser gesture arbitration dan touch-action memengaruhi native scroll. Mematikan scrolling seluruh page bukan solusi universal untuk drag.

Pointerup computes release once; pointercancel uses separate cancellation policy. Component teardown harus clean capture/listeners/animation loop dan mark owner disposed. Returning async result later tidak boleh revive removed element.

## Multiple writers

Hover motion, drag, scroll, layout transition dan physics dapat menulis transform yang sama. Pilih one composition owner: independent components menghasilkan separate channels atau transform layers lalu owner combines. CSS transition plus JS assignment pada property sama bisa menghasilkan trajectories sulit direproduksi.

Author explicit priority: drag supersedes autonomous motion, navigation may cancel local interaction, reduced-motion preference may switch presentation model. Tidak semua aplikasi memakai priorities yang sama; contract harus mengatakan siapa menang dan apa state akhir.

## Test histories

Test click spam; Escape saat opening; pointer leaves target; OS cancel; window loses focus; resize mid-drag; content unmount; delayed fetch completion; preference changes mid-motion; navigation back/forward. Untuk tiap history nyatakan semantic state, pose continuity, active resource count dan focus expected.

The Python guard tests logical stale completion only. Browser input lifecycle, focus and actual frame continuity are NOT_RUN in this release. Saat menambah implementation browser, reuse histories rather than treating Python PASS as UI proof.

## Review output

Record commands with sequence/time, before/after state, owner token, target and completion acceptance. Trace position/velocity near interruption and count active loops. Jika pose snaps, inspect initial state. Jika final visibility salah, inspect stale callback/semantic state. Jika memory grows, inspect disposal symmetry. Diagnosis yang dipisahkan mempercepat perbaikan.
