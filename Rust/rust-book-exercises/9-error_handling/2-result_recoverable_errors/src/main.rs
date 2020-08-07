/// # Recoverable Errors with `Result`
/// 
/// Most errors aren't serious enough to require the program to stop entirely.
/// Sometimes, when a function fails, it's for a reason
/// that you can easily interpret and respond to.
/// For example, if you try to open a file and that operation falis
/// because the file dosen't exist, you might want to create
/// the file instead of terminating the process.
/// 
/// The `Result` enum is defined as having two variants,
/// -> `Ok` and `Err`, as follows:
/// 
/// ```
/// emun Result<T, E> {
///     Ok(T),
///     Err(E),
/// }
/// ```
/// 
/// Where the `T` and `E` are generic type parameters.
/// T: the type of the value that will be returned
///    in a success case within the `Ok` variant
/// E: the type of the erro that will be returned
///    in a failure case within the `Err` variant

use std::fs::File;
use std::io::ErrorKind;

fn main() {
    // 1. Let’s call a function that returns a Result value 
    //    because the function could fail.
    let f = File::open("hello.txt");

    let f = match f {
        Ok(file) => file,

        //Err(error) => {
        //    panic!("There was a problem opening the file: {:?}", error);
        //},

        // Matching on Different Errors
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Tried to create file but there was a problem: {:?}", e),
            },
            other_error => panic!("There was a problem opening the file: {:?}", other_error),
        },
    };

    // 2. `unwrap` and `expect`
    // 2-1. `unwrap`:
    //   Is a shortcut method that is implemented just like the `match` expression
    //   If the `Result` value is the ok variant, `unwrap` will return the value inside the `ok`.
    //   If the `Result` is the Err variant, `unwrap` will call the `panic!` macro for us.
    //let f = File::open("hello2.txt").unwrap();

    // 2-2. `expect`\
    //  Let us also choose the `panic!` error message.
    let f = File::open("hello3.txt").expect("Falied to open hello3.txt");
}
