# API Versioning

## Use When

- Changing public or multi-consumer API contracts.

## Core Idea

Versioning is a compatibility strategy. The best versioning work is often avoiding breaking changes through additive fields, tolerant readers, and staged migrations.

## Agent Heuristics

- Prefer additive response fields over changing existing meanings.
- Do not remove fields until consumers have migrated.
- Avoid changing enum semantics silently.
- Document deprecation and migration windows.
- For events, treat schemas as long-lived contracts.

## Verification

- Old clients still work.
- New clients can use the new shape.
- Rollback does not strand data or consumers.

