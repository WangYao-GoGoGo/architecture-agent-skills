package com.example.order;

import java.util.List;

/** Persistence boundary for orders. */
public interface OrderRepository {
    String save(String userId, List<OrderItem> items, double total);
}
