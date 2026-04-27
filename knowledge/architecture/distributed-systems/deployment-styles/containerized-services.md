# Containerized Services

## Project Fit

Containerized services fit applications that need repeatable packaging, deployment portability, and process-level control without managing raw machines directly.

## Use When

- Services need consistent runtime environments across dev, CI, and production.
- Scaling, rolling deploys, and resource limits matter.
- The team uses Kubernetes, Nomad, ECS, Docker Compose, or similar platforms.

## Avoid When

- A simpler platform or single process deployment is enough.
- Container orchestration would add more complexity than the product needs.
- Persistent state, networking, and observability are not understood.

## Core Idea

Containerization packages application processes with dependencies while orchestration manages scheduling, health, scaling, and rollout behavior.

## Heuristics

- Keep containers stateless unless state management is deliberate.
- Define health checks, resource limits, environment configuration, and shutdown behavior.
- Treat images, secrets, and deployment manifests as architecture artifacts.
- Keep database migrations and app rollout order explicit.

## Risks

- Containers hide but do not remove operational complexity.
- Missing graceful shutdown causes data loss or failed requests.
- Configuration drift between environments.

## Verification

- Health checks reflect real readiness.
- Rollback and rollout behavior are tested.
- Logs, metrics, and traces are available per service instance.
