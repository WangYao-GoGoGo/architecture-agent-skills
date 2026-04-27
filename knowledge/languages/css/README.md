# CSS Architecture Idioms

## Use When

- Reviewing CSS layout strategy, naming conventions, responsive design, or styling architecture.

## Heuristics

- Use CSS Grid for 2D layouts, Flexbox for 1D layouts (rows or columns).
- Use CSS custom properties (variables) for theme values — prefer over preprocessor variables.
- Use a consistent naming methodology — BEM, SMACSS, or CSS Modules.
- Use `clamp()`, `min()`, `max()` for fluid typography and spacing.
- Use `container queries` for component-level responsive design.
- Keep specificity flat — avoid `!important` and deep nesting in preprocessors.
- Use `:where()` and `:is()` for managing specificity.
- Use `@layer` for controlling cascade order in large stylesheets.

## Common Risks

- Overly specific selectors causing maintenance headaches.
- Using `!important` as a shortcut instead of fixing specificity.
- Not testing responsive breakpoints on real devices.
- CSS-in-JS runtime performance impact in large applications.
- Missing focus-visible styles for keyboard accessibility.
