package com.example.order;

import java.util.List;
import java.util.Map;

/** Concrete pricing strategy using a fixed discount map. */
public class FixedDiscountPolicy implements PricingPolicy {
    private static final Map<String, Double> DISCOUNTS = Map.of(
        "SAVE10", 0.10,
        "SAVE20", 0.20
    );

    @Override
    public double calculateTotal(List<OrderItem> items, String couponCode) {
        double subtotal = items.stream()
            .mapToDouble(i -> i.getPrice() * i.getQuantity())
            .sum();
        double discount = DISCOUNTS.getOrDefault(couponCode, 0.0);
        return subtotal * (1 - discount);
    }
}
