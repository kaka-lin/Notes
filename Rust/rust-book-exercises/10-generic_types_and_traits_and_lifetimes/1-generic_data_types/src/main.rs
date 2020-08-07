/// Generic Data Types
/// 
/// ```
/// fn largest_i32(list: &[i32]) -> i32 {
///     let mut largest = list[0];
///
///     for &item in list.iter() {
///         if item > largest {
///             largest = item;
///         }
///     }
///
///     largest
/// }
/// ```
/// 
/// ```
/// fn largest_char(list: &[char]) -> char {
///     let mut largest = list[0];
///
///     for &item in list.iter() {
///         if item > largest {
///             largest = item;
///         }
///     }
///
///     largest
/// }
/// ```

// 1. In function definitions
//   `>`: difined in std::cmp::PartialOrd
//   
//    like i32 and char that have a known size can be stored on the stack, 
//    so they implement the Copy trait. 
//    But when we made the largest function generic, 
//    it became possible for the list parameter to have types in it 
//    that don’t implement the Copy trait. 
//   `list[0]`: Copy
fn largest<T: PartialOrd + Copy>(list: &[T]) -> T {
    let mut largest = list[0];

    for &item in list.iter() {
        if item > largest {
            largest = item;
        }
    }

    largest
}

// 2. In Struct Definitions
struct Point<T> {
    x: T,
    y: T,
}

// Have different types.
struct Point2<T, U> {
    x: T,
    y: U,
}

// 3. In Enum Definitions
enum Option<T> {
    Some(T),
    None,
}

// Have different types.
enum Result<T, E> {
    Ok(T),
    Err(E),
}

// 4. In Method definitions
impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

// This code means the type `Point<f32> will have a method
// named distance_from_origin and other instance of  `Point<T>`
// where T is not of type f32 will not have this method defined. 
impl Point<f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}

// 5. A method that uses different generic types than its struct’s definition
impl<T, U> Point2<T, U> {
    fn mixup<V, W>(self, other: Point2<V, W>) -> Point2<T, W> {
        Point2 {
            x: self.x,
            y: other.y,
        }
    }
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];
    let result = largest(&number_list);
    println!("The largest number is {}", result);
    let char_list = vec!['y', 'm', 'a', 'q'];
    let result = largest(&char_list);
    println!("The largest char is {}", result);

    let integer = Point{ x: 5, y: 10 };
    let float = Point{ x: 1.0, y: 4.0 };

    let both_integer = Point2{ x: 5, y: 10 };
    let both_float = Point2{ x: 1.0, y: 4.0 };
    let integer_and_float = Point2{ x: 5, y: 4.0 };

    // method
    let p = Point{ x: 5, y: 10 };
    println!("p.x = {}", p.x());

    let p1 = Point2{ x: 5, y: 10};
    let p2 = Point2{ x: "Hello", y: 'c' };

    let p3 = p1.mixup(p2);
    println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
}
