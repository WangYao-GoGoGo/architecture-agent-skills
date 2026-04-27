# Saga

## Project Fit

Saga fits business workflows that span multiple services or data stores where one database transaction is not possible.

## Use When

- A business workflow spans multiple services or data stores and cannot use one transaction.
- Each step can commit locally and expose success or failure.
- The workflow can tolerate compensation or state-based recovery.

## Avoid When

- One local transaction is possible and simpler.
- Compensation cannot meaningfully handle failed steps.
- The team cannot observe workflow state and retries.

## Core Idea

A saga coordinates a sequence of local transactions with compensating actions or state transitions.

## Fits Best With

- Orders, payments, reservations, fulfillment, onboarding, cross-service provisioning.

## Heuristics

- Define each local transaction and compensation.
- Make retries and idempotency explicit.
- Choose orchestration when a central workflow owner is helpful.
- Choose choreography when services can react independently without hidden coupling.

## Risks

- Compensation may not truly undo business effects.
- Workflow state becomes hard to observe.
- Duplicate messages or partial failures break assumptions.

## Verification

- Every step has retry and failure behavior.
- Compensation is business-valid, not just technical rollback.
- Workflow status can be inspected and repaired.
