#include <stdio.h>

void printReverse(const char *str);

int main() {
	const char *str = "Hello, printReverse!!!";
    printReverse(str);
    putchar('\n');

	return 0;
}

void printReverse(const char *str) {
    if (!*str)
        return;
    printReverse(str + 1);
    putchar(*str);
}
