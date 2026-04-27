# ThingsBoard IoT Platform Knowledge

## Use When

Reviewing or designing ThingsBoard IoT platform integration, rule engine, or telemetry architecture.

## Heuristics

- Separate device code, gateway code, ThingsBoard ingestion (MQTT, CoAP, HTTP), rule engine processing, command handling, and device management.
- Treat device identity (access tokens, X.509 certificates), provisioning, telemetry schema, attributes, RPC calls, and alarm definitions as contracts.
- Keep hardware drivers and vendor SDKs behind explicit adapters.
- Design for intermittent connectivity, clock drift, message replay, and ThingsBoard's specific rule engine capabilities.

## Common Risks

- Cloud services assuming devices are always online.
- Remote commands (RPC) without acknowledgement, timeout, or idempotency behavior.
- Rule engine logic mixed with device code.
