# Architecture Review Checklist

## Project Fit

Use this checklist when reviewing non-trivial architecture changes across any language, framework, or domain.

## Use When

- A change affects boundaries, data ownership, API contracts, deployment, operations, or long-term maintainability.

## Checklist

- What problem is being solved?
- What alternatives were considered?
- What owns data, behavior, and failure response?
- What dependencies are introduced?
- What is the migration or rollout path?
- What can go wrong in production?
- How will the decision be verified?
- What would justify revisiting the decision?

## Avoid When

- The change is local and low-risk.
- The review becomes a generic approval gate without useful feedback.

## Verification

- Review findings are concrete and actionable.
- The decision owner can explain tradeoffs.
- Follow-up checks or ADRs exist for important decisions.
