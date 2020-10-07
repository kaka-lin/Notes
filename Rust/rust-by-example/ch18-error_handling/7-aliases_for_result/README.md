# aliases for `Result`

How about when we want ot reuse a specific `Result` type many times? -> [aliases](#jump).


<span id="jump"></span>
## Aliasing 

The `type` statement can be used to give a new name to an existing type.

## Exmaple

At a module level, creating `aliases` can be particularly helpful. Errors found in a specific module often have the same `Err` type, so a single alias can succinctly(簡潔的) define all associated `Results`. This is so useful that the `std` library even supplies one: [io:Result](#jump2)!

```rust
use std::num::ParseIntError;

// Define a generic alias for a `Result` with the error type `ParseIntError`.
type AliasedResult<T> = Result<T, ParseIntError>;

// Use the above alias to refer to our specific `Result` type.
fn multiply(first_number_str: &str, second_number_str: &str) -> AliasedResult<i32> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

// Here, the alias again allows us to save some space.
fn print(result: AliasedResult<i32>) {
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

---

<span id="jump2"></span>
## std::io::Result

A specialized `Result` type for I/O operations.

This type is broadly used across `std::io` for any operation which may produce an error.

This typedef is generally used to avoid writing out `io::Error` directly and is otherwise a direct mapping to `Result`.

While usual Rust style is to import types directly, aliases of `Result` often are not, to make it easier to distinguish between them. `Resul`t is generally assumed to be `std::result::Result`, and so users of this alias will generally use `io::Result` instead of shadowing the prelude's import of `std::result::Result`.

```rust
type Result<T> = Result<T, Error>
```
where Error: `std::io::Error`

### Example

```rust
use std::io;

fn get_string() -> io::Result<String> {
    let mut buffer = String::new();

    io::stdin().read_line(&mut buffer)?;

    Ok(buffer)
}
```
