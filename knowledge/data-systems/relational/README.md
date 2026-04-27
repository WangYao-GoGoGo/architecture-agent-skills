# Relational Databases

## Use When

- Reviewing tables, constraints, joins, transactions, normalization, indexes, and migrations.

## Heuristics

- Model facts once unless denormalization has a clear owner and update path.
- Use primary keys, foreign keys, uniqueness, and check constraints to protect invariants.
- Design indexes from queries and write volume.
- Keep transaction boundaries aligned with business invariants.
- Plan schema changes for rolling deploy compatibility.

## Common Risks

- Accidental many-to-many fanout in joins.
- Constraints replaced by inconsistent application checks.
- Over-indexing write-heavy tables.
- Migrations that lock large tables during deploy.

