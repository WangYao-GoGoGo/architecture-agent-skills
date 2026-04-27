# Architecture Fitness Functions

## Project Fit

Fitness functions fit projects where architecture rules can drift and checks help catch regressions.

## Use When

- A team wants executable or reviewable checks that architecture rules continue to hold.
- Dependency direction, API compatibility, migration safety, or performance budgets matter.

## Avoid When

- The rule is too judgment-heavy for automation and better handled by review.
- The check would encode an outdated or unimportant constraint.
- The maintenance cost is higher than the risk.

## Core Idea

Fitness functions are tests, checks, metrics, or review criteria that detect architecture drift.

## Fits Best With

- Module dependency rules, forbidden imports, API compatibility, schema migration safety, latency budgets, bundle size budgets, query plan checks.

## Heuristics

- Check dependency direction, forbidden imports, public API compatibility, schema migration safety, or performance budgets.
- Prefer automated checks for brittle rules.
- Use review checklists for judgment-heavy rules.
- Keep checks tied to real architecture risks.

## Risks

- Too many checks block harmless change.
- Checks encode outdated architecture assumptions.
- Manual-only checks are forgotten.

## Verification

- The check fails when the architecture rule is violated.
- The check is documented and owned.
- False positives are low enough that teams respect it.
