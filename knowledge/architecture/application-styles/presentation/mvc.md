# MVC

## Project Fit

MVC is primarily a presentation and web/UI architecture style. It can fit server-rendered web apps, frontend apps, desktop apps, and backend frameworks that expose controllers and views.

## Use When

- UI or web code needs separation between presentation, user actions, and domain/data interaction.
- The framework already uses controller, view/template, and model concepts.
- A page or screen has enough interaction to benefit from clear presentation boundaries.

## Avoid When

- There is no UI or presentation layer.
- A small page can be simpler with one component or handler.
- Controllers would become the place for domain, persistence, and formatting logic.

## Core Idea

Model represents data and domain state, View renders presentation, and Controller coordinates user input or requests.

## Fits Best With

- Server-rendered web apps.
- Traditional web frameworks.
- UI applications that need clear request/action coordination.

## Adaptation Notes

- Backend web: controller handles transport, not business rules.
- Frontend: component or route handlers may act like controllers, but business rules should stay outside rendering code.
- Desktop/mobile: controller coordinates user actions and updates view state.
- API-only backend: use controller/service separation, but MVC view concepts may not apply.

## Risks

- Controllers become too large.
- Models become persistence-only records with domain logic scattered elsewhere.
- Views gain data fetching or business rules.

## Verification

- Controllers are thin coordinators.
- Domain or application logic is testable outside the view.
- Views do not own business policy.
