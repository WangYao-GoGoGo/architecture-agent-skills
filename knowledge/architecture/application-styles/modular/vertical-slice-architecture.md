# Vertical Slice Architecture

## Project Fit

Vertical slice architecture is language-neutral. It fits projects where features or use cases are easier to understand when grouped end to end.

## Use When

- Features or use cases change independently.
- Layer-based organization scatters one feature across many folders.
- A team works primarily by feature and wants local reasoning.

## Avoid When

- Shared domain rules are the main source of complexity and should be centralized.
- Slices would duplicate important invariants.
- Cross-slice workflows dominate the application.

## Core Idea

Vertical slice architecture groups code by feature or use case rather than by technical layer. Each slice owns the request, validation, workflow, and persistence interaction needed for that feature.

## Fits Best With

- Backend APIs organized by command/query/use case.
- Frontend feature modules and route-level features.
- Full-stack feature folders where one use case spans UI, API, validation, and data access.

## Heuristics

- Group files around a business capability or user action.
- Keep shared abstractions small and earned.
- Avoid forcing every slice through broad generic services.
- Extract common behavior only after duplication represents the same concept.

## Adaptation Notes

- Backend: each slice may own handler, validator, use case, and query.
- Frontend: each slice may own page, components, state, API calls, and tests.
- Scripts/data tools: each slice can represent one operation or pipeline stage.
- Database: shared schema changes still need cross-slice coordination.

## Risks

- Slices duplicate rules that should be shared domain policy.
- Cross-slice consistency becomes unclear.
- Feature folders become mini god modules.

## Verification

- A feature can be changed by reading a small local set of files.
- Shared domain rules are not copied silently.
- Slice boundaries match user/business behavior, not arbitrary screens.
