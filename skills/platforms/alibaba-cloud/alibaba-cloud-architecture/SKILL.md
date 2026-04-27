---
name: alibaba-cloud-architecture
description: Use when reviewing or designing Alibaba Cloud architecture, including compute, storage, networking, RAM, managed services, and Alibaba Cloud best practice considerations.
---

# Alibaba Cloud Architecture

## Knowledge To Use

- `knowledge/platform/cloud/`
- `knowledge/platform/`
- `knowledge/api/`

## Workflow

1. Identify architecture components: compute (ECS, ACK, SAE, FC), storage (OSS, RDS, Table Store, NAS), networking (VPC, CDN, SLB), RAM (Resource Access Management), and managed services.
2. Map Alibaba Cloud service contracts: region/zone topology, RAM policy boundaries, VPC/subnet design, service quotas, and data residency requirements.
3. Check whether application code, infrastructure definition, RAM policies, or deployment logic are mixed without clear separation of concerns.
4. Review operational concerns: cost optimization, security (RAM, KMS, Security Center), reliability (multi-zone, backup, DR), and compliance (ISO, SOC, GDPR).
5. Recommend service boundaries, infrastructure-as-code structure, RAM policy design, and observability strategy.
6. Verify with Alibaba Cloud Well-Architected review, cost analysis, RAM policy simulation, and disaster recovery testing.

## Output Format

```markdown
Alibaba Cloud architecture:
- Architecture components:
- Service coupling:
- Security/RAM concerns:
- Proposed boundaries:
- Verification:
```
