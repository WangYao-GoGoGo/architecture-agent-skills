---
name: ember-app-architecture-review
description: Use when reviewing Ember.js application architecture, components, routes, services, controllers, Ember Data, and application structure.
---

# Ember.js App Architecture Review

## When To Use

- The main decision is about Ember.js project structure, route organization, component design, service boundaries, or Ember Data model design.
- Reviewing controller responsibilities or addon usage.

## Workflow

1. Identify project structure — are routes, components, services, and controllers organized by domain?
2. Review route organization — do routes follow the application's URL structure?
3. Check component design — are components focused on UI or owning business logic?
4. Review service boundaries — are services scoped by domain or becoming dumping grounds?
5. Check Ember Data model design — are models representing persistence or domain concepts?
6. Review controller responsibilities — are controllers handling presentation logic?
7. Recommend the smallest change that clarifies structure.

## Output Format

```markdown
Ember.js architecture review:
- Project structure:
- Route organization:
- Component design:
- Service boundaries:
- Ember Data models:
- Controller responsibilities:
- Recommended change:
- Verification:
```
