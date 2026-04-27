#ifndef BUFFER_H
#define BUFFER_H

#include <stddef.h>
#include <stdbool.h>

/* Opaque struct type — implementation hidden in buffer.c */
typedef struct Buffer Buffer;

/* Lifecycle */
Buffer *buffer_create(size_t capacity);
void buffer_destroy(Buffer *buf);

/* Operations */
bool buffer_write(Buffer *buf, const char *data, size_t len);
void buffer_flush(Buffer *buf);
bool buffer_ok(const Buffer *buf);

#endif
