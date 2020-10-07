fn main() {
    let s1 = String::from("Hello");
    let len = calculate_length(&s1);
    println!("The length of '{}' is {}.", s1, len);

    let mut s2 = String::from("Hello");
    change(&mut s2);
    println!("{}", s2);

    /// # Restriction for Mutable Reference
    /// But Mutable references have ong big restriction:
    ///   you can have only one mutable reference to
    ///   a particular piece of data in a particular scope
    ///
    /// This code will fall:
    /// 
    /// ``` 
    /// fn main() {
    /// 
    ///     let mut s = String::from("hello");
    /// 
    ///     let r1 = &mut s;
    ///     let r1 = &mut s;
    ///     println!("{}, {}", r1, r2);
    /// }  
    /// ```
    /// 
    /// --> error[E0499]: cannot borrow `s` as mutable more than once at a time
    
    // we can use curly brackets(大括號) to create a new scope, 
    // allowing for multiple mutable references,
    // just not simultaneous ones
    let mut s = String::from("Hello multi mutable reference");

    {
        let r1 = &mut s;
        println!("{}", r1);
    } // r1 goes out of scope here, so we can make a new reference with no problems.

    let r2 = &mut s;
    println!("{}", r2);
}

// immutable reference
fn calculate_length(s: &String) -> usize {
    s.len()
}

// mutable reference
fn change(s: &mut String) {
    s.push_str(", world");
}
