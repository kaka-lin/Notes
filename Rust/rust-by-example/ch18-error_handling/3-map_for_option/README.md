# Combinators: `map`

`match` is a valid method for handling `Option`. However, you may enventually find heavy usage tedious, especially with operations only valid with input. In this case, `combinators` can be used to manage control flow in a modular fashion(模組化方式).

## `map()`

Is a `Option`'s built in method.

A combinator for the simple mpping of `Some -> Some` and `None -> None`. 

Multiple `map()` calls can be chained together for even more flexibility.

```rust
pub fn map<U, F>(self, f: F) -> Option<U>
```
where F: [FnOnce(T)](#jump) -> U,

Maps an `Option<T>` to `Option<T>` by applying a function o a contained value.

### Examples

Converts an `Option<String>` into an `Option<usize>`

```rust
let some_string = Some(String::from("Hello, World!"));
// `Option`::map` takes self *by value*, comsuming `some_string`
let some_len = some_string.map(|s| s.len);

assert_eq!(maybe_some_len, Some(13));
```

<span id="jump"></span>
## `FnOnce`
It is an `anonymous function(closures)`, like python's `lambda`.



The version of the call operator that takes a by-value receiver.

```rust
pub trait FnOnce<Args> {
    type Output;
    extern "rust-call" fn call_once(self, args: Args) -> Self::Output;
}
```

### Examples

By-value `closures(anonymous function)` automatically implement this trait, which allows them to be invoked.

```rust 
let x = 5
let square_x = move || x * x;
assert_eq!(square_x(), 25);
```
```rust
let plus_one = |x: i32| x + 1;
assert_eq!(2, plus_one(1));
```

python:

```python
square_x = lambda x: x * x
assert square_x(5) == 25
```

```python
plus_one = lambda x: x + 1
assert plus_one(1) == 2
```


