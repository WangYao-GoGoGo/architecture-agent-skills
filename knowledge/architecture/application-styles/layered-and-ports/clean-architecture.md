# Clean Architecture

## Project Fit

Clean architecture is language-neutral. It fits projects where business rules need protection from frameworks, databases, UI, external services, or generated clients.

## Use When

- Domain policy should remain independent from frameworks, UI, databases, and vendors.
- The project has enough complexity to justify explicit boundaries.
- Use cases must be testable without starting the full framework.
- Multiple delivery mechanisms may drive the same behavior, such as API, CLI, jobs, events, or tests.

## Avoid When

- The project is mostly simple CRUD with little domain policy.
- The team would create interfaces and layers without real substitution or boundary value.
- Framework conventions are the main source of productivity and do not currently cause coupling pain.

## Core Idea

Keep business rules near the center and implementation details at the edges. Dependencies point inward.

## Fits Best With

- Backend services with important domain rules.
- Python, Java, TypeScript, and C# applications where framework independence and testing matter.
- Long-lived systems expected to change infrastructure or delivery mechanisms.

## Practical Guidance

- Use cases orchestrate application workflows.
- Entities or domain models hold core rules.
- Adapters translate between external details and internal contracts.
- Ports should exist because substitution or boundary control matters, not by habit.

## Adaptation Notes

- Java: use packages and constructor injection to enforce boundaries.
- Python: use protocols or callables only where substitution helps.
- TypeScript: avoid leaking generated API/ORM types into the core.
- Frontend: use sparingly for complex client-side domain workflows, not every component.

## Verification

- Core rules can be tested without framework boot, database, network, or UI.
- Adapters are the only code that knows vendor or framework-specific shapes.
- Simple use cases did not become harder to read.
