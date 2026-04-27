# Project Taxonomy

This repository organizes architecture guidance by the kind of decision an agent needs to make.

## Core Skills

Cross-cutting workflows that apply across languages and domains.

Examples:

- architecture before coding
- refactoring planning
- dependency boundary review
- architecture decision review
- anti-overengineering review

Use `skills/core/` when the workflow is not specific to one language, paradigm, framework, or domain.

## Paradigm Skills

Guidance based on programming model.

Examples:

- object-oriented design
- procedural modular design
- functional composition
- systems boundary design

Use `skills/paradigms/` when the main question is how code should be structured according to a programming paradigm.

## Language Skills

Guidance based on language idioms and constraints.

Examples (40+ languages across categories):

**Systems & Performance**: Go, Rust, C, C++, C#, Swift, Kotlin, Zig, Nim, Assembly, Ada
**Scripting & Dynamic**: Ruby, PHP, JavaScript, TypeScript, Python, Shell, Lua, Perl
**Web & Markup**: HTML, CSS
**Scientific & Numerical**: R, Julia, MATLAB, Fortran
**Functional & JVM**: Scala, Clojure, Haskell, OCaml/F#, Elixir, Erlang
**Database & Query**: SQL, GraphQL
**Hardware & Embedded**: VHDL/Verilog
**Blockchain**: Solidity
**Mainframe & Legacy**: COBOL
**WebAssembly**: WASM
**Java Ecosystem**: Java
**Mobile & UI**: Dart, Groovy

Use `skills/languages/` when the answer depends on language-specific mechanics or idioms.

## Domain Skills

Guidance based on product or technical domain.

Examples:

- backend service boundaries
- frontend component and state ownership
- database modeling and indexing
- cache strategy and invalidation
- search indexing
- data pipeline architecture
- operations and shell automation

Use `skills/domains/` when the decision is about the architecture of a technical area rather than a language.

## Framework Skills

Guidance based on a specific framework, library ecosystem, middleware, or runtime framework.

Examples (80+ frameworks across 12 categories):

**Backend**: Spring Boot, Django, FastAPI, Flask, Express, NestJS, Rails, Laravel, ASP.NET Core, Gin, Ktor, Play, Actix-web, Axum, Phoenix, Fiber, Echo, Micronaut, Quarkus, Vert.x, Rocket, Tornado, Sanic, Falcon
**Frontend**: React, Vue, Angular, Svelte, Next.js, Nuxt, Remix, Solid.js, Qwik, Preact, Astro, Ember.js, Lit, Alpine.js, SvelteKit, Mithril, Backbone.js, Stencil
**Mobile**: Android, iOS, Flutter, React Native, Kotlin Multiplatform, Ionic, Expo, Xamarin
**Desktop**: Electron, Tauri, Qt, .NET MAUI, JavaFX
**Data**: Spark, Flink, Airflow, Kafka, dbt, Prefect, Dagster, Beam, Kubeflow
**AI Agent**: LangChain, LlamaIndex, Semantic Kernel, CrewAI, AutoGen, Haystack, Dify, Rasa, DSPy
**Database Tools**: Flyway, Liquibase, Atlas, Bytebase
**Java Ecosystem**: Hibernate, MyBatis, Spring Data JPA, Spring MVC, Struts, jOOQ, Reactor
**Python ORM**: SQLAlchemy, Alembic, Django ORM, Peewee, SQLModel
**TypeScript Data**: Prisma, TypeORM, Sequelize, Mongoose, Drizzle ORM, Knex.js, MikroORM
**Robotics**: ROS 2, MoveIt, Gazebo, Webots, Isaac Sim

Use `skills/frameworks/` when the guidance depends on framework behavior, lifecycle, conventions, or APIs.

## Platform Skills

Guidance based on external platform ecosystems where the platform owns runtime constraints, permissions, deployment, callbacks, managed services, account rules, hardware behavior, or review processes.

Examples:

- WeChat mini program and official account architecture
- WeChat Pay callback and reconciliation boundaries
- Alipay mini program and payment integration
- LINE bot and Messaging API architecture
- Facebook/Meta platform (Login, Graph API, Messenger bot)
- Slack, Discord, Telegram, Feishu, DingTalk, WhatsApp Business app architecture
- Stripe and PayPal payment integration
- AWS, Azure, GCP, Alibaba Cloud service boundaries
- Pepper/NAOqi robot application structure
- robot arm and industrial controller integration
- DJI drone and ArduPilot/PX4 UAV platform integration
- AWS IoT, Azure IoT, ThingsBoard device fleet architecture
- Steam, PlayStation, Xbox, Nintendo, Epic Games platform integration
- Twitter/X, TikTok, Instagram, YouTube social media API integration
- chat and bot platform event handling

Use `skills/platforms/` when the decision depends on vendor ecosystem constraints more than a language or framework.

If a technology can be replaced like a library or framework inside the application, start in `frameworks/`. If the technology controls identity, permissions, deployment, callbacks, review rules, hardware state, billing, or managed runtime behavior outside the application, start in `platforms/` and `knowledge/platform-ecosystems/`.

## Knowledge Cards

Reusable concepts that skills can reference.

Examples:

- principles
- design patterns
- architecture patterns
- code smells
- schema smells
- refactoring moves
- language idioms
- framework boundaries
- Linux and operational architecture

Use `knowledge/` for durable concepts. Use `skills/` for executable agent workflows.

## Knowledge Layers

Use `knowledge/` as the shared concept library behind skills:

- `knowledge/principles/`: reusable design principles.
- `knowledge/paradigms/`: programming model concepts.
- `knowledge/languages/`: 40+ language-specific architecture idioms.
- `knowledge/application-areas/`: backend, frontend, pipeline, and operations workload concepts.
- `knowledge/data-systems/`: 30+ relational, non-relational, cache, search, vector, and data architecture concepts.
- `knowledge/frameworks/`: 80+ framework, ORM, migration, and generated-client concepts across 12 categories.
- `knowledge/platform-ecosystems/`: external runtimes, vendor SDKs, platform callbacks, cloud, IoT, robotics, WeChat, communication, payment, gaming, social media, drone, and bot ecosystems.
- `knowledge/platform/`: Linux, shell, process, filesystem, configuration, and deployment concerns.
- `knowledge/methodologies/`: named learning systems, curricula, and source-oriented maps.

For alignment rules, see `docs/knowledge-skill-map.md`.

## Placement Rule

If a contribution could fit multiple places, choose the narrowest useful home:

1. Platform-ecosystem-specific
2. Framework-specific
3. Language-specific
4. Domain-specific
5. Paradigm-specific
6. Core

Core should stay small. It is the shared operating system, not a dumping ground.
