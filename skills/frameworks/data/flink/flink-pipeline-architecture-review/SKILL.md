---
name: flink-pipeline-architecture-review
description: Use when reviewing Apache Flink streaming pipeline architecture, event time, watermarks, state management, checkpoints, and exactly-once semantics.
---

# Flink Pipeline Architecture Review

## When To Use

- The main decision is about Flink stream processing topology, state management, checkpointing strategy, watermark configuration, or exactly-once semantics.
- Reviewing recovery behavior, backpressure handling, or late data strategy.

## Workflow

1. Identify the stream topology — sources, transformations, sinks, and keyed/partitioned streams.
2. Review event time vs processing time — watermark configuration and allowed lateness.
3. Check state management — state type, state backend, state TTL, and migration strategy.
4. Review checkpointing configuration — interval, exactly-once vs at-least-once, and unaligned checkpoints.
5. Check sink idempotency and transactional behavior.
6. Review backpressure, recovery, and late data handling.
7. Recommend the smallest structural change that improves reliability or performance.

## Output Format

```markdown
Flink pipeline review:
- Stream topology:
- Event time & watermarks:
- State management:
- Checkpointing:
- Sink behavior:
- Recovery & late data:
- Recommended change:
- Verification:
```
