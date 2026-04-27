# Phoenix Knowledge

## Heuristics

- Keep contexts as bounded business domains with explicit public interfaces.
- Use LiveView for real-time UI; keep side effects in `handle_info` and `handle_event`.
- Organize PubSub topics by domain and subscription granularity.
- Keep Ecto schemas focused on persistence; use embedded schemas for value objects.
- Use channels for bidirectional real-time communication; avoid request-response patterns.

## Common Risks

- Contexts that are too large or too fragmented.
- LiveViews owning too much business logic.
- Ecto schemas leaking into every layer.
