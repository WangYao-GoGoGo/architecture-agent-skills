# Frameworks Gap Analysis

## Current `skills/frameworks/` Structure

```
skills/frameworks/
├── README.md
├── framework-boundary-review/   (通用框架边界审查 SKILL)
├── orm-boundary-review/         (通用 ORM 边界审查 SKILL)
├── database/
│   ├── README.md
│   ├── flyway/
│   └── liquibase/
├── java/
│   ├── README.md
│   ├── hibernate/
│   ├── spring-data-jpa/
│   └── mybatis/
├── python/
│   ├── README.md
│   ├── sqlalchemy/
│   ├── alembic/
│   └── django-orm/
└── typescript/
    ├── README.md
    ├── prisma/
    ├── typeorm/
    ├── sequelize/
    └── mongoose/
```

## `knowledge/frameworks/` 中已有但 `skills/frameworks/` 缺失的框架

### Java 框架 (skills/frameworks/java/)
| 框架 | knowledge 中已有 | skills 中缺失 |
|------|:---:|:---:|
| Spring Boot | ✅ | ❌ |
| Spring MVC | ❌ | ❌ |
| Struts | ❌ | ❌ |

### 后端框架 (skills/frameworks/backend/ — 新目录)
| 框架 | knowledge 中已有 | skills 中缺失 |
|------|:---:|:---:|
| Spring Boot | ✅ | ❌ |
| Django | ✅ | ❌ |
| FastAPI | ✅ | ❌ |
| Flask | ✅ | ❌ |
| Express | ✅ | ❌ |
| NestJS | ✅ | ❌ |
| Rails | ✅ | ❌ |
| Laravel | ✅ | ❌ |
| ASP.NET Core | ✅ | ❌ |
| Gin | ✅ | ❌ |

### 前端框架 (skills/frameworks/frontend/ — 新目录)
| 框架 | knowledge 中已有 | skills 中缺失 |
|------|:---:|:---:|
| React | ✅ | ❌ |
| Vue | ✅ | ❌ |
| Angular | ✅ | ❌ |
| Svelte | ✅ | ❌ |
| Next.js | ✅ | ❌ |
| Nuxt | ✅ | ❌ |

### 移动端框架 (skills/frameworks/mobile/ — 新目录)
| 框架 | knowledge 中已有 | skills 中缺失 |
|------|:---:|:---:|
| Android | ✅ | ❌ |
| iOS | ✅ | ❌ |
| Flutter | ✅ | ❌ |
| React Native | ✅ | ❌ |
| Kotlin Multiplatform | ✅ | ❌ |
| Ionic | ✅ | ❌ |

### 桌面端框架 (skills/frameworks/desktop/ — 新目录)
| 框架 | knowledge 中已有 | skills 中缺失 |
|------|:---:|:---:|
| Electron | ✅ | ❌ |
| Tauri | ✅ | ❌ |

### 数据处理框架 (skills/frameworks/data/ — 新目录)
| 框架 | knowledge 中已有 | skills 中缺失 |
|------|:---:|:---:|
| Spark | ✅ | ❌ |
| Flink | ✅ | ❌ |
| Airflow | ✅ | ❌ |

### AI Agent 框架 (skills/frameworks/ai-agent/ — 新目录)
| 框架 | knowledge 中已有 | skills 中缺失 |
|------|:---:|:---:|
| LangChain | ✅ | ❌ |
| LlamaIndex | ✅ | ❌ |
| Semantic Kernel | ✅ | ❌ |
| CrewAI | ✅ | ❌ |
| AutoGen | ✅ | ❌ |

### 机器人框架 (skills/frameworks/robotics/ — 新目录)
| 框架 | knowledge 中已有 | skills 中缺失 |
|------|:---:|:---:|
| ROS 2 | ✅ | ❌ |
| MoveIt | ✅ | ❌ |
| Gazebo | ✅ | ❌ |

## 总计

- **已有 knowledge 卡片但缺少 skills 的框架**: 36 个
- **需要新建的 skills 子目录**: 7 个 (backend, frontend, mobile, desktop, data, ai-agent, robotics)
- **需要补全的现有子目录**: 1 个 (java — 添加 Spring Boot, Spring MVC, Struts)
