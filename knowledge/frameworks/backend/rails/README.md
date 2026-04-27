# Rails Knowledge

## Heuristics

- Keep controllers thin and move business workflows into application services or domain objects when callbacks and models become overloaded.
- Treat Active Record models as persistence-aware domain objects only when the domain remains simple.
- Make background jobs, transactions, mailers, policies, and serializers explicit architecture boundaries.
- Use Rails conventions where they reduce friction, and introduce layers only when change pressure justifies them.

## Common Risks

- Fat models that own validation, persistence, policy, orchestration, and integration behavior.
- Callback chains that hide workflow order and failure behavior.
- API contracts coupled directly to database shape.
