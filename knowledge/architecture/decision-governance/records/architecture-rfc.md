# Architecture RFC

## Project Fit

Architecture RFCs fit larger or more controversial decisions that need review before acceptance.

## Use When

- A change affects multiple teams, services, schemas, frameworks, or deployment workflows.
- The design needs feedback before implementation.
- The decision is not yet accepted.

## Avoid When

- A small ADR or issue comment is enough.
- The RFC process would slow urgent local fixes.
- The proposal lacks enough concrete context to review.

## Core Idea

An RFC proposes an architecture change, gathers feedback, and records the path to acceptance, revision, or rejection.

## Fits Best With

- Service extraction, database migration strategy, framework adoption, public API changes, event contract changes, platform changes.

## Verification

- The RFC states goals, non-goals, alternatives, risks, rollout, and verification.
- Reviewers and decision owner are clear.
- The outcome is recorded and linked to implementation work.
