# `extern crate`

To link a crate to this new library, the `extern crate` declaration must be used. This will not onlt link the library, but also import all its items under a module named the same as the library.  The visibility rules that apply to modules also apply to libraries.

## Example

Filename: src/main.rs

```rust 
extern crate libtest;

fn main() {
    libtest::public_function();
```

```bash
# 1. build library crate
$ rustc --crate-type=lib --out-dir=src src/libtest.rs

# 2. build bin crate
$ rustc src/main.rs --extern libtest=src/liblibtest.rlib

# 3. run
$ ./main
```

## Note

In `2018 edition`, `extern crate` is no longer needed in 99% of circumstances.

Filename: src/main.rs

```rust
use libtest;

fn main() {
    libtest::public_function();
```

```bash
$ cargo run
```
