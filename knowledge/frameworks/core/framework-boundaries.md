# Framework Boundaries

## Core Idea

Frameworks are useful at the edges, but core domain or workflow policy should not become impossible to test without booting the framework.

## Heuristics

- Keep framework lifecycle objects near entry points.
- Translate framework request, response, model, or event types into local concepts.
- Do not wrap every framework feature; wrap volatile or widely coupled features.
- Keep framework-specific annotations from becoming the only architecture boundary.

## Common Risks

- Domain logic only works inside framework runtime.
- Tests require full application boot for simple rules.
- Framework models leak into API and domain contracts.

