# AWS Cloud Architecture

## Heuristics

- Separate application code, infrastructure as code (CloudFormation/CDK/Terraform), platform-managed services, and operational policy.
- Treat IAM roles and policies, VPC/subnet design, security groups, regions/AZs, S3 buckets, DynamoDB tables, Lambda functions, SQS queues, and CloudWatch observability as architecture.
- Keep AWS SDK calls behind adapters when portability, testing, or policy enforcement matters.
- Make cost, quotas, cold starts, data residency, backup, and disaster recovery visible in decisions.
- Use AWS Well-Architected Framework pillars: operational excellence, security, reliability, performance efficiency, cost optimization, sustainability.

## Common Risks

- Business logic tied directly to one AWS SDK without a reason.
- IAM permissions broader than the workflow needs (least privilege violation).
- Infrastructure drift between environments.
- Reliability assumptions that ignore regional, quota, or managed-service failure modes.
- Cost not considered in architecture decisions (e.g., data transfer, NAT gateway, provisioned capacity).
