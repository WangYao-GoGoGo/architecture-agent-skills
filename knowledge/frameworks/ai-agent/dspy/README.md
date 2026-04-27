# DSPy Knowledge

## Heuristics

- Separate module composition, teleprompter selection, metric design, and evaluation.
- Keep program structure inspectable and versioned.
- Treat prompt optimization as a build-time concern, not runtime.
- Add evaluation with representative examples and metrics.

## Common Risks

- Over-optimized prompts that don't generalize.
- Teleprompter choices not validated against held-out data.
- Program structure too complex to debug.
