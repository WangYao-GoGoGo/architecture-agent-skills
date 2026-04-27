# API Gateway

## Project Fit

API gateway fits systems with multiple backend services and shared edge concerns such as routing, auth, rate limits, and protocol translation.

## Use When

- Multiple backend services need a unified entry point for clients.
- Cross-cutting concerns such as auth, routing, rate limiting, or protocol translation belong at the edge.
- Client traffic needs consistent observability and policy enforcement.

## Avoid When

- The gateway would contain business logic or complex response composition.
- There is only one backend and no shared edge concerns.
- Gateway changes would become a bottleneck for all teams.

## Core Idea

An API gateway centralizes edge routing and shared API concerns while backend services keep business ownership.

## Fits Best With

- Microservices, SOA, public APIs, multi-client systems, edge policy enforcement.

## Heuristics

- Keep business logic out of the gateway.
- Make routing, auth, rate limits, and observability explicit.
- Avoid gateway response composition becoming a hidden application layer.

## Risks

- Gateway becomes a bottleneck or god service.
- Backend ownership is hidden behind gateway transformations.
- Versioning and client compatibility become unclear.

## Verification

- Gateway rules are observable and testable.
- Business logic remains owned by backend services or BFFs.
- Gateway failure and rate-limit behavior are defined.
