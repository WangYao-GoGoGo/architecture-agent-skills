# Assembly Architecture Idioms

## Use When

- Reviewing assembly code for bootloaders, interrupt handlers, performance-critical hot paths, or hardware interaction.

## Heuristics

- Follow the platform's calling convention (System V AMD64, ARM AAPCS, etc.) for function calls.
- Use registers for frequently accessed values — minimize memory loads/stores.
- Align code and data to cache-line boundaries for performance.
- Use SIMD instructions (SSE, AVX, NEON) for data-parallel operations.
- Keep interrupt handlers minimal — defer complex work to task level.
- Use stack frames for local variables when registers are exhausted.
- Document instruction choices that depend on specific microarchitecture features.
- Use atomic instructions (LOCK prefix, load-linked/store-conditional) for synchronization.

## Common Risks

- Missing memory barriers in multi-core synchronization code.
- Stack overflow from deep recursion or large stack frames.
- Incorrect calling convention causing register corruption.
- Pipeline stalls from data dependencies between adjacent instructions.
- Endianness assumptions when accessing multi-byte data.
