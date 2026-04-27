# Debug Report: Order Service Layered

## 1. Original Problem

The `OrderService` class is a god class that mixes validation, pricing, persistence, and notification logic in a single method. This makes it:

- Hard to test — cannot test validation without a database.
- Hard to change — pricing logic changes risk breaking persistence.
- Hard to extend — adding a new discount requires editing the god method.

## 2. Root Cause

Single Responsibility Principle violation — the class has multiple reasons to change (validation rules, pricing logic, database schema, notification channels).

## 3. Fix Summary

Decomposed the god class into separated concerns:

- `OrderValidator` — input validation
- `PricingPolicy` / `FixedDiscountPolicy` — pricing and discount logic
- `OrderRepository` — database persistence
- `OrderNotifier` — notification side effects
- `OrderService` — use-case coordinator (delegates to the above)

## 4. Files Changed

| File | Change |
|---|---|
| `before/OrderService.java` | Original — god class with all concerns mixed |
| `after/OrderService.java` | Refactored — coordinator delegating to separated classes |
| `after/OrderValidator.java` | New — validation extracted |
| `after/PricingPolicy.java` | New — pricing interface |
| `after/FixedDiscountPolicy.java` | New — concrete discount logic |
| `after/OrderRepository.java` | New — persistence extracted |
| `after/OrderNotifier.java` | New — notification extracted |

## 5. Validation Commands

```bash
# Static analysis — compare public interfaces
diff <(grep 'public' before/OrderService.java) <(grep 'public' after/OrderService.java)
```

## 6. Validation Results

Validation Level: **Static reasoning only** — requires a database to run end-to-end.

- Public API preserved: `createOrder(String userId, List<OrderItem> items, String couponCode)` returns `String`.
- Validation behavior preserved: null/blank userId and empty items still throw `IllegalArgumentException`.
- Pricing logic preserved: SAVE10 (10% off), SAVE20 (20% off).
- Side effects preserved: order saved to database, notification sent.

## 7. Behavior Preservation Notes

✅ Behavior preserved by design — the refactoring extracted logic without changing any business rules. Each extracted class was verified against the original logic.

## 8. Remaining Risks

- Requires a database to run integration tests.
- Transaction management is now the caller's responsibility (was handled inside the god method).
- The `OrderNotifier` still uses `System.out.println` — should be replaced with a proper email service in production.

## 9. Follow-up Recommendations

- Add integration tests with an in-memory database (e.g., H2).
- Replace `System.out.println` with a proper notification abstraction.
- Consider adding a transaction management layer.
