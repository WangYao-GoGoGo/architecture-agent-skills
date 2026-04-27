# Global State → Explicit Context

Refactored from module-level globals to an explicit context struct passed by pointer.

## Design Pressure

- Global state prevents multiple buffer instances (non-reentrant).
- Unit tests cannot run in parallel or isolate state.
- Error flag is implicit — caller must remember to check it.

## Applied Pattern

**Opaque struct + explicit context** — the buffer state is bundled into a struct, allocated by the caller, and passed to every function. The struct definition is hidden in the `.c` file; the header exposes only the pointer type.

## After Code

### `buffer.h` — Public interface

```c
#ifndef BUFFER_H
#define BUFFER_H

#include <stddef.h>
#include <stdbool.h>

typedef struct Buffer Buffer;

Buffer *buffer_create(size_t capacity);
void buffer_destroy(Buffer *buf);

bool buffer_write(Buffer *buf, const char *data, size_t len);
void buffer_flush(Buffer *buf);
bool buffer_ok(const Buffer *buf);

#endif
```

### `buffer.c` — Implementation

```c
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
```

## Verification

- Multiple `Buffer` instances can be created and used independently.
- Thread-safety is now possible (caller controls locking per instance).
- Tests can create a buffer, write, flush, and destroy without affecting other tests.
- Memory ownership is explicit: caller creates and destroys.
