# i++ 與 ++i

- `i++`: `post-increment`

    ```
    在這一行程式完成之後，再進行+1的動作
    ```

- `++i`: `pre-increment`

    ```
    先進行+1，再進行後面的動作
    ```

## Examples

範例 1:

```C
int x;
int y;

// Pre-increment
//   x is incremented by 1, then y is assigned the value of x
x = 1;
y = ++x; // x is now 2, y is also 2

// Post-increment
//   y is assigned the value of x, then x is incremented by 1
x = 1;
y = x++; // x is now 2, y is also 1
```

範例 2:

If you want to get and run this example, please see [example](./example/) folder.

```C
#include <iostream>

int num = 10;

void hello() {
  printf("%d ", num++);
  int num = 20;
  printf("%d ", num++);
}

void world() {
  printf("%d ", ++num);
  int num = 30;
  printf("%d ", ++num);
}

int main() {
  hello();
  world();
  hello();
  world();
  return 0;
}
```

Output:

```sh
10 20 12 31 12 20 14 31
```
