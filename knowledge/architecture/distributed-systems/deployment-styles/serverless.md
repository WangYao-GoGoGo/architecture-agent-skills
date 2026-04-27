# Serverless

## Project Fit

Serverless fits event-driven or bursty workloads where managed runtime operations are valuable and platform constraints are acceptable.

## Use When

- Workloads are event-driven, bursty, or operational simplicity matters more than long-running process control.
- Functions can be small and bounded by trigger, timeout, and permission scope.
- Managed services reduce operational burden.

## Avoid When

- Workflows require long-running processes, stable low latency, or deep runtime control.
- Local testing and tracing would become too hard for the team.
- Platform limits, cold starts, or vendor coupling are unacceptable.

## Core Idea

Serverless delegates runtime management to a platform. Architecture centers on functions, managed services, events, permissions, and deployment configuration.

## Fits Best With

- Event handlers, scheduled jobs, lightweight APIs, file processing, glue logic, and bursty workloads.

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

## Verification

- Timeouts, retries, permissions, and idempotency are explicit.
- Tracing connects function chains.
- Cost and latency are measured under realistic traffic.
