"""After: Strategy pattern — each payment method is a separate strategy class."""

from typing import Protocol


class PaymentStrategy(Protocol):
    """Interface for all payment strategies."""

    def pay(self, amount: int, user: dict) -> dict:
        ...


class CreditCardPayment:
    """Handles credit card payments."""

    def pay(self, amount: int, user: dict) -> dict:
        if not user.get("card_token"):
            raise ValueError("Missing card token")
        print(f"Charging card {user['card_token']} for {amount}")
        return {"status": "paid", "provider": "card"}


class PaypalPayment:
    """Handles PayPal payments."""

    def pay(self, amount: int, user: dict) -> dict:
        if not user.get("paypal_email"):
            raise ValueError("Missing PayPal email")
        print(f"Charging PayPal {user['paypal_email']} for {amount}")
        return {"status": "paid", "provider": "paypal"}


class BankTransferPayment:
    """Handles bank transfer payments."""

    def pay(self, amount: int, user: dict) -> dict:
        if not user.get("bank_account"):
            raise ValueError("Missing bank account")
        print(f"Creating bank transfer from {user['bank_account']} for {amount}")
        return {"status": "pending", "provider": "bank"}


class PaymentStrategyFactory:
    """Factory that maps method names to strategy instances."""

    def __init__(self) -> None:
        self._strategies: dict[str, PaymentStrategy] = {
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
    """Use-case coordinator that delegates to the appropriate strategy."""

    def __init__(self, factory: PaymentStrategyFactory) -> None:
        self._factory = factory

    def pay(self, method: str, amount: int, user: dict) -> dict:
        strategy = self._factory.get(method)
        return strategy.pay(amount, user)
