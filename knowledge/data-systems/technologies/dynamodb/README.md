# DynamoDB Knowledge

## Heuristics

- Design tables around access patterns; one table per workload is common.
- Choose partition keys that distribute traffic evenly; avoid hot partitions.
- Use sort keys for range queries, time ordering, and composite sort patterns.
- Use global secondary indexes (GSIs) sparingly; each GSI consumes write capacity.
- Use local secondary indexes (LSIs) only when strong consistency is required.
- Plan read/write capacity mode: on-demand for variable traffic, provisioned for predictable.
- Use DynamoDB Streams for change data capture and event-driven architectures.
