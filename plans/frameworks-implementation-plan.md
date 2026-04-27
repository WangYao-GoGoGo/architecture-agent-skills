# Frameworks Skills Implementation Plan

## 总体策略

每个框架技能目录需要创建：
1. `README.md` — 描述该框架的技能规划（参考现有 hibernate/README.md 格式）
2. 后续可选的 `SKILL.md`（本次先创建 README.md 占位）

## Phase 1: 补全 Java 框架

**目录**: `skills/frameworks/java/`

| 框架 | README 内容要点 |
|------|----------------|
| spring-boot | Auto-configuration, bean lifecycle, transaction boundaries, actuator, profiles |
| spring-mvc | Controller boundaries, view resolution, interceptor, exception handling |
| struts | Action mapping, form beans, interceptors, validation, tile layout |

同时更新 `skills/frameworks/java/README.md` 添加这三个框架的引用。

## Phase 2: 新建 backend/ 目录

**目录**: `skills/frameworks/backend/`

| 框架 | README 内容要点 |
|------|----------------|
| spring-boot | Auto-configuration, bean lifecycle, transaction boundaries, actuator, profiles |
| django | App structure, models/views/serializers, middleware, signals |
| fastapi | Dependency injection, async endpoints, Pydantic models, OpenAPI |
| flask | Blueprints, app factories, extensions, request lifecycle |
| express | Middleware pipeline, routing, error handling, async patterns |
| nestjs | Modules, providers, guards, interceptors, decorators |
| rails | MVC, ActiveRecord, concerns, service objects, callbacks |
| laravel | Service providers, facades, Eloquent, middleware, queues |
| aspnet-core | Middleware pipeline, DI, controllers, Razor Pages, EF Core |
| gin | Routing, middleware, binding/validation, grouping |

## Phase 3: 新建 frontend/ 目录

**目录**: `skills/frameworks/frontend/`

| 框架 | README 内容要点 |
|------|----------------|
| react | Component lifecycle, hooks, state management, effects, context |
| vue | Composition API, reactivity, components, router, Pinia/Vuex |
| angular | Modules, components, services, DI, RxJS, guards |
| svelte | Reactivity, stores, components, lifecycle, transitions |
| nextjs | Pages/router, SSR/SSG, API routes, middleware, app router |
| nuxt | Auto-import, modules, SSR/SSG, middleware, composables |

## Phase 4: 新建 mobile/ 目录

**目录**: `skills/frameworks/mobile/`

| 框架 | README 内容要点 |
|------|----------------|
| android | Activity/Fragment lifecycle, MVVM, Jetpack Compose, DI |
| ios | ViewController lifecycle, SwiftUI, MVC/MVVM, delegates |
| flutter | Widget tree, state management, BLoC/Provider, platform channels |
| react-native | Component lifecycle, bridge, native modules, navigation |
| kotlin-multiplatform | Shared module, expect/actual, platform-specific UI |
| ionic | WebView bridge, Capacitor/Cordova plugins, lazy loading |

## Phase 5: 新建 desktop/ 目录

**目录**: `skills/frameworks/desktop/`

| 框架 | README 内容要点 |
|------|----------------|
| electron | Main/renderer process, IPC, native APIs, packaging |
| tauri | Rust backend, web frontend, command system, security |

## Phase 6: 新建 data/ 目录

**目录**: `skills/frameworks/data/`

| 框架 | README 内容要点 |
|------|----------------|
| spark | RDD/DataFrame/Dataset, transformations, actions, partitioning |
| flink | Stream/batch processing, checkpointing, state, watermarks |
| airflow | DAG design, operators, task dependencies, scheduling |

## Phase 7: 新建 ai-agent/ 目录

**目录**: `skills/frameworks/ai-agent/`

| 框架 | README 内容要点 |
|------|----------------|
| langchain | Chains, agents, tools, memory, retrievers, callbacks |
| llamaindex | Indexing, retrieval, query engine, document processing |
| semantic-kernel | Plugins, planners, memory, connectors, skills |
| crewai | Agent roles, tasks, tools, process flow, collaboration |
| autogen | Multi-agent conversation, agent roles, tool registration |

## Phase 8: 新建 robotics/ 目录

**目录**: `skills/frameworks/robotics/`

| 框架 | README 内容要点 |
|------|----------------|
| ros2 | Nodes, topics, services, actions, lifecycle, launch |
| moveit | Motion planning, kinematics, collision checking, OMPL |
| gazebo | Simulation, plugins, sensors, URDF/SDF, physics |

## Phase 9: 更新顶层 README

更新 `skills/frameworks/README.md`，添加所有新目录的引用。
