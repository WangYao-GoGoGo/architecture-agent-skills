# Platform Ecosystem Knowledge

Platform ecosystems are external runtimes, vendor SDKs, app stores, webhook platforms, bot platforms, and hardware controllers where the platform owns identity, permissions, events, delivery, and some operational constraints.

## Platform Categories

- **Social & Communication**: `communication-platforms/` — WeChat, Alipay, LINE, Facebook, Slack, Discord, Telegram, Feishu, DingTalk, WhatsApp Business
- **Payment & Commerce**: `payment/` — Stripe, PayPal (Alipay Pay and WeChat Pay covered under communication-platforms/ and wechat/)
- **Cloud**: `cloud/` — AWS, Azure, GCP, Alibaba Cloud
- **Robotics & Hardware**: `robotics/` — industrial robotics, robot arm control, Pepper/NAOqi
- **Drone & UAV**: `drone/` — DJI, ArduPilot/PX4
- **IoT & Edge**: `iot-edge/` — AWS IoT, Azure IoT, ThingsBoard
- **Gaming**: `gaming/` — Steam, PlayStation, Xbox, Nintendo, Epic Games
- **Social Media**: `social-media/` — Twitter/X, TikTok, Instagram, YouTube
- **WeChat**: `wechat/` — mini program, official account, WeChat Pay

## Review Focus

- Treat platform SDKs, APIs, webhooks, events, and rate limits as platform contracts.
- Keep platform-specific adapters, authentication, and data formats at the integration edge.
- Separate domain workflow from platform integration logic.
- Design for platform outages, rate limits, API versioning, and permission changes.
- Make platform-specific constraints (review process, package size, certification) visible in architecture decisions.
