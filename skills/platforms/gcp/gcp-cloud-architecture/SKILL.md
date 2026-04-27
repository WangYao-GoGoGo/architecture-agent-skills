---
name: gcp-cloud-architecture
description: Use when reviewing or designing Google Cloud architecture, including compute, storage, networking, IAM, managed services, and GCP best practice considerations.
---

# Google Cloud Architecture

## Knowledge To Use

- `knowledge/platform-ecosystems/cloud/`
- `knowledge/platform/`
- `knowledge/api/`

## Workflow

1. Identify architecture components: compute (GCE, GKE, Cloud Run, Cloud Functions), storage (Cloud Storage, Cloud SQL, Firestore, Bigtable), networking (VPC, Cloud CDN, Load Balancing), IAM, and managed services.
2. Map GCP service contracts: project quotas, VPC topology, IAM roles, service accounts, data residency, and service limits.
3. Check whether application code, infrastructure definition, IAM policies, or deployment logic are mixed without clear separation of concerns.
4. Review operational concerns: cost management, security (IAM, Cloud KMS, Secret Manager), reliability (multi-region, backup, disaster recovery), and organization policy governance.
5. Recommend service boundaries, infrastructure-as-code structure, IAM design, and observability strategy.
6. Verify with GCP Well-Architected review, cost analysis, IAM policy tester, and disaster recovery testing.

## Output Format

```markdown
Google Cloud architecture:
- Architecture components:
- Service coupling:
- Security/IAM concerns:
- Proposed boundaries:
- Verification:
```
