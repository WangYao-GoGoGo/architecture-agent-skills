# Knowledge To Skill Map

This map keeps `knowledge/` and `skills/` aligned.

## Core Skills

Core skills should load only the knowledge needed for the task:

- `architecture-before-coding`: `principles/`, `architecture/application-styles/`, `architecture/integration-patterns/`, `patterns/`, `smells/`
- `refactoring-planner`: `refactoring/`, `smells/`, `principles/`
- `dependency-boundary-review`: `principles/dependency-inversion.md`, `principles/separation-of-concerns.md`, `frameworks/core/framework-boundaries.md`
- `anti-overengineering-review`: `principles/`, `smells/`, `patterns/`
- `architecture-decision-review`: `architecture/`, especially `architecture/decision-governance/`, plus `data-systems/`, `api/`, `frameworks/`, `platform-ecosystems/` as needed

## Paradigm Skills

- `skills/paradigms/object-oriented/`: `knowledge/paradigms/object-oriented/`, `principles/solid.md`, `principles/grasp.md`, `patterns/`
- `skills/paradigms/procedural/`: `knowledge/paradigms/procedural/`, `knowledge/languages/c/`, `refactoring/`
- `skills/paradigms/functional/`: `knowledge/paradigms/functional/`
- `skills/paradigms/systems/`: `knowledge/paradigms/systems-oriented/`, `knowledge/platform/`

## Language Skills

Each language skill pairs with its corresponding knowledge card:

**Systems & Performance:**
- Go: `knowledge/languages/go/`, plus concurrency and systems cards.
- Rust: `knowledge/languages/rust/`, plus ownership and systems cards.
- C: `knowledge/languages/c/`, plus procedural and systems-oriented cards.
- C++: `knowledge/languages/cpp/`, plus OO and template cards.
- C#: `knowledge/languages/csharp/`, plus .NET and async cards.
- Swift: `knowledge/languages/swift/`, plus iOS and protocol cards.
- Kotlin: `knowledge/languages/kotlin/`, plus JVM and coroutine cards.
- Zig: `knowledge/languages/zig/`, plus systems cards.
- Nim: `knowledge/languages/nim/`, plus systems cards.
- Assembly: `knowledge/languages/assembly/`, plus low-level and hardware cards.
- Ada: `knowledge/languages/ada/`, plus safety-critical and real-time cards.

**Scripting & Dynamic:**
- Ruby: `knowledge/languages/ruby/`, plus Rails and metaprogramming cards.
- PHP: `knowledge/languages/php/`, plus Laravel/Symfony cards.
- JavaScript: `knowledge/languages/javascript/`, plus frontend, API, and framework cards.
- TypeScript: `knowledge/languages/typescript/`, plus frontend, API, and framework cards.
- Python: `knowledge/languages/python/`, plus clean architecture, ORM, and framework cards.
- Shell: `knowledge/languages/shell/`, plus operations cards.
- Lua: `knowledge/languages/lua/`, plus embedded and game cards.
- Perl: `knowledge/languages/perl/`, plus text processing and CPAN cards.

**Web & Markup:**
- HTML: `knowledge/languages/html/`, plus accessibility and SEO cards.
- CSS: `knowledge/languages/css/`, plus responsive and layout cards.

**Scientific & Numerical:**
- R: `knowledge/languages/r/`, plus statistics and data science cards.
- Julia: `knowledge/languages/julia/`, plus scientific computing cards.
- MATLAB: `knowledge/languages/matlab/`, plus numerical computing cards.
- Fortran: `knowledge/languages/fortran/`, plus HPC cards.

**Functional & JVM:**
- Scala: `knowledge/languages/scala/`, plus functional and JVM cards.
- Clojure: `knowledge/languages/clojure/`, plus functional and JVM cards.
- Haskell: `knowledge/languages/haskell/`, plus functional and type-level cards.
- OCaml/F#: `knowledge/languages/ocaml/`, plus functional and .NET cards.
- Elixir: `knowledge/languages/elixir/`, plus OTP and Phoenix cards.
- Erlang: `knowledge/languages/erlang/`, plus OTP and distributed systems cards.

**Database & Query:**
- SQL: `knowledge/languages/sql/`, plus data-system cards.
- GraphQL: `knowledge/languages/graphql/`, plus API design cards.

**Hardware & Embedded:**
- VHDL/Verilog: `knowledge/languages/vhdl/`, plus FPGA and digital design cards.

**Blockchain:**
- Solidity: `knowledge/languages/solidity/`, plus Ethereum and smart contract cards.

**Mainframe & Legacy:**
- COBOL: `knowledge/languages/cobol/`, plus mainframe cards.

**WebAssembly:**
- WASM: `knowledge/languages/wasm/`, plus browser and performance cards.

**Java Ecosystem:**
- Java: `knowledge/languages/java/`, plus OO, framework, and data-system cards.

**Mobile & UI:**
- Dart: `knowledge/languages/dart/`, plus Flutter cards.
- Groovy: `knowledge/languages/groovy/`, plus Gradle and Grails cards.

## Domain Skills

- Backend: `knowledge/application-areas/backend/`, `knowledge/api/`, `knowledge/data-systems/`
- Frontend: `knowledge/application-areas/frontend/`, `knowledge/languages/typescript/`, `knowledge/languages/javascript/`, `knowledge/frameworks/frontend/frontend-frameworks.md`
- Data systems: `knowledge/data-systems/`, plus technology-specific skill instructions.
- Vector search: `knowledge/data-systems/vector/`, `knowledge/data-systems/search/`, `knowledge/data-systems/core/access-patterns.md`
- Data pipeline: `knowledge/application-areas/data-pipeline/`, `knowledge/data-systems/core/consistency.md`, `knowledge/api/contract-design.md`
- Operations and shell automation: `knowledge/application-areas/operations/`, `knowledge/platform/`, `knowledge/languages/shell/`

## Framework Skills

- **Framework boundary review**: `knowledge/frameworks/core/framework-boundaries.md`
- **ORM boundary review**: `knowledge/frameworks/orm/orm-boundaries.md`, `knowledge/data-systems/`
- **Backend frameworks**: `knowledge/frameworks/backend/` (Spring Boot, Django, FastAPI, Flask, Express, NestJS, Rails, Laravel, ASP.NET Core, Gin, Ktor, Play, Actix-web, Axum, Phoenix, Fiber, Echo, Micronaut, Quarkus, Vert.x, Rocket, Tornado, Sanic, Falcon)
- **Frontend frameworks**: `knowledge/frameworks/frontend/frontend-frameworks.md`, `knowledge/frameworks/frontend/` (React, Vue, Angular, Svelte, Next.js, Nuxt, Remix, Solid.js, Qwik, Preact, Astro, Ember.js, Lit, Alpine.js, SvelteKit, Mithril, Backbone.js, Stencil)
- **Mobile frameworks**: `knowledge/frameworks/mobile/` (Android, iOS, Flutter, React Native, Kotlin Multiplatform, Ionic, Expo, Xamarin)
- **Desktop frameworks**: `knowledge/frameworks/desktop/` (Electron, Tauri, Qt, .NET MAUI, JavaFX)
- **Data frameworks**: `knowledge/frameworks/data/` (Spark, Flink, Airflow, Kafka, dbt, Prefect, Dagster, Beam, Kubeflow)
- **AI Agent frameworks**: `knowledge/frameworks/ai-agent/` (LangChain, LlamaIndex, Semantic Kernel, CrewAI, AutoGen, Haystack, Dify, Rasa, DSPy)
- **Database tools**: `knowledge/frameworks/database/` (Flyway, Liquibase, Atlas, Bytebase)
- **Java ecosystem**: `knowledge/frameworks/java/` (Hibernate, MyBatis, Spring Data JPA, Spring MVC, Struts, jOOQ, Reactor)
- **Python ORM**: `knowledge/frameworks/python/` (SQLAlchemy, Alembic, Django ORM, Peewee, SQLModel)
- **TypeScript data**: `knowledge/frameworks/typescript/` (Prisma, TypeORM, Sequelize, Mongoose, Drizzle ORM, Knex.js, MikroORM)
- **Robotics frameworks**: `knowledge/frameworks/robotics/` (ROS 2, MoveIt, Gazebo, Webots, Isaac Sim), plus `knowledge/platform-ecosystems/robotics/` when hardware or vendor runtime constraints matter.
- **Migration tools**: `knowledge/frameworks/migrations/migration-tools.md`, `knowledge/data-systems/core/migrations.md`

## Platform Skills

- Platform ecosystem review: `knowledge/platform-ecosystems/`, `knowledge/api/`, `knowledge/frameworks/core/framework-boundaries.md`, `knowledge/platform/`
- WeChat mini program architecture: `knowledge/platform-ecosystems/wechat/`, `knowledge/languages/javascript/`, `knowledge/languages/typescript/`, `knowledge/api/`
- WeChat Pay integration: `knowledge/platform-ecosystems/wechat/`, `knowledge/api/`, `knowledge/platform/`
- Alipay mini program architecture: `knowledge/platform-ecosystems/communication-platforms/`, `knowledge/languages/javascript/`, `knowledge/languages/typescript/`, `knowledge/api/`
- Alipay payment integration: `knowledge/platform-ecosystems/payment/`, `knowledge/api/`, `knowledge/platform/`
- LINE bot architecture: `knowledge/platform-ecosystems/communication-platforms/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- Facebook/Meta platform architecture: `knowledge/platform-ecosystems/communication-platforms/`, `knowledge/languages/javascript/`, `knowledge/api/`
- Slack app architecture: `knowledge/platform-ecosystems/communication-platforms/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- Discord bot architecture: `knowledge/platform-ecosystems/communication-platforms/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- Telegram bot architecture: `knowledge/platform-ecosystems/communication-platforms/`, `knowledge/languages/python/`, `knowledge/languages/javascript/`, `knowledge/api/`
- Feishu/Lark app architecture: `knowledge/platform-ecosystems/communication-platforms/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- DingTalk app architecture: `knowledge/platform-ecosystems/communication-platforms/`, `knowledge/languages/javascript/`, `knowledge/languages/java/`, `knowledge/api/`
- WhatsApp Business API architecture: `knowledge/platform-ecosystems/communication-platforms/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- Stripe payment architecture: `knowledge/platform-ecosystems/payment/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- PayPal payment architecture: `knowledge/platform-ecosystems/payment/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- AWS cloud architecture: `knowledge/platform-ecosystems/cloud/`, `knowledge/platform/`, `knowledge/api/`
- Azure cloud architecture: `knowledge/platform-ecosystems/cloud/`, `knowledge/platform/`, `knowledge/api/`
- GCP cloud architecture: `knowledge/platform-ecosystems/cloud/`, `knowledge/platform/`, `knowledge/api/`
- Alibaba Cloud architecture: `knowledge/platform-ecosystems/cloud/`, `knowledge/platform/`, `knowledge/api/`
- Robotics platform architecture: `knowledge/platform-ecosystems/robotics/`, `knowledge/frameworks/robotics/`, `knowledge/languages/python/`, `knowledge/languages/c/`, `knowledge/platform/`
- DJI drone platform architecture: `knowledge/platform-ecosystems/drone/`, `knowledge/languages/java/`, `knowledge/languages/c/`, `knowledge/languages/python/`, `knowledge/platform/`
- ArduPilot/PX4 platform architecture: `knowledge/platform-ecosystems/drone/`, `knowledge/languages/c/`, `knowledge/languages/cpp/`, `knowledge/languages/python/`, `knowledge/platform/`
- AWS IoT architecture: `knowledge/platform-ecosystems/iot-edge/`, `knowledge/platform-ecosystems/cloud/`, `knowledge/languages/c/`, `knowledge/languages/python/`, `knowledge/platform/`
- Azure IoT architecture: `knowledge/platform-ecosystems/iot-edge/`, `knowledge/platform-ecosystems/cloud/`, `knowledge/languages/c/`, `knowledge/languages/csharp/`, `knowledge/platform/`
- ThingsBoard IoT architecture: `knowledge/platform-ecosystems/iot-edge/`, `knowledge/languages/java/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/platform/`
- Steam platform architecture: `knowledge/platform-ecosystems/gaming/`, `knowledge/languages/cpp/`, `knowledge/languages/csharp/`, `knowledge/api/`
- PlayStation platform architecture: `knowledge/platform-ecosystems/gaming/`, `knowledge/languages/cpp/`, `knowledge/languages/csharp/`, `knowledge/api/`
- Xbox platform architecture: `knowledge/platform-ecosystems/gaming/`, `knowledge/languages/cpp/`, `knowledge/languages/csharp/`, `knowledge/api/`
- Nintendo platform architecture: `knowledge/platform-ecosystems/gaming/`, `knowledge/languages/cpp/`, `knowledge/languages/c/`, `knowledge/api/`
- Epic Games platform architecture: `knowledge/platform-ecosystems/gaming/`, `knowledge/languages/cpp/`, `knowledge/languages/csharp/`, `knowledge/api/`
- Twitter/X platform architecture: `knowledge/platform-ecosystems/social-media/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- TikTok platform architecture: `knowledge/platform-ecosystems/social-media/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- Instagram platform architecture: `knowledge/platform-ecosystems/social-media/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- YouTube platform architecture: `knowledge/platform-ecosystems/social-media/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`

## Coverage Checks

When adding a new category, check both sides:

- Knowledge exists for durable concepts.
- A skill exists for executable review or implementation workflow.

Examples:

- `knowledge/languages/shell/` is paired with `skills/languages/shell/shell-script-architecture`.
- `knowledge/languages/typescript/` is paired with `skills/languages/typescript/typescript-module-architecture`.
- `knowledge/languages/javascript/` is paired with `skills/languages/javascript/javascript-module-architecture`.
- `knowledge/platform/` is paired with `skills/domains/operations/operational-script-review`.
- `knowledge/frameworks/` is paired with `skills/frameworks/framework-boundary-review` and `skills/frameworks/orm-boundary-review`.
- `knowledge/data-systems/vector/` is paired with `skills/domains/database/vector/vector-search-architecture-review`.
- `knowledge/platform-ecosystems/` is paired with `skills/platforms/platform-ecosystem-architecture-review`.
- `knowledge/platform-ecosystems/wechat/` is paired with `skills/platforms/wechat/wechat-mini-program-architecture` and `skills/platforms/wechat/wechat-pay-integration`.
- `knowledge/platform-ecosystems/robotics/` is paired with `skills/platforms/robotics/robotics-platform-architecture`.
- `knowledge/platform-ecosystems/communication-platforms/` is paired with `skills/platforms/alipay/alipay-mini-program-architecture`, `skills/platforms/line/line-bot-architecture`, `skills/platforms/facebook/facebook-platform-architecture`, `skills/platforms/slack/slack-app-architecture`, `skills/platforms/discord/discord-bot-architecture`, `skills/platforms/telegram/telegram-bot-architecture`, `skills/platforms/feishu/feishu-app-architecture`, `skills/platforms/dingtalk/dingtalk-app-architecture`, `skills/platforms/whatsapp/whatsapp-business-architecture`.
- `knowledge/platform-ecosystems/payment/` is paired with `skills/platforms/alipay/alipay-payment-integration`, `skills/platforms/stripe/stripe-payment-architecture`, `skills/platforms/paypal/paypal-payment-architecture`.
- `knowledge/platform-ecosystems/cloud/` is paired with `skills/platforms/aws/aws-cloud-architecture`, `skills/platforms/azure/azure-cloud-architecture`, `skills/platforms/gcp/gcp-cloud-architecture`, `skills/platforms/alibaba-cloud/alibaba-cloud-architecture`.
- `knowledge/platform-ecosystems/drone/` is paired with `skills/platforms/dji/dji-drone-platform-architecture`, `skills/platforms/ardupilot/ardupilot-platform-architecture`.
- `knowledge/platform-ecosystems/iot-edge/` is paired with `skills/platforms/aws-iot/aws-iot-architecture`, `skills/platforms/azure-iot/azure-iot-architecture`, `skills/platforms/thingsboard/thingsboard-iot-architecture`.
- `knowledge/platform-ecosystems/gaming/` is paired with `skills/platforms/steam/steam-platform-architecture`, `skills/platforms/playstation/playstation-platform-architecture`, `skills/platforms/xbox/xbox-platform-architecture`, `skills/platforms/nintendo/nintendo-platform-architecture`, `skills/platforms/epic/epic-platform-architecture`.
- `knowledge/platform-ecosystems/social-media/` is paired with `skills/platforms/twitter/twitter-platform-architecture`, `skills/platforms/tiktok/tiktok-platform-architecture`, `skills/platforms/instagram/instagram-platform-architecture`, `skills/platforms/youtube/youtube-platform-architecture`.

## Rule For New Skills

Every non-trivial skill should include a short `Knowledge To Use` section listing relevant knowledge cards. This keeps each `SKILL.md` concise while making deeper context discoverable.

## Methodology Notes

Named learning systems such as Suntone architecture, Java architecture curricula, or GoF reading paths belong under `knowledge/methodologies/`. Reusable concepts from those systems should still be linked to their canonical cards in `principles/`, `patterns/`, `architecture/`, `languages/`, or `frameworks/`.
