# Observability

## Project Fit

Use this card for any system where behavior crosses modules, services, jobs, queues, or infrastructure boundaries.

## Use When

- Reviewing logs, metrics, traces, audit events, health checks, or operational dashboards.
- A team cannot explain failures or latency from existing signals.

## Avoid When

- Do not add noisy metrics or logs that do not support decisions.

## Core Idea

Observability lets teams understand system behavior from the outside. It is part of architecture, not an afterthought.

## Heuristics

- Correlate requests, events, jobs, and retries.
- Log business-relevant state transitions without leaking secrets.
- Measure latency, error rate, saturation, freshness, and queue lag where relevant.
- Add health checks that reflect real readiness and liveness.

## Verification

- A failed user workflow can be traced across boundaries.
- Alerts map to actionable ownership.
- Dashboards reveal degradation before users report it.
