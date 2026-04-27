# Order Service Refactor

Refactored from a god class into a layered architecture with separated responsibilities.

## Design Pressure

- `OrderService` mixed validation, pricing, persistence, and notification in one method.
- Transaction boundary was unclear — rollback logic was duplicated.
- Notification side effect was coupled to order creation, making testing hard.
- Coupon logic used string comparison — adding a new coupon required editing the service.

## Applied Pattern

**Layered architecture + Strategy** — the service becomes a use-case coordinator. Validation, pricing, persistence, and notification each get their own abstraction.

## After Structure

```
com.example.order/
├── OrderService.java          # Use-case coordinator
├── OrderValidator.java        # Validation rules
├── PricingPolicy.java         # Strategy interface for pricing
├── FixedDiscountPolicy.java   # Concrete discount strategy
├── OrderRepository.java       # Persistence boundary
├── OrderNotifier.java         # Notification adapter interface
└── EmailNotifier.java         # Concrete email implementation
```

### `OrderService.java`

```java
package com.example.order;

public class OrderService {
    private final OrderValidator validator;
    private final PricingPolicy pricingPolicy;
    private final OrderRepository repository;
    private final OrderNotifier notifier;

    public OrderService(OrderValidator validator, PricingPolicy pricingPolicy,
                        OrderRepository repository, OrderNotifier notifier) {
        this.validator = validator;
        this.pricingPolicy = pricingPolicy;
        this.repository = repository;
        this.notifier = notifier;
    }

    public String createOrder(String userId, List<OrderItem> items, String couponCode) {
        validator.validate(userId, items);
        double total = pricingPolicy.calculateTotal(items, couponCode);
        String orderId = repository.save(userId, items, total);
        notifier.orderCreated(userId, orderId);
        return orderId;
    }
}
```

### `OrderValidator.java`

```java
package com.example.order;

import java.util.List;

public class OrderValidator {
    public void validate(String userId, List<OrderItem> items) {
        if (userId == null || userId.isBlank()) {
            throw new IllegalArgumentException("User ID is required");
        }
        if (items == null || items.isEmpty()) {
            throw new IllegalArgumentException("Order must have at least one item");
        }
    }
}
```

### `PricingPolicy.java`

```java
package com.example.order;

import java.util.List;

public interface PricingPolicy {
    double calculateTotal(List<OrderItem> items, String couponCode);
}
```

### `FixedDiscountPolicy.java`

```java
package com.example.order;

import java.util.List;
import java.util.Map;

public class FixedDiscountPolicy implements PricingPolicy {
    private static final Map<String, Double> DISCOUNTS = Map.of(
        "SAVE10", 0.10,
        "SAVE20", 0.20
    );

    @Override
    public double calculateTotal(List<OrderItem> items, String couponCode) {
        double subtotal = items.stream()
            .mapToDouble(i -> i.getPrice() * i.getQuantity())
            .sum();
        double discount = DISCOUNTS.getOrDefault(couponCode, 0.0);
        return subtotal * (1 - discount);
    }
}
```

### `OrderRepository.java`

```java
package com.example.order;

import java.util.List;

public interface OrderRepository {
    String save(String userId, List<OrderItem> items, double total);
}
```

### `OrderNotifier.java`

```java
package com.example.order;

public interface OrderNotifier {
    void orderCreated(String userId, String orderId);
}
```

## Verification

- Order creation behavior is preserved (same DB schema, same return value).
- Invalid orders still fail with the same exception types.
- Pricing rules are independently testable without a database.
- Notification failure does not roll back the transaction.
- Adding a new coupon requires only adding to the `DISCOUNTS` map.
