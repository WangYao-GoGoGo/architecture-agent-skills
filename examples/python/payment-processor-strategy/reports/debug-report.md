# Debug Report: Payment Processor

## 1. Original Problem

The `PaymentProcessor.pay()` method uses a large `if-elif` conditional chain to handle different payment methods. This makes the class hard to extend, test, and maintain. Adding a new payment method requires editing the existing chain, which risks breaking existing behavior.

## 2. Root Cause

The design violates the Open/Closed Principle — the class is not open for extension without modification. All payment logic is coupled in a single method, making it impossible to test individual payment methods independently.

## 3. Fix Summary

Refactored the large conditional into the Strategy pattern:

- Extracted each payment method into its own strategy class (`CreditCardPayment`, `PaypalPayment`, `BankTransferPayment`).
- Created a `PaymentStrategyFactory` to map method names to strategy instances.
- Simplified `PaymentProcessor.pay()` to delegate to the factory.

## 4. Files Changed

| File | Change |
|---|---|
| `before/payment_processor.py` | Original — 21-line if-elif chain |
| `after/payment_processor.py` | Refactored — Strategy pattern with 6 classes |

## 5. Validation Commands

```bash
python -m pytest tests/ -v
```

## 6. Validation Results

All 7 test cases pass identically for both the original and refactored implementations:

- Credit card success
- PayPal success
- Bank transfer success
- Missing card token (error)
- Missing PayPal email (error)
- Missing bank account (error)
- Unsupported method (error)

## 7. Behavior Preservation Notes

✅ Behavior preserved — all inputs produce identical outputs and errors.

## 8. Remaining Risks

- No integration tests with actual payment gateways.
- The factory uses hardcoded strategy instances — dynamic registration would be needed for plugin architectures.

## 9. Follow-up Recommendations

- Add integration tests if payment gateways are involved.
- Consider using dependency injection for the factory in larger systems.
