# Pulling `Result`s out of `Option`s

The most basic way of handling mixed error types is to just embed them in each other.

## Example

```rust
use std::num::ParseIntError;

fn double_first(vec: Vec<&str>) -> Option<Result<i32, ParseIntError>> {
    vec.first().map(|first| {
        first.parse::<i32>().map(|n| 2 * n)
    })
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("The first doubled is {:?}", double_first(numbers));

    println!("The first doubled is {:?}", double_first(empty));
    // Error 1: the input vector is empty

    println!("The first doubled is {:?}", double_first(strings));
    // Error 2: the element doesn't parse to a number
}
```

There are times when we'll want to stop processing on errors (like with `?`) but keep going when the `Option` is `None`. A couple of combinators come in hany to swap the `Result` and `Option`.

```rust
use std::num::ParseIntError;

fn double_first(vec: Vec<&str>) -> Result<Option<i32>, ParseIntError> {
    let opt = vec.first().map(|first| {
        first.parse::<i32>().map(|n| 2 * n)
    });

    let opt = opt.map_or(Ok(None), |r| r.map(Some))?;

    Ok(opt)
}
```

---

## Method of `Option`: `map_or`

```rust
pub fn map_or<U, F>(self, default: U, f: F) -> U )
```

where F: `FnOnce`(T) -> U,

Applies a function to the contained value (if any),
or returns the provided default (if not).

### Example

```rust
let x = Some("foo");
// x.map_or(42, |v| v.len()) -> return 3
assert_eq!(x.map_or(42, |v| v.len()), 3);

let x: Option<&str> = None;
// x.map_or(42, |v| v.len()) -> return 42 (default value)
assert_eq!(x.map_or(42, |v| v.len()), 42);
```
