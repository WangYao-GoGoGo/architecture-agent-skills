"""Tests for Monolith Service — validates behavior preservation after refactoring."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "before"))

from monolith_service import MonolithService


class FakeDB:
    """In-memory database stub for testing."""
    def __init__(self):
        self.tables = {}
        self.id_counter = 0

    def insert(self, table, data):
        self.id_counter += 1
        record = {"id": self.id_counter, **data}
        if table not in self.tables:
            self.tables[table] = []
        self.tables[table].append(record)
        return self.id_counter

    def execute(self, query, params=None):
        pass  # no-op for testing


class TestMonolithService:
    def setup_method(self):
        self.db = FakeDB()
        self.service = MonolithService(self.db)

    def test_create_user_and_order(self):
        result = self.service.create_user_and_order(
            {"name": "Alice", "email": "alice@example.com"},
            {"items": [{"product_id": 1, "quantity": 2}]},
            {"amount": 100, "method": "credit_card"}
        )

        assert "user_id" in result
        assert "order_id" in result
        assert "payment_id" in result
        assert result["user_id"] == 1
        assert result["order_id"] == 2
        assert result["payment_id"] == 3

    def test_all_tables_have_records(self):
        result = self.service.create_user_and_order(
            {"name": "Bob"},
            {"items": [{"product_id": 2, "quantity": 1}]},
            {"amount": 50, "method": "paypal"}
        )

        assert "users" in self.db.tables
        assert "orders" in self.db.tables
        assert "payments" in self.db.tables
        assert "notifications" in self.db.tables

    def test_multiple_orders(self):
        for i in range(3):
            result = self.service.create_user_and_order(
                {"name": f"User{i}"},
                {"items": [{"product_id": i, "quantity": 1}]},
                {"amount": 100 * i, "method": "card"}
            )
            assert result["user_id"] == i * 3 + 1
            assert result["order_id"] == i * 3 + 2
            assert result["payment_id"] == i * 3 + 3
