# Backend For Frontend

## Project Fit

BFF fits products where specific clients need tailored API shapes, aggregation, or workflows that should not live in generic backend services.

## Use When

- Different clients need different API shapes, workflows, or aggregation.
- A generic backend API forces UI clients to over-fetch, under-fetch, or own backend orchestration.
- Client teams need a boundary that reflects their user experience needs.

## Avoid When

- One API shape serves all clients well.
- The BFF would duplicate domain rules from backend services.
- Many BFFs would copy the same behavior without ownership.

## Core Idea

A BFF provides a client-specific backend boundary. It adapts backend capabilities to one frontend or client family.

## Fits Best With

- Mobile vs web clients, admin vs public UI, complex frontend aggregation, microservice backends.

## Heuristics

- Use BFF for client-specific orchestration and shaping.
- Keep core business rules in backend services or domain modules.
- Avoid duplicating the same BFF logic across many clients.
- Define ownership between frontend team and backend services.

## Risks

- BFF accumulates business policy.
- Too many BFFs duplicate behavior.
- Backend contracts become unstable because only BFFs consume them.

## Verification

- Client code becomes simpler.
- Domain rules remain in the proper backend owner.
- BFF response contracts are tested against client needs.
