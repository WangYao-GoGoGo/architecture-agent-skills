# Layered Architecture

## Use When

- A system benefits from clear separation between presentation, application, domain, and persistence concerns.
- The team needs predictable dependency rules.

## Core Idea

Organize code into layers with dependencies flowing in controlled directions. Common layers include controller/API, application service, domain, and infrastructure.

## Risks

- Layers can become pass-through ceremony.
- Domain rules can leak into controllers or repositories.
- Strict layering can fight simple use cases.

## Verification

- Each layer has a clear reason to change.
- Dependencies do not cycle.
- Tests can target domain and application logic without full infrastructure.
