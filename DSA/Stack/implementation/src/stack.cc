#include "stack.h"

void MyStack::push(int x) {
  data.push_back(x);
}

bool MyStack::pop() {
  if (isEmpty()) {
    return false;
  }
  data.pop_back();
  return true;
}

int MyStack::top() {
  return data.back();
};

bool MyStack::isEmpty()  {
  return data.empty();
}
