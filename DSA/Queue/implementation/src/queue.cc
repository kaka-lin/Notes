#include "queue.h"

MyQueue::MyQueue() {
  p_start = 0;
}

bool MyQueue::enQueue(int x) {
  data.push_back(x);
  return true;
}

bool MyQueue::deQueue() {
  if (isEmpty()) {
    return false;
  }
  p_start++;
  return true;
}

int MyQueue::Front() {
  return data[p_start];
};

bool MyQueue::isEmpty()  {
  return p_start >= data.size();
}
