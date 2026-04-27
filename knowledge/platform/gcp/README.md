# GCP Platform Knowledge

## Use When

Reviewing or designing GCP cloud architecture, IAM, networking, or managed service integration.

## Heuristics

- Separate application code, infrastructure as code, platform-managed services, and operational policy.
- Treat IAM roles, VPC networks, projects, regions, and managed services as architecture.
- Keep GCP SDK calls behind adapters when portability or testing matters.
- Make cost, quotas, cold starts, data residency, and disaster recovery visible in decisions.

## Common Risks

- Business logic tied directly to GCP SDK without a reason.
- IAM permissions broader than the workflow needs.
- Infrastructure drift between environments.
