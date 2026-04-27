# Language Pack Guide

Language packs adapt architecture guidance to language idioms and runtime constraints.

## What Belongs In A Language Pack

- module/package conventions
- type system or interface idioms
- dependency injection style
- error handling conventions
- testing conventions
- framework boundary guidance when common in the language

## What Does Not Belong

- Generic pattern explanations that belong in `knowledge/`.
- Domain-specific database/cache/frontend rules that belong in `skills/domains/`.
- Framework-specific rules that deserve `skills/frameworks/`.

## Quality Bar

A language skill should help an agent avoid translating patterns mechanically from another language.

Examples:

- Python may use protocols or callables instead of heavy interface hierarchies.
- Java may use packages, constructor injection, and explicit interfaces where substitution matters.
- C may use headers, opaque structs, and explicit ownership contracts.
- SQL may use constraints, indexes, migrations, and query plans as architecture tools.
