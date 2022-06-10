#include <iostream>

#include "stack.h"

int main() {
  MyStack s;

  s.push(1);
  s.push(2);
  s.push(3);

  for (int i = 0; i < 4; ++i) {
    if (!s.isEmpty()) {
      std::cout << s.top() << std::endl;
    }
    std::cout << (s.pop() ? "true" : "false") << std::endl;
  }
}
