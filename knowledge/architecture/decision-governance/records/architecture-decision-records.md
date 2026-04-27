# Architecture Decision Records

## Project Fit

ADRs fit any project where architecture decisions have consequences beyond one small code change.

## Use When

- A decision affects long-term structure, dependencies, data ownership, deployment, or operations.
- The team needs to remember why one option was chosen.
- Future contributors will need context.

## Avoid When

- The decision is trivial, local, or easily reversible.
- The document would only repeat what the code already says.

## Core Idea

An ADR records context, decision, alternatives, consequences, and revisit triggers.

## Fits Best With

- Architecture style choices, database choices, service boundaries, framework adoption, API compatibility decisions, migration strategies.

## Heuristics

- Keep ADRs short and decision-focused.
- Include rejected alternatives and why they were rejected.
- Name consequences, not only benefits.
- Add revisit triggers for assumptions that may change.

## Risks

- ADRs become status reports instead of decisions.
- Decisions are recorded after the fact without tradeoffs.
- No one knows when to revisit them.

## Verification

- A reader can understand context, decision, alternatives, consequences, and revisit trigger.
- The ADR points to concrete affected systems or code.
- The decision can be challenged or superseded later.
