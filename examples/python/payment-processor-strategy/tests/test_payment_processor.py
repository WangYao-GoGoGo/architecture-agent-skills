"""Tests for Payment Processor — validates both before and after implementations."""

import sys
import os

# Add both before and after directories to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "before"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "after"))

from payment_processor import PaymentProcessor as BeforeProcessor
from payment_processor import (
    PaymentProcessor as AfterProcessor,
    PaymentStrategyFactory,
)


def make_before_processor():
    return BeforeProcessor()


def make_after_processor():
    return AfterProcessor(PaymentStrategyFactory())


class TestPaymentProcessor:
    """Test suite that runs against both before and after implementations."""

    def _run_tests(self, processor):
        # Normal cases
        result = processor.pay("credit_card", 100, {"card_token": "tok_123"})
        assert result == {"status": "paid", "provider": "card"}, f"Expected paid, got {result}"

        result = processor.pay("paypal", 200, {"paypal_email": "a@b.com"})
        assert result == {"status": "paid", "provider": "paypal"}, f"Expected paid, got {result}"

        result = processor.pay("bank_transfer", 300, {"bank_account": "ACC-001"})
        assert result == {"status": "pending", "provider": "bank"}, f"Expected pending, got {result}"

        # Error cases
        import pytest
        with pytest.raises(ValueError, match="Missing card token"):
            processor.pay("credit_card", 100, {})

        with pytest.raises(ValueError, match="Missing PayPal email"):
            processor.pay("paypal", 200, {})

        with pytest.raises(ValueError, match="Missing bank account"):
            processor.pay("bank_transfer", 300, {})

        with pytest.raises(ValueError, match="Unsupported payment method"):
            processor.pay("bitcoin", 100, {})

    def test_before(self):
        self._run_tests(make_before_processor())

    def test_after(self):
        self._run_tests(make_after_processor())
