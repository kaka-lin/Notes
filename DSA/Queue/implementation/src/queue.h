#ifndef QUEUE_H
#define QUEUE_H

#include <vector>

class MyQueue {
 public:
  MyQueue();
  ~MyQueue() {};

  /** Insert an element into the queue. Return true if the operation is successful. */
  bool enQueue(int x);
  /** Delete an element from the queue. Return true if the operation is successful. */
  bool deQueue();
  /** Get the front item from the queue. */
  int Front();
  /** Checks whether the queue is empty or not. */
  bool isEmpty();

 private:
  // store elements
  std::vector<int> data;
  // a pointer to indicate the start position
  int p_start;
};

#endif // QUEUE_H
