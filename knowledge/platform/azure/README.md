# Azure Platform Knowledge

## Use When

Reviewing or designing Azure cloud architecture, RBAC, networking, or managed service integration.

## Heuristics

- Separate application code, infrastructure as code, platform-managed services, and operational policy.
- Treat Azure RBAC, managed identities, virtual networks, resource groups, regions, and managed services as architecture.
- Keep Azure SDK calls behind adapters when portability or testing matters.
- Make cost, quotas, cold starts, data residency, and disaster recovery visible in decisions.

## Common Risks

- Business logic tied directly to Azure SDK without a reason.
- RBAC permissions broader than the workflow needs.
- Infrastructure drift between environments.
