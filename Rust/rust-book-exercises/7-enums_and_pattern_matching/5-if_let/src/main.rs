#[derive(Debug)] 
enum UsState {
    Alabama,
    Alaska,
    // --snip--
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}

fn main() {
    let some_u8_value = Some(0u8);
    //match some_u8_value {
    //    Some(3) => println!("three"),
    //    _ => (),
    //}
    if let Some(3) = some_u8_value {
        println!("three");
    }

    let coin = Coin::Quarter(UsState::Alaska);
    value_in_cents(coin);
}

fn value_in_cents(coin: Coin) {
    let mut count = 0;
    //match coin {
    //    Coin::Quarter(state) => println!("State quarter from {:?}!", state),
    //    _ => count += 1,  
    //}
    if let Coin::Quarter(state) = coin {
        println!("State quarter from {:?}!", state);
    } else {
        count += 1;
    }
}
