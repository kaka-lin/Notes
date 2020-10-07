# Combinators: `and_then`

`map()` was described as a chainable way to simplify `match` statements. However, using `map()` on a function that returns an `Option<T>` results in the nested `Option<Option<T>>`. Chaining multiple calls together can then become confusing. That's where another combinator called `and_then()`, known in some language as `flatmap`, comes in. 

## `and_then()`

Calling its function input with the wrapped value and returns the result.

`Some -> Some`, `None -> None`

```rust
pub fn and_then<U, F>(self, f: F) -> Option<U>
```

where F: `FnOnce(T)` -> `Option<U>`,

Returns `None` if the option is `None`, otherwise calls `f` with the wrapped value and returns the result.

### Examples

```rust
fn sq(x: u32) -> Option<u32> {
    x * x
}

fn nope(_: u32) -> Option<u32> {
    None
}

assert_eq!(Some(2).and_then(sq).and_then(sq), Some(16));
assert_eq!(Some(2).and_then(sq).and_then(nope), None);
assert_eq!(Some(2).and_then(nope).and_then(sq), None);
assert_eq!(None.and_then(sq).and_then(sq), None);
```


