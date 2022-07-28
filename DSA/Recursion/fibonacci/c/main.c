/* fibonacci number */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

// Recursion
int fr(int n) {
    if (n < 2)
        return 1;
    else
        return fr(n - 1) + fr(n - 2);
}

int main(int argc, char **argv) {
    int n;
    uint64_t answer;

    printf("Fibonacci: ");
    scanf("%d", &n);

    answer = fr(n);
    printf("F(%d) is %ld\n", n, answer);

    return 0;
}
