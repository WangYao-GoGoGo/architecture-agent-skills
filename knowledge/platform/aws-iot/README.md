# AWS IoT Platform Knowledge

## Use When

Reviewing or designing AWS IoT Core integration, device management, or telemetry architecture.

## Heuristics

- Separate device code, gateway code, AWS IoT Core ingestion, rule processing, command handling, and fleet management.
- Treat device identity (X.509 certificates, IoT policies), provisioning, OTA updates, telemetry schema, and offline queues as contracts.
- Keep hardware drivers and vendor SDKs behind explicit adapters.
- Design for intermittent connectivity, clock drift, message replay, and partial rollout.

## Common Risks

- Cloud services assuming devices are always online.
- Remote commands without acknowledgement, timeout, or idempotency behavior.
- Telemetry schemas changing without compatibility planning.
