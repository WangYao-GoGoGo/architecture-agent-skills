# Core Skills

Core skills are the fundamental architecture skills that apply across all languages, frameworks, and domains. They form the foundation of the architecture agent workflow.

## Skills

| Skill | Purpose |
|---|---|
| [`architecture-before-coding`](architecture-before-coding/README.md) | Design responsibilities, boundaries, and patterns before implementing a non-trivial change. |
| [`refactoring-planner`](refactoring-planner/README.md) | Plan behavior-preserving refactors for existing code with unclear ownership, duplication, or coupling. |
| [`design-pattern-selector`](design-pattern-selector/README.md) | Decide whether a design pattern is justified and choose the smallest pattern that reduces real complexity. |
| [`dependency-boundary-review`](dependency-boundary-review/README.md) | Review whether dependencies between modules, services, and components point in maintainable directions. |
| [`architecture-decision-review`](architecture-decision-review/README.md) | Review or document architecture decisions, tradeoffs, alternatives, consequences, and verification. |
| [`anti-overengineering-review`](anti-overengineering-review/README.md) | Check whether a proposed architecture or abstraction is larger than the current problem needs. |
| [`new-project-scaffolding`](new-project-scaffolding/README.md) | Generate a complete project structure with clear boundaries, dependency direction, and testability from the start. |
| [`architecture-quality-review`](architecture-quality-review/README.md) | Evaluate whether generated or existing code meets architecture quality standards. |
| [`runtime-error-diagnosis`](runtime-error-diagnosis/README.md) | Diagnose code that fails at runtime — identify root cause and suggest the smallest safe fix. |
| [`test-generation-planner`](test-generation-planner/README.md) | Plan minimal tests for generated, modified, or refactored code. |
| [`behavior-preservation-validator`](behavior-preservation-validator/README.md) | Check whether refactored code preserves the original behavior. |
| [`debug-report-generator`](debug-report-generator/README.md) | Generate a human-readable debugging report after a bug fix or validation task. |

## Workflow Integration

The core skills work together in a natural workflow:

1. **New project?** → [`new-project-scaffolding`](new-project-scaffolding/README.md) to generate the initial structure.
2. **New feature?** → [`architecture-before-coding`](architecture-before-coding/README.md) to design before implementing.
3. **Need a pattern?** → [`design-pattern-selector`](design-pattern-selector/README.md) to pick the right one.
4. **Refactoring?** → [`refactoring-planner`](refactoring-planner/README.md) to plan incremental changes.
5. **Reviewing?** → [`dependency-boundary-review`](dependency-boundary-review/README.md) or [`architecture-decision-review`](architecture-decision-review/README.md) for targeted reviews.
6. **Too complex?** → [`anti-overengineering-review`](anti-overengineering-review/README.md) to simplify.
7. **Done?** → [`architecture-quality-review`](architecture-quality-review/README.md) to verify quality.

### Debugging and Validation Workflows

For runtime errors:

```text
User provides code or error log
        ↓
runtime-error-diagnosis
        ↓
minimal code fix
        ↓
test-generation-planner
        ↓
run or describe validation checks
        ↓
debug-report-generator
```

For refactoring:

```text
code-smell-detector
        ↓
refactoring-planner
        ↓
code modification
        ↓
behavior-preservation-validator
        ↓
architecture-quality-review
        ↓
anti-overengineering-review
        ↓
debug-report-generator
```

For new code generation:

```text
architecture-before-coding
        ↓
new-project-scaffolding
        ↓
code generation
        ↓
test-generation-planner
        ↓
architecture-quality-review
        ↓
debug-report-generator
```

## Knowledge Packs

Each core skill has a corresponding knowledge pack in [`knowledge/core/`](../../knowledge/core/README.md) with architecture-level heuristics.
