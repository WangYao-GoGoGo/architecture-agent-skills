# Skill Output Format

Most architecture skills should produce a compact, inspectable structure.

## Recommended Sections

```markdown
Diagnosis:
- What problem or design pressure exists?

Recommended design:
- What structure should be used?
- Why is it the smallest useful structure?

Alternatives considered:
- What was rejected and why?

Implementation plan:
- Behavior-preserving steps.

Verification:
- Tests, checks, examples, query plans, or manual validation.

Overengineering check:
- What abstraction was avoided?
```

## Quality Rules

- Prefer specific file/module references over generic advice.
- Name tradeoffs instead of presenting one design as universally correct.
- Preserve existing behavior during refactors.
- Do not require a pattern when simple code is enough.
- Include domain-specific verification for databases, caches, APIs, and frontend state.
