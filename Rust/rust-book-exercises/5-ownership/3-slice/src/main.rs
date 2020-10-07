fn main() {
    let mut s = String::from("Hello, world!");

    let word = first_word(&s); // word will get the value 5

    s.clear(); // this empties the String, making it equal to ""

    // word still has the value 5 here, 
    // but there's no more string that
    // we could meaningfully use the value eith. 
    // word is now totally invalid!

    /// # Solution for string slices
    /// 
    /// ```
    /// let s = String::from("Hello, world");
    /// let len = s.len();
    ///
    /// let hello = &s[0..5];  // or &s[..5]
    /// let world = &s[6..11]; // or &s[6..]
    /// 
    /// let slice = &s[0..len]; // or &s[..]
    /// ```


    /////////////////////////////////////////////////////
    //let mut s2 = String::from("Hello, world!");
    
    // this is immutable reference 
    // we cannot also take a mutable reference.
    //let word_solution = first_word_solution(&s2);

    // Because clear need to truncate the String,
    // it tries to take a mutable reference, which fails.
    //s2.clear(); // error!
    ///////////////////////////////////////////////////////
    
    // Fix
    let mut my_string = String::from("hello, world");
    let word_1 = first_word_solution_fix(&my_string[..]);

    // The type of "my_string_literal" here is &str
    let my_string_literal = "hello, world";
    let word_1 = first_word_solution_fix(&my_string_literal[..]);

    let word_1 = first_word_solution_fix(my_string_literal);

    my_string.clear();
    println!("the first word is: {}", word_1);
}

fn first_word(s: &String) -> usize {
    // Convert string to an array of bytes
    let bytes = s.as_bytes();

    // iter: create an iterator over the array of bytes
    // Because we get a reference to the element from .iter().enumerate(), 
    // we use & in the pattern.
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return i;
        }

        println!("{}: {}", i, item);
    }

    s.len()
}

/// Having to worry about the index in word 
/// getting out of sync with the data in s 
/// is tedious and error prone!
/// Managing these indices is even more brittle 
/// if we write a second_word function.
/// 
/// 
/// This fn tracking a strating and an endind index,
/// and we have even more values that were
/// caiculated from data in particular state
/// but aren't tied to that state at all.
/// 
/// `` 
/// fn second_word(s: &String) -> (usize, usize) {
///
/// }
/// ```

// Luckliy, Rust has a solution to this proble: string slices.

// Return a slice
// The type that signifies "string slice" is written as &str
fn first_word_solution(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}

// Fix!!! 
fn first_word_solution_fix(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}

