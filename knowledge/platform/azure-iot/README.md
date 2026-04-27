# Azure IoT Platform Knowledge

## Use When

Reviewing or designing Azure IoT Hub integration, device management, or telemetry architecture.

## Heuristics

- Separate device code, gateway code, Azure IoT Hub ingestion, message routing, command handling, and device management.
- Treat device identity (SAS tokens, X.509 certificates, DPS), provisioning, OTA updates, telemetry schema, and offline queues as contracts.
- Keep hardware drivers and vendor SDKs behind explicit adapters.
- Design for intermittent connectivity, clock drift, message replay, and partial rollout.

## Common Risks

- Cloud services assuming devices are always online.
- Remote commands without acknowledgement, timeout, or idempotency behavior.
- IoT Hub message size, retention, and throttling limits not accounted for.
