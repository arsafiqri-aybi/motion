# Springs, integrasi, dan control

Menghubungkan D08, D10, D12 dan D35. Contoh memiliki linear 1D fixed-target assumptions; bukan full physics engine.

## Parameter yang mempunyai arti

Model m x″+c x′+k(x−r)=0 mempunyai mass m>0, stiffness k>0 dan damping c≥0. Definisikan y=x−r untuk target tetap, natural frequency ω=√(k/m), damping ratio ζ=c/(2√km). Frequency di sini rad/s, bukan Hz. c mempunyai unit mass/time, sedangkan k mass/time².

ζ<1 underdamped, ζ=1 critically damped, ζ>1 overdamped. Klasifikasi ini berlaku untuk linear fixed-coefficient system, bukan setiap spring tool yang menyebut parameter damping. Parameter library mungkin berupa damping ratio, friction, duration approximation atau gain; baca contract sebelum konversi.

## Solusi analitik

Untuk ζ<1, ωd=ω√(1−ζ²), y(t)=e^(−ζωt)[A cos(ωd t)+B sin(ωd t)]. A=y0 dan B=(v0+ζωy0)/ωd. Untuk ζ=1, y(t)=[y0+(v0+ωy0)t]e^(−ωt). Turunannya v(t)=[v0−ω(v0+ωy0)t]e^(−ωt).

Untuk ζ>1, roots λ1,2=−ζω±ω√(ζ²−1), sehingga y=Ae^(λ1t)+Be^(λ2t). A=(v0−λ2 y0)/(λ1−λ2), B=y0−A. Dekat ζ=1 roots hampir sama; direct formula dapat kehilangan precision. Gunakan stable near-critical formulation atau analytic critical branch dengan threshold yang dapat dijelaskan. Jangan memakai arbitrary branch tanpa error assessment.

## Euler berbeda dengan semi-implicit Euler

Explicit Euler: x_next=x+h v, v_next=v+h a(x,v). Semi-implicit: v_next=v+h a(x,v), x_next=x+h v_next. Keduanya first-order methods, tetapi dynamics/stability behavior berbeda. Higher-order RK4 meningkatkan accuracy untuk smooth ODE, tetap tidak unrestricted-stable untuk stiff systems.

Increasing stiffness menaikkan ω, sehingga relevant dimensionless step adalah hω. Stable numerical response belum tentu accurate phase/settling. Gunakan refinement h,h/2,h/4 pada trajectory error dan energy behavior. `spring_step` di repo memakai semi-implicit, sementara `critical_spring` adalah analytic oracle. Lab tidak memilih timestep universal untuk seluruh k,c,m.

## Moving target dan damping semantics

Jika damping adalah −c v_world, moving target memberi behavior berbeda dari −c(v−v_target). Untuk relative damping, target velocity perlu tersedia/estimated. Transform ke y=x−r(t) menambahkan terms terkait r′/r″; fixed-target solution tidak dapat diterapkan begitu saja pada moving target continuously. Piecewise target changes dapat memakai analytic propagation antar changes, dengan x,v tetap continuous.

## Control interpretation

Acceleration-command PD: x″=Kp(r−x)+Kd(vr−v). Dengan fixed target dan no extra dynamics, Kp=ω², Kd=2ζω. Jika output adalah force, gains harus memasukkan mass; jika output adalah actuator position, model berbeda. Saturation, delay, friction dan disturbance dapat invalidate nominal tuning.

Controller integral bukan efek tambahan wajib. Integral mengakumulasi error; ketika blocked/saturated ia dapat wind up. Gunakan anti-windup dan reset/pause behavior yang sesuai plant. Virtual UI spring umumnya tidak membutuhkan hardware-style integral control.

## Eksperimen dan diagnosis

Lab 05 verifies exact critical response. Lab 06 measures semi-implicit error reduction at selected timesteps; tests include derivative consistency of oracle and RK4 smooth decay. Periksa `reports/labs/spring-trace.csv` untuk time, x, v dan analytic x. Ini tidak menguji target interruptions, nonlinear spring atau contacts.

Jika response explodes: audit dt/unit, sign, mass, stiffness dan solver stability sebelum mengganti easing. Jika position jumps: audit retarget initialization/clock. Jika lag mengikuti input: audit model bandwidth/filtering/delay. Jika high fps changes speed: audit frame-based increments. Pisahkan cause classes sebelum tuning.
