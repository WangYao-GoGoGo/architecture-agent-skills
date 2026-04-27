# Architecture Principles

## Project Fit

Architecture principles fit teams that need stable decision heuristics across many projects.

## Use When

- Decisions repeatedly face similar tradeoffs.
- Teams need shared language for maintainability, coupling, data ownership, and operations.

## Avoid When

- Principles are vague slogans that cannot guide choices.
- Principles conflict without priority or examples.

## Core Idea

Architecture principles are durable rules of thumb that guide decisions before specific patterns or technologies are chosen.

## Examples

- Prefer explicit ownership over shared mutable responsibility.
- Prefer local simplicity until distributed complexity is justified.
- Prefer behavior-preserving migration paths.
- Prefer observable failure over hidden best effort.

## Verification

- Principles help reject or choose concrete options.
- Exceptions can be documented with reasons.
- Principles appear in ADRs, RFCs, and review checklists.
