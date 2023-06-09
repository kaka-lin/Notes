#include <iostream>
#include <string>
#include <vector>

#include <GL/glew.h>
#include <GLFW/glfw3.h>

#ifdef __APPLE__
#include <OpenGL/gl.h>  // Header File For The OpenGL32 Library
#include <OpenGL/glu.h> // Header File For The GLu32 Library
#endif

void userInit();
void render();
void run(GLFWwindow* window);
void framebuffer_size_callback(
    GLFWwindow* window, int width, int height);
void processInput(GLFWwindow *window);

uint32_t vbo;
uint32_t vao;
uint32_t program;

uint32_t LoadShader(GLenum type, const char* src) {
  uint32_t shader;

  // Create a shader by type
  shader = glCreateShader(type); // GL_VERTEX_SHADER or GL_FRAGMENT_SHADER

  // Bind vertex shader and complier
  // void glShaderSource(
  //   GLuint shader, GLsizei count, const GLchar **string, const GLint *length);
  glShaderSource(shader, 1, &src, nullptr);
  glCompileShader(shader);

  // Check compile success or not
  int success;
  char log[512];
  glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
  if (!success) {
      glGetShaderInfoLog(shader, 512, nullptr, log);
      printf("Error Shader %s compile error\n%s\n",
          type == GL_VERTEX_SHADER ? "Vertex" : "Fragment", log);
      return 0;
  }
  return shader;
}

// Linking Shader Program
// 把編譯好的 Shader 連結(Link)成一個 Shader Program Object
// 當我們要渲染時啟用該 Shader Program ，之後呼叫的渲染指令便會去調用該 Shader Program
uint32_t LinkShaderProgram(uint32_t vertex_shader, uint32_t fragment_shader) {
  // Create Shader Program
  uint32_t program = glCreateProgram();

  // 將 Shader Attach 到 Program 上
  glAttachShader(program, vertex_shader);
  glAttachShader(program, fragment_shader);
  glLinkProgram(program);

  // check link program success or not
  int success;
  char log[512];
  glGetProgramiv(program, GL_LINK_STATUS, &success);
  if (!success) {
    glGetProgramInfoLog(program, 512, nullptr, log);
    printf("Error Shader Linking error\n%s\n", log);
    return 0;
  }
  return program;
}

int main(int argc, char* argv[]) {
  // Initialise GLFW
  if (!glfwInit()) {
		std::cout << "glfwInit() failed." << std::endl;
		return -1;
	}

  // We want OpenGL 3.3. This is for shader
  glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
  glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
  glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
#ifdef __APPLE__
  // uncomment this statement to fix compilation on OS X
  glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
#endif

  // Open a window and create its OpenGL context
  GLFWwindow* window = glfwCreateWindow(640, 480, "Hello World", NULL, NULL);
  if (window == NULL) {
    std::cout << "Failed to create GLFW window" << std::endl;
    glfwTerminate();
    return -1;
  }
  // Make the window's context current
  glfwMakeContextCurrent(window);
  glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

  /* Initialize GLEW */
  // glewInit() 必須在 opengl context 之後，
  // 即必須在 `glfwMakeContextCurrent(window)` 之後
  glewExperimental = GL_TRUE;
  if (glewInit() != GLEW_OK) {
    std::cout << "Failed to initialize GLEW" << std::endl;
    return -1;
  }

  // Ensure we can capture the escape key being pressed below
  glfwSetInputMode(window, GLFW_STICKY_KEYS, GL_TRUE);

  userInit();
  // call run (display) function
  run(window);

  // release resources
  glDeleteVertexArrays(1, &vao);
  glDeleteBuffers(1, &vbo);
  glDeleteProgram(program);

  glfwTerminate();

	return 0;
}

// like processing setting
void userInit() {
	glClearColor(0.0, 0.0, 0.0, 0.0);

  // Create Vertex data
  // OpenGL 只會處理 3D 座標在值在 [−1.0,1.0] 的座標
  float vertices[] = {
    -0.5f, -0.5f, 0.0f,
    0.5f, -0.5f, 0.0f,
    0.0f,  0.5f, 0.0f
  };

  // 建立並綁定 VAO
  glGenVertexArrays(1, &vao);
  glBindVertexArray(vao);

  // 建立 VBO 複製頂點資料
  glGenBuffers(1, &vbo); // number, array to object id
  glBindBuffer(GL_ARRAY_BUFFER, vbo); // 綁定
  glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW); //傳輸資料

  // 設定頂點屬性
  // 由於 OpenGL 沒有規定傳入頂點資料的格式，這意味著我們可以自己決定，但也必須要我們手動指定給 OpenGL。
  // 根據我們上面訂出的頂點陣列 vertices[] ，有底下幾種屬性是必須告訴 OpenGL 的:
  // 1. 開始位置是 0 (location=0)
  // 2. 每個頂點有 3 個 float 資料，分別是 x, y, z
  // 3. 頂點資料是儲存在 float 大小是 sizeof(float)
  // 4. 每個頂點之間沒有空隙或是其他的資料，是緊密排列(Tightly Packed)
  //
  // `glVertexAttribPointer()` 會從 `GL_ARRAY_BUFFER`中
  // 按照參數給定的方式去讀取資料，然後將頂點資料的資訊告訴 Vertex Shader
  // 讓它知道該怎麼解析這些頂點資料。
  // 其中第一個參數 0 就是對應 vertex shader 中的 location=0
  glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
  glEnableVertexAttribArray(0); // 是否啟動 VAO; 啟動 location=0

  // Vertex Shader
  const char* vertexShaderSource = R"(
  #version 330 core
  layout (location = 0) in vec3 aPos;

  void main() {
    gl_Position.xyz = aPos;
    gl_Position.w = 1.0;
  }
  )";

  // Fragment Shader
  const char* fragmentShaderSoucre = R"(
  #version 330 core
  out vec4 FragColor;

  void main() {
    FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);
  }
  )";

  // Load shader
  // std::vector<GLuint> shader_vector;
  uint32_t vertexShader = LoadShader(GL_VERTEX_SHADER, vertexShaderSource);
  uint32_t fragmentShader = LoadShader(GL_FRAGMENT_SHADER, fragmentShaderSoucre);
  program = LinkShaderProgram(vertexShader, fragmentShader);

  // 可以刪除，如果之後沒有要用到的話
  glDeleteShader(vertexShader);
  glDeleteShader(fragmentShader);

  // 啟用 Shader Program
  glUseProgram(program);
}

void run(GLFWwindow* window) {
  // Loop until the user closes the window
  while (!glfwWindowShouldClose(window)) {
    // preprecess input
    processInput(window);

    // Render loop
    render();

    // Swap front and back buffers
    glfwSwapBuffers(window);
    // Poll for and process events (監聽滑鼠和鍵盤事件)
    glfwPollEvents();
  }
}

void render() {
  // call glClear() 來清空 buffer
  // 他可以清空:
  //   1. color: GL_COLOR_BUFFER_BIT
  //   2. depth: GL_DEPTH_BUFFER_BIT
  //   3. 模板:  GL_STENCIL_BUFFER_BIT
  glClearColor(0.0, 0.0, 0.0, 0.0);
  glClear(GL_COLOR_BUFFER_BIT);
  // glUseProgram(program);
  // glBindVertexArray(vao);
  glDrawArrays(GL_TRIANGLES, 0, 3);
}

// glfw: whenever the window size changed
// this callback function executes
void framebuffer_size_callback(
    GLFWwindow* window, int width, int height) {
  // make sure the viewport matches the new window dimensions; note that width and
  // height will be significantly larger than specified on retina displays.
  glViewport(0, 0, width, height);
}

// process all input: query GLFW whether relevant keys are pressed/released
// this frame and react accordingly
void processInput(GLFWwindow *window) {
  if(glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) {
    glfwSetWindowShouldClose(window, true);
  }
}

