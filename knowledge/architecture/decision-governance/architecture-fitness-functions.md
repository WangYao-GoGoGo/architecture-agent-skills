# Architecture Fitness Functions

## Use When

- A team wants executable or reviewable checks that architecture rules continue to hold.

## Core Idea

Fitness functions are tests, checks, metrics, or review criteria that detect architecture drift.

## Heuristics

- Check dependency direction, forbidden imports, public API compatibility, schema migration safety, or performance budgets.
- Prefer automated checks for brittle rules.
- Use review checklists for judgment-heavy rules.
- Keep checks tied to real architecture risks.

## Risks

- Too many checks block harmless change.
- Checks encode outdated architecture assumptions.
- Manual-only checks are forgotten.

