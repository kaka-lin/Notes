/// # Unrecoverable Errors with `panic!`
/// 
/// Sometimes, bad things happen in your code,
/// and there's nothing you can do about it.
/// In these case, Rust has the `panic!` macro executes,
/// your program will print a failure message, 
/// unwind and clean up the stack, and then quit.
/// This most commonly occurs when a bug of some kind has been detected
/// and it's not clear to the programmer how to handle the error.
/// 
/// ## Unwinding the stack or Aborting in Response to a Panic
/// 
/// 1. Unwinding(default)
///   Rust walks back up the stack and cleans up the data 
///   from each function it encounters.
/// 2. Abort
///   Ending the program without cleaning up.
///   
///   If in your project you need to make the resulting binary
///   as small as possible, you can switch form unwinding to aborting upon a panic
///   by adding ```panic - abort``` to the appropriate [profile] sections
///   in your `Cargo.toml` file, For example:
/// 
///   Cargo.toml
///   
///   ```
///   [profile.release]
///   panic = 'abort'
///   ```

fn main() {
    // 1. Calling `panic` directly!
    //panic!("crash and burn"); // -> RUST_BACKTRACE=1 cargo run

    // 2. bug in our code
    let v = vec![1, 2, 3];

    v[99];
}
