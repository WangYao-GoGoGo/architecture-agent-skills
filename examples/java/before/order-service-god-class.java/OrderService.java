/* Before: God class mixing validation, pricing, persistence, and notification. */

package com.example.order;

import java.sql.*;
import java.util.*;

public class OrderService {
    private Connection conn;

    public OrderService(Connection conn) {
        this.conn = conn;
    }

    public String createOrder(String userId, List<OrderItem> items, String couponCode) {
        // Validation mixed in
        if (userId == null || userId.isBlank()) {
            throw new IllegalArgumentException("User ID is required");
        }
        if (items == null || items.isEmpty()) {
            throw new IllegalArgumentException("Order must have at least one item");
        }

        // Pricing logic mixed in
        double total = 0;
        for (OrderItem item : items) {
            total += item.getPrice() * item.getQuantity();
        }
        if (couponCode != null && !couponCode.isBlank()) {
            if (couponCode.equals("SAVE10")) {
                total *= 0.9;
            } else if (couponCode.equals("SAVE20")) {
                total *= 0.8;
            }
        }

        // Persistence mixed in
        String orderId = UUID.randomUUID().toString();
        try {
            conn.setAutoCommit(false);

            PreparedStatement ps = conn.prepareStatement(
                "INSERT INTO orders (id, user_id, total, status) VALUES (?, ?, ?, ?)");
            ps.setString(1, orderId);
            ps.setString(2, userId);
            ps.setDouble(3, total);
            ps.setString(4, "CREATED");
            ps.executeUpdate();

            for (OrderItem item : items) {
                PreparedStatement ips = conn.prepareStatement(
                    "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)");
                ips.setString(1, orderId);
                ips.setString(2, item.getProductId());
                ips.setInt(3, item.getQuantity());
                ips.setDouble(4, item.getPrice());
                ips.executeUpdate();
            }

            conn.commit();
        } catch (SQLException e) {
            try { conn.rollback(); } catch (SQLException ignored) {}
            throw new RuntimeException("Order creation failed", e);
        }

        // Notification side effect mixed in
        System.out.println("Sending email to user " + userId + " for order " + orderId);
        // Imagine actual email sending code here

        return orderId;
    }
}
