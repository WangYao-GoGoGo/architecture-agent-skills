# Strangler Fig

## Use When

- Replacing or restructuring a large module, service, API, or subsystem incrementally.

## Core Idea

Route new or migrated behavior through a new structure while old behavior continues to run. Gradually move capabilities until the old structure can be removed.

## Agent Heuristics

- Define routing or adapter boundaries first.
- Migrate one capability at a time.
- Keep observability on old and new paths.
- Plan the final removal step before starting.

