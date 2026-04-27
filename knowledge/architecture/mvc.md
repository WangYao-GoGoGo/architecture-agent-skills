# MVC

## Use When

- UI or web code needs separation between presentation, user actions, and domain/data interaction.

## Core Idea

Model represents data and domain state, View renders presentation, and Controller coordinates user input or requests.

## Risks

- Controllers become too large.
- Models become persistence-only records with domain logic scattered elsewhere.
- Views gain data fetching or business rules.

## Verification

- Controllers are thin coordinators.
- Domain or application logic is testable outside the view.
- Views do not own business policy.
