# Migration Tools

## Core Idea

Migration tools coordinate schema evolution, but they do not remove the need for rollout design.

## Heuristics

- Review generated migrations before committing.
- Split risky changes into expand, migrate, contract steps.
- Keep backfills separate from blocking schema changes when needed.
- Define rollback or forward-fix behavior.
- Test migrations against representative data.

## Common Risks

- Auto-generated destructive changes.
- Long locks during deploy.
- Irreversible data transformations without backup.

