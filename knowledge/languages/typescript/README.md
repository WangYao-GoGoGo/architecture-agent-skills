# TypeScript Architecture Idioms

## Use When

- Reviewing TypeScript modules, frontend state, backend APIs, type boundaries, or ORM clients.

## Heuristics

- Use types to express domain contracts, not just transport shapes.
- Keep generated API/ORM types from leaking everywhere when they cause coupling.
- Separate UI state, server state, and domain state.
- Prefer discriminated unions for well-known variants.
- Keep side effects at framework or adapter boundaries.

## Common Risks

- `any` erasing important architecture contracts.
- Shared type packages becoming dumping grounds.
- Frontend components owning too much server workflow logic.
- ORM model types leaking into API contracts.

