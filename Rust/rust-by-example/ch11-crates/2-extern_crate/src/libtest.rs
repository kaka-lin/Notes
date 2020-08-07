pub fn public_function() {
    println!("called libtest's `public_function()`");
}

fn private_function() {
    println!("called libtest's `private_function()`");
}

pub fn indirect_access() {
    print!("called libtest's `indirect_access()`, that\n> ");

    private_function();
}
