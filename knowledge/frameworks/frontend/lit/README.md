# Lit Knowledge

## Heuristics

- Keep components focused on UI; use services or stores for business logic.
- Use reactive properties for public API; keep internal state in private fields.
- Use shadow DOM for style and DOM encapsulation; ensure accessibility with ARIA attributes.
- Use events for parent-child communication; use shared services or stores for cross-component state.
- Use `update` and `updated` lifecycle callbacks for side effects; avoid `firstUpdated` for data loading.

## Common Risks

- Components owning business logic.
- Shadow DOM creating accessibility barriers.
- Events used for complex cross-component data flow.
