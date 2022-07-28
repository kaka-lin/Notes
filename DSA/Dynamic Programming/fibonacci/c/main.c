/* fibonacci number */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

// method 1: recurrence

int fr(int n) {
    if (n < 2)
        return 1;
    else
        return fr(n - 1) + fr(n - 2);
}

// method 2: DP, Top-down
//int table[10]; // 表格，儲存全部問題的答案，假設到10
//bool solve[10] = {0}; // 紀錄問題是否已經計算完畢
uint64_t fdp_top_down(int n, uint64_t *table, uint64_t *solve) {
    // 1. Initial memo
    if (n < 2) return table[n] = 1;

    // 2. 如果已經計算過，就直接讀取表格的答案
    if (solve[n]) return table[n];

    // 3. 如過不曾計算過，就計算一遍，儲存答案
    table[n] = fdp_top_down(n-1, table, solve) +
               fdp_top_down(n-2, table, solve);
    solve[n] = true;

    return table[n];
}

// method 3: DP, Bottom-Up
//int table[10]; // 表格，儲存全部問題的答案，假設到10
uint64_t fdp_bottom_up(int n, uint64_t *table) {
    // 1. Initial memo
    if (n < 2) return table[n] = 1;

    for (int i = 2; i <= n; i++) {
      table[n] = table[n-1] + table[n-2];
    }

    return table[n];
}

int main(int argc, char **argv) {
    int n;
    uint64_t answer;

    printf("Fibonacci: ");
    scanf("%d", &n);

    // recurrence
    //answer = fr(n);
    //printf("F(%d) is %ld\n", n, answer);

    // DP, Top-down
    uint64_t *table = calloc(n+1, sizeof(uint64_t));
    uint64_t *solve = calloc(n+1, sizeof(uint64_t));

    answer = fdp_top_down(n, table, solve);
    printf("F(%d) is %ld\n", n, answer);

    // DP, Bottom-up
    answer = fdp_bottom_up(n, table);
    printf("F(%d) is %ld\n", n, answer);

    free(table);
    free(solve);
    return 0;
}
