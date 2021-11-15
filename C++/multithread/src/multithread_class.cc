#include <iostream>
#include <thread>
#include <unistd.h>
#include <vector>

class Counter {
 public:
  explicit Counter(int i) : id_(i) {};
  ~Counter() {};

  void run() {
    int count = 0;
    for (int i = 0; i < 10000; i++) {
      count += 1;
    }
    printf("\tthread_%d, count: %d\n", id_, count);
  }
 private:
  int id_;
};

int main(int argc, char** argv) {
  std::vector<std::thread> threads_;

  // 建立5個子行緒
  for (int i = 0; i < 5; i++) {
    threads_.push_back(std::move(
      std::thread(&Counter::run, Counter(i))
    ));
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
