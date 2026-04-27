package com.example.order;

import java.util.List;

/**
 * Use-case coordinator that delegates to separated concerns.
 * No longer mixes validation, pricing, persistence, and notification.
 */
public class OrderService {
    private final OrderValidator validator;
    private final PricingPolicy pricingPolicy;
    private final OrderRepository repository;
    private final OrderNotifier notifier;

    public OrderService(OrderValidator validator, PricingPolicy pricingPolicy,
                        OrderRepository repository, OrderNotifier notifier) {
        this.validator = validator;
        this.pricingPolicy = pricingPolicy;
        this.repository = repository;
        this.notifier = notifier;
    }

    public String createOrder(String userId, List<OrderItem> items, String couponCode) {
        validator.validate(userId, items);
        double total = pricingPolicy.calculateTotal(items, couponCode);
        String orderId = repository.save(userId, items, total);
        notifier.orderCreated(userId, orderId);
        return orderId;
    }
}
