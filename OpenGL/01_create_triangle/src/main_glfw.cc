#include <iostream>

// Include GLEW. Always include it before gl.h and glfw3.h,
// since it's a bit magic.
#include <GL/glew.h>
#include <GLFW/glfw3.h>

#ifdef __APPLE__
#include <OpenGL/gl.h>  // Header File For The OpenGL32 Library
#include <OpenGL/glu.h> //
#endif

void userInit();
void render();
void run(GLFWwindow* window);
void framebuffer_size_callback(
    GLFWwindow* window, int width, int height);
void processInput(GLFWwindow *window);

// Vertex Buffer Object (VBO)
// OpenGL 中以 GL_ARRAY_BUFFER 表示
uint32_t vbo;
// Vertex Array Object (VAO)
uint32_t vao;

int main(int argc, char* argv[]) {
  // Initialise GLFW
  if (!glfwInit()) {
		std::cout << "glfwInit() failed." << std::endl;
		return -1;
	}

  // Open a window and create its OpenGL context
  GLFWwindow* window;
  window = glfwCreateWindow(640, 480, "Hello OpenGL", NULL, NULL);
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

  glfwTerminate();

	return 0;
}

void userInit() {
  // when call glClear()，清除 color buffer 後
  // 整個 color buffer 都會被填充為 glClearColor() 裡所設置的顏色
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
}

void run(GLFWwindow* window) {
  // Loop until the user closes the window
  while (!glfwWindowShouldClose(window)) {
    // preprecess input
    processInput(window);

    // Render here
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
  glBindVertexArray(vao);
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
