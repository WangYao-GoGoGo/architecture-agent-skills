# Commands

## Run Original Code

```bash
# Compile the original god-class version
javac -d out before/OrderService.java

# Note: Requires OrderItem class and JDBC connection setup
# The original code is not runnable standalone — it needs a database
```

## Run Refactored Code

```bash
# Compile the refactored layered version
javac -d out after/OrderService.java after/OrderValidator.java after/PricingPolicy.java \
      after/OrderRepository.java after/OrderNotifier.java after/FixedDiscountPolicy.java

# Note: Requires OrderItem class and JDBC connection setup
```

## Run Tests

```bash
# If using Maven:
mvn test

# If using Gradle:
gradle test

# Manual compilation:
javac -d out tests/OrderServiceTest.java after/*.java
java -cp out com.example.order.OrderServiceTest
```

## Validate Behavior Preservation

The refactored code separates validation, pricing, persistence, and notification into distinct classes. The public API (`createOrder(String userId, List<OrderItem> items, String couponCode)`) remains unchanged.

Validation Level: **Static reasoning only** — requires a database to run end-to-end.
