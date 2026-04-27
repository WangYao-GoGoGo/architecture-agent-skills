# API Gateway

## Use When

- Multiple backend services need a unified entry point for clients.
- Cross-cutting concerns such as auth, routing, rate limiting, or protocol translation belong at the edge.

## Core Idea

An API gateway centralizes edge routing and shared API concerns while backend services keep business ownership.

## Heuristics

- Keep business logic out of the gateway.
- Make routing, auth, rate limits, and observability explicit.
- Avoid gateway response composition becoming a hidden application layer.

## Risks

- Gateway becomes a bottleneck or god service.
- Backend ownership is hidden behind gateway transformations.
- Versioning and client compatibility become unclear.

