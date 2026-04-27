# ASP.NET Core Knowledge

## Heuristics

- Keep controllers or minimal API endpoints as transport adapters.
- Put use-case orchestration in application services, handlers, or feature modules.
- Treat dependency injection, middleware, filters, hosted services, configuration, and options as architecture.
- Make EF Core transaction and tracking boundaries explicit when persistence is involved.

## Common Risks

- Business logic spread across middleware, controllers, filters, and EF entities.
- Service registration hiding dependency direction.
- Long-lived hosted services without clear failure, retry, and shutdown behavior.
