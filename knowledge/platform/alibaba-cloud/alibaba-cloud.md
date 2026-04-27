# Alibaba Cloud Architecture

## Heuristics

- Separate application code, infrastructure as code (ROS/Terraform), platform-managed services, and operational policy.
- Treat RAM roles and policies, VPC, security groups, regions/zones, OSS, Table Store, Function Compute, Message Service (MNS), and CloudMonitor observability as architecture.
- Keep Alibaba Cloud SDK calls behind adapters when portability, testing, or policy enforcement matters.
- Make cost, quotas, cold starts, data residency, backup, and disaster recovery visible in decisions.
- Design for Alibaba Cloud's specific service naming, region availability, and compliance requirements (e.g., ICP filing).

## Common Risks

- Business logic tied directly to Alibaba Cloud SDK without a reason.
- RAM permissions broader than the workflow needs.
- Infrastructure drift between environments.
- Reliability assumptions that ignore regional, quota, or managed-service failure modes.
- Cost not considered in architecture decisions (e.g., data transfer, NAT, OSS storage classes).
