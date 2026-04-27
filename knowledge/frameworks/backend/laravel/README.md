# Laravel Knowledge

## Heuristics

- Keep controllers focused on HTTP input/output and move workflow logic into services, actions, jobs, or domain modules.
- Treat Eloquent models, events, queues, policies, and service providers as architecture boundaries.
- Keep validation, authorization, transactions, and integration calls explicit.
- Use framework conventions for simple CRUD and add local boundaries when features grow.

## Common Risks

- Controllers and models becoming the only architecture.
- Hidden behavior through service container bindings, events, observers, or global helpers.
- Job retry behavior that is not idempotent.
