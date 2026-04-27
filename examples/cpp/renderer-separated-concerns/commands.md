# Commands

## Run Original Code

```bash
g++ -std=c++11 -Wall -Wextra -c before/Renderer.cpp -o before/Renderer.o
```

Note: The original file defines a class only — it does not include a `main()` function. Compile as an object file.

## Run Refactored Code

```bash
# Compile the refactored version (if after/ files exist)
g++ -std=c++11 -Wall -Wextra -c after/*.cpp -o after/renderer.o 2>&1 || echo "No after/*.cpp files yet"
```

## Run Tests

```bash
g++ -std=c++11 -Wall -Wextra -o test_renderer tests/test_renderer.cpp before/Renderer.cpp && ./test_renderer
```

## Validate Behavior Preservation

The refactoring separates window management, shader compilation, mesh loading, and rendering into distinct classes. The public API should remain compatible.

Validation Level: **Static reasoning only** — requires OpenGL context to run end-to-end.
