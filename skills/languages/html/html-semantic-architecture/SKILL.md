---
name: html-semantic-architecture
description: Use when reviewing HTML document structure, semantic markup, accessibility compliance, and web component architecture.
---

# HTML Semantic Architecture

## When To Use
- The main decision is about document outline, semantic element selection, ARIA usage, or accessibility compliance.
- Reviewing web component design, form structure, or SEO optimization.

## Workflow
1. Identify document structure — is there a clear heading hierarchy with one `h1`?
2. Review semantic element usage — are `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>` used appropriately?
3. Check accessibility — do all images have `alt` text? Are form controls properly labeled?
4. Review ARIA usage — are ARIA roles/attributes used only when native semantics are insufficient?
5. Check form structure — are `<label>` elements properly associated with inputs?
6. Review interactive elements — are `<button>` used for actions and `<a>` for navigation?
7. Recommend the most semantic and accessible HTML structure.

## Output Format
```markdown
HTML semantic review:
- Document structure:
- Semantic elements:
- Accessibility:
- ARIA usage:
- Form structure:
- Interactive elements:
- Recommended change:
- Verification:
```
