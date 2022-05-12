#include <iostream>
#include <queue>
#include <vector>
#include <string>

typedef std::pair<int, std::string> StringPair;
// custom compare func
class PairComp {
 public:
  // 由小到大排序
  bool operator()(const StringPair& n1, const StringPair& n2) const {
    //因為優先出列判定為!cmp，所以反向定義實現最小值優先
    if (n1.first == n2.first) {
      return (n1.first > n2.first);
    }

    return n1.first > n2.first;;
  }
};

template<typename T>
void print_queue(T q) { // NB: pass by value so the print uses a copy
  while(!q.empty()) {
    std::cout << q.top().first << ", " << q.top().second << "\n";
    q.pop();
  }
}

int main(int argc, char** argv) {
  std::priority_queue<StringPair, std::vector<StringPair>, PairComp> pq;

  pq.push(std::make_pair(257, "Hello"));
  pq.push(std::make_pair(12, "Pair"));
  pq.push(std::make_pair(100, "Priority Queue"));

  print_queue(pq);

  return 0;
}
