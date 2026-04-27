# WebAssembly Architecture Idioms

## Use When

- Reviewing WebAssembly module design, memory layout, JS/WASM boundary, or performance-critical web architecture.

## Heuristics

- Keep the JS/WASM interface thin — minimize cross-boundary calls.
- Use linear memory as a flat array — manage memory manually or via a language runtime.
- Use `WebAssembly.Memory` for shared memory in multi-threaded scenarios.
- Export only the minimum necessary functions and memory regions.
- Use streaming compilation (`WebAssembly.instantiateStreaming`) for faster load times.
- Use SIMD instructions for data-parallel workloads in WASM.
- Use `wasm-bindgen` or `wasm-pack` for Rust/AssemblyScript to WASM tooling.
- Profile before optimizing — WASM overhead varies by browser engine.

## Common Risks

- Large JS/WASM call overhead from fine-grained function calls.
- Memory leaks from manual memory management without proper cleanup.
- Linear memory fragmentation from frequent allocation/deallocation.
- Debugging difficulty — WASM stack traces are less informative than native.
- Browser compatibility differences in WASM feature support (SIMD, threads, GC).
