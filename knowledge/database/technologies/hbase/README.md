# HBase Knowledge

## Heuristics

- Design row keys from scan patterns and region distribution.
- Avoid hot regions with salting or better key prefixes when needed.
- Keep column families few and access-pattern driven.
- Review TTL, compaction, and wide-row risks.
- Plan row key changes as data migrations.

