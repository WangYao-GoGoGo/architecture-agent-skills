# Adapter

## Use When

- External API, vendor SDK, legacy module, or framework interface does not match local needs.
- Core code should not depend on vendor-specific shapes.

## Avoid When

- The external interface is already local, stable, and simple.

## Core Idea

Wrap an incompatible interface behind a local interface that callers understand.

## Refactoring Moves

1. Define the local interface around caller needs.
2. Implement an adapter that translates to the external API.
3. Move direct vendor calls behind the adapter.
4. Test core logic with the local interface.

## Verification

- Vendor changes are isolated to adapter code.
- Core logic can be tested without the vendor runtime.
