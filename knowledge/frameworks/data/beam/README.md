# Beam Knowledge

## Heuristics

- Separate pipeline construction, PTransform composition, windowing, triggers, and I/O.
- Keep transforms testable with the DirectRunner.
- Treat windowing, triggering, and watermark behavior as architecture.
- Add idempotency and exactly-once semantics for output writes.

## Common Risks

- Pipeline graphs too complex to reason about.
- Windowing and triggering not aligned with business semantics.
- Runner-specific behavior assumed in pipeline design.
