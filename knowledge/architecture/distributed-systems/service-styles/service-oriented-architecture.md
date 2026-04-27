# Service-Oriented Architecture

## Project Fit

SOA fits organizations that need multiple coarse-grained services and explicit contracts, but not necessarily microservice-level independence for every capability.

## Use When

- Multiple services coordinate business capabilities but do not require fine-grained independent teams or deployments for every capability.
- Contracts and integration governance matter.
- Shared platform services or enterprise integration are part of the environment.

## Avoid When

- Services are split only by technical layer.
- A shared canonical model forces all teams to change together.
- Central orchestration hides ownership and slows delivery.

## Core Idea

SOA organizes capabilities into services with explicit contracts. It often uses coarser-grained service boundaries than microservices.

## Fits Best With

- Enterprise systems.
- Coarse-grained business capability services.
- Organizations with integration platforms, shared contracts, and governance needs.

## Heuristics

- Define service contracts around business capabilities.
- Keep shared schemas and enterprise contracts versioned.
- Make integration and ownership visible.
- Avoid turning the service bus or shared platform into hidden coupling.

## Risks

- Over-centralized orchestration.
- Shared canonical models that every team must change together.
- Network boundaries without ownership boundaries.

## Verification

- Each service has clear ownership and contract.
- Shared schemas are versioned and governed.
- Integration does not require synchronized releases for ordinary changes.
