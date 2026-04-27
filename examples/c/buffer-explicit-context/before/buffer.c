/* Before: Global state makes the module untestable and non-reentrant.
 * The buffer size, current position, and error flag are all module-level globals.
 */

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define BUFFER_SIZE 1024

static char buffer[BUFFER_SIZE];
static size_t pos = 0;
static bool has_error = false;

void write_data(const char *data, size_t len) {
    if (pos + len > BUFFER_SIZE) {
        has_error = true;
        return;
    }
    memcpy(buffer + pos, data, len);
    pos += len;
}

void flush_buffer(void) {
    if (has_error) {
        fprintf(stderr, "Cannot flush: buffer error\n");
        return;
    }
    for (size_t i = 0; i < pos; i++) {
        putchar(buffer[i]);
    }
    pos = 0;
}

bool is_buffer_ok(void) {
    return !has_error;
}
