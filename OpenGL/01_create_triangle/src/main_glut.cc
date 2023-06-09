#include <iostream>
#include <string>

#ifdef __APPLE__
#include <OpenGL/gl.h>  // Header File For The OpenGL32 Library
#include <OpenGL/glu.h> // Header File For The GLu32 Library
#include <GLUT/glut.h>  // Header File For The GLut Library
#define glGenVertexArrays glGenVertexArraysAPPLE
#define glBindVertexArray glBindVertexArrayAPPLE
#define glDeleteVertexArrays glDeleteVertexArraysAPPLE
#else
#include <GL/glut.h>
#include <GL/glew.h>
#endif

void userInit();
void display();

// Vertex Buffer Object (VBO)
// OpenGL 中以 GL_ARRAY_BUFFER 表示
GLuint vbo;
// Vertex Array Object (VAO)
GLuint vao;

int main(int argc, char* argv[]) {
	glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_DEPTH | GLUT_SINGLE | GLUT_RGB);
  glutInitWindowPosition(100, 100);
	glutInitWindowSize(320, 320);
	glutCreateWindow("Hello OpenGL");

  userInit();
	glutDisplayFunc(display);

	//Enter the GLUT event loop
  glutMainLoop();

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

  // Create VAO
  glGenVertexArrays(1, &vao);
  glBindVertexArray(vao);

  // Create VBO and Copy vertex data
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

// like processing draw
void display() {
  // clear color buffer
  glClearColor(0.0, 0.0, 0.0, 0.0);
  glClear(GL_COLOR_BUFFER_BIT);

  // Draw the triangle !
  // Starting from vertex 0; 3 vertices total -> 1 triangle
  // glBindVertexArray(vao);
  glDrawArrays(GL_TRIANGLES, 0, 3);
  glutSwapBuffers();
}
