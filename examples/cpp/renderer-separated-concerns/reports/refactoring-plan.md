# God Class → Separated Concerns

Refactored a monolithic `Renderer` class into focused components with clear ownership.

## Design Pressure

- `Renderer` owned window creation, shader compilation, mesh data, and rendering loop.
- No way to swap shaders or use different meshes.
- Resource cleanup was manual and error-prone.
- Testing required the full rendering pipeline.

## Applied Pattern

**Single Responsibility + RAII** — each concern gets its own class. Resources are owned via RAII wrappers.

## After Structure

```
renderer/
├── Window.h / Window.cpp       # Window creation and lifecycle
├── Shader.h / Shader.cpp       # Shader compilation and program management
├── Mesh.h / Mesh.cpp           # Vertex data and buffer management
└── Renderer.h / Renderer.cpp   # Coordinates rendering with injected dependencies
```

### `Window.h`

```cpp
#pragma once
#include <string>

class Window {
public:
    Window(const std::string &title, int width, int height);
    ~Window();

    void clear();
    void swap();
    bool shouldClose() const;

private:
    int handle_ = 0;
};
```

### `Shader.h`

```cpp
#pragma once
#include <string>

class Shader {
public:
    Shader(const std::string &vertexSrc, const std::string &fragmentSrc);
    ~Shader();

    void use() const;

private:
    int program_ = 0;
    int compile(const std::string &src, int type) const;
};
```

### `Mesh.h`

```cpp
#pragma once
#include <vector>

class Mesh {
public:
    explicit Mesh(const std::vector<float> &vertices);
    ~Mesh();

    void draw() const;
    int vertexCount() const { return vertexCount_; }

private:
    int vao_ = 0, vbo_ = 0;
    int vertexCount_ = 0;
};
```

### `Renderer.h`

```cpp
#pragma once
#include "Window.h"
#include "Shader.h"
#include "Mesh.h"

class Renderer {
public:
    Renderer(Window &window, Shader &shader, Mesh &mesh);

    void render();

private:
    Window &window_;
    Shader &shader_;
    Mesh &mesh_;
};
```

## Verification

- Each class can be unit-tested independently (Shader without a Window, Mesh without a Shader).
- Resources are released automatically via destructors (RAII).
- Adding a new shader or mesh requires no changes to existing classes.
- The `Renderer` class is now a thin coordinator, not a god object.
