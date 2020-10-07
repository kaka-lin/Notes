# Re-exporting Names with `pub use`

When you bring a name into scope with the `use` keyword, the name being available in the new scope is private, example:

```rust
mod sound {
    pub mod instrument {
        pub fn clarinet() {
            println!("sound::instrument::clarinet()");
        }
    }
}

mod performance_group {
    use crate::sound::instrument;

    pub fn clarinet_trio() {
        instrument::clarinet();
        instrument::clarinet();
        instrument::clarinet();
    }
}

fn main() {
    // error[E0603]: module `instrument` is private
    performance_group::instrument::clarinet();
}
```

If you want to enable code calling your code to be able to refer to the type as if it was defined in that scope just as your code does, you can combine `pub` and `use`. 

So, the `use` within the `performance_group` module change to `pub use`.

```rust
mod sound {
    pub mod instrument {
        pub fn clarinet() {
            println!("sound::instrument::clarinet()");
        }
    }
}

mod performance_group {
    pub use crate::sound::instrument;

    pub fn clarinet_trio() {
        instrument::clarinet();
        instrument::clarinet();
        instrument::clarinet();
    }
}

fn main() {
    // Now, we can call the `clarinet` function through this new path.
    performance_group::instrument::clarinet();
}
```
