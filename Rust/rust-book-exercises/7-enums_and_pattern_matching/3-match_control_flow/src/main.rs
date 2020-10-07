/// The match Control Flow Operator
/// 
/// Think of a match expression as being like a coin-sorting machine
/// coins slide down a track with variously sizes holes along it,
/// and each coin falls through the first hole it encouters that it fits into.
/// In the same way, values go through each pattern in a match,
/// and at the first pattern the value "fits",
/// tje value falls into the associated code block to be used during execution.

/// # Patterns that Bind to Values
/// 
/// Another useful feature of match arms is
/// that they can bind to the parts of the values 
/// that match the patterns.
/// This is how we can extract values out of enum variants.

#[derive(Debug)] // so we can inspect the state in a minute
enum UsState {
    Alabama,
    Alaska,
    // --snip--
}

// We can add UsState to our enum bu changing the Quarter variant 
// to include a UsState value stored inside it
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}

fn value_in_cents(coin: Coin) -> u8 {
    // This seems very similar to an expression use with if,
    // but there's a big difference: with if,
    // the expression needs to return a Boolean value,
    // but match, it can be any type.
    match coin {
        // Coin::Penny -> pattern value, => separates the pattern and the code to run
        Coin::Penny => {
            println!("Lucky penny!");
            1
        }
        Coin::Nickel => 5,
        Coin::Dime => 10,
        // We add a variable call state to the pattern 
        // that natches values of the variant Coin::Quarter.
        // When a Coin::Quarter matches, the state variable will
        // bind to the value of that quarter's state
        // Then we can use state in the code for thar arm.
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        },
    }
}

fn main() {
    // coin would be 'Coin::Quarter(UsState::Alaska)'
    // When we compare that value with each of the match arms, 
    // none of them match until we reach Coin::Quarter(state).
    // At the point, the binding for state will be the value 'UsState::Alaska'.
    // We can then use that binding in the 'parintln!' expression,
    // thus getting the inner state value out of the 'Coin' enum variant for 'Quarter'
    let coin = value_in_cents(Coin::Quarter(UsState::Alaska));
}
