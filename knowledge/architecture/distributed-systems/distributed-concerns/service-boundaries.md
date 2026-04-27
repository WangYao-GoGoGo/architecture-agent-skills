# Service Boundaries

## Project Fit

Use this card whenever a system has multiple services or modules that might become services.

## Use When

- Deciding whether to split, merge, or redraw service boundaries.
- Reviewing ownership, data access, APIs, events, or team responsibility.

## Avoid When

- The problem is only code organization inside one module; use application styles first.

## Core Idea

Good service boundaries follow ownership and business capability. Network boundaries without ownership boundaries create cost without autonomy.

## Heuristics

- Identify who owns writes, data, APIs, and incidents.
- Prefer boundaries around business capabilities.
- Avoid splitting by controller/service/repository technical layers.
- Check whether release, scaling, and failure needs justify the boundary.

## Verification

- A service can evolve without many coordinated releases.
- Data ownership is clear.
- Contracts are versioned or compatibility-tested.
