# Skill Design Guide

This guide defines how to write skills for Architecture Agent Skills.

## Skill Contract

Every skill should help an agent do one job well. A skill is not a blog post, a full textbook chapter, or a list of every possible pattern. It should be concise, operational, and testable through examples.

Each skill folder should contain:

- `SKILL.md`: required agent-facing instructions
- `README.md`: optional human-facing summary for GitHub readers
- `references/`: optional deeper material loaded only when needed
- `scripts/`: optional deterministic helpers

## Recommended SKILL.md Shape

```markdown
---
name: short-skill-name
description: Use when ...
---

# Skill Name

## When To Use

## Inputs To Inspect

## Workflow

## Decision Rules

## Output Format

## Stop Conditions
```

## Writing Rules

- Start with the trigger: when should the agent use this skill?
- Give a workflow, not just concepts.
- Prefer checklists and decision rules over long explanations.
- Include negative guidance: when not to use the skill.
- Keep detailed pattern catalogs in `knowledge/`, not inside every skill.
- Require the agent to preserve existing behavior during refactors.
- Require verification steps when code is changed.

## Architecture Skill Quality Bar

A useful architecture skill should make the agent:

- inspect existing code before proposing structure
- identify current pain: coupling, duplication, unclear ownership, fragile conditionals, schema friction, cache inconsistency, state sprawl, poor testability
- choose the smallest structure that solves the pain
- respect the target paradigm, language, framework, and domain
- name tradeoffs clearly
- produce a step-by-step implementation or refactoring plan
- avoid introducing abstractions without an immediate reason

## Naming

Use task-oriented names:

- Good: `architecture-before-coding`, `java-oo-refactor`, `c-modular-architecture`, `redis-cache-design-review`, `dependency-boundary-review`
- Weak: `patterns`, `clean-code`, `architecture-notes`

## Output Formats

Skills should standardize output when possible. Suggested sections:

- `Diagnosis`
- `Recommended Design`
- `Alternatives Considered`
- `Implementation Plan`
- `Verification`
- `Overengineering Check`

## Example Requirement

Any important skill should eventually have at least one example:

- `examples/<language>/before/...`
- `examples/<language>/after/...`
- notes explaining why the design improved
