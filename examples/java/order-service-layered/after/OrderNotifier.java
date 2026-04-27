package com.example.order;

/** Notification adapter interface for order events. */
public interface OrderNotifier {
    void orderCreated(String userId, String orderId);
}
