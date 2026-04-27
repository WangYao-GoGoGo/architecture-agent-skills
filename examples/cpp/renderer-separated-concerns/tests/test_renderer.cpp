/**
 * Tests for Renderer — validates the original god class behavior.
 *
 * Compile:
 *   g++ -std=c++11 -Wall -Wextra -o test_renderer test_renderer.cpp ../before/Renderer.cpp
 * Run:
 *   ./test_renderer
 */

#include "../before/Renderer.cpp"
#include <cassert>
#include <iostream>

static int tests_passed = 0;
static int tests_failed = 0;

#define TEST(name) do { std::cout << "  TEST: " << name << " ... "; } while(0)
#define PASS() do { std::cout << "PASS\n"; tests_passed++; } while(0)
#define FAIL(msg) do { std::cout << "FAIL: " << msg << "\n"; tests_failed++; } while(0)

void test_init_and_render() {
    TEST("init and render");
    Renderer renderer;
    renderer.init("Test Window", 800, 600);
    renderer.render();  // should not crash
    renderer.cleanup();
    PASS();
}

void test_multiple_init() {
    TEST("multiple init calls");
    Renderer renderer;
    renderer.init("First", 800, 600);
    renderer.init("Second", 1024, 768);
    renderer.render();
    renderer.cleanup();
    PASS();
}

void test_render_without_init() {
    TEST("render without init");
    Renderer renderer;
    // Should not crash — default state is valid
    renderer.render();
    renderer.cleanup();
    PASS();
}

void test_cleanup_without_init() {
    TEST("cleanup without init");
    Renderer renderer;
    renderer.cleanup();  // should not crash
    PASS();
}

int main() {
    std::cout << "Renderer Tests\n";
    std::cout << "==============\n\n";

    test_init_and_render();
    test_multiple_init();
    test_render_without_init();
    test_cleanup_without_init();

    std::cout << "\nResults: " << tests_passed << " passed, " << tests_failed << " failed\n";
    return tests_failed > 0 ? 1 : 0;
}
