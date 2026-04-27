# PHP Architecture Idioms

## Use When

- Reviewing PHP namespace structure, Composer autoloading, PSR compliance, or Laravel/Symfony application architecture.

## Heuristics

- Use PSR-4 autoloading with Composer — namespace directories mirror the filesystem.
- Declare strict types (`declare(strict_types=1)`) at the top of every file.
- Use type hints for parameters and return types — avoid mixed/array without specificity.
- Prefer constructor property promotion (PHP 8+) for value objects.
- Use enums (PHP 8.1+) for finite value sets instead of class constants.
- Keep controllers thin — move business logic into services or actions.
- Use dependency injection over static facades for testability.
- Follow PSR-12 coding style for consistency.

## Common Risks

- Overusing magic methods (`__get`, `__call`, `__invoke`) that bypass type safety.
- Mixing framework facades with injected dependencies inconsistently.
- Ignoring return type declarations on interface implementations.
- Long-lived requests with memory leaks from global state.
- Over-relying on `extract()` or `compact()` which make data flow opaque.
