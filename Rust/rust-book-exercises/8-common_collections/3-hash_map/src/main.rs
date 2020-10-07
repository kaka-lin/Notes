/// Hash Map
use std::collections;

fn main() {
    // 1. Creating an empty hash map with new
    let mut scores = collections::HashMap::new();

    // ket: String, value: i32
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);

    // 2. Creating a hash map with collect
    //  The collect method gathers data 
    //  into a number of collection types. Including HashMap
    //  For example, if we had the team names and initial scores
    //  in two separate vectors, we could use the zip method
    //  to create a vector of tuples where "Blue" is paired with 10, and so forth.
    //  Then we could use the `collect` method to turn that vector of tuples into a hash map
    let teams = vec![String::from("Blue"), String::from("Yellow")];
    let initial_scores = vec![10, 50];
    
    // The type annotation HashMap<_, _> is needed here 
    // because it's possible to `collect` into many different data structures
    // and Rust doesn't know which you want unless you specify.
    let scores: collections::HashMap<_, _> = teams.iter().zip(initial_scores.iter()).collect();

    for (key, value) in &scores {
        println!("{}: {}", key, value);
    }

    // 3. Ownership
    let field_name = String::from("Favorite color");
    let field_value = String::from("Blue");

    let mut map = collections::HashMap::new();
    map.insert(field_name, field_value);
    // field_name and field_value are invalid at this point, try using them and
    // see what compiler error you get!

    // 4. Updating a Hash Map
    let mut scores = collections::HashMap::new();
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Blue"), 25);

    println!("{:?}", scores);

    // 4-1. Only Inserting a Value if the Key Has No Value
    //  -> `entry`
    let mut scores = collections::HashMap::new();
    scores.insert(String::from("Blue"), 10);

    // The or_insert method on Entry is defined to 
    // return a mutable reference to the value for the corresponding Entry key if that key exists, 
    // and if not, inserts the parameter as the new value for this key and returns a mutable reference to the new value.
    scores.entry(String::from("Yellow")).or_insert(50);
    scores.entry(String::from("Blue")).or_insert(50);

    println!("{:?}", scores);

    // 4-2. Updating a Value Based on the Old Value
    println!();
    let text = "hello world wonderful world";

    let mut map = collections::HashMap::new();

    for word in text.split_whitespace() {
        // The or_insert method actually returns 
        // a mutable reference (&mut V) to the value for this key. 
        let count = map.entry(word).or_insert(10);
        *count += 1;
    }

    println!("{:?}", map);
}
