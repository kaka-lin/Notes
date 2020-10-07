# Introducing `?`

Sometimes we just want the simplicity of `unwrap` without the possible of a `panic`.

Until now, `unwrap` has forced us to nest deeper and deeper when what we really was to get the value out.

=> This is exactly the purpose of `?`

Upon finding an `Err`, there are two valid actions to take:

1. `panic!` which we already decided to try to avoid if possibe.
2. `return` because an `Err` means it cannot be handled.

`?` is alimost exactly equivalent to an `unwrap` which returns instead of panics on `Err`

## The `try!` macro

Before there was `?`, the same functionallity was achived with the `try!` macro. The `?` operator is now recommended.

### Example

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = try!(first_number_str.parse::<i32>());
    let second_number = try!(second_number_str.parse::<i32>());

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```
