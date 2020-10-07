// The commoner has seen it all, and can handle any gift well.
// All gifts are handle explicitly using `match`
fn give_commoner(gift: Option<&str>) {
    match gift {
        // Specify a course of action for each case.
        Some("snake") => println!("Yuck! I'm throwing that snake in a fire"),
        Some(inner) => println!("{}? How nice.", inner),
        None => println!("No gift? Oh well."),
    }
}

// Our sheltered princess will `panic` at the sight of snakes.
// All gifts are handled implicitly using `unwrap`.
fn give_princess(gift: Option<&str>) {
    // `unwrap` returns a `panic` when it receives a `None`.
    let inside = gift.unwrap();
    if inside == "snake" {
        panic!("AAAaaaaa!!!!");
    }

    println!("I love {}s!!!!!", inside);
}

fn main() {
    let food  = Some("cabbage");
    let snake = Some("snake");
    let null_string  = Some("");
    let void  = None;

    give_commoner(food);
    give_commoner(snake);
    give_commoner(null_string);
    give_commoner(void);

    let bird = Some("robin");
    let nothing = None;

    give_princess(bird);
    give_princess(nothing);
}
