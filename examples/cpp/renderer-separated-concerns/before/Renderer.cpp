/* Before: A renderer class that does everything — window management,
 * shader compilation, mesh loading, and frame rendering — all in one class.
 */

#include <vector>
#include <string>
#include <iostream>

class Renderer {
public:
    void init(const std::string &title, int width, int height) {
        // Window creation
        windowHandle = 1; // pretend
        width_ = width;
        height_ = height;

        // Shader compilation
        vertexShaderSrc = R"(
            #version 330 core
            layout(location = 0) in vec3 aPos;
            void main() { gl_Position = vec4(aPos, 1.0); }
        )";
        fragmentShaderSrc = R"(
            #version 330 core
            out vec4 FragColor;
            void main() { FragColor = vec4(1.0, 0.0, 0.0, 1.0); }
        )";
        shaderProgram = compileShader(vertexShaderSrc, fragmentShaderSrc);

        // Mesh loading
        vertices = {
            0.0f, 0.5f, 0.0f,
            -0.5f, -0.5f, 0.0f,
            0.5f, -0.5f, 0.0f
        };
        setupMesh(vertices);
    }

    void render() {
        // Clear
        std::cout << "Clearing screen\n";
        // Use shader
        std::cout << "Using shader program " << shaderProgram << "\n";
        // Draw
        std::cout << "Drawing " << vertexCount << " vertices\n";
    }

    void cleanup() {
        std::cout << "Cleaning up resources\n";
    }

private:
    int windowHandle = 0;
    int width_ = 0, height_ = 0;
    std::string vertexShaderSrc;
    std::string fragmentShaderSrc;
    int shaderProgram = 0;
    std::vector<float> vertices;
    int vao = 0, vbo = 0;
    int vertexCount = 0;

    int compileShader(const std::string &vs, const std::string &fs) {
        std::cout << "Compiling shaders\n";
        return 42;
    }

    void setupMesh(const std::vector<float> &verts) {
        std::cout << "Setting up mesh with " << verts.size() << " floats\n";
        vertexCount = static_cast<int>(verts.size()) / 3;
    }
};
