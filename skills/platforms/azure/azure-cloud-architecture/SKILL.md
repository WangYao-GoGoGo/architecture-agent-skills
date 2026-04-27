---
name: azure-cloud-architecture
description: Use when reviewing or designing Azure cloud architecture, including compute, storage, networking, identity, managed services, and Azure Well-Architected Framework considerations.
---

# Azure Cloud Architecture

## Knowledge To Use

- `knowledge/platform/cloud/`
- `knowledge/platform/`
- `knowledge/api/`

## Workflow

1. Identify architecture components: compute (VMs, App Service, AKS, Azure Functions), storage (Blob, SQL Database, Cosmos DB), networking (VNet, Front Door, API Management), identity (Entra ID), and managed services.
2. Map Azure service contracts: subscription limits, resource group topology, RBAC role definitions, VNet peering, data residency, and service quotas.
3. Check whether application code, infrastructure definition, RBAC policies, or deployment logic are mixed without clear separation of concerns.
4. Review operational concerns: cost management, security (Entra ID, managed identities, Key Vault), reliability (availability zones, backup, disaster recovery), and governance (Policy, Blueprints).
5. Recommend service boundaries, infrastructure-as-code structure, RBAC design, and observability strategy.
6. Verify with Azure Well-Architected review, cost analysis, RBAC testing, and disaster recovery drills.

## Output Format

```markdown
Azure cloud architecture:
- Architecture components:
- Service coupling:
- Security/identity concerns:
- Proposed boundaries:
- Verification:
```
