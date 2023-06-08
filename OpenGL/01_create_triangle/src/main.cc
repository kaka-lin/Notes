#include <iostream>

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

int main(int argc, char* argv[]) {
  std::cout << "000000";
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

  // Create VBO and Copy vertex data
  glGenBuffers(1, &vbo); // number, array to object id
  glBindBuffer(GL_ARRAY_BUFFER, vbo); // 綁定
  glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW); //傳輸資料
}

// like processing draw
void display() {
  // clear color buffer
  glClear(GL_COLOR_BUFFER_BIT);

  // 1st attribute buffer : vertices
  glEnableVertexAttribArray(0);
  glBindBuffer(GL_ARRAY_BUFFER, vbo);
  // Setting Attribution
  // glVertexAttribPointer(
  //   0,          // attribute 0. No particular reason for 0, but must match the layout in the shader.
  //   3,          // size
  //   GL_FLOAT,   // type
  //   GL_FALSE,   // normalized?
  //   0,          // stride
  //   (void*)0    // array buffer offset
  // );
  glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, (void*)0);
  // Draw the triangle !
  //Starting from vertex 0; 3 vertices total -> 1 triangle
  glDrawArrays(GL_TRIANGLES, 0, 3);
  glDisableVertexAttribArray(0);
  glutSwapBuffers();
}
