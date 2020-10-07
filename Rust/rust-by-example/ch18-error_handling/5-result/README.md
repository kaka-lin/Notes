# Result

Result is an richer version of the `Option` type that describes possible `error` instead of possible `absence`.


```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

- `Ok<T>`: An element `T` was found

- `Err<E>`: An error was found with element `E`

Like `Option`, `Result` has many methods associated with it.

For example:

- `unwrap()`:

    either yields the element `T` or `panics`

For case handling, there are many combinators between Result and Option that overlap.

## Examples

```rust
#[derive(Debug)]
enum Version { Version1, Version2 }

fn parse_version(header: &[u8]) -> Result<Version, &'static str> {
    match header.get(0) {
        None     => Err("invalid header length"),
        Some(&1) => Ok(Version::Version1),
        Some(&2) => Ok(Version::Version2),
        Some(_)  => Err("invalid version"), 
    }
}

let version = parse_version(&[1, 2, 3, 4]);
match version {
    Ok(v) => println!("working with version: {:?}", v),
    Err(e) => println!("error parsing header: {:?}", e),
}
```

In working with Rust, you will likely encounter methods that return the `Result` type, such as the `parse()` method. It might not always be possible to parse a string into the other type, so `parse()` returns a `Result` indicating possible failure.

```rust
fn multiply(first_number_str: &str, second_number_str: &str) -> i32 {
    // Let's try using `unwrap()` to get the number out. Will it bite us?
    let first_number = first_number_str.parse::<i32>().unwrap();
    let second_number = second_number_str.parse::<i32>().unwrap();
    first_number * second_number
}

fn main() {
    let twenty = multiply("10", "2");
    println!("double is {}", twenty);

    let tt = multiply("t", "2");
    println!("double is {}", tt);
}
```

In the unsuccessful case, `parse()` leaves us with an error for `unwrap()` to `panic` on. Additionally, the `panic` exits our program and provides an unpleasant error message.

To improve the quality of our error message, we should be more specific about the return type and consider explicitly handling the error.

### Using `Result` in `main`

The `Result` type can also be the return type of the `main` function.

If an error occurs within the `main` function it will return an error code and print a debug representation of the error(Using the `Debug` trait).

```rust
use std::num::ParseIntError;

// () is the unit type, analogous to a void return type in other languages.
fn main() -> Result<(),  ParseIntError> {
    let number_str = "10";
    let number = match number_str.parse::<i32>() {
        Ok(number) => number,
        Err(e) => return Err(e),
    };

    println!("{}", number);

    Ok(())
}
```

## Notes

`Result<T, E>` is the type used for returning and `propagating errors`.

---

## Primitive Type `unit`

The `()` type, sometimes called "unit" ot "nil".

The `()` type has exactly one value `()`, and is uesd when there is no other meaningful value that could be returnded.

`()` is most commonly seen implicitly: functions whthout a  `-> ...` implicitly have return type `()`, that is, these are equivalent:

```rust
fn long() -> () {}

fn short() {}
```

The semicolon `;` can be used to discard the result of an expression at the end of a block, making the expression (and thus the block) evaluate to `()`. For example,

```rust
fn returns_i64() -> i64 {
    li64
}

fn returns_unit() {
    li64;
}

let is_i64 = {
    returns_i64()
};

let is_unit = {
    returns_i64();
};
```



