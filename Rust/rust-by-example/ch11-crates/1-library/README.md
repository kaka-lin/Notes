# Library

Let's create a library, and then see how to link it to another crate.

```rust
pub fn public_function() {
    println!("called rary's `public_function()`");
}

fn private_function() {
    println!("called rary's `private_function()`");
}

pub fn indirect_access() {
    print!("called rary's `indirect_access()`, that\n> ");

    private_function();
}
```

```bash
$ rustc --crate-type=lib src/libtest.rs
$ ls lib*
liblibtest.rlib
```

Libraries get prefixes with `"lib"`, and default  they get named after their crate file, but this default name can be overridden usinf the `crate_name` attribute.
