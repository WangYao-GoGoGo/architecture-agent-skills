# Backend For Frontend

## Use When

- Different clients need different API shapes, workflows, or aggregation.
- A generic backend API forces UI clients to over-fetch, under-fetch, or own backend orchestration.

## Core Idea

A BFF provides a client-specific backend boundary. It adapts backend capabilities to one frontend or client family.

## Heuristics

- Use BFF for client-specific orchestration and shaping.
- Keep core business rules in backend services or domain modules.
- Avoid duplicating the same BFF logic across many clients.
- Define ownership between frontend team and backend services.

## Risks

- BFF accumulates business policy.
- Too many BFFs duplicate behavior.
- Backend contracts become unstable because only BFFs consume them.

