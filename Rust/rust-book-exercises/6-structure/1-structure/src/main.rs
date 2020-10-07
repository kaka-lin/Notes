/// # Adding Useful Functionally with Derived Traits
/// 
/// Adding the annotation(註解) to derive(派生) the Debug trait(特徵) 
/// and printing the Rectangle instance using debug formatting

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle { width: 30, height: 50 };

    println!("rect1 is {:#?}", rect1);

    println!(
        "The area of the rectangle is {} square pixels.",
        area(&rect1)
    );
}

fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}
