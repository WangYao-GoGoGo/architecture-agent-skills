# AWS IoT Architecture

## Heuristics

- Separate device code, gateway code, AWS IoT Core ingestion, rule processing, command handling, fleet management, and domain workflows.
- Treat device identity (X.509 certificates, IoT policies), provisioning (Fleet Provisioning), OTA updates (IoT Device Management), telemetry schema (MQTT topics, shadow state), offline queues, and command acknowledgements as contracts.
- Keep hardware drivers and vendor SDKs behind explicit adapters.
- Design for intermittent connectivity, clock drift, message replay, and partial rollout.
- Use AWS IoT Device SDKs behind adapters for testability.

## Common Risks

- Cloud services assuming devices are always online.
- Remote commands without acknowledgement, timeout, or idempotency behavior.
- OTA update paths mixed with product workflow logic.
- Telemetry schemas changing without compatibility planning.
- IoT policies and certificate management not designed for scale.

## Verification

- Device logic can be tested without real AWS IoT Core connections.
- Offline queue and command acknowledgement behavior is explicitly designed.
- OTA update rollback and partial rollout scenarios are covered.
