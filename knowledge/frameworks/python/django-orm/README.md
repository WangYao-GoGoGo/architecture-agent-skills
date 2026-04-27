# Django ORM Knowledge

## Heuristics

- Keep models, managers, querysets, views, and serializers from absorbing every responsibility.
- Watch N+1 queries in serializers and templates.
- Keep transactions explicit around multi-write workflows.
- Review migrations for data and lock risks.

