/**
 * Tests for Buffer — validates the refactored explicit-context implementation.
 *
 * Compile:
 *   gcc -Wall -Wextra -o test_buffer test_buffer.c ../after/buffer.c
 * Run:
 *   ./test_buffer
 */

#include "../after/buffer.h"
#include <assert.h>
#include <string.h>
#include <stdio.h>

static int tests_passed = 0;
static int tests_failed = 0;

#define TEST(name) do { printf("  TEST: %s ... ", name); } while(0)
#define PASS() do { printf("PASS\n"); tests_passed++; } while(0)
#define FAIL(msg) do { printf("FAIL: %s\n", msg); tests_failed++; } while(0)

void test_create_and_destroy(void) {
    TEST("create and destroy");
    Buffer *buf = buffer_create(1024);
    assert(buf != NULL);
    assert(buffer_ok(buf));
    buffer_destroy(buf);
    PASS();
}

void test_write_and_flush(void) {
    TEST("write and flush");
    Buffer *buf = buffer_create(1024);
    const char *data = "Hello";
    assert(buffer_write(buf, data, 5));
    assert(buffer_ok(buf));
    /* flush writes to stdout — we can't easily capture that,
     * but we can verify the buffer is reset after flush */
    buffer_flush(buf);
    assert(buffer_ok(buf));
    buffer_destroy(buf);
    PASS();
}

void test_overflow_detection(void) {
    TEST("overflow detection");
    Buffer *buf = buffer_create(10);
    const char *data = "This is too long for the buffer";
    assert(!buffer_write(buf, data, strlen(data)));
    assert(!buffer_ok(buf));  /* error flag set */
    buffer_destroy(buf);
    PASS();
}

void test_multiple_writes(void) {
    TEST("multiple writes");
    Buffer *buf = buffer_create(100);
    assert(buffer_write(buf, "Hello", 5));
    assert(buffer_write(buf, " ", 1));
    assert(buffer_write(buf, "World", 5));
    assert(buffer_ok(buf));
    buffer_flush(buf);
    buffer_destroy(buf);
    PASS();
}

void test_empty_buffer_flush(void) {
    TEST("empty buffer flush");
    Buffer *buf = buffer_create(100);
    buffer_flush(buf);  /* should not crash or error */
    assert(buffer_ok(buf));
    buffer_destroy(buf);
    PASS();
}

void test_error_state_persists(void) {
    TEST("error state persists after overflow");
    Buffer *buf = buffer_create(5);
    assert(!buffer_write(buf, "TooLong", 7));
    assert(!buffer_ok(buf));
    /* Subsequent writes should also fail */
    assert(!buffer_write(buf, "Hi", 2));
    assert(!buffer_ok(buf));
    buffer_destroy(buf);
    PASS();
}

void test_destroy_null(void) {
    TEST("destroy NULL pointer");
    buffer_destroy(NULL);  /* should not crash */
    PASS();
}

int main(void) {
    printf("Buffer Tests\n");
    printf("============\n\n");

    test_create_and_destroy();
    test_write_and_flush();
    test_overflow_detection();
    test_multiple_writes();
    test_empty_buffer_flush();
    test_error_state_persists();
    test_destroy_null();

    printf("\nResults: %d passed, %d failed\n", tests_passed, tests_failed);
    return tests_failed > 0 ? 1 : 0;
}
