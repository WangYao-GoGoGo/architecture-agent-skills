# ThingsBoard IoT Architecture

## Heuristics

- Separate device code, gateway code, ThingsBoard ingestion (MQTT, CoAP, HTTP), rule engine processing, command handling, device management, and domain workflows.
- Treat device identity (access tokens, X.509 certificates, basic MQTT credentials), provisioning, telemetry schema, attributes, RPC calls, and alarm definitions as contracts.
- Keep hardware drivers and vendor SDKs behind explicit adapters.
- Design for intermittent connectivity, clock drift, message replay, and ThingsBoard's specific rule engine and dashboard capabilities.
- Use ThingsBoard REST API and MQTT APIs behind adapters for testability.

## Common Risks

- Cloud services assuming devices are always online.
- Remote commands (RPC) without acknowledgement, timeout, or idempotency behavior.
- Rule engine logic mixed with device code.
- Telemetry and attribute schemas changing without compatibility planning.
- ThingsBoard's specific scalability and high-availability configuration not considered.

## Verification

- Device logic can be tested without real ThingsBoard connections.
- Offline queue and RPC acknowledgement behavior is explicitly designed.
- Rule engine logic is testable independently of device code.
