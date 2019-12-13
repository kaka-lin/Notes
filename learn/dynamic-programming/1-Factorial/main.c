#include <stdio.h>

int factorial_1(int N)
{
    int f[N];
    
    f[0] = 1;
    f[1] = 1;

    for (int i = 2; i <= N; ++i) {
        f[i] = f[i - 1] * i;
        //printf("%d! = %d\n", i, f[i]);
    }

    return f[N];
}

int factorial_2(int N)
{
    int f = 1;
    
    for (int i = 2; i <= N; ++i) {
        f *= i;
        //printf("%d! = %d\n", i, f);
    }

    return f;
}

int main(int argc, char **argv)
{
    int answer;

    answer = factorial_1(10);
    printf("Method 1:\n");
    printf("\t10! is %d\n", answer);

    answer = factorial_2(10);
    printf("Method 2:\n");
    printf("\t10! is %d\n", answer);

    return 0;
}
