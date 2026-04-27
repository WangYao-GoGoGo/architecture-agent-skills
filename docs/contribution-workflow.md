# Contribution Workflow

## 1. Pick A Narrow Unit

Choose one contribution type:

- skill
- knowledge card
- before/after example
- evaluation checklist
- documentation improvement

Avoid broad pull requests that add many empty placeholders.

## 2. Connect It To A Real Agent Task

Every contribution should answer:

- What user request should trigger this?
- What should the agent inspect?
- What decision should the agent make?
- What output should the agent produce?
- How can a reviewer tell whether the result is better?

## 3. Prefer Practical Examples

Good examples are small enough to read but realistic enough to reveal a design problem.

For refactoring examples, include:

- before code
- after code or after explanation
- design pressure
- selected pattern, if any
- verification notes

## 4. Review Checklist

- Does the contribution reduce confusion for an agent?
- Does it avoid unnecessary abstraction?
- Does it preserve existing behavior?
- Does it give concrete decision rules?
- Does it fit the repository layout?

## 5. Documentation Language

Use clear English for project files so the repository is friendly to global contributors. Bilingual examples or translations can be added later when they help adoption.
