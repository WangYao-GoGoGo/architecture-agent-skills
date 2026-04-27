---
name: airflow-pipeline-architecture-review
description: Use when reviewing Apache Airflow DAG architecture, task dependencies, operator design, scheduling, retries, and pipeline maintainability.
---

# Airflow Pipeline Architecture Review

## When To Use

- The main decision is about Airflow DAG structure, task decomposition, operator selection, scheduling strategy, or retry/idempotency design.
- Reviewing backfill behavior, SLA configuration, or alerting setup.

## Workflow

1. Identify the DAG structure — task dependencies, fan-in/fan-out, and sub-DAG usage.
2. Review task decomposition — are tasks atomic and independently retryable?
3. Check operator selection — PythonOperator vs KubernetesPodOperator vs sensors.
4. Review scheduling and backfill strategy — catchup, max_active_runs, and concurrency.
5. Check retry and idempotency design — retry delays, exponential backoff, and task idempotency.
6. Review SLA, alerting, and failure notification setup.
7. Recommend the smallest structural change that improves reliability or maintainability.

## Output Format

```markdown
Airflow pipeline review:
- DAG structure:
- Task decomposition:
- Operator selection:
- Scheduling & backfill:
- Retry & idempotency:
- SLA & alerting:
- Recommended change:
- Verification:
```
