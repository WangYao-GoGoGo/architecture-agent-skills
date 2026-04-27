# Oracle Knowledge

## Heuristics

- Review execution plans with `DBMS_XPLAN` for critical queries.
- Use partitions, indexes, and materialized views deliberately for large tables.
- Treat PL/SQL packages as deployment units with clear interface boundaries.
- Watch undo, redo, and temporary tablespace usage for bulk operations.
- Use RAC only when availability requirements justify the complexity.
- Keep optimizer statistics up to date and review adaptive cursor sharing behavior.
