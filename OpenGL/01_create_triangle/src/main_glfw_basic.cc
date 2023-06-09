#include <iostream>
#include <GLFW/glfw3.h>

#ifdef __APPLE__
#include <OpenGL/gl.h>  // Header File For The OpenGL32 Library
#include <OpenGL/glu.h> //
#endif

void framebuffer_size_callback(
    GLFWwindow* window, int width, int height);
void processInput(GLFWwindow *window);

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

  // Ensure we can capture the escape key being pressed below
  glfwSetInputMode(window, GLFW_STICKY_KEYS, GL_TRUE);

  // Loop until the user closes the window */
  while (!glfwWindowShouldClose(window)) {
    // preprecess input
    processInput(window);

    // Render here
    glClear(GL_COLOR_BUFFER_BIT);

    // Draw triangles begin
    glBegin(GL_TRIANGLES);
    glVertex2f(-0.5f, -0.5f);
    glVertex2f(0.0f, 0.5f);
    glVertex2f(0.5f, -0.5f);
    glEnd();

    // Swap front and back buffers
    glfwSwapBuffers(window);
    // Poll for and process events (監聽滑鼠和鍵盤事件)
    glfwPollEvents();
  }

  glfwTerminate();
  return 0;
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
