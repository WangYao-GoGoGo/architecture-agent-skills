# Chain of Responsibility

## Intent
Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along until an object handles it.

## Use When
- More than one object may handle a request, and the handler is not known in advance.
- You want to issue a request to one of several objects without specifying the receiver explicitly.
- The set of handlers should be defined dynamically.

## Structure
- Handler defines an interface for handling requests and optionally implements the successor link.
- ConcreteHandler handles requests it is responsible for and forwards others to the successor.
- Client initiates the request to the first handler in the chain.

## Heuristics
1. **Default handler**: Always have a default handler at the end of the chain to handle unhandled requests.
2. **Break the chain**: A handler can decide to stop propagation or pass to the next handler.
3. **Dynamic chains**: Handlers can be added, removed, or reordered at runtime.
4. **Logging middleware**: Chain of Responsibility is the basis for middleware pipelines (Express, ASP.NET Core, etc.).

## Common Risks
1. **Unhandled requests**: If no handler processes the request and there's no default, the request is silently dropped.
2. **Performance**: Long chains add latency to every request.
3. **Debugging difficulty**: Tracing which handler processed a request can be hard.
4. **Handler ordering**: The order of handlers matters and incorrect ordering can cause bugs.

## Related Patterns
- **Composite**: Chain can be seen as a linear Composite.
- **Command**: Chain can process Command objects.
- **Decorator**: Similar structure. Decorator adds behavior; Chain forwards requests.
- **Mediator**: Mediator coordinates communication; Chain passes along a fixed path.
