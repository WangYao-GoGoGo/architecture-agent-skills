# Migration Strategies

Strategies for incrementally migrating existing code to a better architecture without losing business value.

## Use When

- Replacing or restructuring a large module, service, API, or subsystem.
- Moving from one architecture style to another (e.g., monolith → microservices, layered → hexagonal).
- Upgrading a framework or library that requires broad changes.
- Introducing new patterns into legacy code incrementally.

## Strategy Selection Guide

| Situation | Recommended Strategy |
|---|---|
| Can route traffic between old and new | Strangler Fig |
| Need to change interface gradually | Branch By Abstraction |
| Must keep both versions running | Parallel Run |
| Small, safe extraction | Extract Module/Class |
| Database schema change needed | Expand-Contract |
| Feature toggle needed | Feature Flag |
| Risk is very high | Toggle + Parallel Run |

## Strategy Cards

### Strangler Fig

Route new or migrated behavior through a new structure while old behavior continues to run. Gradually move capabilities until the old structure can be removed.

**Use When**: Replacing a large module, service, API, or subsystem incrementally.

**Heuristics**:
- Define routing or adapter boundaries first.
- Migrate one capability at a time.
- Keep observability on old and new paths.
- Plan the final removal step before starting.
- Do not start without a clear decommission plan for the old path.

**Risks**:
- Routing logic becomes complex if too many capabilities are migrated simultaneously.
- Old and new paths may diverge behaviorally if not monitored.
- Teams may never complete the migration if removal is not enforced.

### Branch By Abstraction

Introduce an abstraction layer that both old and new implementations satisfy. Migrate callers one by one, then remove the old implementation.

**Use When**: Changing a core interface or API that many callers depend on.

**Heuristics**:
- Define the abstraction based on what callers need, not what the implementation provides.
- Keep the abstraction stable during migration.
- Migrate callers in small batches.
- Remove the old implementation only after all callers are migrated.

**Risks**:
- The abstraction may become a leaky or overly generic interface.
- Two implementations must be maintained during the migration period.
- Callers may depend on old behavior that the new implementation does not support.

### Parallel Run

Run old and new implementations simultaneously, compare outputs, and switch when confidence is high.

**Use When**: Risk of behavioral differences is high (e.g., financial calculations, critical business rules).

**Heuristics**:
- Define comparison criteria: exact match, tolerance, or statistical equivalence.
- Log or alert on mismatches without blocking production.
- Run parallel long enough to cover edge cases and boundary conditions.
- Plan the switch-over window and rollback procedure.

**Risks**:
- Running two systems doubles operational cost.
- Mismatches may be noisy or hard to interpret.
- Teams may delay the switch-over indefinitely.

### Expand-Contract (aka Sync-Point)

Add new schema or API elements alongside existing ones, migrate consumers, then remove the old elements.

**Use When**: Database schema or API contract changes are required.

**Heuristics**:
- **Expand**: Add new columns, endpoints, or fields without removing old ones.
- **Migrate**: Update consumers to use the new elements.
- **Contract**: Remove old elements after all consumers are migrated.
- Keep the expand and contract phases separate in time.

**Risks**:
- Schema grows temporarily, which may affect performance.
- Old and new data must be kept consistent during migration.
- Orphaned old columns or endpoints may accumulate if not cleaned up.

### Feature Flag

Wrap new behavior behind a configuration flag that can be toggled at runtime.

**Use When**: Deploying incomplete or experimental features to production safely.

**Heuristics**:
- Keep flags short-lived; remove them after the feature stabilizes.
- Use a flag management system, not environment variables for complex toggles.
- Test both flag states in CI.
- Avoid nested flags that create combinatorial complexity.

**Risks**:
- Flag debt accumulates if flags are not removed.
- Testing all flag combinations becomes expensive.
- Flag logic clutters the codebase.

## Related Knowledge

- [`knowledge/refactoring/strangler-fig.md`](../../refactoring/strangler-fig.md) — detailed strangler fig refactoring technique.
- [`knowledge/architecture/decision-governance/`](../decision-governance/README.md) — for documenting migration decisions.
- [`knowledge/architecture/integration-patterns/`](../integration-patterns/README.md) — for routing and adapter patterns.
- [`skills/core/refactoring-planner/`](../../skills/core/refactoring-planner/README.md) — for planning incremental refactoring steps.
