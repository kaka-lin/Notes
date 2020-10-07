fn give_princess(gift: &str) {
    // Princess hate snakes, so we need to stop if she disapproves！
    if gift == "snake" {
        panic!("AAAaaaaa!!!!");
    }

    println!("I love {}s!", gift);
}

fn main() {
    give_princess("teddy bear");
    give_princess("snake");
}
