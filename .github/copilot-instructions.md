# Copilot Instructions for Architecture Agent Skills

This repository is a Markdown-based architecture skill library, not a compiled application or service. The primary source of truth is the content under `skills/`, `knowledge/`, `docs/`, `examples/`, and `tests/`.

## What to focus on
- `skills/` contains workflow-oriented agent tasks. Each non-trivial skill should have `SKILL.md`, a clear `name`, `description`, and an explicit `Knowledge To Use` section.
- `knowledge/` contains reusable architecture concepts, patterns, smells, and ecosystem-specific guidance. Use these cards as the reasoning basis for decisions.
- `docs/` contains project structure and contributor rules. Key files are `docs/directory-structure.md`, `docs/taxonomy.md`, `docs/skill-design-guide.md`, and `docs/knowledge-skill-map.md`.
- `examples/` stores before/after examples. Keep them small, realistic, and directly tied to the skill or guidance.
- `tests/` describes manual evaluation and skill output expectations; it is not an automated test suite.

## Project-specific conventions
- Prefer narrow contributions: one skill, one knowledge card, one before/after example, or one evaluation checklist.
- Choose placement in this order: platform-ecosystem → framework → language → domain → paradigm → core.
- Use `skills/core/architecture-before-coding/SKILL.md` for architecture-first design tasks.
- Use `skills/core/design-pattern-selector/SKILL.md` when advising whether a pattern is justified.
- Use `skills/core/refactoring-planner` when reviewing or changing existing code.
- Keep framework behavior in `knowledge/frameworks/` and external runtime/platform constraints in `knowledge/platform-ecosystems/`.

## Important workflow notes
- There is no `package.json`, `pyproject.toml`, `Makefile`, or CI workflow in this repo. Do not invent build or runtime commands.
- Validation is primarily manual: verify the markdown structure, file placement, and whether a new skill clearly points to relevant knowledge cards.
- If asked for build/test/debug commands, explain that this repository contains content and guidance only, and refer to the documentation files rather than asking for code execution.

## How to use this repo effectively
- Start with `README.md` to understand the top-level model and the distinction between `skills/` and `knowledge/`.
- Use `docs/directory-structure.md` to map new contributions to the correct folder.
- Use `docs/contribution-workflow.md` and `CONTRIBUTING.md` to keep changes small and reviewable.
- When improving a skill, link to reusable cards under `knowledge/` instead of duplicating explanation in `skills/`.
- When adding a skill, make sure it is actionable and includes explicit decision rules rather than broad architectural theory.

## Key files to reference
- `README.md`
- `CONTRIBUTING.md`
- `docs/directory-structure.md`
- `docs/taxonomy.md`
- `docs/skill-design-guide.md`
- `skills/core/architecture-before-coding/SKILL.md`
- `skills/core/design-pattern-selector/SKILL.md`
- `tests/README.md`
