# Distributed System Styles

Distributed system cards describe service shape, deployment/runtime shape, and cross-service operational concerns.

## Structure

- `service-styles/`: monolith, SOA, microservices, and distributed monolith.
- `deployment-styles/`: serverless and containerized services.
- `distributed-concerns/`: service boundaries, resilience, observability, and operational complexity.

## Selection Guide

| Pressure | Start With |
| --- | --- |
| How many deployable services should exist? | `service-styles/` |
| How should services run and scale? | `deployment-styles/` |
| How do services fail, communicate, and get observed? | `distributed-concerns/` |

## Fit Rule

Distributed architecture is not automatically better architecture. Use these cards only when deployment, ownership, scaling, failure, or team boundaries matter.
