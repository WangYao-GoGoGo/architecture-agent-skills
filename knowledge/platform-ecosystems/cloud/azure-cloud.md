# Azure Cloud Architecture

## Heuristics

- Separate application code, infrastructure as code (ARM/Bicep/Terraform), platform-managed services, and operational policy.
- Treat Azure RBAC, managed identities, virtual networks, resource groups, regions, storage accounts, Cosmos DB, Azure Functions, Service Bus, and Monitor observability as architecture.
- Keep Azure SDK calls behind adapters when portability, testing, or policy enforcement matters.
- Make cost, quotas, cold starts, data residency, backup, and disaster recovery visible in decisions.
- Use Microsoft Azure Well-Architected Framework pillars: reliability, security, cost optimization, operational excellence, performance efficiency.

## Common Risks

- Business logic tied directly to Azure SDK without a reason.
- RBAC permissions broader than the workflow needs.
- Infrastructure drift between environments.
- Reliability assumptions that ignore regional, quota, or managed-service failure modes.
- Cost not considered in architecture decisions (e.g., data egress, premium tiers, reserved capacity).
