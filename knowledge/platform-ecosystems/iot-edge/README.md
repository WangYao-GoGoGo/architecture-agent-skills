# IoT and Edge Platform Ecosystem Knowledge

IoT and edge architecture depends on devices, gateways, unreliable networks, telemetry, firmware or app updates, local storage, remote commands, security, and fleet operations.

## Platform-Specific Cards

- `aws-iot.md`: AWS IoT Core, device identity, provisioning, OTA, MQTT topics, shadow state.
- `azure-iot.md`: Azure IoT Hub, DPS, device identity, OTA, message routing, command handling.
- `thingsboard-iot.md`: ThingsBoard, MQTT/CoAP/HTTP ingestion, rule engine, RPC, dashboards.

## Heuristics

- Separate device code, gateway code, cloud ingestion, command handling, fleet management, and domain workflows.
- Treat device identity, provisioning, OTA updates, telemetry schema, offline queues, and command acknowledgements as contracts.
- Keep hardware drivers and vendor SDKs behind explicit adapters.
- Design for intermittent connectivity, clock drift, replay, and partial rollout.

## Common Risks

- Cloud services assuming devices are always online.
- Remote commands without acknowledgement, timeout, or idempotency behavior.
- Firmware update paths mixed with product workflow logic.
- Telemetry schemas changing without compatibility planning.
