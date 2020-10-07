/// Method Syntax
/// 
/// Methods are defined within the context of a struct
/// (or an enum or a trait object), 
/// and their first parameter is always self,
/// which represents the instance of the struct the method is being called on.
/// 

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

// implementation block
// start an impl(implementation) block.
// Then we move the area function within the impl curly brackets
// and change the first parameter to be self 
// in the signature and everywhere within the body.
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }

    // Associated Function
    // we are allowed to define function
    // within impl blocks that don't take self as a parameter.
    // ex: String::from
    //
    // Associated finctions are often used for constructors that
    // will return a new instance of the struct.
    fn square(size: u32) -> Rectangle {
        Rectangle { width: size, height: size }
    }
}

/// Multiple impl Blocks
/// 
/// Each struct is allowed to have multiple impl blocks.
impl Rectangle {
    fn multi_impl(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

// In main, where we called the area function 
// and passed rect1 as a argument,
// we can intead use method syntax 
// to call the area method on our Rectangle instance.
fn main() {
    let rect1 = Rectangle { width: 30, height: 50 };
    let rect2 = Rectangle { width: 10, height: 40 };
    let rect3 = Rectangle { width: 60, height: 45 }; 

    println!(
        "The area of the rectangle is {} square pixels.",
        rect1.area()
    );

    // Methods with more Parameters
    // we want an instance of Rectangle to take another instance of Rectangle 
    // and return true if the second Rectangle can fit completely within self
    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));

    let sq = Rectangle::square(3);
    println!("sq: {:#?}", sq);   
}

