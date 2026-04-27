---
name: liquibase-changeset-review
description: Use when reviewing Liquibase changeset design, rollback strategy, checksums, environment conditions, and schema evolution workflow.
---

# Liquibase Changeset Review

## When To Use

- The main decision is about Liquibase changeset structure, rollback definitions, checksum management, or environment-specific logic.
- Reviewing generated changeset readability, deployment ordering, or application compatibility.

## Workflow

1. Identify the changeset structure — author, id, file path, and logical ordering.
2. Review rollback definitions — are rollback SQL or commands provided for each changeset?
3. Check checksum management — what happens when checksums change?
4. Review environment-specific logic — preconditions, contexts, and labels.
5. Check generated changeset readability — is the auto-generated SQL reviewed and cleaned up?
6. Review deployment ordering and application compatibility planning.
7. Recommend the smallest structural change that improves migration safety.

## Output Format

```markdown
Liquibase changeset review:
- Changeset structure:
- Rollback definitions:
- Checksum management:
- Environment logic:
- Changeset readability:
- Deployment compatibility:
- Recommended change:
- Verification:
```
