# Dependency Inversion

## Use When

- Core policy depends on infrastructure, frameworks, vendors, databases, caches, or UI.
- Tests require heavy setup because dependencies cannot be substituted.
- A module should be reusable without dragging in implementation details.

## Core Idea

High-level policy should depend on stable abstractions. Low-level details should implement or adapt to those abstractions.

## Agent Heuristics

- Keep domain rules independent from transport and persistence when possible.
- Put interfaces near the consumer when the consumer owns the policy.
- Use adapters at the boundary to translate vendor or framework APIs.
- Avoid abstracting stable, local code just for style.

## Verification

- Core logic can be tested without the database, network, UI, or framework runtime.
- Replacing a vendor or storage detail does not rewrite domain rules.
