<p align="center">
  <img src="https://img.shields.io/badge/skills-200%2B-blue?style=flat-square" alt="Skills">
  <img src="https://img.shields.io/badge/knowledge%20cards-300%2B-green?style=flat-square" alt="Knowledge Cards">
  <img src="https://img.shields.io/badge/languages-40%2B-orange?style=flat-square" alt="Languages">
  <img src="https://img.shields.io/badge/frameworks-80%2B-purple?style=flat-square" alt="Frameworks">
  <img src="https://img.shields.io/badge/platforms-33%2B-teal?style=flat-square" alt="Platforms">
  <img src="https://img.shields.io/badge/license-MIT-yellow?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square" alt="PRs Welcome">
</p>

> **🌐 Language / 语言**: This README is in English. GitHub provides built-in page translation — use the language dropdown in your browser or append `?l=zh-CN` / `?l=ja` / `?l=ko` to the URL for auto-translation. We do not maintain separate translated files because the project has 200+ files across skills, knowledge, docs, and examples — keeping them in sync would be impractical.

# Architecture Agent Skills

Architecture Agent Skills is an open-source skill library for helping AI coding agents design, review, and refactor software with explicit architecture thinking before they write large blocks of code.

The project covers architecture across programming paradigms, languages, and technical domains: object-oriented design, procedural modular design, functional composition, backend services, frontend components, databases, caches, data pipelines, and more. Object-oriented architecture is an early focus, not the final boundary of the project.

The goal is not to make agents use patterns everywhere. The goal is to help agents choose simple, readable structures that make code easier to understand, test, change, and extend.

## What This Project Is For

- Review existing code and identify architecture smells.
- Plan refactors before changing code.
- Select design patterns only when the problem actually fits.
- Design new code around responsibilities, boundaries, and extension points.
- Provide paradigm-specific guidance for object-oriented, procedural, functional, and systems-oriented code.
- Provide language-specific guidance for Java, Python, C, SQL, TypeScript, JavaScript, Shell, and future language packs.
- Provide domain-specific guidance for backend, frontend, database, cache, search, data pipeline, and operations architecture.
- Provide platform-ecosystem guidance for WeChat, robotics, cloud, IoT, bot platforms, and vendor SDK integrations.
- Build a shared knowledge base that contributors can improve over time.

## Repository Layout

```text
skills/
  core/                 Cross-language architecture workflows
  paradigms/            Object-oriented, functional, procedural, systems thinking
  languages/            Java, Python, C, SQL, TypeScript, JavaScript, Shell guidance
  domains/              Backend, frontend, database, data pipeline, operations guidance
  frameworks/           Framework, ORM, migration-tool, generated-client guidance
  platforms/            External platform, vendor SDK, robot, IoT, cloud ecosystem guidance

knowledge/
  principles/           SOLID, GRASP, coupling/cohesion, boundaries
  patterns/             Design pattern and architecture pattern cards
  smells/               Code, schema, boundary, and architecture smell cards
  architecture/         Application styles, distributed systems, integration patterns, governance
  paradigms/            OO, procedural, functional, systems-oriented concepts
  languages/            Java, Python, C, SQL, TypeScript, JavaScript, Shell idioms
  application-areas/    Backend, frontend, data pipeline, operations
  data-systems/         Relational, document, key-value, graph, search, vector, cache
  api/                  Contracts, versioning, idempotency, pagination, errors
  frameworks/           Framework boundaries, ORM, migrations, frontend frameworks
  platform/             Platform-specific knowledge for 33+ platforms (social, communication, payment, cloud, gaming, social media, IoT, drone, robotics) plus generic operations (Linux, shell, process, filesystem, configuration)
  methodologies/        Named learning systems and source-oriented maps

templates/              Reusable templates for new skills and reports
docs/                   Project vision, contribution workflow, design guide
examples/               Before/after examples for evaluation and learning
tests/                  Human-readable evaluation checklists
```

## Core Skills

| Skill | When To Use |
|---|---|
| [`architecture-before-coding`](skills/core/architecture-before-coding/README.md) | Before implementing a feature — design responsibilities, boundaries, patterns, and risks first. |
| [`refactoring-planner`](skills/core/refactoring-planner/README.md) | Before changing existing code — plan behavior-preserving refactors. |
| [`design-pattern-selector`](skills/core/design-pattern-selector/README.md) | When code has conditionals, duplication, or creation complexity — pick the smallest pattern that fits. |
| [`dependency-boundary-review`](skills/core/dependency-boundary-review/README.md) | When dependencies between modules or services are tangled or point in the wrong direction. |
| [`architecture-decision-review`](skills/core/architecture-decision-review/README.md) | To document or review architecture decisions, tradeoffs, and alternatives. |
| [`anti-overengineering-review`](skills/core/anti-overengineering-review/README.md) | To check whether a proposed abstraction is larger than the current problem needs. |
| [`new-project-scaffolding`](skills/core/new-project-scaffolding/README.md) | When creating a new project from scratch — generate architecture-correct structure from day one. |
| [`architecture-quality-review`](skills/core/architecture-quality-review/README.md) | After generating or refactoring code — verify it meets architecture quality standards. |
| [`runtime-error-diagnosis`](skills/core/runtime-error-diagnosis/README.md) | When code fails to run, throws an exception, or produces an error log — diagnose root cause and suggest the smallest safe fix. |
| [`test-generation-planner`](skills/core/test-generation-planner/README.md) | Before or after code changes — identify minimal tests needed to validate behavior. |
| [`behavior-preservation-validator`](skills/core/behavior-preservation-validator/README.md) | After refactoring — check whether original behavior is preserved. |
| [`debug-report-generator`](skills/core/debug-report-generator/README.md) | After debugging — summarize root cause, fix, validation steps, and remaining risks. |

## Frameworks vs Platform Ecosystems

Put framework behavior in `knowledge/frameworks/`: Spring Boot, React, Django, Electron, ROS 2, ORMs, migration tools, and similar runtime or library ecosystems.

Put external ecosystem constraints in `knowledge/platform/`: WeChat, Pepper/NAOqi, robot arms, cloud accounts, IoT fleets, chat/bot platforms, app review rules, hardware controllers, platform callbacks, and vendor SDK boundaries.

## Design Philosophy

1. Prefer clear responsibility and boundaries over clever abstraction.
2. Prefer the idioms of the target paradigm and language.
3. Prefer composition before inheritance unless the domain model genuinely benefits from inheritance.
4. Prefer naming the tradeoff over forcing a pattern.
5. Prefer behavior-preserving refactors with tests or executable checks.
6. Avoid pattern shopping. A pattern is useful only when it reduces real change cost.
7. Treat data architecture, caching, APIs, and frontend state as first-class architecture concerns.

## Debugging and Validation

Architecture improvement is not complete unless behavior is checked.

This project includes debugging and validation skills that help AI coding agents diagnose runtime errors, plan tests, verify behavior preservation, and generate human-readable debug reports.

Key validation skills include:

- [`runtime-error-diagnosis`](skills/core/runtime-error-diagnosis/README.md) — diagnose code that fails at runtime, identify root cause, and suggest the smallest safe fix.
- [`test-generation-planner`](skills/core/test-generation-planner/README.md) — plan minimal tests for generated, modified, or refactored code.
- [`behavior-preservation-validator`](skills/core/behavior-preservation-validator/README.md) — check whether refactored code preserves the original behavior.
- [`debug-report-generator`](skills/core/debug-report-generator/README.md) — generate a human-readable debugging report after a bug fix or validation task.

These skills help agents avoid silent behavior changes during refactoring and ensure that generated or modified code actually works.

### Validation Levels

| Level | Description | When To Use |
|---|---|---|
| **Static reasoning** | Compare interfaces, inputs, outputs, and side effects by reasoning alone | When code cannot be executed |
| **Test-based** | Write and run unit tests or regression tests | When tests can be written or run |
| **Golden master** | Run original code on representative inputs, save outputs, compare with refactored code | For behavior-preserving refactors |

### Example Structure

Each major example in `examples/` follows this structure:

```text
examples/<language>/<example-name>/
  README.md
  before/          Original source code
  after/           Refactored source code
  reports/         Architecture, behavior, and debug reports
    refactoring-plan.md
    behavior-preservation-report.md
    debug-report.md
  tests/           Executable validation tests
  commands.md      How to run, test, and validate
```

## Installation

### Claude Code (Manual)

Copy skill directories into your Claude Code skills folder:

```bash
# Global install (all users, all projects)
cp -r skills/core ~/.claude/skills/
cp -r skills/paradigms ~/.claude/skills/
cp -r skills/languages ~/.claude/skills/
cp -r skills/domains ~/.claude/skills/

# Project-local install (single project)
mkdir -p .claude/skills/
cp -r skills/core .claude/skills/
cp -r skills/paradigms .claude/skills/
```

Restart Claude Code or reload skills after installation.

### Using the Install Scripts

Python 3.8+ scripts are provided in [`scripts/`](scripts/):

```bash
# List available skills
python3 scripts/list_skills.py

# Install all core skills globally
python3 scripts/install_skill.py

# Install a specific skill
python3 scripts/install_skill.py --skill runtime-error-diagnosis

# Install project-local (in .claude/skills/)
python3 scripts/install_skill.py --project

# Validate all installed skills
python3 scripts/validate_skills.py

# Validate with strict mode (fail on warnings)
python3 scripts/validate_skills.py --strict
```

### Using the npm CLI

If you have Node.js 18+, install the [`archskill`](package.json) CLI globally:

```bash
# Install globally from npm
npm install -g archskill

# Or link locally for development
npm link

# List installed skills
archskill list

# Install all skills
archskill install

# Validate skills
archskill validate

# Scaffold a new skill
archskill new my-custom-skill
```

The CLI delegates to the Python scripts under [`scripts/`](scripts/).

### What Gets Installed

| Directory | Contents |
|---|---|
| `~/.claude/skills/core/` | Cross-language architecture skills (12 skills) |
| `~/.claude/skills/paradigms/` | Paradigm-specific skills (OO, functional, procedural) |
| `~/.claude/skills/languages/` | Language-specific skills (SQL, etc.) |
| `~/.claude/skills/domains/` | Domain-specific skills |
| `~/.claude/skills/frameworks/` | Framework-specific skills (80+ frameworks) |

## Contributing

### Branch Model

This project uses a two-branch model:

| Branch | Purpose |
|---|---|
| [`master`](https://github.com/architecture-agent-skills/architecture-agent-skills/tree/master) | Stable releases. All changes arrive via pull requests from `dev`. |
| [`dev`](https://github.com/architecture-agent-skills/architecture-agent-skills/tree/dev) | Active development. Contributors fork from and submit pull requests to this branch. |

### Contribution Workflow

```text
1. Fork this repository on GitHub
2. Create a feature branch from dev
3. Make your changes
4. Run validation: python3 scripts/validate_skills.py
5. Submit a pull request to the dev branch
6. Maintainers review and merge into dev
7. Changes are batched and merged from dev into master for releases
```

### What You Can Contribute

This repository is intentionally organized so contributors can add one small, high-quality unit at a time:

- a **skill** under `skills/` — see [`docs/skill-design-guide.md`](docs/skill-design-guide.md)
- a **knowledge card** under `knowledge/`
- a **before/after example** under `examples/`
- an **evaluation checklist** under `tests/`
- an **install script improvement** under `scripts/`

### Getting Started

1. **Fork** the repo on GitHub.
2. **Clone** your fork and switch to the `dev` branch:
   ```bash
   git clone https://github.com/WangYao-GoGoGo/architecture-agent-skills.git
   cd architecture-agent-skills
   git checkout dev
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feat/my-new-skill
   ```
4. **Make your changes** and validate:
   ```bash
   python3 scripts/validate_skills.py --strict
   ```
5. **Commit and push**:
   ```bash
   git push origin feat/my-new-skill
   ```
6. **Open a pull request** on GitHub against the `dev` branch.

### Guidelines

- Use the templates in [`templates/`](templates/) as starting points.
- For placement rules, see [`docs/taxonomy.md`](docs/taxonomy.md).
- For the full directory model, see [`docs/directory-structure.md`](docs/directory-structure.md).
- For skill-to-knowledge alignment, see [`docs/knowledge-skill-map.md`](docs/knowledge-skill-map.md).
- Run `python3 scripts/validate_skills.py --strict` before submitting.
- Keep each pull request focused on a single change.
