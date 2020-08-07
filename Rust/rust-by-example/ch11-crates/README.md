# Crates

A crate is a compilation unit in Rust. Whenever `rustc some_file.rs` is called, `some_file.rs` is treated as the crate file. 

If `some_file.rs` has `mod` declarations in it, then the contents of module files would be insert in places where `mod` declarations in the crate file are found, `before` running the compiler over it. In other words, `modules do not get compiled individually, only crates get compiled.`

A crate can be compiled into a binary or into a library. By default, `rustc` will produce a binary from a crate. This behavior can be overridden by passing the `--crate-type` flag to `rustc`.

## Example

Filename: src/libtest.rs

```rust
pub fn public_function() {
    println!("called rary's `public_function()`");
}
```

you can use `rustc` or `cargo` 

1. rustc

    ```bash
    $ rustc --crate-type=lib src/libtest.rs
    $ ls lib*
    liblibtest.rlib
    ```

2. cargo

    Adding the following contents in `Cargo.toml`.
    
    ```
    [lib]
    name = "libtest"
    path = "src/libtest.rs"
    crate-type = ["lib"]
    ```

    then build

    ```bash
    # the liblibtest.rlib is located at target/debug
    $ cargo build 
    ```
