# Contributing

Thanks for helping build Architecture Agent Skills.

This project grows best through small, practical contributions:

- one focused skill
- one knowledge card
- one before/after example
- one evaluation checklist
- one improvement to existing guidance

## Contribution Flow

1. Choose a narrow problem an AI coding agent should handle better.
2. Add or update the smallest relevant file.
3. Include examples when the behavior is hard to judge from instructions alone.
4. Keep skills operational: workflows, decision rules, output format, verification.
5. Avoid copying long textbook explanations into skills. Put reusable concepts in `knowledge/`.

## Good First Contributions

- Fill a GoF pattern card in `knowledge/patterns/`.
- Add a Java or Python before/after refactoring example.
- Improve `skills/core/architecture-before-coding`.
- Add evaluation cases under `tests/`.

## Review Criteria

Contributions should make agent behavior more:

- maintainable
- readable
- testable
- locally consistent with the target codebase
- resistant to overengineering

If a proposed pattern or abstraction does not reduce real complexity, document the tradeoff and prefer the simpler design.
