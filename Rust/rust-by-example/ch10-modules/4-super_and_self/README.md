# `super` and `self`

The `super` and `self` keywords can be used in the path to remove ambiguity when accessing items and to prevent unnecessary hardcoding of paths.

## `super`

You can construct relative paths beginning with `super`. Doing so is like starting a filesystem path with `..`: the path starts from the `parent` module, rather than current module.

### Example

```rust
mod instrument {
    fn clarinet() {
        super::breathe_in();
    }
}

fn breathe_in() {

}
```

### Advantage

The reason you might want to choose a relative path starting with `super` rather than an absolute path starting with `crate` is that using `super` may make it easier to update your code to have a different module hierarchy, if the code defining the item and the code calling the item are moved together.

#### Example

```rust
mod sound {
    mod instrument {
        fn clarinet() {
            super::breathe_in();
        }
    }

    fn breathe_in() {
        // Function body code goes here
    }
}
```

---

## `self`

If you want to bring an item into scope with `use` and a relative path, you must start the path given to `use` with `self`.

### Example 

```rust
mod sound {
    pub mod instrument {
        pub fn clarinet() {
            // Function body code goes here
        }
    }
}

use self::sound::instrument;

fn main() {
    instrument::clarinet();
}
```
### Note

Starting relative paths with `self` when specified after `use` might not be necessary in the future.
