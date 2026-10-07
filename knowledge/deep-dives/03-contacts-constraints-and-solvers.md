# Contacts, constraints, dan solver boundaries

Menghubungkan D02, D08, D09, D10 dan D39. Formula di sini menjelaskan ideal rigid-contact subset; frictional multibody contact membutuhkan solver lebih luas.

## Geometri sebelum response

Collision detection menghasilkan candidate contact, point, normal dan penetration/time-of-impact menurut convention. Response memakai informasi tersebut untuk mengubah velocity/position. Salah contact normal tidak dapat diperbaiki dengan lebih banyak solver iterations. Broad phase false positives boleh ditapis narrow phase, tetapi false negatives menghilangkan contact.

## Normal impulse

Untuk two rigid bodies, relative velocity di contact mencakup linear velocity dan ω×r. Pilih normal n dari body B menuju A dan v_rel=vA_contact−vB_contact. Incoming contact mempunyai dot(v_rel,n)<0. Impulse pada A adalah +jn dan pada B −jn.

Dalam ideal frictionless impact, j=−(1+e)dot(v_rel,n)/denominator. Denominator mengandung inverse masses serta rotational terms ((I_A⁻¹(r_A×n))×r_A + (I_B⁻¹(r_B×n))×r_B)·n. Inertia tensors/r lever arms harus berada pada frame sama. Static body memberi inverse mass/inertia nol. Formula tidak diterapkan lagi pada already separating contacts untuk menambah energy.

## Friction dan resting contact

Tangential impulses menentang relative tangential velocity dengan bound terkait normal impulse; simple Coulomb approximation memakai norm(jt)≤μjn. Static/kinetic models dan cone approximation perlu dinyatakan. Resting contacts tidak hanya impact berulang: gravity dan penetration correction harus ditangani tanpa restitution jitter. Many-contact systems biasanya diselesaikan iteratively dengan warm starts dan residual diagnostics.

Position correction menyelesaikan penetration tetapi bukan physical impulse yang sama. Terlalu agresif correction dapat inject energy atau jitter; terlalu lemah memungkinkan sinking. Record bias/compliance/substep choices dan test stacks, not just bouncing ball.

## Continuous collision detection

Discrete samples bisa miss thin obstacles. Swept intersection/time-of-impact mencari event di interval timestep. Advance to impact, apply response, lalu integrate remainder menurut method. Multiple impacts, rotating bodies dan changing shapes menambah complexity. Clamping body di wall pada frame akhir bukan equal-time solution.

## Constraint formulation

Distance constraint C(x)=norm(xA−xB)−L. Gradient ∂C/∂xA=d/norm(d), opposite for B. Jika d=0, gradient undefined; fallback needs explicit policy. Position projection with inverse-mass weights uses Δλ=−C/(Σwi norm(∇iC)²) for simple ideal constraint, then Δxi=wi∇iC Δλ.

XPBD-style compliance introduces α_tilde=α/h² and accumulated multiplier: Δλ=(−C−α_tilde λ)/(Σwi norm(∇iC)²+α_tilde). Update λ and positions consistently. Compliance units, timestep and multiplier reset/warm-start conventions matter; copying formula without these contracts does not give timestep-independent behavior universally.

## Validation progression

Start free flight and single distance constraint. Add single impact and compare momentum/restitution. Add resting contact, friction, stack, high-speed thin wall, and mixed masses. Sweep h, substeps, solver iterations and ordering. Measure residual, penetration, energy/work budget and convergence. Physics tests can pass numerical properties while still wrong material calibration.

The runnable repo lab covers a linear spring, not this contact solver. These derivations are authored technical synthesis; implement and independently test contact-specific fixtures before claiming a contact engine. Specialist friction/complementarity/soft-body research remains open in [gap register](../../governance/open-gaps.md).
