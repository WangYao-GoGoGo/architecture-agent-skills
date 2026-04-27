# Spring MVC Knowledge

## Heuristics

- Keep controllers thin: they should parse input, delegate to services, and format responses.
- Use `@RequestMapping` or specific annotations (`@GetMapping`, `@PostMapping`) at the type level for base paths.
- Validate request bodies with `@Valid` and custom validators when needed.
- Return `ResponseEntity` for fine-grained control over status codes and headers.
- Use `@ExceptionHandler` in `@ControllerAdvice` for centralized error handling.
- Keep handler method signatures clean: avoid `HttpServletRequest`/`HttpServletResponse` unless absolutely necessary.
- Use DTOs for request/response objects; do not expose domain entities directly.
- Prefer content negotiation (JSON, XML) via `Accept` headers rather than URL suffixes.
- Use `@ModelAttribute` for populating model objects in view-oriented controllers.

## Common Risks

- Controllers with too many responsibilities (parsing, validation, business logic, formatting).
- Domain entities leaked into controller signatures, coupling API shape to internal models.
- Inconsistent error response formats across different controllers.
- Overusing `@RequestParam` when a dedicated DTO would be cleaner.
- Mixing view-oriented and REST-oriented controllers in the same class.
