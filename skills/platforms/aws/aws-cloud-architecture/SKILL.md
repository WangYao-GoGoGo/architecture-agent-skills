---
name: aws-cloud-architecture
description: Use when reviewing or designing AWS cloud architecture, including compute, storage, networking, IAM, managed services, serverless, and AWS Well-Architected Framework considerations.
---

# AWS Cloud Architecture

## Knowledge To Use

- `knowledge/platform-ecosystems/cloud/`
- `knowledge/platform/`
- `knowledge/api/`

## Workflow

1. Identify architecture components: compute (EC2, Lambda, ECS/EKS), storage (S3, EBS, RDS, DynamoDB), networking (VPC, CloudFront, API Gateway), IAM, and managed services.
2. Map AWS service contracts: service quotas, IAM policy boundaries, VPC/subnet topology, data transfer costs, availability zone design, and service limits.
3. Check whether application code, infrastructure definition, IAM policies, or deployment logic are mixed without clear separation of concerns.
4. Review operational concerns: cost optimization, security (IAM least privilege, encryption), reliability (multi-AZ, backup, DR), performance efficiency, and sustainability.
5. Recommend service boundaries, infrastructure-as-code structure, IAM policy design, and observability strategy.
6. Verify with AWS Well-Architected review, cost analysis, IAM policy simulation, and disaster recovery testing.

## Output Format

```markdown
AWS cloud architecture:
- Architecture components:
- Service coupling:
- Security/IAM concerns:
- Proposed boundaries:
- Verification:
```
