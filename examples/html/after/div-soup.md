# Div Soup → Semantic Landmarks

Refactored from generic `<div>` containers to semantic HTML5 elements with ARIA landmarks.

## Design Pressure

- Screen readers cannot navigate the page — no landmarks, no heading hierarchy.
- CSS selectors depend on fragile class names like `.header`, `.nav-item`.
- No semantic meaning — search engines cannot identify the main content.
- The document structure is flat — no hierarchy for assistive technology.

## Applied Pattern

**Semantic HTML + ARIA landmarks** — replace `<div>` with `<header>`, `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>`. Use heading levels (`h1`–`h6`) for content hierarchy.

## After Code

```html
<header>
  <a href="/" aria-label="Home page">
    <img src="logo.png" alt="Company Logo">
  </a>
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
      <li><a href="/contact">Contact</a></li>
    </ul>
  </nav>
</header>

<main>
  <article>
    <header>
      <h1>Welcome to Our Site</h1>
      <p><time datetime="2025-01-15">January 15, 2025</time></p>
    </header>
    <section aria-labelledby="intro-heading">
      <h2 id="intro-heading">Introduction</h2>
      <p>Lorem ipsum dolor sit amet...</p>
    </section>
    <section aria-labelledby="features-heading">
      <h2 id="features-heading">Features</h2>
      <p>Our product includes...</p>
    </section>
  </article>
  <aside aria-labelledby="sidebar-heading">
    <h2 id="sidebar-heading">Categories</h2>
    <ul>
      <li>Tech</li>
      <li>Design</li>
    </ul>
  </aside>
</main>

<footer>
  <p>&copy; 2025 Company Name</p>
</footer>
```

## Key Changes

| Before | After |
|--------|-------|
| `<div class="header">` | `<header>` — semantic landmark |
| `<div class="nav">` | `<nav aria-label="Main navigation">` |
| `<div class="main">` | `<main>` — primary content landmark |
| `<div class="article">` | `<article>` — self-contained content |
| `<div class="sidebar">` | `<aside>` — complementary content |
| `<div class="footer">` | `<footer>` — footer landmark |
| `<div class="title">` | `<h1>` — proper heading level |
| `<div class="section-title">` | `<h2>` — nested heading |
| No list semantics | `<ul>` / `<li>` for navigation and lists |

## Verification

- Screen reader can jump between landmarks (`header`, `nav`, `main`, `aside`, `footer`).
- Heading hierarchy is logical: `h1` → `h2` (no skipped levels).
- Navigation is announced as a list with 3 items.
- CSS selectors can use element selectors (`nav ul`, `article h2`) instead of fragile classes.
- Search engines correctly identify the main content and article boundaries.
