class PaymentProcessor:
    def pay(self, method, amount, user):
        if method == "credit_card":
            if not user.get("card_token"):
                raise ValueError("Missing card token")
            print(f"Charging card {user['card_token']} for {amount}")
            return {"status": "paid", "provider": "card"}

        if method == "paypal":
            if not user.get("paypal_email"):
                raise ValueError("Missing PayPal email")
            print(f"Charging PayPal {user['paypal_email']} for {amount}")
            return {"status": "paid", "provider": "paypal"}

        if method == "bank_transfer":
            if not user.get("bank_account"):
                raise ValueError("Missing bank account")
            print(f"Creating bank transfer from {user['bank_account']} for {amount}")
            return {"status": "pending", "provider": "bank"}

        raise ValueError(f"Unsupported payment method: {method}")
