# Stencil Knowledge

## Heuristics

- Keep components focused on UI; use services for business logic.
- Use `@Prop` for public API, `@State` for internal state, `@Watch` for reacting to changes.
- Use shadow DOM for style and DOM encapsulation; ensure accessibility.
- Use `@Event` for parent-child communication; use shared services for cross-component state.
- Use `componentWillLoad` and `componentDidLoad` for initialization and data loading.

## Common Risks

- Components owning business logic.
- Shadow DOM creating accessibility barriers.
- Events used for complex cross-component data flow.
