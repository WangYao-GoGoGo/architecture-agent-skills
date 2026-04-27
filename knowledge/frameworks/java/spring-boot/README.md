# Spring Boot Knowledge

## Heuristics

- Separate application layers: controller, service, repository, domain model, and configuration.
- Use constructor injection over field injection for better testability and explicit dependencies.
- Keep `@Configuration` classes focused: group related beans and externalize property sources.
- Use `@Transactional` at the service layer, not the controller or repository layer.
- Prefer `application.yml` or `application.properties` with profile-specific files (`application-dev.yml`, `application-prod.yml`).
- Use `@ExceptionHandler` in `@ControllerAdvice` for consistent error responses.
- Keep auto-configuration simple; override only when the default behavior does not fit.
- Use `@Valid` and `@Validated` for request validation at the controller boundary.
- Structure packages by feature (e.g., `order/`, `payment/`, `user/`) rather than by layer.

## Common Risks

- Overusing `@Autowired` with field injection, making classes hard to unit test.
- Putting business logic in controllers or configuration classes.
- Large `Application.java` classes with too many `@Bean` definitions.
- Ignoring profile-specific configuration, leading to environment-specific bugs.
- Over-relying on Spring Boot auto-configuration magic without understanding what is being configured.
