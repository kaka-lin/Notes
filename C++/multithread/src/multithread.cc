#include <iostream>
#include <thread>
#include <unistd.h>
#include <vector>

void job() {
  for (int i = 0; i < 5; i++) {
    std::cout << "\tChild thread 0: " << i << std::endl;
    sleep(1); // 1s
  }
}

void job2(int thread_num) {
  for (int i = 0; i < 5; i++) {
    printf("\tChild thread %d: %d\n", thread_num, i+1);
    sleep(1); // 1s
  }
}

int main(int argc, char** argv) {
  std::vector<std::thread> threads_;

  // 建立子執行緒
  // std::thread(func, params)
  std::thread t(job);

  // Now, as std::thread objects are move only
  // i.e. we can not copy them, only move them.
  // Therefore, we need to move these 2 thread objects in vector i.e.
  // -> "thread: movable, not copyable"
  //
  // Move thread objects to vector
  threads_.push_back(std::move(t));

  for (int i = 0; i < 5; i++) {
    threads_.push_back(std::move(std::thread(job2, i)));
  }

  // Main Thread繼續執行自己的工作
  for (int i = 0; i < 3; i++) {
    std::cout << "Main thread: " << i << std::endl;
    sleep(1); // 1s
  }

  // 等待子執行緒執行結束
  for (auto& thread : threads_) {
    thread.join();
  }

  std::cout << "All Done." << std::endl;

  return 0;
}
