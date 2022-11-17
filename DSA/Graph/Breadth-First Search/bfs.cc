#include <iostream>
#include <string>
#include <list>
#include <queue>
using namespace std;

bool BFS(vector<list<int>> graph, int n, int start, int end) {
  // initialize
  vector<bool> visited;
  visited.resize(n, false); // n node
  queue<int> q;

  visited[start] = true;
  q.push(start);

  // BFS
  while (!q.empty()) {
    int curr_node = q.front();
    q.pop();

    if (curr_node == end)
      return true;

    for (auto neighbor: graph[curr_node]) {
      if (!visited[neighbor]) {
        visited[neighbor] = true;
        q.push(neighbor);
      }
    }
  }
  return false;
}

int main() {
  return 0;
}
