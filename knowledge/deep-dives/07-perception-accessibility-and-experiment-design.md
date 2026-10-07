# Perception, accessibility, dan experiment design

Menghubungkan D22, D32, D33, D34 dan D39. Bedakan human experience dengan numeric/render properties sepanjang development.

## Tiga jenis pertanyaan

Apakah trajectory continuous? Itu dapat diuji melalui evaluated positions/derivatives. Apakah visual ditampilkan tanpa missed frames? Itu memerlukan actual runtime/presentation evidence. Apakah pengguna merasa nyaman dan memahami perubahan? Itu membutuhkan users, task, context dan metode evaluation. Satu PASS tidak pindah otomatis ke pertanyaan lain.

## Hypothesis yang bisa diuji

Contoh hypothesis: shared-element transition membantu pengguna melacak object dari list ke detail dalam task tertentu. Define population, device, input, task, alternative, learning effects dan outcomes seperti correct recognition/errors/time. "Motion premium lebih baik" bukan hypothesis operational. Adjectives perlu diterjemahkan menjadi timing/path/visual properties serta task consequences.

Keep preference separate from performance. Users may prefer an animation yet finish task slower; both observations can be true. Confidence dan sample limits harus dilaporkan, tidak diganti score certainty buatan. AI editorial review dapat membantu menemukan crop/distraction but is not user study.

## Controlled comparisons

Ubah satu factor bila ingin infer effect khusus, atau gunakan factorial design ketika interactions perlu diteliti. Randomize/counterbalance order untuk mengurangi order/learning bias. Ensure alternatives carry same content; otherwise result confounds wording/layout with motion. Recorded fps/settings should reflect actual delivered stimulus.

If participants sensitive to motion, provide control and termination aligned study protocol. Repo does not conduct medical assessment or declare clinical thresholds. Human findings must retain tested population/system limitations.

## Accessible information mapping

Inventory every fact communicated through motion: progress, direction, selection, causality, loading, error. Assign equivalent text/static state wherever needed. Reduced-motion mode should preserve task completion and meaningful feedback, not blank out diagram/state. If essential interaction uses motion, evaluate definition/context rather than assume every flourish essential.

WCAG 2.2 SC 2.3.3 is AAA and addresses disabling interaction-triggered motion unless essential. This specific criterion does not mean a site is fully conformant. Pause/stop/hide, flashing, keyboard/focus and other applicable criteria require separate evaluation. The exact scoped standard claim is in [claim ledger](../../references/claims.csv).

## Implementation paths

CSS preference handling does not automatically stop JS timelines, Canvas loops or shader movement. Runtime must observe preference changes and switch/cancel safely. Provide stable final state on cancellation; prevent duplicate DOM representation and focusable exit content. Keyboard commands should reach same semantic state without depending on gesture velocity.

## Report categories

Technical: property, environment, method, expected, measured, PASS/FAIL. Editorial: reviewer/context and observed issues. Human study: participants/task/method/results/limitations. Unknown: not measured or not enough evidence. Do not merge them into one "quality 100/100" score.

For a portfolio hero, technical tests can check offscreen pause, reduced motion, text readability/crop and frame traces; editorial review assesses message/identity; actual user tasks assess understanding. Background motion should not compete with portfolio content merely to demonstrate effects. These are authored design recommendations pending context review, not universal scientific law.
