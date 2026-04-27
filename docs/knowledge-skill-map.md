# Knowledge To Skill Map

This map keeps `knowledge/` and `skills/` aligned.

## Core Skills

Core skills pair with `knowledge/core/` for architecture-level heuristics:

- `architecture-before-coding`: `knowledge/core/architecture-before-coding/`, `knowledge/principles/`, `knowledge/architecture/application-styles/`, `knowledge/architecture/integration-patterns/`, `knowledge/patterns/`, `knowledge/smells/`
- `refactoring-planner`: `knowledge/core/refactoring-planner/`, `knowledge/refactoring/`, `knowledge/smells/`, `knowledge/principles/`
- `dependency-boundary-review`: `knowledge/core/dependency-boundary-review/`, `knowledge/principles/dependency-inversion.md`, `knowledge/principles/separation-of-concerns.md`, `knowledge/frameworks/core/framework-boundaries.md`
- `anti-overengineering-review`: `knowledge/core/anti-overengineering-review/`, `knowledge/principles/`, `knowledge/smells/`, `knowledge/patterns/`
- `architecture-decision-review`: `knowledge/core/architecture-decision-review/`, `knowledge/architecture/`, especially `knowledge/architecture/decision-governance/`, plus `knowledge/data-systems/`, `knowledge/api/`, `knowledge/frameworks/`, `knowledge/platform/` as needed
- `design-pattern-selector`: `knowledge/core/design-pattern-selector/`, `knowledge/patterns/`, `knowledge/principles/`

## Paradigm Skills

- `skills/paradigms/object-oriented/`: `knowledge/paradigms/object-oriented/`, `knowledge/patterns/object-oriented/`
  - `oo-design-review`: OO responsibility, encapsulation, SOLID, GRASP review
  - `design-pattern-selector`: OO pattern selection — references 35 patterns in `knowledge/patterns/object-oriented/` (7 creational, 7 structural, 11 behavioral, 12 extended)
- `skills/paradigms/procedural/`: `knowledge/paradigms/procedural/`, `knowledge/languages/c/`, `knowledge/languages/go/`
  - `modular-procedural-refactor`: refactor procedural code into clearer modules
  - `procedural-architecture-review`: review procedural module boundaries, data flow, side effects
- `skills/paradigms/functional/`: `knowledge/paradigms/functional/`
  - `functional-composition-review`: functional composition and purity review
- `skills/paradigms/systems/`: `knowledge/paradigms/systems-oriented/`, `knowledge/platform/`
  - `systems-boundary-review`: systems boundary and resource ownership review
- Cross-paradigm: `knowledge/paradigms/cross-paradigm/` — paradigm comparison and decision guide

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
- **Java ecosystem**: `knowledge/frameworks/java/` (Hibernate, MyBatis, Spring Data JPA, Spring Boot, Spring MVC, Struts, jOOQ, Reactor)
- **Python ORM**: `knowledge/frameworks/python/` (SQLAlchemy, Alembic, Django ORM, Peewee, SQLModel)
- **TypeScript data**: `knowledge/frameworks/typescript/` (Prisma, TypeORM, Sequelize, Mongoose, Drizzle ORM, Knex.js, MikroORM)
- **Robotics frameworks**: `knowledge/frameworks/robotics/` (ROS 2, MoveIt, Gazebo, Webots, Isaac Sim), plus `knowledge/platform/robotics/` when hardware or vendor runtime constraints matter.
- **Migration tools**: `knowledge/frameworks/migrations/migration-tools.md`, `knowledge/data-systems/core/migrations.md`

## Platform Skills

- Platform ecosystem review: `knowledge/platform/`, `knowledge/api/`, `knowledge/frameworks/core/framework-boundaries.md`
- WeChat mini program architecture: `knowledge/platform/wechat/`, `knowledge/languages/javascript/`, `knowledge/languages/typescript/`, `knowledge/api/`
- WeChat Pay integration: `knowledge/platform/wechat/`, `knowledge/api/`
- Alipay mini program architecture: `knowledge/platform/alipay/`, `knowledge/languages/javascript/`, `knowledge/languages/typescript/`, `knowledge/api/`
- Alipay payment integration: `knowledge/platform/alipay/`, `knowledge/api/`
- LINE bot architecture: `knowledge/platform/line/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- Facebook/Meta platform architecture: `knowledge/platform/facebook/`, `knowledge/languages/javascript/`, `knowledge/api/`
- Slack app architecture: `knowledge/platform/slack/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- Discord bot architecture: `knowledge/platform/discord/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- Telegram bot architecture: `knowledge/platform/telegram/`, `knowledge/languages/python/`, `knowledge/languages/javascript/`, `knowledge/api/`
- Feishu/Lark app architecture: `knowledge/platform/feishu/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- DingTalk app architecture: `knowledge/platform/dingtalk/`, `knowledge/languages/javascript/`, `knowledge/languages/java/`, `knowledge/api/`
- WhatsApp Business API architecture: `knowledge/platform/whatsapp/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- Stripe payment architecture: `knowledge/platform/stripe/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- PayPal payment architecture: `knowledge/platform/paypal/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- AWS cloud architecture: `knowledge/platform/aws/`, `knowledge/api/`
- Azure cloud architecture: `knowledge/platform/azure/`, `knowledge/api/`
- GCP cloud architecture: `knowledge/platform/gcp/`, `knowledge/api/`
- Alibaba Cloud architecture: `knowledge/platform/alibaba-cloud/`, `knowledge/api/`
- Robotics platform architecture: `knowledge/platform/robotics/`, `knowledge/frameworks/robotics/`, `knowledge/languages/python/`, `knowledge/languages/c/`
- DJI drone platform architecture: `knowledge/platform/dji/`, `knowledge/languages/java/`, `knowledge/languages/c/`, `knowledge/languages/python/`
- ArduPilot/PX4 platform architecture: `knowledge/platform/ardupilot/`, `knowledge/languages/c/`, `knowledge/languages/cpp/`, `knowledge/languages/python/`
- AWS IoT architecture: `knowledge/platform/aws-iot/`, `knowledge/platform/aws/`, `knowledge/languages/c/`, `knowledge/languages/python/`
- Azure IoT architecture: `knowledge/platform/azure-iot/`, `knowledge/platform/azure/`, `knowledge/languages/c/`, `knowledge/languages/csharp/`
- ThingsBoard IoT architecture: `knowledge/platform/thingsboard/`, `knowledge/languages/java/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`
- Steam platform architecture: `knowledge/platform/steam/`, `knowledge/languages/cpp/`, `knowledge/languages/csharp/`, `knowledge/api/`
- PlayStation platform architecture: `knowledge/platform/playstation/`, `knowledge/languages/cpp/`, `knowledge/languages/csharp/`, `knowledge/api/`
- Xbox platform architecture: `knowledge/platform/xbox/`, `knowledge/languages/cpp/`, `knowledge/languages/csharp/`, `knowledge/api/`
- Nintendo platform architecture: `knowledge/platform/nintendo/`, `knowledge/languages/cpp/`, `knowledge/languages/c/`, `knowledge/api/`
- Epic Games platform architecture: `knowledge/platform/epic/`, `knowledge/languages/cpp/`, `knowledge/languages/csharp/`, `knowledge/api/`
- Twitter/X platform architecture: `knowledge/platform/twitter/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- TikTok platform architecture: `knowledge/platform/tiktok/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- Instagram platform architecture: `knowledge/platform/instagram/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`
- YouTube platform architecture: `knowledge/platform/youtube/`, `knowledge/languages/javascript/`, `knowledge/languages/python/`, `knowledge/api/`

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
- `knowledge/platform/` is paired with `skills/platforms/platform-ecosystem-architecture-review` and `skills/domains/operations/operational-script-review`.
- `knowledge/platform/wechat/` is paired with `skills/platforms/wechat/wechat-mini-program-architecture` and `skills/platforms/wechat/wechat-pay-integration`.
- `knowledge/platform/robotics/` is paired with `skills/platforms/robotics/robotics-platform-architecture`.
- `knowledge/platform/alipay/` is paired with `skills/platforms/alipay/alipay-mini-program-architecture` and `skills/platforms/alipay/alipay-payment-integration`.
- `knowledge/platform/line/` is paired with `skills/platforms/line/line-bot-architecture`.
- `knowledge/platform/facebook/` is paired with `skills/platforms/facebook/facebook-platform-architecture`.
- `knowledge/platform/slack/` is paired with `skills/platforms/slack/slack-app-architecture`.
- `knowledge/platform/discord/` is paired with `skills/platforms/discord/discord-bot-architecture`.
- `knowledge/platform/telegram/` is paired with `skills/platforms/telegram/telegram-bot-architecture`.
- `knowledge/platform/feishu/` is paired with `skills/platforms/feishu/feishu-app-architecture`.
- `knowledge/platform/dingtalk/` is paired with `skills/platforms/dingtalk/dingtalk-app-architecture`.
- `knowledge/platform/whatsapp/` is paired with `skills/platforms/whatsapp/whatsapp-business-architecture`.
- `knowledge/platform/stripe/` is paired with `skills/platforms/stripe/stripe-payment-architecture`.
- `knowledge/platform/paypal/` is paired with `skills/platforms/paypal/paypal-payment-architecture`.
- `knowledge/platform/aws/` is paired with `skills/platforms/aws/aws-cloud-architecture`.
- `knowledge/platform/azure/` is paired with `skills/platforms/azure/azure-cloud-architecture`.
- `knowledge/platform/gcp/` is paired with `skills/platforms/gcp/gcp-cloud-architecture`.
- `knowledge/platform/alibaba-cloud/` is paired with `skills/platforms/alibaba-cloud/alibaba-cloud-architecture`.
- `knowledge/platform/dji/` is paired with `skills/platforms/dji/dji-drone-platform-architecture`.
- `knowledge/platform/ardupilot/` is paired with `skills/platforms/ardupilot/ardupilot-platform-architecture`.
- `knowledge/platform/aws-iot/` is paired with `skills/platforms/aws-iot/aws-iot-architecture`.
- `knowledge/platform/azure-iot/` is paired with `skills/platforms/azure-iot/azure-iot-architecture`.
- `knowledge/platform/thingsboard/` is paired with `skills/platforms/thingsboard/thingsboard-iot-architecture`.
- `knowledge/platform/steam/` is paired with `skills/platforms/steam/steam-platform-architecture`.
- `knowledge/platform/playstation/` is paired with `skills/platforms/playstation/playstation-platform-architecture`.
- `knowledge/platform/xbox/` is paired with `skills/platforms/xbox/xbox-platform-architecture`.
- `knowledge/platform/nintendo/` is paired with `skills/platforms/nintendo/nintendo-platform-architecture`.
- `knowledge/platform/epic/` is paired with `skills/platforms/epic/epic-platform-architecture`.
- `knowledge/platform/twitter/` is paired with `skills/platforms/twitter/twitter-platform-architecture`.
- `knowledge/platform/tiktok/` is paired with `skills/platforms/tiktok/tiktok-platform-architecture`.
- `knowledge/platform/instagram/` is paired with `skills/platforms/instagram/instagram-platform-architecture`.
- `knowledge/platform/youtube/` is paired with `skills/platforms/youtube/youtube-platform-architecture`.

## Rule For New Skills

Every non-trivial skill should include a short `Knowledge To Use` section listing relevant knowledge cards. This keeps each `SKILL.md` concise while making deeper context discoverable.

## Methodology Notes

Named learning systems such as Suntone architecture, Java architecture curricula, or GoF reading paths belong under `knowledge/methodologies/`. Reusable concepts from those systems should still be linked to their canonical cards in `principles/`, `patterns/`, `architecture/`, `languages/`, or `frameworks/`.
