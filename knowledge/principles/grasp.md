# GRASP

## Use When

- Assigning responsibilities in object-oriented designs.
- Deciding which class should create, coordinate, or own behavior.

## Core Idea

GRASP offers responsibility assignment patterns. It helps answer "who should do this?"

## Practical Heuristics

- Information Expert: put behavior near the data and knowledge it needs.
- Creator: let an object create another object when it contains, aggregates, or closely uses it.
- Controller: route system events through a small coordinator, not through UI or persistence classes.
- Low Coupling: avoid unnecessary knowledge between units.
- High Cohesion: keep responsibilities that change together in the same unit.
- Polymorphism: use type-specific behavior instead of repeated conditionals when variation is stable.
- Protected Variations: wrap volatile dependencies behind stable interfaces.

## Avoid

- Turning controllers into god classes.
- Using polymorphism before the variation point is clear.
