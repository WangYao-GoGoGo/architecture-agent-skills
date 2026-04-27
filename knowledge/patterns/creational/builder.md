# Builder

## Use When

- Object construction has many optional fields, validation rules, or stepwise assembly.
- Constructor calls are becoming unreadable.

## Avoid When

- A simple constructor or named factory function is enough.

## Core Idea

Separate construction steps from the final object representation.

## Verification

- Invalid construction fails in one clear place.
- Call sites become easier to read.
