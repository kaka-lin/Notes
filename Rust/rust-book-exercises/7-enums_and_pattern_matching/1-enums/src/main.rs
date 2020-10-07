/// Enums
/// 
/// Enum values can only be one of the variants
/// ex: IP address (version four and version six)
enum IpAddr {
    v4(String), 
    v6(String),
    v4_2(u8, u8, u8, u8),
}

/// Standard Library 
///
/// struct Ipv4Addr {
///     // --snip--
/// }
/// 
/// struct Ipv6Addr {
///     // --snip--
/// }
/// 
/// enum IpAddr {
///     V4(Ipv4Addr),
///     V6(Ipv6Addr),
/// }

enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

// There is one more similarity between enums and structs: 
// just as we’re able to define methods on structs using impl, 
// we’re also able to define methods on enums. 
// Here’s a method named call 
// that we could define on our Message enum:
impl Message {
    fn call(&self) {
        // method body would be defined here
        // pattern matching 來決定要執行什麼程式
    }
}

fn main() {
    let home = IpAddr::v4(String::from("127.0.0.1"));
    let loopback = IpAddr::v6(String::from("::1"));

    let hoem_2 = IpAddr::v4_2(127, 0, 0, 1);

    let m = Message::Write(String::from("hello"));
    m.call();
}

