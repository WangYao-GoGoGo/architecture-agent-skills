# GCP Cloud Architecture

## Heuristics

- Separate application code, infrastructure as code (Deployment Manager/Terraform), platform-managed services, and operational policy.
- Treat IAM roles, VPC networks, projects, regions, Cloud Storage, Firestore, Bigtable, Cloud Functions, Pub/Sub, and Cloud Monitoring observability as architecture.
- Keep GCP SDK calls behind adapters when portability, testing, or policy enforcement matters.
- Make cost, quotas, cold starts, data residency, backup, and disaster recovery visible in decisions.
- Use Google Cloud Architecture Framework pillars: system design, operational excellence, security/privacy/compliance, reliability, cost optimization, performance optimization.

## Common Risks

- Business logic tied directly to GCP SDK without a reason.
- IAM permissions broader than the workflow needs.
- Infrastructure drift between environments.
- Reliability assumptions that ignore regional, quota, or managed-service failure modes.
- Cost not considered in architecture decisions (e.g., network egress, Cloud NAT, premium tiers).
