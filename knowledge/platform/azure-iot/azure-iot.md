# Azure IoT Architecture

## Heuristics

- Separate device code, gateway code, Azure IoT Hub ingestion, message routing, command handling, device management, and domain workflows.
- Treat device identity (SAS tokens, X.509 certificates, DPS), provisioning (Device Provisioning Service), OTA updates (Device Update for IoT Hub), telemetry schema, offline queues, and command acknowledgements as contracts.
- Keep hardware drivers and vendor SDKs behind explicit adapters.
- Design for intermittent connectivity, clock drift, message replay, and partial rollout.
- Use Azure IoT SDKs behind adapters for testability.

## Common Risks

- Cloud services assuming devices are always online.
- Remote commands without acknowledgement, timeout, or idempotency behavior.
- OTA update paths mixed with product workflow logic.
- Telemetry schemas changing without compatibility planning.
- IoT Hub message size, retention, and throttling limits not accounted for.

## Verification

- Device logic can be tested without real Azure IoT Hub connections.
- Offline queue and command acknowledgement behavior is explicitly designed.
- OTA update rollback and partial rollout scenarios are covered.
