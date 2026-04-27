#include "buffer.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Buffer {
    char *data;
    size_t capacity;
    size_t pos;
    bool has_error;
};

Buffer *buffer_create(size_t capacity) {
    Buffer *buf = malloc(sizeof(Buffer));
    if (!buf) return NULL;
    buf->data = malloc(capacity);
    if (!buf->data) {
        free(buf);
        return NULL;
    }
    buf->capacity = capacity;
    buf->pos = 0;
    buf->has_error = false;
    return buf;
}

void buffer_destroy(Buffer *buf) {
    if (buf) {
        free(buf->data);
        free(buf);
    }
}

bool buffer_write(Buffer *buf, const char *data, size_t len) {
    if (buf->pos + len > buf->capacity) {
        buf->has_error = true;
        return false;
    }
    memcpy(buf->data + buf->pos, data, len);
    buf->pos += len;
    return true;
}

void buffer_flush(Buffer *buf) {
    if (buf->has_error) {
        fprintf(stderr, "Cannot flush: buffer error\n");
        return;
    }
    for (size_t i = 0; i < buf->pos; i++) {
        putchar(buf->data[i]);
    }
    buf->pos = 0;
}

bool buffer_ok(const Buffer *buf) {
    return !buf->has_error;
}
