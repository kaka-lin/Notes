/// Propagating Errors
/// 
/// When you're writing a function whose implementation 
/// calls something that might fall, instead of handling 
/// the error within this function, you can return 
/// the error to calling code so that it can decide what to do.
/// This is known as `propagating` the error and gives more control
/// to calling code, where there might be more information or
/// logic that dictates how the error should be handle
/// than what you have available in the context of your code.

use std::io::{self, Read};
use std::fs::{self, File};

////////////////////////////////////////////////////////////////////////////////
// 1. A function that returns errors to the calling code using match. 
//
// Result<String, io::Error>
//   This means the function is returning a value of the type Result<T, E>
//   We chose io::Error as the return type of this function 
//   because that happens to be the type of the error value 
//   returned from both of the operations we’re calling in this function’s body 
//   that might fail: the File::open function and the read_to_string method.
fn read_username_from_file() -> Result<String, io::Error> {
    let f = File::open("hello.txt");

    let mut f = match f {
        Ok(file) => file,
        // we return early from this function 
        // and pass the error value from File::open back to the calling code 
        // as this function’s error value
        Err(e) => return Err(e),
    };

    let mut s = String::new();

    // read_to_string()
    //   Reading the contents of the file into s.
    //   Also returns a Result because it might fail,
    //   even thought File::open succeeded.
    //   So we need anthoer match to handle that Result.
    match f.read_to_string(&mut s) {
        Ok(_) => Ok(s),
        // However, we don’t need to explicitly say return, 
        // because this is the last expression in the function.
        Err(e) => Err(e),
    }
}
// We don't have enough information on what the calling code 
// is actually trying to do, so we propagate all the success
// or error information upward fot it to handle appropriately.

////////////////////////////////////////////////////////////////////////////////
// 2. A shortcut for Propagating Errors: the `?` Operator
fn read_username_from_file_2() -> Result<String, io::Error> {
    // The `?` placed after a `Result` value is defined to 
    // work in almost the same way as the `match` expressions
    // we defined to handle the `Result` values in function read_username_from_file().
    let mut f = File::open("hello.txt")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}

////////////////////////////////////////////////////////////////////////////////
// 3. Chaining method calls after the ? operator
// 
// The ? operator eliminates a lot of boilerplate 
// and makes this function’s implementation simpler.
// We could even shorten this code further 
// by chaining method calls immediately after the ?, as follow:
fn read_username_from_file_3() -> Result<String, io::Error> {
    let mut s = String::new();

    File::open("hello.txt")?.read_to_string(&mut s)?;
    Ok(s)
}

fn read_username_from_file_4() -> Result<String, io::Error> {
    fs::read_to_string("hello.txt")
}

////////////////////////////////////////////////////////////////////////////////
// 3. The ? Operator Can Only Be Used in Functions That Return Result
//
//    We can change how we write the main function 
//    so that it does return a Result<T, E>:
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let f = File::open("hello.txt")?;

    Ok(())
}
