# Pepper and NAOqi Architecture

## Heuristics

- Keep interaction scripts, dialog state, perception events, motion commands, and backend integration separated.
- Treat NAOqi services, tablet UI, sensors, speech, and motion APIs as platform adapters.
- Keep long-running behavior observable and interruptible.
- Design fallback behavior for network, speech recognition, sensor, and motion failures.

## Common Risks

- Dialog logic directly issuing motion and backend commands.
- Global robot state hidden across scripts.
- Blocking calls that make interaction feel frozen or unsafe.
- Platform SDK types leaking into reusable domain logic.

## Verification

- Interaction flows can be replayed or simulated without a physical robot.
- Motion commands have safety and interruption behavior.
- Platform adapter failures have visible fallback paths.
