# Generic Types, Traits, and Lifetimes

Every programming language has tools for effectively handling the duplication of concepts. In Rust, one such tools is `generic`.

## Generic Types

Generics are abstract stand-ins for concrete types of other properties.

When we're writing code, we can express the behavior of generics or how they relate to other generics without knowing what will be in their place when compiling and running code.

## Traits

```
A trait is a collection of methods defined for unknown type:`self`. They can access other methods declared in the same trait.

Traits can be implemented for any data type. 
```

In this sections, we'll learn how to use `trait` to deifne behavior in a generic way. You can combine traits with generci types to constrain a generic type to only those types that have a particular behavior, as opposed to just any type.

## Lifetimes

A variety of generics that give the compiler information about how references relate to each other.

Lifetimes allow us to borrow values in many situations while still enabling the compiler to check that the references are valid.


