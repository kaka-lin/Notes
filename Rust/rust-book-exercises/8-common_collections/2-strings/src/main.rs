fn main() {
    // 1. Creating a new, empty String
    let mut s1 = String::new();

    // 2. Using the to_string method to create a String from a string literal
    let data = "initial contents";
    let s_2 = data.to_string();
    // the method also works on a literal directly;
    let s_3 = "initial contents".to_string();
    // or 
    let s_4 = String::from("initial contents");

    // Remember that strings are UTF-8 encoded, 
    // so we can include any properly encoded data in them.
    // ex:
    let hello = String::from("hello");
    let hello_tw = String::from("你好");
    let hello_jp = String::from("こんにちは");
    println!("{}", hello);
    println!("    中文: {}", hello_tw);
    println!("    日文: {}", hello_jp);

    // 3. Updating a String
    // 
    // 3-1. push_str
    // The push_str method takes a string slice 
    // because we don’t necessarily want to 
    // take ownership of the parameter.
    let mut s_5 = String::from("foo");
    let s_6 = "bar";
    s_5.push_str(s_6); // s_5.push_str("bar"); 
    println!("s_6 is {}", s_6); // -> s_6 is bar

    // 3-2. +
    let s1 = String::from("Hello ");
    let s2 = String::from("world!");
    let s3 = s1 + &s2;
    // note s1 has been moved here and can no longer be used
    println!("s2: {}, s3: {}",s2, s3);

    // The reason s1 is no longer valid after the addition 
    // and the reason we used a reference to s2 
    // has to do with the signature of the method 
    // that gets called when we use the + operator. 
    // 
    // fn add(self, s: &str) -> String {}
    
    // 4. Concatenating multiple strings: format!
    let s1 = String::from("tic");
    let s2 = String::from("tac");
    let s3 = String::from("toe");

    let s = format!("{}-{}-{}", s1, s2, s3);
    println!("{}", s);

    // 5. Indexing into Strings -> non valid
    //
    // if you try to access parts of a String using indexing syntax 
    // in Rust, you’ll get an error.
    //let hello = String::from("hello world");
    //let answer = hello[0];
    //println!("{}", answer);

    // 6. Slicing Strings
    let hello = "hello world";
    let s = &hello[0..4];
    println!("{}", s); // hell

    // 7. Methods for literating Over Strings
    // 7-1 char
    for c in "Hello world! kaka".chars() {
        print!("{} ", c);
    }
    println!();

    // 7-2 bytes
    for b in "Hello world! kaka".bytes() {
        print!("{} ", b);
    }
    println!();
}
