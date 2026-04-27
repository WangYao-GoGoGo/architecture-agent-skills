# Specificity War → Utility-First Layout

Refactored from high-specificity overrides to a predictable utility-first approach with CSS custom properties for theming.

## Design Pressure

- `!important` was used as a crutch — the cascade was unpredictable.
- Adding a new variant required increasing specificity, making the problem worse.
- Theming (`.dark-theme`) required overriding every component.
- No one could predict which styles would apply to a given element.

## Applied Pattern

**Utility-first + CSS custom properties** — use low-specificity utility classes for layout. Use CSS custom properties for theme values — no overrides needed.

## After Code

```css
/* === Design tokens (CSS custom properties) === */
:root {
  --card-bg: white;
  --card-border: #ddd;
  --card-shadow: 0 2px 4px rgba(0,0,0,0.1);
  --card-radius: 8px;
  --card-padding: 16px;
  --card-text: #333;
}

.dark-theme {
  --card-bg: #333;
  --card-border: #555;
  --card-text: white;
}

/* === Component styles (low specificity) === */
.card {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: var(--card-radius);
  padding: var(--card-padding);
  box-shadow: var(--card-shadow);
  color: var(--card-text);
}

/* === Utility classes for variants === */
.card--featured {
  --card-border: blue;
  --card-shadow: 0 4px 8px rgba(0,0,255,0.2);
}

.card--compact {
  --card-padding: 8px;
  font-size: 14px;
}
```

## Key Changes

| Before | After |
|--------|-------|
| `.content .card` (specificity 0,2,0) | `.card` (specificity 0,1,0) — one rule |
| `#featured-card.card` (specificity 1,1,0) | `.card--featured` (specificity 0,1,0) — BEM modifier |
| `!important` for overrides | CSS custom properties — no overrides needed |
| `.dark-theme .card` (duplicated) | `--card-bg` token — one source of truth |
| Unpredictable cascade | Predictable, low-specificity rules |

## Verification

- No `!important` declarations.
- All `.card` rules have the same specificity (0,1,0).
- Dark theme requires zero component overrides — just set custom properties.
- Adding a new variant (e.g., `.card--warning`) requires no cascade knowledge.
- Theming is predictable: change a token, all components update.
