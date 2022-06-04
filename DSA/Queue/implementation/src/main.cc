#include <iostream>

#include "queue.h"

int main() {
  MyQueue q;
  q.enQueue(5);
  q.enQueue(3);
  if (!q.isEmpty()) {
    std::cout << q.Front() << std::endl;
  }

  q.deQueue();
  if (!q.isEmpty()) {
    std::cout << q.Front() << std::endl;
  }

  q.deQueue();
  if (!q.isEmpty()) {
    std::cout << q.Front() << std::endl;
  }
}
