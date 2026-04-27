# Roadmap

## Phase 1: Usable Core

- Fill `architecture-before-coding`.
- Fill `design-pattern-selector`.
- Fill `refactoring-planner`.
- Fill `dependency-boundary-review`.
- Fill `new-project-scaffolding` — generate architecture-correct project structure from scratch.
- Fill `architecture-quality-review` — verify code against architecture quality standards.
- Fill `knowledge/architecture/migration-strategies/` — strangler fig, branch by abstraction, parallel run, expand-contract, feature flags.
- Add at least one application-code example and one data/domain architecture example.

## Phase 2: Paradigm Packs

- Object-oriented: SOLID, GRASP, GoF patterns, OO smells, refactoring moves.
- Procedural: module boundaries, header/interface discipline, data ownership, side-effect control.
- Functional: composition, immutability, pure core with imperative shell, error handling.
- Systems-oriented: resource ownership, concurrency boundaries, observability, failure isolation.
- Add examples that show when a paradigm-specific pattern is not needed.

## Phase 3: Language Packs

- **Systems & Performance**: Go (concurrency, interfaces), Rust (ownership, traits), C++ (RAII, templates), C# (async, LINQ), Swift (protocols, value types), Kotlin (coroutines, sealed classes), Zig (comptime, allocators), Nim (macros, templates), Assembly (calling conventions, SIMD), Ada (strong typing, SPARK).
- **Scripting & Dynamic**: Ruby (metaprogramming, blocks), PHP (PSR, DI), TypeScript (type-driven design), JavaScript (modules, async), Python (clean architecture, protocols), Shell (idempotency, pipelines), Lua (metatables, coroutines), Perl (CPAN, Moose).
- **Web & Markup**: HTML (semantic markup, ARIA), CSS (Grid, Flexbox, custom properties).
- **Scientific & Numerical**: R (vectorized ops), Julia (multiple dispatch), MATLAB (matrix ops), Fortran (HPC arrays).
- **Functional & JVM**: Scala (type classes, implicits), Clojure (immutable data, macros), Haskell (type-level, monads), OCaml/F# (modules, variants), Elixir (OTP, GenServer), Erlang (processes, fault tolerance).
- **Database & Query**: SQL (schema, queries, indexing), GraphQL (schema, resolvers, DataLoader).
- **Hardware & Embedded**: VHDL/Verilog (FSM, FPGA, CDC).
- **Blockchain**: Solidity (smart contracts, gas optimization).
- **Mainframe & Legacy**: COBOL (program structure, file processing).
- **WebAssembly**: WASM (module design, memory, JS interop).
- **Java Ecosystem**: Java (OO refactor, Spring, DI, transactions).
- **Mobile & UI**: Dart (null safety, Flutter), Groovy (DSLs, Gradle).

## Phase 4: Domain Packs

- Backend service boundaries and API architecture.
- Frontend component architecture and state ownership.
- Database modeling, indexing, migrations, transactions, and query architecture.
- Cache strategy, invalidation, Redis data structures, and consistency tradeoffs.
- Search architecture and indexing strategy.
- Vector search, embeddings, chunking, metadata filters, and retrieval quality.
- Data pipeline architecture and processing boundaries.
- Operations architecture for scripts, configuration, deployment, rollback, and filesystem/process boundaries.

## Phase 5: Framework Packs

- **Generic**: Framework boundary review, ORM boundary review.
- **Backend (24)**: Spring Boot, Django, FastAPI, Flask, Express, NestJS, Rails, Laravel, ASP.NET Core, Gin, Ktor, Play, Actix-web, Axum, Phoenix, Fiber, Echo, Micronaut, Quarkus, Vert.x, Rocket, Tornado, Sanic, Falcon.
- **Frontend (18)**: React, Vue, Angular, Svelte, Next.js, Nuxt, Remix, Solid.js, Qwik, Preact, Astro, Ember.js, Lit, Alpine.js, SvelteKit, Mithril, Backbone.js, Stencil.
- **Mobile (8)**: Android, iOS, Flutter, React Native, Kotlin Multiplatform, Ionic, Expo, Xamarin.
- **Desktop (5)**: Electron, Tauri, Qt, .NET MAUI, JavaFX.
- **Data (9)**: Spark, Flink, Airflow, Kafka, dbt, Prefect, Dagster, Beam, Kubeflow.
- **AI Agent (9)**: LangChain, LlamaIndex, Semantic Kernel, CrewAI, AutoGen, Haystack, Dify, Rasa, DSPy.
- **Database Tools (4)**: Flyway, Liquibase, Atlas, Bytebase.
- **Java Ecosystem (7)**: Hibernate, MyBatis, Spring Data JPA, Spring MVC, Struts, jOOQ, Reactor.
- **Python ORM (5)**: SQLAlchemy, Alembic, Django ORM, Peewee, SQLModel.
- **TypeScript Data (7)**: Prisma, TypeORM, Sequelize, Mongoose, Drizzle ORM, Knex.js, MikroORM.
- **Robotics (5)**: ROS 2, MoveIt, Gazebo, Webots, Isaac Sim.

## Phase 6: Evaluation

- Add prompt-based evaluation cases.
- Add human review checklists.
- Add before/after examples for common refactoring scenarios.
- Define quality gates for maintainability, readability, testability, and overengineering.

Expansion should follow evidence from examples and evaluations, not just directory coverage.
