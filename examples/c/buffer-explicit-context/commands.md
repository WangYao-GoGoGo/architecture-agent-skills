# Commands

## Run Original Code

```bash
cd before && gcc -Wall -Wextra -o buffer_test buffer.c 2>&1 || echo "No main() — compile as object file"
```

The original file defines functions only — it does not include a `main()` function. Compile as an object file:

```bash
gcc -Wall -Wextra -c before/buffer.c -o before/buffer.o
```

## Run Refactored Code

```bash
gcc -Wall -Wextra -c after/buffer.c -o after/buffer.o
```

## Run Tests

```bash
gcc -Wall -Wextra -o test_buffer tests/test_buffer.c after/buffer.c && ./test_buffer
```

## Validate Behavior Preservation

The refactored code replaces global state with an explicit `Buffer` struct. All operations are preserved:

- `buffer_write()` replaces `write_data()`
- `buffer_flush()` replaces `flush_buffer()`
- `buffer_ok()` replaces `is_buffer_ok()`
