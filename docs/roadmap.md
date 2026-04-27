# Roadmap

## Phase 1: Usable Core

- Fill `architecture-before-coding`.
- Fill `design-pattern-selector`.
- Fill `refactoring-planner`.
- Fill `dependency-boundary-review`.
- Add at least one application-code example and one data/domain architecture example.

## Phase 2: Paradigm Packs

- Object-oriented: SOLID, GRASP, GoF patterns, OO smells, refactoring moves.
- Procedural: module boundaries, header/interface discipline, data ownership, side-effect control.
- Functional: composition, immutability, pure core with imperative shell, error handling.
- Systems-oriented: resource ownership, concurrency boundaries, observability, failure isolation.
- Add examples that show when a paradigm-specific pattern is not needed.

## Phase 3: Language Packs

- Java: OO refactor, Spring architecture, package boundaries, dependency injection, transaction boundaries.
- Python: OO refactor, clean architecture, protocols, dependency injection without framework overuse.
- C: modular architecture, header/interface boundaries.
- SQL: schema refactor and query structure.
- TypeScript: frontend state boundaries, backend API shape, type-driven module design.

## Phase 4: Domain Packs

- Backend service boundaries and API architecture.
- Frontend component architecture and state ownership.
- Database modeling, indexing, migrations, transactions, and query architecture.
- Cache strategy, invalidation, Redis data structures, and consistency tradeoffs.
- Search architecture and indexing strategy.
- Data pipeline architecture and processing boundaries.

## Phase 5: Evaluation

- Add prompt-based evaluation cases.
- Add human review checklists.
- Add before/after examples for common refactoring scenarios.
- Define quality gates for maintainability, readability, testability, and overengineering.

Expansion should follow evidence from examples and evaluations, not just directory coverage.
