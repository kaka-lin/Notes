# Multiple error types

Somtimes an `Option` needs to interact with a `Reasult`, or a `Result<T, Error1>` need to interact with a `Result<T, Error2>`. In those cases, we want to manage our different error types in a way that makes them composable and easy to interact with.

## Example

In the following code, two instances of `unwrap` generate different error types.

`Vec::first` returns an `Option`,
while `parse::<i32>` returns a `Result<i32, ParseIntError>`

```rust
fn double_first(vec: Vec<&str>) -> i32 {
    let first = vec.first().unwrap(); // Generate error 1
    2 * first.parse::<i32>().unwrap() // Generate error 2
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("The first doubled is {}", double_first(numbers));

    println!("The first doubled is {}", double_first(empty));
    // Error 1: the input vector is empty

    println!("The first doubled is {}", double_first(strings));
    // Error 2: the element doesn't parse to a number
}
```
