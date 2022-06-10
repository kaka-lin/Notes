#ifndef STACK_H
#define STACK_H

#include <vector>

class MyStack {
 public:
  MyStack() {};
  ~MyStack() {};

  /** Insert an element into the stack. */
  void push(int x);
  /** Delete an element from the queue. Return true if the operation is successful. */
  bool pop();
  /** Get the top item from the queue. */
  int top();
  /** Checks whether the stack is empty or not. */
  bool isEmpty();

 private:
  // store elements
  std::vector<int> data;
  // a pointer to indicate the start position
  int p_start;
};

#endif // STACK_H
