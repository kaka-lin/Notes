use deeply::nested::function as other_function;

fn function() {
    println!("function()");
}

mod deeply {
    pub mod nested {
        pub fn function() {
            println!("deeply::nested::function()");
        }

        pub fn my_first_function() {
            println!("deeply::nested::my_first_function()");
        }

        pub fn my_second_function() {
            println!("deeply::nested::my_second_function()");
        }
    }
}

/*
use deeply::nested::{
    my_first_function,
    my_second_function,
    function
};
*/

fn main() {
    //my_first_function();

    // Easier access to `deeply::nested::function`
    other_function();

    println!("Enter block");
    {
        // This is equivalent to `use deeply::nested::function as function`.
        // This `function()` will shadow the outer one.
        use deeply::nested::function;
        function();

        println!("Leaving block");
    }

    function();
}

