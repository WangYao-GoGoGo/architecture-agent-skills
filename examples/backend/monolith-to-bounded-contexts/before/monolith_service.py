# Before: A monolithic service that handles users, orders, and payments
# in one module — no clear boundaries between domains.

class MonolithService:
    def __init__(self, db):
        self.db = db

    def create_user_and_order(self, user_data, order_data, payment_data):
        # User creation
        user_id = self.db.insert("users", user_data)

        # Order creation
        order_id = self.db.insert("orders", {**order_data, "user_id": user_id})

        # Payment processing
        payment_id = self.db.insert("payments", {**payment_data, "order_id": order_id})

        # Inventory update
        for item in order_data["items"]:
            self.db.execute("UPDATE products SET stock = stock - 1 WHERE id = ?", [item["product_id"]])

        # Notification
        self.db.insert("notifications", {
            "user_id": user_id,
            "type": "order_confirmation",
            "message": f"Order {order_id} created"
        })

        return {"user_id": user_id, "order_id": order_id, "payment_id": payment_id}
