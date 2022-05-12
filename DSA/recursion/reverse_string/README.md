# Print a string in reverse order

You can easily solve this problem iteratively, i.e. looping through the string starting from its last character. But how about solving it recursively?

First, we can define the desired function as `printReverse(str[0...n-1])`, where `str[0]` represents the first character in the string. Then we can accomplish the given task in two steps:

1. `printReverse(str[1...n-1])`: print the substring `str[1...n-1]` in reverse order.
2. `print(str[0])`: print the first character in the string.

## Usage

```
$ make

$./example
```
