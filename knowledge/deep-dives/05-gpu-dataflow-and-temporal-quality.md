# GPU dataflow dan temporal quality

Menghubungkan D05, D25, D26, D27 dan D35. [Shader contoh](../../examples/particles.wgsl) belum dicompile/dieksekusi dalam release ini; numerical tests Python tidak memvalidasi shader.

## Contract data sebelum shader

Particle struct contoh berisi position vec2<f32> dan velocity vec2<f32>; layout storage stride adalah 16 bytes dalam aturan WGSL yang relevan. Uniform Params menggunakan dt:f32, count:u32 dan padding:vec2<u32>, total 16 bytes. Host harus menulis byte offsets/type tepat, bukan mengirim object JSON langsung. Detail ABI/version perlu diperiksa terhadap WGSL pada target implementation.

Buffer A adalah snapshot read-only; B output. Semua invocations membaca A, tidak partly updated neighbor state. Count tidak harus multiple workgroup size; dispatch ceil(N/64) groups dan guard index≥N. Empty workload can skip dispatch. Setelah pass compute, render memakai B; berikutnya swap roles. API pass ordering/resource usage harus memenuhi backend contract; jangan menganggap shader barrier mengurutkan semua workgroups.

## CPU submission versus GPU completion

Calling submit measures enqueue overhead, bukan selesai seluruh work. Accurate GPU time memerlukan supported timestamp queries atau dedicated profiling. Readback synchronous/waiting dapat stall pipeline; profiling method sendiri bisa mengubah workload. Report CPU and GPU measurements separately plus rendering outcome.

## Correctness progression

Start one particle, zero gravity/dt identity, known velocity, known constant acceleration, count 63/64/65, large coordinates, invalid inputs rejected host-side. Compare CPU reference with defined tolerance. Add multiple particles only after layout/bounds pass. Neighbors require extra data structure/passes; shader contoh tidak melakukan collision atau interaction.

## Motion vectors dan history

Temporal algorithms need previous/current transforms and camera projections. Screen motion from world pose can include camera movement even when object static. A velocity buffer needs convention: current-minus-previous normalized coordinates versus pixels/second menghasilkan scaling berbeda. Include deformation if required; rigid matrix velocity cannot capture animated cloth completely.

History invalid ketika camera cut, render size changes, object spawned, mesh correspondence changed, or disocclusion reveals previously invisible geometry. Reprojection without validity mask menghasilkan ghost trails. Transparent materials may need special handling rather than blindly reuse opaque depth history.

## Anti-aliasing trade-offs

Spatial jaggies, temporal shimmer, motion blur dan accumulation noise adalah symptoms berbeda. Higher resolution helps some spatial artifacts but not automatically temporal sampling. TAA may stabilize detail while blurring/ghosting; sharpen may increase flicker. Measure representative sequences with camera/object motion and cuts.

## Resource lifecycle

Buffers, textures, render targets dan pipelines perlu ownership and reuse. Resize can recreate targets and invalidate history. Device/context loss requires stop current work, establish capability and rebuild resources; unsupported backend needs content-preserving fallback. Target limits—not desktop development machine—determine maximum buffer/texture/workgroup workloads.

## Failure classification

Wrong values across all particles: inspect offsets/stride/type. Last particles corrupted: inspect dispatch/bounds. Flicker repeated runs: inspect races/history. CPU fast but frame slow: inspect GPU/pass bandwidth/overdraw. Huge delay during diagnostics: inspect readback. Particle acceleration changes refresh rate: inspect dt/clock mapping.

Do not claim WebGPU verified from a WGSL file existing. GPU source retrieval failed in this build; its references remain review-open. Full graphics validation requires actual device, adapter versions, compiled shader, resource checks and rendered/compute readback fixtures.
