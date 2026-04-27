# Alibaba Cloud Platform Knowledge

## Use When

Reviewing or designing Alibaba Cloud architecture, RAM, networking, or managed service integration.

## Heuristics

- Separate application code, infrastructure as code, platform-managed services, and operational policy.
- Treat RAM roles, VPC, security groups, regions/zones, and managed services as architecture.
- Keep Alibaba Cloud SDK calls behind adapters when portability or testing matters.
- Make cost, quotas, cold starts, data residency, and disaster recovery visible in decisions.

## Common Risks

- Business logic tied directly to Alibaba Cloud SDK without a reason.
- RAM permissions broader than the workflow needs.
- Infrastructure drift between environments.
