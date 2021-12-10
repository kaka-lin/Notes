#include <iostream>
#include <queue>

template<typename T>
void print_queue(T q) { // NB: pass by value so the print uses a copy
  while(!q.empty()) {
    std::cout << q.top() << ' ';
    q.pop();
  }
  std::cout << '\n';
}

// custom compare func
class Cmp {
 public:
  // 由小到大排序
  bool operator()(const int& a, const int& b) const {
    //因為優先出列判定為!cmp，所以反向定義實現最小值優先
    return a > b;
  }
};

int main(int argc, char** argv) {
  const auto data = {1, 8, 5, 6, 3, 4, 0, 9, 7, 2};

  // 1. 由大到小 (default: std::less)
  std::priority_queue<int> q;
  for (auto& d : data) {
    q.push(d);
  }
  print_queue(q); // 9 8 7 6 5 4 3 2 1 0

  // 2. 由小到大
  std::priority_queue<int, std::vector<int>, std::greater<int>>
      q2(data.begin(), data.end());
  print_queue(q2); // 0 1 2 3 4 5 6 7 8 9

  // 3. Custom compare func
  std::priority_queue<int, std::vector<int>, Cmp> q3;
  for (auto& d : data) {
    q3.push(d);
  }
  print_queue(q3); // 0 1 2 3 4 5 6 7 8 9

  return 0;
}
