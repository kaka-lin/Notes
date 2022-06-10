#include <iostream>
#include <stack>

int main() {
  std::stack<int> s;

  // Push new element
  s.push(5);
  s.push(13);
  s.push(8);
  s.push(6);

  // Check if stack is empty.
  if (s.empty()) {
    std::cout << "Stack is empty!" << std::endl;
      return 0;
  }

  // Pop an element.
  s.pop();

  // Get the top element.
  std::cout << "The top element is: " << s.top() << std::endl;
  // Get the size of the stack.
  std::cout << "The size is: " << s.size() << std::endl;
}
