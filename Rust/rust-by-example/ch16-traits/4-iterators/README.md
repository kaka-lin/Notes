# Iterators

The `Iterator` trait is uesd to implement iterators over collections such as arrays.

The trait requires only a meths to be defined for the `next` element, which may be manually defined in an `impl` block or automatically defined (as in arrays and ranges).

As a point of convenience for common situations, the `for` construct turns some collections into iterators using the `.into_iterator()` method.

## Example

```rust
struct Fibonacci {
    curr: u32,
    next: u32,
}

// Implement `Iterator` for `Fibonacci`.
// The `Iterator` trait only requires a method to be defined for the `next` element.
impl Iterator for Fibonacci {
    type Item = u32;

    // Here we define the sequence using `.curr` and `.next`.
    // the return type is `Option<T>`:
    //     * When the `Iterator` is finished, `None` is returned.
    //     * Otherwise, the next value is wrapped in `Some` and re
    fn next(&mut self) -> Option<u32> {
        let new_next = self.curr + self.next;

        self.curr = self.next;
        self.next = new_next;

        // Since there's no endpoint to a Fibonacci sequence, the `Iterator` 
        // will never return `None`, and `Some` is always returned.
        Some(self.curr)
    }
}

// Returns a Fibonacci sequence generator
fn fibonacci() -> Fibonacci {
    Fibonacci { curr: 1, next: 1 }
}
```

---

## Trait std::iter::`IntoIterator`

```rust 
pub trait IntoIterator
where
    <Self::IntoIter as Iterator>::Item == Self::Item,
{
    type Item;
    type IntoIter: Iterator;
    fn into_iter(self) -> Self::IntoIter;
}
```

Conversion into an `Interator`.

By implementing `IntoIterator` for a type, you define how it will be converted to an iterator. This is common for types which describe a collections of some kinf.

One benefit of implementing IntoIterator is that your type will [work with Rust's for loop syntax](https://doc.rust-lang.org/std/iter/index.html#for-loops-and-intoiterator).

### Examples

Basice usage:

```rust
let v = vec![1, 2, 3];
let mut iter = v.into_iter();

assert_eq!(Some(1), iter.next());
assert_eq!(Some(2), iter.next());
assert_eq!(Some(3), iter.next());
assert_eq!(None, iter.next());
```

Implementing `IntoIterator` for your type:

```rust
// A sample collection, that's just a wrapper over Vec<T>
#[derive(Debug)]
struct MyCollection(Vec<i32>);

// Let's give it some methods so we can create one and add things
// to it.
impl MyCollection {
    fn new() -> MyCollection {
        MyCollection(Vec::new())
    }

    fn add(&mut self, elem: i32) {
        self.0.push(elem);
    }
}

// and we'll implement IntoIterator
impl IntoIterator for MyCollection {
    type Item = i32;
    type IntoIter = ::std::vec::IntoIter<i32>;

    fn into_iter(self) -> Self::IntoIter {
        self.0.into_iter()
    }
}

// Now we can make a new collection...
let mut c = MyCollection::new();

// ... add some stuff to it ...
c.add(0);
c.add(1);
c.add(2);

// ... and then turn it into an Iterator:
for (i, n) in c.into_iter().enumerate() {
    assert_eq!(i as i32, n);
}
```

It is common to use IntoIterator as a trait bound. This allows the input collection type to change, so long as it is still an iterator. Additional bounds can be specified by restricting on Item:

```rust
fn collect_as_strings<T>(collection: T) -> Vec<String>
    where T: IntoIterator,
          T::Item : std::fmt::Debug,
{
    collection
        .into_iter()
        .map(|item| format!("{:?}", item))
        .collect()
}
```


