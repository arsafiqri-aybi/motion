// Educational semi-implicit Euler particles, uncompiled in this release.
// y-up, consistent position units, dt seconds; no collisions or neighbors.
struct Particle { position: vec2<f32>, velocity: vec2<f32> }
struct Params { dt: f32, count: u32, padding: vec2<u32> }
@group(0) @binding(0) var<storage, read> previous: array<Particle>;
@group(0) @binding(1) var<storage, read_write> current: array<Particle>;
@group(0) @binding(2) var<uniform> params: Params;

@compute @workgroup_size(64)
fn step(@builtin(global_invocation_id) invocation: vec3<u32>) {
    let i = invocation.x;
    if (i >= params.count) { return; }
    let p = previous[i];
    let velocity = p.velocity + vec2<f32>(0.0, -9.81) * params.dt;
    current[i].velocity = velocity;
    current[i].position = p.position + velocity * params.dt;
}
