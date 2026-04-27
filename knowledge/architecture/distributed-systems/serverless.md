# Serverless

## Use When

- Workloads are event-driven, bursty, or operational simplicity matters more than long-running process control.

## Core Idea

Serverless delegates runtime management to a platform. Architecture centers on functions, managed services, events, permissions, and deployment configuration.

## Heuristics

- Keep functions small around one trigger or use case.
- Make cold starts, timeouts, retries, and idempotency explicit.
- Treat permissions and configuration as architecture.
- Avoid scattering one workflow across many opaque functions without tracing.

## Risks

- Hidden coupling through events and managed services.
- Hard local testing.
- Cost and latency surprises.
- Weak observability across function chains.

