# Ember.js Knowledge

## Heuristics

- Keep routes focused on data loading and URL state; delegate rendering to components.
- Keep components focused on UI; use services for business logic and state management.
- Keep services scoped by domain with clear public APIs.
- Use Ember Data models for persistence mapping; use plain objects or classes for domain concepts.
- Keep controllers thin; prefer components for presentation logic.

## Common Risks

- Routes owning too much logic.
- Services becoming dumping grounds.
- Ember Data models leaking into every layer.
