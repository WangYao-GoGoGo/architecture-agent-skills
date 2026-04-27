# MVP

## Project Fit

MVP is a presentation architecture style. It fits UI projects where a presenter can own presentation decisions while the view stays passive or mostly passive.

## Use When

- Presentation logic should be separated from a passive view.
- The UI framework makes direct view testing difficult.
- The same presentation behavior needs tests without a full UI runtime.

## Avoid When

- The framework naturally favors unidirectional state, view models, or component-local state.
- Screens are simple enough that a presenter adds ceremony.
- The presenter would duplicate application-service or domain logic.

## Core Idea

Model-View-Presenter separates view rendering from presentation decisions. The presenter coordinates user actions, prepares view data, and talks to the model or application layer.

## Fits Best With

- Desktop, mobile, and older web UI patterns.
- UI frameworks where views can be passive interfaces.
- Teams that need presentation behavior tested outside UI rendering.

## Heuristics

- Keep the view passive where possible.
- Put UI decision logic in the presenter.
- Keep domain rules outside the presenter.
- Test presenter behavior without full UI runtime when useful.

## Adaptation Notes

- Frontend: presenters can be hooks, controllers, or plain modules when the framework fits.
- Backend server-rendered UI: presenters can prepare template view models.
- API-only backend: MVP usually does not apply.

## Risks

- Presenter becomes a god object.
- Too much boilerplate for simple screens.
- Presenter duplicates application service logic.

## Verification

- Presenter can be tested without rendering the full UI.
- View remains focused on display and forwarding user actions.
- Domain rules do not live in the presenter.
