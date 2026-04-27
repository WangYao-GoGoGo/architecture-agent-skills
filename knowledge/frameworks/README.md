# Framework Knowledge

Framework cards describe common architecture issues introduced by frameworks, ORMs, migration tools, and generated clients.

This is a starter coverage map, not a claim that the framework list is complete. Add new framework cards when a framework changes lifecycle, boundaries, testing, deployment, state ownership, or integration behavior enough to affect architecture decisions.

- `core/`: framework boundary concepts.
- `orm/`: ORM boundary concepts.
- `migrations/`: migration tool concepts.
- `frontend/`: React, Vue, Angular, Svelte, Next.js, Nuxt, Remix, Solid.js, Qwik, Preact, Astro, Ember.js, Lit, Alpine.js, SvelteKit, Mithril, Backbone.js, Stencil.
- `backend/`: Spring Boot, Django, FastAPI, Flask, Express, NestJS, Rails, Laravel, ASP.NET Core, Gin, Ktor, Play, Actix-web, Axum, Phoenix, Fiber, Echo, Micronaut, Quarkus, Vert.x, Rocket, Tornado, Sanic, Falcon.
- `java/`: Hibernate, Spring Data JPA, MyBatis, jOOQ, Reactor.
- `python/`: SQLAlchemy, Alembic, Django ORM, Peewee, SQLModel.
- `typescript/`: Prisma, TypeORM, Sequelize, Mongoose, Drizzle ORM, Knex.js, MikroORM.
- `mobile/`: Android, iOS, Flutter, React Native, Kotlin Multiplatform, Ionic, Expo, Xamarin.
- `desktop/`: Electron, Tauri, Qt, .NET MAUI, JavaFX.
- `data/`: Spark, Flink, Airflow, Kafka, dbt, Prefect, Dagster, Beam, Kubeflow.
- `ai-agent/`: LangChain, LlamaIndex, Semantic Kernel, CrewAI, AutoGen, Haystack, Dify, Rasa, DSPy.
- `robotics/`: ROS 2, MoveIt, Gazebo, Webots, Isaac Sim.
- `database/`: Flyway, Liquibase, Atlas, Bytebase.

Use these cards when a skill in `skills/frameworks/` needs reusable concepts without copying them into every framework-specific skill.

External ecosystems such as WeChat, Pepper/NAOqi, industrial robot controllers, cloud accounts, IoT fleets, and chat/bot platforms belong in `knowledge/platform/` because the platform owns runtime rules, deployment channels, permissions, review processes, hardware contracts, or callback behavior.
