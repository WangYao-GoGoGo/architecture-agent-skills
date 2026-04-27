# iOS Knowledge

## Heuristics

- Separate view, state/view model, domain/use cases, and infrastructure.
- Treat app lifecycle, permissions, background execution, and persistence as architecture.
- Keep UIKit/SwiftUI details from dominating domain logic.
- Make concurrency and main-thread boundaries explicit.

## Common Risks

- View controllers or views becoming god objects.
- Business rules tied to UI lifecycle.
- Async work without clear cancellation or ownership.

