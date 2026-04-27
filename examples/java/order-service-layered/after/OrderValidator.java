package com.example.order;

import java.util.List;

/** Validates order creation inputs. */
public class OrderValidator {
    public void validate(String userId, List<OrderItem> items) {
        if (userId == null || userId.isBlank()) {
            throw new IllegalArgumentException("User ID is required");
        }
        if (items == null || items.isEmpty()) {
            throw new IllegalArgumentException("Order must have at least one item");
        }
    }
}
