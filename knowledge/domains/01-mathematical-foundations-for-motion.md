# D01 — Mathematical Foundations for Motion

Bahasa kuantitatif untuk merepresentasikan perubahan. Gerak yang dapat diprogram membutuhkan besaran, hubungan antarbesaran, dan asumsi yang memungkinkan perhitungan serta pembuktian.

Rumpun: **A — Foundations**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Fokus pada fondasi matematika yang dipakai motion. Algoritma integrasi komputer dibahas D10; struktur geometri D02; keputusan statistik perlu menyatakan model observasi dan ketidakpastian.

Prasyarat: [D05](../../architecture/domain-map.md#d05).

## Subdomain dan pengetahuan inti

### D01.01 — Besaran, satuan, dan dimensional analysis

Posisi, kecepatan, dan percepatan mempunyai dimensi berbeda. Nilai piksel, meter, detik, dan milidetik tidak dapat dipertukarkan hanya karena semuanya angka. Konversi satuan diletakkan pada batas sistem.

**Model / prosedur.** [x]=L, [v]=L/T, [a]=L/T². Untuk x=x0+v0 t+½at², setiap suku harus berdimensi L.

**Kegagalan.** Delta-time dalam ms dikalikan kecepatan per detik menghasilkan gerak 1000 kali terlalu besar.

**Verifikasi.** Ubah seluruh input detik menjadi milidetik melalui konversi resmi; trajectory fisik harus tetap sama.

### D01.02 — Vector dan linear algebra

Vector menyatakan arah dan besar relatif pada basis. Dot product mengukur proyeksi; cross product 3D memberi vector tegak lurus sesuai orientasi. Matriks menyatakan transformasi linear dan sistem persamaan.

**Model / prosedur.** dot(a,b)=Σaᵢbᵢ; norm(a)=√dot(a,a). Normalisasi hanya dilakukan jika norm cukup jauh dari nol.

**Kegagalan.** NaN dari vector nol; menganggap transformasi dengan skala selalu mempertahankan panjang.

**Verifikasi.** Uji dot(a,a)≥0 dan norm(unit)=1; tetapkan tolerance sesuai magnitude dan precision.

### D01.03 — Functions dan trigonometry

Motion sering berupa fungsi posisi terhadap waktu. Periodic motion memerlukan pemisahan amplitude, frequency, phase, dan offset. Sudut radian adalah kontrak umum persamaan trigonometri.

**Model / prosedur.** x(t)=b+A sin(2πft+φ); period=1/f untuk f>0. Dua sinyal beda fase dapat membentuk lintasan elips.

**Kegagalan.** Derajat masuk fungsi radian; frequency dihitung per frame sehingga berubah mengikuti refresh rate.

**Verifikasi.** Evaluasi pada t dan t+1/f menghasilkan nilai sama dalam tolerance.

### D01.04 — Calculus dan differential equations

Derivative menghubungkan posisi dengan kecepatan dan percepatan. Integral mengakumulasi perubahan. ODE menentukan laju perubahan state; PDE juga melibatkan turunan ruang.

**Model / prosedur.** v=dx/dt, a=dv/dt; x(t)=x0+∫v dt. Model spring adalah m x″+c x′+k(x−target)=0.

**Kegagalan.** Derivative dari data berisik dianggap sebagai kecepatan akurat; ODE dipakai tanpa initial conditions.

**Verifikasi.** Bandingkan derivative analitik dengan central difference pada beberapa h; periksa error dan roundoff.

### D01.05 — Probability dan stochastic processes

Variasi acak perlu model distribusi dan korelasi. Independent samples berbeda dari random walk maupun noise yang halus. Seed menjamin reproduksi dalam generator yang sama, bukan kesamaan semua platform.

**Model / prosedur.** Random walk x[n+1]=x[n]+ε[n]. Untuk ε independen zero-mean dengan variance σ², variance displacement setelah n langkah adalah nσ².

**Kegagalan.** Random per frame membuat sifat statistik bergantung fps; seed direset setiap frame.

**Verifikasi.** Uji ensemble mean/variance dan autocorrelation, selain satu trajectory yang kebetulan terlihat bagus.

### D01.06 — Discrete mathematics dan graphs

Animation graph, dependency graph, dan planning graph memodelkan hubungan yang berbeda. Directed edge mempunyai makna, sehingga urutan evaluasi tidak boleh ditentukan dari posisi visual node.

**Model / prosedur.** Topological sorting berlaku pada DAG; strongly connected components mengenali kelompok siklus. FSM menyatakan state dan transition relation.

**Kegagalan.** Dependency cycle menyebabkan evaluasi tak berhingga; semua graph diasumsikan DAG.

**Verifikasi.** Buat fixture diamond dependency dan cyclic dependency; sistem harus mengevaluasi yang pertama dan mendeteksi yang kedua.

### D01.07 — Approximation dan uncertainty

Model ideal, hasil numerik, dan observasi empiris mempunyai batas berbeda. Tolerance diturunkan dari magnitude, noise, dan kebutuhan penggunaan, bukan satu epsilon universal.

**Model / prosedur.** Gunakan error absolute |a−b| dan relative |a−b|/max(|a|,|b|,scale). Catat propagation uncertainty pada fungsi input.

**Kegagalan.** Hasil banyak digit dianggap lebih akurat; pembagian relative error dekat nol menjadi tidak informatif.

**Verifikasi.** Lakukan perturbation test input dan lihat apakah output sensitif sesuai estimasi conditioning.

## Contoh kerja dan alasan pemilihan

Contoh: objek bergerak dari x0=2 m dengan v0=3 m/s dan a=−1 m/s². Pada t=2 s, x=2+6−2=6 m dan v=1 m/s. Pada t=3 s, kecepatannya nol. Setelah itu persamaan tetap sah, tetapi objek mulai bergerak berlawanan arah. Jika brief mensyaratkan berhenti permanen, diperlukan perubahan state/model setelah t=3; clamp posisi diam-diam akan mengubah physical model. Contoh ini membedakan persamaan, satuan, kondisi awal, serta kebijakan perilaku.

## Alur implementasi

Tulis state dan unit; definisikan fungsi/ODE; nyatakan domain input; tentukan representasi numerik; turunkan invariants; implementasikan; bandingkan terhadap solusi analitik; dokumentasikan approximation dan singular cases.

## Kriteria penguasaan

Dapat menurunkan v dan a dari trajectory, mengaudit satuan persamaan, mengenali singularity, serta membedakan stochastic variation dari numerical error. Latihan: bentuk gerak elips dengan dua sinus dan hitung velocity vector-nya.

## Cabang lanjut yang tetap termasuk cakupan

Complex analysis untuk oscillation; Lie groups/algebras; differential geometry; stochastic differential equations; Bayesian inference; information theory; tensor calculus; interval arithmetic dan formal error bounds.

## Rujukan dan batas bukti

- [S01](../../references/source-map.md#s01)
- [S02](../../references/source-map.md#s02)
- [S03](../../references/source-map.md#s03)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
