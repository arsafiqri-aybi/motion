# Ruang, waktu, dan trajectory yang benar

Menghubungkan D01, D02, D03, D06, D07 dan D27. Mulai dari [master map](../../architecture/domain-map.md); contoh numerik ada di [motion_math.py](../../examples/motion_math.py).

## Tiga parameter yang berbeda

Curve parameter u, physical distance s, dan clock time t bukan besaran yang sama. Curve p(u) mendefinisikan geometry; time law u(t) menentukan cara curve dilalui. Menulis p(progress) sering menyembunyikan dua keputusan sekaligus. Perubahan easing dapat mengubah speed/acceleration meskipun curve geometry tetap.

Untuk x(t)=p(u(t)), chain rule memberi v=p′(u)u′ dan a=p″(u)(u′)²+p′(u)u″. Karena itu continuity C1 pada p(u) belum menjamin world velocity continuous jika u′ meloncat. Sebaliknya time law halus tidak menghilangkan tangent discontinuity pada path corner. Dokumentasikan parameter dan unit derivative setiap kali tangents disimpan.

## Constant-speed derivation

Arc length dari curve origin adalah s(u)=∫₀ᵘ norm(p′(ξ))dξ. Untuk desired speed V konstan, s(t)=Vt, lalu u(t)=s⁻¹(Vt). Local rate adalah u′=V/norm(p′(u)), selama norm derivative tidak nol. At cusp/singular region, inverse mapping dapat rapuh dan orientation tangent tidak tersedia. Lookup table mengaproksimasi integral/inverse; itu tidak menghasilkan exact constant speed secara otomatis.

Practical implementation: subdivide curve, accumulate segment lengths, binary-search desired distance, interpolate neighboring u. Refine lebih banyak pada high curvature. Compare distance/time antar samples dengan reference high-resolution table. Bila curve diedit, transform nonuniform berubah atau tolerance berubah, invalidasikan LUT. Uniform scale memungkinkan scaling lengths, tetapi general deformation membutuhkan rebuild.

## Orientation sepanjang curve

Camera/character orientation tidak ditentukan position curve saja. Look-at memakai tangent dan up, tetapi tangent parallel up membuat basis singular. Frenet frame dapat flip dekat curvature nol. Rotation-minimizing/parallel-transport frames dapat mengurangi twist; closed curve membutuhkan seam correction. Jika camera harus tetap melihat subject, look-at target curve merupakan input terpisah dan perlu diuji ketika target dekat camera.

## Continuity saat retarget

Ketika target berubah, pilih apakah mempertahankan position saja atau position dan velocity. Cubic Hermite dapat menggunakan x0,v0,x1,v1 setelah tangents dikalikan duration untuk normalized parameter. Bila endpoint velocity nol dan incoming speed tinggi, path dapat overshoot. Bounds atau planning constraints harus diperiksa sebelum memilih bridge. Spring retargeting mempertahankan state tetapi mengubah force jika target step berubah.

## Waktu evaluation dan exposure

Frame timestamp menentukan sample pose; exposure interval menentukan integration untuk image. A frame at t can integrate [t−exposure/2,t+exposure/2] under centered-shutter convention, tetapi renderer lain bisa memakai offsets berbeda. Velocity-based blur needs consistent units: pixels/second dikali exposure seconds, bukan display interval tanpa alasan. Camera motion, shape deformation dan disocclusion menambah requirements.

## Eksperimen

Gunakan cubic ((0,0),(0,1),(1,1),(1,0)). Its speed simplifies to 3(2u²−2u+1), sehingga exact length pada u∈[0,1] adalah 2. Lab 03 memeriksa polyline approximation terhadap integral ini. Sampling equal u menghasilkan speed variation; sampling equal s dari LUT menguranginya. Catat maximum relative spacing variation serta error LUT, bukan hanya smooth-looking plot.

Jalankan `python3 examples/run_labs.py --output .local-output/labs`. Lab tidak merender camera atau mengukur perception. Orientation frame, collision constraints dan rendered motion blur memerlukan fixtures tambahan jika digunakan.

## Latihan lanjut

Buat piecewise curves C0/C1/C2, lalu ukur derivative boundary dari time law berbeda. Uji zero-length curve, cusp, nonuniform transform, reversal dan target interruption. Pisahkan failures sebagai geometry, timing, orientation, atau rendering agar perbaikan tidak salah lapisan.
