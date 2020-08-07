#[derive(Debug)]
enum Version { Version1, Version2 }

fn parse_version(header: &[u8]) -> Result<Version, &'static str> {
    match header.get(0) {
        None     => Err("invalid header length"),
        Some(&1) => Ok(Version::Version1),
        Some(&2) => Ok(Version::Version2),
        Some(_)  => Err("invalid version"), 
    }
}

fn multiply(first_number_str: &str, second_number_str: &str) -> i32 {
    // Let's try using `unwrap()` to get the number out. Will it bite us?
    let first_number = first_number_str.parse::<i32>().unwrap();
    let second_number = second_number_str.parse::<i32>().unwrap();
    first_number * second_number
}

use std::num::ParseIntError;

// () is the unit type, analogous to a void return type in other languages.
fn main() -> Result<(), ParseIntError> {
    let version = vec![1, 2, 3, 4];
    for index in &version {
        match index {
            1 => println!("working with version: Version1"),
            2 => println!("working with version: Version2"),
            _ => println!("error pasing"),

        }
    }

    println!("\npase_version: ");
    let version = parse_version(&[1, 2, 3, 4]);
    match version {
        Ok(v) => println!("working with version: {:?}", v),
        Err(e) => println!("error parsing header: {:?}", e),
    }

    ////////////////////////////////////////////////////////
    
    println!("\nmultiply(parse())");
    let twenty = multiply("10", "2");
    println!("double is {}", twenty);

    // unsuccessful case
    //let tt = multiply("t", "2");
    //println!("double is {}", tt);

    ////////////////////////////////////////////////////////

    let number_str = "10";
    let number = match number_str.parse::<i32>() {
        Ok(number)  => number,
        Err(e) => return Err(e),
    };
    println!("{}", number);

    let number_str = "t";
    let number = match number_str.parse::<i32>() {
        Ok(number)  => number,
        Err(e) => return Err(e),
    };
    println!("{}", number);

    ////////////////////////////////////////////////////////

    Ok(())
}
