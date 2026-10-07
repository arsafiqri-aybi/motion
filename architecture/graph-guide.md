# Graph pengetahuan

`graph.json` adalah directed graph many-to-many. Edge `uses` berarti suatu domain memakai pengetahuan domain lain, bukan seluruh handbook harus selesai dibaca sebelumnya. Karena pengetahuan saling bergantung, cycles diperbolehkan. Untuk learning order gunakan tracks yang bertahap.

Relations: `uses`, `provides_representation`, `provides_timeline`, `provides_equations`, `implements`, `provides_data`, `provides_controls`, `orchestrates`, `provides_input`, `provides_state`, `aligns_time`, `informs`, `constrains`, `profiles`, `supplies_assets`, `validates`. Semua edge adalah keputusan pengorganisasian yang dapat ditinjau, bukan hasil trained neural network.

Query lokal: `python3 scripts/search.py "spring"`. Gunakan hasil untuk memilih file, lalu baca bagian lengkap termasuk assumptions/failures. Node existence bukan proof knowledge depth.
