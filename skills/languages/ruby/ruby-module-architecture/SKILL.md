---
name: ruby-module-architecture
description: Use when reviewing Ruby module organization, mixin design, metaprogramming patterns, and Rails application architecture.
---

# Ruby Module Architecture

## When To Use
- The main decision is about module inclusion strategy, metaprogramming usage, or Rails service object design.
- Reviewing `include` vs `prepend` vs `extend`, or `method_missing` usage.

## Workflow
1. Identify module responsibilities — does each module have a single concern?
2. Review `include` vs `prepend` vs `extend` — is the correct inclusion strategy used?
3. Check metaprogramming usage — is `method_missing`/`define_method` justified?
4. Review Rails patterns — are controllers thin, models focused, and services extracted?
5. Check dependency direction — do modules depend on abstractions, not concretions?
6. Review testability — can modules be tested in isolation?
7. Recommend the simplest module structure.

## Output Format
```markdown
Ruby module review:
- Module responsibilities:
- Inclusion strategy:
- Metaprogramming:
- Rails patterns:
- Dependency direction:
- Testability:
- Recommended change:
- Verification:
```
