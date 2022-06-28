#include <stdio.h>

// src = source 來源
// dst = destination 目的地
void hanoi(int n, char buffer, char src, char dst) {
  printf("hanoi(%d, %c, %c, %c)\n", n, buffer, src, dst);
  if (n == 1)
    printf("move disk from %c to %c\n", src, dst);
  else  {
    hanoi(n - 1, dst, src, buffer);
    printf("move disk from %c to %c\n", src, dst);
    hanoi(n - 1, src, buffer, dst);
  }
}

int main() {
  int n;
  //scanf("%d", &n);
  hanoi(3, 'B', 'A', 'C');
  return 0;
}
