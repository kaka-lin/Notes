#include <iostream>

#ifdef __APPLE__
#include <OpenGL/gl.h>  // Header File For The OpenGL32 Library
#include <OpenGL/glu.h> // Header File For The GLu32 Library
#include <GLUT/glut.h>  // Header File For The GLut Library
#else
#include <GL/glut.h>
#endif

void init();
void display();

int main(int argc, char* argv[]) {
  //init the glut
	glutInit(&argc, argv);

  //setting display mode
  glutInitDisplayMode(GLUT_DEPTH | GLUT_SINGLE | GLUT_RGB);

  //set the window position
  glutInitWindowPosition(100, 100);

  //setting the window size
	glutInitWindowSize(300, 300);

  //create the window
	glutCreateWindow("OpenGL 3D View");

	init();
  //call display function
	glutDisplayFunc(display);

	//Enter the GLUT event loop
  glutMainLoop();

	return 0;
}

//like processing setting
void init() {
	glClearColor(0.0, 0.0, 0.0, 0.0);
}

//like processing draw
void display() {
  glClearColor(0, 0, 0, 0);

  glFlush();
}