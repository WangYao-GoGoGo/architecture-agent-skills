# Django Knowledge

## Heuristics

- Keep views focused on request/response coordination.
- Use models, managers, services, or domain modules deliberately rather than making models or views absorb all behavior.
- Review serializers/forms as API and validation boundaries.
- Keep migrations and transaction behavior explicit.
- Watch querysets for N+1 and hidden database work.

## Common Risks

- Fat models or fat views.
- Business rules split across signals, serializers, and views.
- Migrations generated without rollout review.

