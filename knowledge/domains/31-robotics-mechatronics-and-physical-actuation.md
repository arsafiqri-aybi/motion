# D31 — Robotics Mechatronics and Physical Actuation

Menghubungkan motion models, planning dan control dengan actuators, sensors serta physical operating limits.

Rumpun: **E — Graphics and Output**. Status: **AUTHORED_OVERVIEW** — penjelasan dan aturan implementasi telah ditulis; ini bukan tanda seluruh cabang telah diaudit sebagai monograf.

[Indeks seluruh domain](../../architecture/domain-map.md) · [Kebijakan bukti](../../governance/evidence-policy.md) · [Peta sumber](../../references/source-map.md)

## Batas dan prasyarat

Pembahasan repo adalah knowledge dan simulasi. Physical deployment membutuhkan equipment-specific calibration, constraints dan verification; UI animation parameters bukan actuator settings.

Prasyarat: [D07](../../architecture/domain-map.md#d07), [D08](../../architecture/domain-map.md#d08), [D12](../../architecture/domain-map.md#d12), [D13](../../architecture/domain-map.md#d13), [D23](../../architecture/domain-map.md#d23).

## Subdomain dan pengetahuan inti

### D31.01 — Actuators dan transmissions

Motors, servos, linear actuators dan pneumatic mechanisms mempunyai torque/speed/thermal limits berbeda. Gearing changes inertia/friction/backlash.

**Model / prosedur.** Model input→actuator response→mechanical output with units and limits.

**Kegagalan.** Ideal torque model ignores saturation/deadband.

**Verifikasi.** Datasheet/model comparison and bounded simulation fixtures.

### D31.02 — Encoders sensors dan calibration

Position/velocity/force observations mempunyai quantization, bias dan mounting conventions. Homing sets reference, not universal absolute truth.

**Model / prosedur.** Establish zero/reference, scale/sign, timestamp and valid range.

**Kegagalan.** Encoder counts interpreted radians without conversion.

**Verifikasi.** Known positions/directions, stationary noise and disconnect behavior.

### D31.03 — Embedded real-time execution

Control cycles need bounded execution and jitter. General-purpose UI scheduling cannot ensure hard deadlines.

**Model / prosedur.** Separate sensing/control/actuation phases; measure worst-case timing and overruns.

**Kegagalan.** Average timing presented deadline guarantee.

**Verifikasi.** Timing traces, load spikes and deadline handling.

### D31.04 — Manipulators mobile robots dan drones

Kinematics/dynamics differ by platform; nonholonomic mobility, flight dynamics and manipulation need appropriate models.

**Model / prosedur.** Use platform state/action constraints; connect planner/controller with consistent frames.

**Kegagalan.** Holonomic plan given nonholonomic plant.

**Verifikasi.** Reachability/dynamics feasibility and task-specific simulated cases.

### D31.05 — Communication buses dan interfaces

Commands/data over serial/CAN/network need sequence, rate, integrity and stale-command policy.

**Model / prosedur.** Timestamp commands, enforce bounded validity, acknowledge according protocol.

**Kegagalan.** Old packets continue actuation after disconnect.

**Verifikasi.** Reordering, duplicates, delays and connection loss simulation.

### D31.06 — Limits fault handling dan safety functions

Physical bounds, watchdogs and protective functions must not depend solely on presentation animation. Failure response is system-specific engineering.

**Model / prosedur.** Independent limits, state validity checks, stop/fallback contract appropriate equipment.

**Kegagalan.** Simulation PASS claimed hardware safety; software indicator mistaken enforcement.

**Verifikasi.** Fault injection, command saturation, sensor failure and independently verified mechanisms.

### D31.07 — Kinetic installations dan animatronics

Artistic movement still has mechanism, audience distance, synchronization and maintenance constraints.

**Model / prosedur.** Separate choreography from low-level limits; schedule feasible trajectories.

**Kegagalan.** Beautiful path requires impossible actuator acceleration.

**Verifikasi.** Trajectory feasibility, endurance model, synchronized simulation and inspection plan.

## Contoh kerja dan alasan pemilihan

Contoh simulated pan-tilt mechanism accepts angles in radians and max velocity. Choreography supplies desired poses; trajectory generator applies limits; controller tracks; simulated actuator saturates. Commands carry sequence/time validity. Test dropped sensor input and delayed command using simulation. Do not infer actual mechanism torque, thermal behavior or stop performance from this example.

## Alur implementasi

Define physical platform/model; establish units/calibration; implement simulation; constrain trajectory; validate controller/interfaces; document hardware-specific checks separately before deployment.

## Kriteria penguasaan

Dapat menerjemahkan motion intent ke feasible trajectory dan menjelaskan limits serta fault contracts tanpa menyamakan simulasi dengan hardware proof.

## Cabang lanjut yang tetap termasuk cakupan

Robot middleware; real-time OS; motor control; force control; compliant actuation; drone flight control; industrial motion; animatronics; kinetic architecture.

## Rujukan dan batas bukti

- [S03](../../references/source-map.md#s03)
- [S67](../../references/source-map.md#s67)
- [S68](../../references/source-map.md#s68)

Rujukan adalah jalur pembelajaran, bukan dukungan otomatis untuk setiap kalimat. Persamaan dasar dan contoh ditulis sebagai sintesis teknis; klaim API/standar yang diperiksa dipisahkan dalam claim ledger. Cabang lanjut pada daftar cakupan belum semuanya memiliki pembahasan tingkat riset tersendiri.
