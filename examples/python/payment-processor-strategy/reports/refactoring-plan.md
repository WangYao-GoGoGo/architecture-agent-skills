# Payment Processor Refactoring Plan

## Goal

Refactor the large conditional in `PaymentProcessor.pay()` into the Strategy pattern so each payment method is independently testable and adding a new method does not require editing the existing chain.

## Design Pressure

- **Behavior variation by payment method** — each method has different validation and execution rules.
- **Open/closed violation** — adding a new payment method requires editing the `if-elif` chain.
- **Testing friction** — cannot test a single payment method without the entire `PaymentProcessor`.

## Applied Pattern

- **Pattern**: Strategy
- **Supporting structure**: `PaymentStrategyFactory` for method lookup
- **Overengineering check**: strategies are kept small; no inheritance beyond the shared protocol

## Steps

1. Define `PaymentStrategy` protocol with a single `pay(amount, user)` method.
2. Extract each payment method into its own strategy class (`CreditCardPayment`, `PaypalPayment`, `BankTransferPayment`).
3. Create `PaymentStrategyFactory` to map method names to strategy instances.
4. Simplify `PaymentProcessor.pay()` to delegate to the factory.

## Before Structure

```
payment_processor.py
└── PaymentProcessor.pay()    # 21-line if-elif chain
```

## After Structure

```
payment_processor.py
├── PaymentStrategy (Protocol)       # Interface
├── CreditCardPayment                # Concrete strategy
├── PaypalPayment                    # Concrete strategy
├── BankTransferPayment              # Concrete strategy
├── PaymentStrategyFactory           # Factory
└── PaymentProcessor                 # Coordinator (delegates to factory)
```

## Verification

- Existing supported methods return the same statuses and providers.
- Missing user fields still raise `ValueError`.
- Unknown methods still raise `ValueError`.
- Adding a new method requires adding a strategy and registering it in the factory — no existing code changes.
