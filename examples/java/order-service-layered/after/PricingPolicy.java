package com.example.order;

import java.util.List;

/** Strategy interface for pricing calculations. */
public interface PricingPolicy {
    double calculateTotal(List<OrderItem> items, String couponCode);
}
