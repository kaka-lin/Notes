# `Option` & `unwrap`

## `Option`

`Option<T>` is an `enum` in the `std` library.

```rust
enum Option<T> {
    Some(T),
    None,
}
```

`Option<T>` is used when absence is a possible.

It manifests itself as one of two "options":

1. Some(T)

    An element of type `T` was found

2. None:

    No element was found

## `unwrap`

Is a shortcut method that is implement just like the `match` expression.

 - If the `Option` value is `Some(T)` variant, `unwrap` will return the value `T` inside the `Some(T)`.

 - If the `Option` value is `None`, `unwrap` will return a `panic`.
