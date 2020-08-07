# Struct visibility

Structs have an extral level of visibility with their fields. The visibility defaults to private, and can be overridden with the `pub` modifier. 

This visibility only matters when a struct is accessed from outside the module where it is defined, and has the goal of hiding information(encapsulation).

## Example

If you use `pub` before a struct definition, you make the struct public. However, the struct's fields are still private.

You can choose to make each field public or not on a case-by-case basis.

Filename: src/main.rs

```rust
mod plant {
    // public `plant::Vegetable`
    pub struct Vegetable {
        pub name: String, // public `name` field
        id: i32,          // private `id` field
    }

    impl Vegetable {
        pub fn new(name: &str) -> Vegetable {
            Vegetable {
                name: String::from(name),
                id: 1,
            }
        }
    }
}

fn main() {
    let mut v = plant::Vegetable::new("squash");

    v.name = String::from("butternut squash");
    println!("{} are delicious", v.name);

    // The next line won't compile if we uncomment it:
    //println!("The ID is {}", v.id);
}
```

* Note:

    Also note that because `plant::Vegetable has a private field`, the struct `needs to provide a public associated function that constructs an instance` of Vegetable (we’ve used the conventional name `new` here). If Vegetable didn’t have such a function, we wouldn’t be able to create an instance of Vegetable in main because we’re not allowed to set the value of the private id field in main.

---

## Enum visibility

If you make a public enum, all of its variants are public. You only need the `pub` before the `enum` keyword.

### Example

Filename: src/main.rs

```rust
mod menu {
    pub enum Appetizer {
        Soup,
        Salad,
    }
}

fn main() {
    let order1 = menu::Appetizer::Soup;
    let order2 = menu::Appetizer::Salad;
}
```


