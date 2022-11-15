#include <iostream>

int num = 10;

void hello() {
  printf("%d ", num++);
  int num = 20;
  printf("%d ", num++);
}

void world() {
  printf("%d ", ++num);
  int num = 30;
  printf("%d ", ++num);
}

int main() {
  hello();
  world();
  hello();
  world();
  return 0;
}
