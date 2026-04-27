# Coupling And Cohesion

## Use When

- Evaluating whether modules, classes, services, components, or schemas have good boundaries.

## Core Idea

Cohesion means related responsibilities live together. Coupling means one unit depends on another. Good architecture usually has high cohesion and intentional, low coupling.

## Signals Of Low Cohesion

- A module has many unrelated reasons to change.
- Tests need unrelated setup.
- Naming becomes vague: manager, helper, util, common.

## Signals Of Harmful Coupling

- Cyclic dependencies.
- Business rules import infrastructure details.
- UI components know storage details.
- Database schema changes require broad application rewrites.

## Improvement Moves

- Move behavior closer to the data or policy it belongs to.
- Introduce a boundary around volatile details.
- Split modules by reason to change, not by arbitrary file size.
