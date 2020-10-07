# The `use` declaration

The `use` declaration can be used to bind a full path to a new name.

## Example 

```rust
mod sound {
    pub mod instrument {
        pub fn clarinet() {
            // Function body code goes here
        }
    }
}

use crate::sound::instrument;

fn main() {
    instrument::clarinet();
    instrument::clarinet();
    instrument::clarinet();
}
```

## `as` keyword

You can use the `as` keyword to bind imports to a different name

### Example

```rust
use std::fmt::Result;
use std::io::Result as IoResult;

fn function1() -> Result {}
fn function2() -> IoResult<()> {}
```
