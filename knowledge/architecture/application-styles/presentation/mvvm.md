# MVVM

## Project Fit

MVVM is a presentation architecture style. It fits UI projects where view state, derived state, bindings, and commands need a dedicated model for the view.

## Use When

- UI state and binding behavior are central to the framework or application.
- View logic benefits from a view model that exposes observable or derived state.
- Screens have enough state transitions that putting all logic in the view becomes hard to maintain.

## Avoid When

- The UI is simple and component-local state is enough.
- The framework already provides a clearer state management pattern.
- View models would become general application services or persistence wrappers.

## Core Idea

Model-View-ViewModel separates views from state transformation and presentation behavior. The view model exposes data and commands for the view.

## Fits Best With

- Desktop and mobile apps with data binding.
- Frontend applications with complex UI state.
- UI flows that benefit from explicit derived state and commands.

## Heuristics

- Keep view models focused on presentation state and commands.
- Keep domain rules and persistence outside the view model.
- Separate server state, local UI state, and derived state.
- Avoid view models that simply mirror every backend field without purpose.

## Adaptation Notes

- React/Vue/Svelte: view models may appear as composables, hooks, stores, or feature state modules.
- Server-rendered UI: use only when template state preparation is complex.
- Backend-only services: MVVM usually does not apply.

## Risks

- View models become application services.
- Binding hides expensive or side-effecting work.
- State ownership becomes unclear across nested components.

## Verification

- View model exposes only presentation state and commands.
- Expensive side effects are explicit and not hidden in bindings.
- Domain and persistence logic remain outside the view model.
