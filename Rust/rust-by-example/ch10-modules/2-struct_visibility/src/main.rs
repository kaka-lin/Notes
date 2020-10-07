mod my {
    // A public struct with a public field of generic type `T`
    pub struct OpenBox<T> {
        pub contents: T,
    }

    // A public struct with a private field of generic type `T`
    #[allow(dead_code)]
    pub struct CloseBox<T> {
        contents: T,
    }

    impl<T> CloseBox<T> {
        // A public constructor method
        pub fn new(contents: T) -> CloseBox<T> {
            CloseBox { contents }
        }
    }
}

fn main() {
    // Public structs with public fields can be constructed as usual
    let open_box = my::OpenBox {
        contents: "public information",
    };

    // and their fields can be normally accessed.
    println!("The open box contains: {}", open_box.contents);

    // Public structs with private fields cannot be constructed using field names.
    // Error! `ClosedBox` has private fields
    //let closed_box = my::ClosedBox { contents: "classified information" };

    // However, structs with private fields can be created using
    // public constructors
    let _closed_box = my::CloseBox::new("classified information");

    // and the private fields of a public struct cannot be accessed.
    // Error! The `contents` field is private
    //println!("The closed box contains: {}", _closed_box.contents);
}
