# Service-Oriented Architecture

## Use When

- Multiple services coordinate business capabilities but do not require fine-grained independent teams or deployments for every capability.

## Core Idea

SOA organizes capabilities into services with explicit contracts. It often uses coarser-grained service boundaries than microservices.

## Heuristics

- Define service contracts around business capabilities.
- Keep shared schemas and enterprise contracts versioned.
- Make integration and ownership visible.
- Avoid turning the service bus or shared platform into hidden coupling.

## Risks

- Over-centralized orchestration.
- Shared canonical models that every team must change together.
- Network boundaries without ownership boundaries.

