# Proxy

## Intent
Provide a surrogate or placeholder for another object to control access to it.

## Use When
- You need lazy initialization (virtual proxy) — create expensive objects on demand.
- You need access control (protection proxy) — check permissions before delegating.
- You need logging or auditing (logging proxy).
- You need remote communication (remote proxy) — local representative for a remote object.
- You need caching (caching proxy) — return cached results.

## Structure
- Subject defines the common interface for RealSubject and Proxy.
- RealSubject is the real object that the proxy represents.
- Proxy maintains a reference to RealSubject and controls access to it.

## Heuristics
1. **Same interface**: Proxy implements the same interface as RealSubject, so clients can't tell the difference.
2. **Keep proxy transparent**: The proxy should add its behavior (lazy loading, access control) without changing the semantics.
3. **Proxy vs Decorator**: Proxy controls access; Decorator adds behavior. Proxy creates/manages the RealSubject; Decorator is given the Component.
4. **Virtual proxy**: Delay creation until the first time a method is called.

## Common Risks
1. **Performance overhead**: Each method call goes through the proxy, adding indirection.
2. **Transparency violations**: If the proxy's behavior (e.g., lazy loading) causes different timing or errors, transparency is broken.
3. **Proxy chain**: Multiple proxies wrapping each other make debugging difficult.
4. **State synchronization**: Remote proxies must handle network failures and state synchronization.

## Related Patterns
- **Decorator**: Similar structure. Proxy controls access; Decorator adds behavior.
- **Adapter**: Adapter changes interface; Proxy preserves interface.
- **Facade**: Facade provides a simplified interface; Proxy provides the same interface.
