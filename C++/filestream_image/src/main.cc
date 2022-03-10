#include <fstream>
#include <iostream>
#include <string>
#include <unistd.h>

#define MAXPATHLEN 256

using namespace std;

int main(int argc, char** argv) {
  char cwd[MAXPATHLEN];
  string dir_path, root_path;
  size_t pos;
  string image_in_path, image_out_path;
  ifstream image_in;
  ofstream image_out;
  size_t image_size;
  char* buffer;

  if (getcwd(cwd, sizeof(cwd)) != NULL) {
    printf("Current working dir: %s\n", cwd);
    dir_path = string(cwd);
    pos = dir_path.find("build");
    root_path = dir_path.substr(0, pos);
  }

  // image path
  image_in_path = root_path + "images/dog.jpg";
  image_out_path = root_path + "images/dog2.jpg";

  // Open in and out image
  image_in.open(image_in_path, std::ios::in | std::ios::binary);
  if (!image_in) {
    cout << "Failed to open image: " << image_in_path << endl;
    return -1;
  }

  image_out.open(image_out_path, std::ios::out | std::ios::binary);
  if (!image_out) {
    cout << "Failed to open image: " << image_out_path << endl;
    return -1;
  }

  // get size of image
  image_in.seekg(0, ios::end);
  image_size = image_in.tellg();
  image_in.seekg(0, ios::beg);

  // Read image from disk to memory
  buffer = new char[image_size];
  image_in.read(buffer, image_size);  // ifstream.read (buffer,length);

  // Get data from memory and write to image file
  image_out.write(buffer, image_size);

  // release dynamically-allocated memory
  delete[] buffer;

  image_in.close();
  image_out.close();

  return 0;
}
