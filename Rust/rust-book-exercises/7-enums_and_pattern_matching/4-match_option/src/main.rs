/// Match Option<T>
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        None => None,
        Some(i) => Some(i + 1),
    }
}

fn main() {
    let five = Some(5);
    let six = plus_one(five);
    let none = plus_one(None);

    println!("{:?}", five);
    println!("{:?}", six);
    println!("{:?}", none);

    /// The _ Placeholder
    /// 
    /// Rust also has a pattern we can use 
    /// when we don’t want to list all possible values.
    /// 
    /// For example, a 'u8' can have valid values of 0 throught 255.
    /// If we only care about the values 1, 3, 5 and 7,
    /// we don't want to have to list out 0, 2, 4, 6, 8, 9 all the wau up to 255.
    /// We can use the special pattern '_' instead:
    
    let some_u8_value = 0u8;
    match some_u8_value {
        1 => println!("one"),
        3 => println!("three"),
        5 => println!("five"),
        7 => println!("seven"),
        // The () is just the unit value,
        // so nothing will happen in the _ case. 
        _ => (),
    }
    
}
