# Order Service Refactor

Planned Java example for refactoring an order service that mixes validation, pricing, persistence, and notification.

Expected design pressure:

- service has too many responsibilities
- transaction boundary is unclear
- notification side effect is coupled to order persistence

Likely target structure:

- `OrderService` as use-case coordinator
- `OrderValidator` for validation rules
- `PricingPolicy` or `DiscountPolicy` for pricing variation
- `OrderRepository` for persistence boundary
- `OrderNotifier` adapter for notification side effects

Verification:

- order creation behavior is preserved
- invalid orders still fail
- pricing rules are independently testable
- notification failure behavior is explicit
