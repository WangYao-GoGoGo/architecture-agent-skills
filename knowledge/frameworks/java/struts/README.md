# Struts Knowledge

## Heuristics

- Keep Action classes focused on orchestration: delegate business logic to service classes.
- Use ActionForm (or POJO input) for request data binding; validate in the `validate()` method or with a validator framework.
- Separate configuration in `struts-config.xml`: keep action mappings, form beans, and forwards organized by module.
- Use `DispatchAction` or `LookupDispatchAction` when multiple operations share the same Action class.
- Prefer declarative validation (Validator framework or annotation-based) over imperative validation in Action classes.
- Use Tiles or similar templating for consistent page layouts.
- Keep `ActionForward` names meaningful and consistent across the application.
- Use interceptors (filters) for cross-cutting concerns like authentication, logging, and encoding.

## Common Risks

- Action classes that contain business logic instead of delegating to services.
- Overly complex `struts-config.xml` files that are hard to maintain.
- Tight coupling between Action classes and the Servlet API.
- Mixing presentation logic with business logic in ActionForms.
- Ignoring thread safety: Action classes are singletons by default; instance variables must be handled carefully.
