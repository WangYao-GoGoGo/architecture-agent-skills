# Qt Knowledge

## Heuristics

- Separate signal/slot connections, widget hierarchy, model/view separation, and business logic.
- Keep UI thread responsive by moving blocking work to worker threads.
- Treat model/view architecture as the primary data pattern.
- Add proper parent-child ownership for memory management.

## Common Risks

- Signal/slot connections causing lifecycle issues.
- UI thread blocked by long-running operations.
- Model/view patterns not used for complex data displays.
