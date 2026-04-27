# Service Boundary Extraction

Refactored from a monolithic service into bounded contexts with clear domain boundaries.

## Design Pressure

- `MonolithService` handled users, orders, payments, inventory, and notifications.
- No separation of concerns — changing payment logic risked breaking user creation.
- No transaction boundaries — partial failures could leave inconsistent state.
- Testing required the entire database.

## Applied Pattern

**Bounded contexts + domain events** — each domain (User, Order, Payment, Inventory, Notification) gets its own service. Cross-domain communication happens via events.

## After Code

### `user_service.py`

```python
class UserService:
    def __init__(self, db):
        self.db = db

    def create_user(self, user_data):
        return self.db.insert("users", user_data)
```

### `order_service.py`

```python
class OrderService:
    def __init__(self, db, event_bus):
        self.db = db
        self.event_bus = event_bus

    def create_order(self, user_id, order_data):
        order_id = self.db.insert("orders", {**order_data, "user_id": user_id})
        self.event_bus.publish("order.created", {"order_id": order_id, "user_id": user_id, "items": order_data["items"]})
        return order_id
```

### `payment_service.py`

```python
class PaymentService:
    def __init__(self, db):
        self.db = db

    def process_payment(self, order_id, payment_data):
        return self.db.insert("payments", {**payment_data, "order_id": order_id})
```

### `inventory_service.py`

```python
class InventoryService:
    def __init__(self, db, event_bus):
        self.db = db
        event_bus.subscribe("order.created", self.handle_order_created)

    def handle_order_created(self, event):
        for item in event["items"]:
            self.db.execute("UPDATE products SET stock = stock - 1 WHERE id = ?", [item["product_id"]])
```

### `notification_service.py`

```python
class NotificationService:
    def __init__(self, db, event_bus):
        self.db = db
        event_bus.subscribe("order.created", self.handle_order_created)

    def handle_order_created(self, event):
        self.db.insert("notifications", {
            "user_id": event["user_id"],
            "type": "order_confirmation",
            "message": f"Order {event['order_id']} created"
        })
```

### Orchestrator (e.g., API handler or saga)

```python
class OrderOrchestrator:
    def __init__(self, user_svc, order_svc, payment_svc):
        self.user_svc = user_svc
        self.order_svc = order_svc
        self.payment_svc = payment_svc

    def place_order(self, user_data, order_data, payment_data):
        user_id = self.user_svc.create_user(user_data)
        order_id = self.order_svc.create_order(user_id, order_data)
        payment_id = self.payment_svc.process_payment(order_id, payment_data)
        return {"user_id": user_id, "order_id": order_id, "payment_id": payment_id}
```

## Verification

- Each service is independently testable with its own database schema.
- Adding a new subscriber to `order.created` requires no changes to existing services.
- Transaction boundaries are explicit — each service manages its own writes.
- The orchestrator coordinates the workflow without owning domain logic.
- Event bus can be swapped for a message queue (RabbitMQ, Kafka) without changing services.
