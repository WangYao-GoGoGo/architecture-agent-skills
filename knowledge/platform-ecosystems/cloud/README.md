# Cloud Platform Ecosystem Knowledge

Cloud platforms are architecture ecosystems because identity, regions, networking, deployment, managed services, billing, quotas, and observability are partly platform-owned.

## Platform-Specific Cards

- `aws-cloud.md`: AWS IAM, VPC, Lambda, S3, DynamoDB, SQS, and Well-Architected Framework.
- `azure-cloud.md`: Azure RBAC, VNet, Functions, Storage, Cosmos DB, Service Bus, and Well-Architected Framework.
- `gcp-cloud.md`: GCP IAM, VPC, Cloud Functions, Storage, Firestore, Pub/Sub, and Architecture Framework.
- `alibaba-cloud.md`: Alibaba Cloud RAM, VPC, Function Compute, OSS, Table Store, MNS, and compliance.

## Heuristics

- Separate application code, infrastructure definition, platform-managed services, and operational policy.
- Treat IAM, secrets, network boundaries, regions, queues, object storage, databases, serverless runtimes, and observability as architecture.
- Keep provider SDK calls behind adapters when portability, testing, or policy enforcement matters.
- Make cost, quotas, cold starts, data residency, backup, and disaster recovery visible in decisions.

## Common Risks

- Business logic tied directly to one provider SDK without a reason.
- IAM permissions broader than the workflow needs.
- Infrastructure drift between environments.
- Reliability assumptions that ignore regional, quota, or managed-service failure modes.
