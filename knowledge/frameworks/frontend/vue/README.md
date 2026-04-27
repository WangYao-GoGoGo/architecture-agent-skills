# Vue Knowledge

## Heuristics

- Keep components focused on presentation and interaction.
- Use composables for reusable stateful behavior.
- Keep stores for shared state, not every local interaction.
- Separate server state from UI state.
- Make side effects and watchers easy to reason about.

## Common Risks

- Watchers hiding business workflows.
- Stores becoming dumping grounds.
- Components owning too much API and domain logic.

