# Payment Processor Refactor

This example refactors a large conditional into small payment strategies. The design pressure is behavior variation by payment method.

## Recommended Pattern

- Pattern: Strategy
- Supporting structure: small factory for method lookup
- Why: each payment method has different validation and execution rules
- Overengineering check: keep strategies small and do not add inheritance beyond the shared protocol

## Refactored Code

```python
from typing import Protocol


class PaymentStrategy(Protocol):
    def pay(self, amount: int, user: dict) -> dict:
        ...


class CreditCardPayment:
    def pay(self, amount: int, user: dict) -> dict:
        if not user.get("card_token"):
            raise ValueError("Missing card token")
        print(f"Charging card {user['card_token']} for {amount}")
        return {"status": "paid", "provider": "card"}


class PaypalPayment:
    def pay(self, amount: int, user: dict) -> dict:
        if not user.get("paypal_email"):
            raise ValueError("Missing PayPal email")
        print(f"Charging PayPal {user['paypal_email']} for {amount}")
        return {"status": "paid", "provider": "paypal"}


class BankTransferPayment:
    def pay(self, amount: int, user: dict) -> dict:
        if not user.get("bank_account"):
            raise ValueError("Missing bank account")
        print(f"Creating bank transfer from {user['bank_account']} for {amount}")
        return {"status": "pending", "provider": "bank"}


class PaymentStrategyFactory:
    def __init__(self) -> None:
        self._strategies = {
            "credit_card": CreditCardPayment(),
            "paypal": PaypalPayment(),
            "bank_transfer": BankTransferPayment(),
        }

    def get(self, method: str) -> PaymentStrategy:
        try:
            return self._strategies[method]
        except KeyError as exc:
            raise ValueError(f"Unsupported payment method: {method}") from exc


class PaymentProcessor:
    def __init__(self, factory: PaymentStrategyFactory) -> None:
        self._factory = factory

    def pay(self, method: str, amount: int, user: dict) -> dict:
        strategy = self._factory.get(method)
        return strategy.pay(amount, user)
```

## Why This Is Better

- `PaymentProcessor` coordinates the use case instead of owning every payment rule.
- Each payment method can be tested independently.
- Adding a method does not require editing a long conditional.
- Unsupported methods still fail in one predictable place.

## Verification Ideas

- Existing supported methods return the same statuses and providers.
- Missing user fields still raise `ValueError`.
- Unknown methods still raise `ValueError`.
- Adding a new method requires adding a strategy and registering it in the factory.
