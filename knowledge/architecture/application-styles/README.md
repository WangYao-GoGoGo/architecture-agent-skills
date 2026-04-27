# Application Styles

Application style cards describe how code is organized inside an application or deployable unit.

This folder is language-neutral. Java, Python, TypeScript, Shell, and other language-specific architecture idioms belong under `knowledge/languages/`.

## Structure

- `layered-and-ports/`: layered architecture, clean architecture, hexagonal architecture, onion architecture.
- `presentation/`: MVC, MVP, MVVM, and UI-facing application organization.
- `modular/`: modular monolith, vertical slice architecture, plugin architecture, pipe and filter.

## Selection Guide

Choose by the project's dominant pressure:

| Pressure | Start With |
| --- | --- |
| Dependency direction, domain core, framework isolation | `layered-and-ports/` |
| UI presentation logic, view state, user actions | `presentation/` |
| Feature ownership, module boundaries, plugins, processing flows | `modular/` |

## Fit Rule

These styles are not universal templates. They are reusable options for corresponding project types:

- Backend services often fit `layered-and-ports/` or `modular/`.
- Frontend applications often fit `presentation/` or `modular/`.
- Full-stack applications may combine `presentation/` for UI and `layered-and-ports/` or `modular/` for business workflows.
- Shell scripts and data tools may borrow `modular/pipe-and-filter.md` or lightweight layered phases such as parse, validate, execute, and report.
- Small projects should use the lightest version of a style, or no formal style.

## What Belongs Here

- Architecture styles that can be applied across languages.
- Application-internal organization patterns.
- Tradeoffs for choosing one style over another.

## What Belongs Elsewhere

- GoF design patterns: `knowledge/patterns/`
- SOLID, GRASP, coupling/cohesion: `knowledge/principles/`
- Java-specific architecture idioms: `knowledge/languages/java/`
- Spring/Hibernate/JPA details: `knowledge/frameworks/java/`
- Named learning systems or schools, such as Suntone or Java architecture curricula: `knowledge/methodologies/`
