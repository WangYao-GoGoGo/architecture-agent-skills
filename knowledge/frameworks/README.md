# Framework Knowledge

Framework cards describe common architecture issues introduced by frameworks, ORMs, migration tools, and generated clients.

This is a starter coverage map, not a claim that the framework list is complete. Add new framework cards when a framework changes lifecycle, boundaries, testing, deployment, state ownership, or integration behavior enough to affect architecture decisions.

- `core/`: framework boundary concepts.
- `orm/`: ORM boundary concepts.
- `migrations/`: migration tool concepts.
- `frontend/`: frontend framework concepts.
- `backend/`: Spring Boot, Django, FastAPI, Flask, Express, NestJS, Rails, Laravel, ASP.NET Core, Gin.
- `java/`: Hibernate, Spring Data JPA, MyBatis.
- `python/`: SQLAlchemy, Alembic, Django ORM.
- `typescript/`: Prisma, TypeORM, Sequelize, Mongoose.
- `mobile/`: Android, iOS, Flutter, React Native.
- `desktop/`: Electron, Tauri.
- `data/`: Spark, Flink, Airflow.
- `ai-agent/`: LangChain, LlamaIndex, Semantic Kernel, CrewAI, AutoGen.
- `robotics/`: ROS 2, MoveIt, Gazebo and robotics middleware.
- `database/`: Flyway, Liquibase.

Use these cards when a skill in `skills/frameworks/` needs reusable concepts without copying them into every framework-specific skill.

External ecosystems such as WeChat, Pepper/NAOqi, industrial robot controllers, cloud accounts, IoT fleets, and chat/bot platforms belong in `knowledge/platform-ecosystems/` because the platform owns runtime rules, deployment channels, permissions, review processes, hardware contracts, or callback behavior.
