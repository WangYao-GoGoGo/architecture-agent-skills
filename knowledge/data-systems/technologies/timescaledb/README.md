# TimescaleDB Knowledge

## Heuristics

- Model time-series data with hypertables partitioned by time and optionally space.
- Use continuous aggregates for real-time rollups instead of manual materialization.
- Set compression policies for old chunks to reduce storage.
- Use data retention policies to automatically drop old data.
- Choose chunk interval so each chunk fits in memory for fast queries.
- Watch chunk size and number of open chunks for write performance.
