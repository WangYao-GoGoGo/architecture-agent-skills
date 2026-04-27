# Kafka Knowledge

## Heuristics

- Separate topic design, partitioning strategy, consumer groups, producer configuration, and stream processing.
- Treat message schemas and compatibility as architecture contracts.
- Keep consumer offset management and rebalance handling explicit.
- Add monitoring for lag, throughput, and error rates.

## Common Risks

- Topics with too many or too few partitions.
- Schema evolution without backward compatibility.
- Consumer group rebalance causing processing delays.
