# Platform Ecosystem Knowledge

Platform ecosystem cards describe architecture issues created by external runtimes, vendor SDKs, account models, app review channels, callback contracts, hardware controllers, managed services, and permission systems.

Use this directory when the platform is more than a library. A framework usually runs inside the application. A platform ecosystem often owns part of the runtime, deployment path, user identity, permissions, hardware access, billing, review process, or event delivery.

- `wechat/`: mini programs, official accounts, WeChat Pay, cloud development, open platform integration.
- `robotics/`: Pepper/NAOqi, robot arms, industrial controllers, safety and hardware integration.
- `cloud/`: provider-managed runtimes, IAM, regions, managed services, IaC, cost and observability.
- `iot-edge/`: edge devices, gateways, OTA, offline behavior, telemetry, fleet management.
- `communication-platforms/`: chat, bot, collaboration, messaging, and webhook-driven platforms.

## Review Focus

- Which code is platform-owned, application-owned, and vendor-SDK-owned.
- Which contracts are stable local ports versus platform callbacks, events, permissions, or generated clients.
- Where platform constraints affect testing, deployment, observability, versioning, safety, cost, or compliance.
