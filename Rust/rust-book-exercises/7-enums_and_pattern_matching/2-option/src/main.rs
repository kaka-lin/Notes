/// Option
/// 
/// Option which is another enum defined by the standard library.
/// The Option type is used in many palces
/// because it encodes the very commom scenario
/// in which a value could be something or 
/// it could be nothing.
/// 
/// Expressing this concept in terms of the type system
/// means the compiler can check whether you've handle 
/// all the cases you should be handling;
/// this function can prevent bugs that 
/// are extremely common in other programming languages.
///
/// Rust doesn't have the null feature

/// Rust does not have nulls,
/// but it does have an enum that
/// can encode the concept of a value being
/// present(存在) or absent(不存在)
/// This enum is Option<T>, and it is defined by the standard library as follow:
///
/// ```
/// <T> means the Some variant of the Option enum 
/// can hold one piece of data of any type
/// 
/// enum Option<T> {
///     Some(T),
///     None,
/// }
/// ```

fn main() {
    let some_number = Some(5);
    let some_string = Some("a string");

    // If we use None rather than Some,
    // we need to tell Rust what type of Option<T> we have.
    let absent_number: Option<i32> = None;
}
