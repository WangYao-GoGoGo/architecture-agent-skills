# HTML Architecture Idioms

## Use When

- Reviewing HTML document structure, semantic markup, accessibility compliance, or web component design.

## Heuristics

- Use semantic HTML elements (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`) over generic `<div>`.
- Use heading hierarchy (`h1`-`h6`) correctly — one `h1` per page, no skipping levels.
- Use `alt` attributes on all images for accessibility.
- Use ARIA roles and attributes (`role`, `aria-label`, `aria-describedby`) only when native semantics are insufficient.
- Use `<form>` with proper `<label>` associations for all form controls.
- Use `<button>` for actions, `<a>` for navigation — never use `<div>` as a button.
- Use `<picture>` and `srcset` for responsive images.
- Use `defer` or `async` for script loading to avoid render blocking.

## Common Risks

- Non-semantic `<div>`-soup that harms accessibility and SEO.
- Missing or incorrect heading hierarchy.
- Missing form label associations.
- Using `<div>` with click handlers instead of `<button>`.
- Not providing text alternatives for non-text content.
