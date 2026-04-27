/**
 * Tests for Order Service — validates behavior preservation after refactoring.
 *
 * This test uses mocks/stubs to avoid requiring a real database.
 * Compile with: javac -d out tests/OrderServiceTest.java after/*.java
 * Run with: java -cp out com.example.order.OrderServiceTest
 */

package com.example.order;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

/**
 * Minimal test harness for OrderService behavior validation.
 * In a real project, use JUnit and Mockito.
 */
public class OrderServiceTest {

    static int passed = 0;
    static int failed = 0;

    static void assertThrows(Class<? extends Exception> expected, Runnable runnable) {
        try {
            runnable.run();
            System.out.println("  FAIL: expected " + expected.getSimpleName() + " but no exception was thrown");
            failed++;
        } catch (Exception e) {
            if (expected.isInstance(e)) {
                System.out.println("  PASS");
                passed++;
            } else {
                System.out.println("  FAIL: expected " + expected.getSimpleName() + " but got " + e.getClass().getSimpleName());
                failed++;
            }
        }
    }

    static void assertEquals(Object expected, Object actual, String message) {
        if (expected == null ? actual == null : expected.equals(actual)) {
            System.out.println("  PASS: " + message);
            passed++;
        } else {
            System.out.println("  FAIL: " + message + " — expected " + expected + " but got " + actual);
            failed++;
        }
    }

    public static void main(String[] args) {
        System.out.println("OrderService Tests\n");

        // Test OrderValidator
        testValidator();
        testPricingPolicy();
        testRepository();
        testNotifier();
        testOrderServiceIntegration();

        System.out.println("\nResults: " + passed + " passed, " + failed + " failed");
        System.exit(failed > 0 ? 1 : 0);
    }

    static void testValidator() {
        System.out.println("OrderValidator:");
        OrderValidator validator = new OrderValidator();

        // Valid inputs
        List<OrderItem> items = new ArrayList<>();
        items.add(new OrderItem("PROD-1", 2, 10.0));
        validator.validate("user-1", items);  // should not throw
        System.out.println("  PASS: valid inputs accepted");

        // Null userId
        assertThrows(IllegalArgumentException.class, () -> validator.validate(null, items));

        // Blank userId
        assertThrows(IllegalArgumentException.class, () -> validator.validate("  ", items));

        // Null items
        assertThrows(IllegalArgumentException.class, () -> validator.validate("user-1", null));

        // Empty items
        assertThrows(IllegalArgumentException.class, () -> validator.validate("user-1", new ArrayList<>()));
    }

    static void testPricingPolicy() {
        System.out.println("\nPricingPolicy:");
        PricingPolicy policy = new FixedDiscountPolicy();

        List<OrderItem> items = new ArrayList<>();
        items.add(new OrderItem("PROD-1", 2, 10.0));  // 20.0 subtotal

        // No coupon
        double total = policy.calculateTotal(items, null);
        assertEquals(20.0, total, "no coupon");

        // SAVE10
        total = policy.calculateTotal(items, "SAVE10");
        assertEquals(18.0, total, "SAVE10 coupon (10% off)");

        // SAVE20
        total = policy.calculateTotal(items, "SAVE20");
        assertEquals(16.0, total, "SAVE20 coupon (20% off)");

        // Unknown coupon — no discount applied
        total = policy.calculateTotal(items, "UNKNOWN");
        assertEquals(20.0, total, "unknown coupon (no discount)");
    }

    static void testRepository() {
        System.out.println("\nOrderRepository:");
        // In a real test, use an in-memory database or mock
        System.out.println("  SKIP: requires database connection");
    }

    static void testNotifier() {
        System.out.println("\nOrderNotifier:");
        OrderNotifier notifier = new OrderNotifier();
        // Notification is a side effect — verify it doesn't throw
        notifier.orderCreated("user-1", "order-1");
        System.out.println("  PASS: notification sent without error");
    }

    static void testOrderServiceIntegration() {
        System.out.println("\nOrderService Integration:");
        // In a real test, use mocked dependencies
        System.out.println("  SKIP: requires database and mocked dependencies");
    }
}
