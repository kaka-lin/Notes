/// 所有權(Ownership)
/// 
/// 本指南是當前 Rust 的三個所有權之一
/// 這是 Rust 最獨特且引人注目的功能之一
/// 所有權是 Rust 用來達成其最大的目標 '記憶體安全' 的方法
/// 他有幾個概念，各自有各自的章節：
/// 
///   1. 所有權(ownership)
///   2. 借用(borrowing)，及其相關功能 '參照(reference)'
///   3. 生命週期(lifetime)，借用的進階概念
/// 
/// 這三章依序相關，你需要了解全部三章來完整了解所有權系統

fn main() {
    /// 1. 所有權(Ownership)
    ///
    /// 變數綁定在 Rust 中有個屬性：它們會有所綁定值的『所有權』
    /// 這代表當綁定離開有效範圍，Rust就會釋放所綁定的資源
    /// 
    /// ```
    /// fn foo() {
    ///     let v = vec![1, 2, 3]
    /// }
    /// ```
    
    /// 2. 移動語意(Move semantics)
    /// 
    /// Rust 確保所有的資源都只有一個對應的綁定, ex:
    ///
    /// ```
    /// let v = vec![1, 2, 3];
    /// let v2 = v;
    /// println!("v[0] is: {}", v[0]); 
    ///   --> error[E0382]: use of moved value: `v`
    /// ```
    /// 
    /// 當我們定義一個會取得所有權的函式,且試著在傳遞參數後使用同個參數時
    /// 會發生類似的事情
    /// 
    /// ```
    /// fn take(v: Vec<i32>) {
    ///     // what happens here isn’t important.
    /// }
    /// 
    /// let v = vec![1, 2, 3];
    /// take(v)
    /// println!("v[0] is: {}", v[0]);
    ///   --> error[E0382]: use of moved value: `v`
    /// ```
    /// 
    
    ///////////////////////////////////////////////////////////
    /// The string type (heap)
    
    let mut s = String::from("hello");
    s.push_str(", world!"); // push_str() appends a literal to a String
    println!("{}", s); // This is will print `hello world!`

    //let s1 = String::from("hello");
    //let s2 = s1;
    //println!("{}, world!", s1); // error[E0382]: use of moved value: `s1`

    // deeply copy -> clone()
    let s1 = String::from("Hello");
    let s2 = s1.clone();
    println!("s1 = {}, s2 = {}", s1, s2);

    // Stack-Only Data: Copy
    let x = 5;
    let y = x;
    println!("x = {}, y = {}", x, y);
    /// But this code seems to contradict what we just learned: 
    /// we don’t have a call to clone, 
    /// but x is still valid and wasn’t moved into y.
    /// 
    /// The reason is that types such as integers 
    /// that have a known size at compile time 
    /// are stored entirely on the stack, 
    /// so copies of the actual values are quick to make
    /// That means there’s no reason 
    /// we would want to prevent x from being valid 
    /// after we create the variable y.
    /// In other words, 
    /// there’s no difference between deep and shallow copying here, 
    /// so calling clone wouldn’t do anything 
    /// different from the usual shallow copying
    ///  and we can leave it out.   
    /// 
    /// Here are some of the types that are Copy:
    /// 
    /// 1. All the integer types, such as u32.
    /// 2. The Boolean type, bool, with values true and false.
    /// 3. All the floating point types, such as f64.
    /// 4. The character type, char.
    /// 5. Tuples, if they only contain types 
    ///    that are also Copy. 
    ///    For example, (i32, i32) is Copy, 
    ///             but (i32, String) is not.

    /// Ownership and function
    ///
    /// The semantics for passing a value to a function 
    /// are similar to those for assigning a value to a variable.
    ///
    /// Passing a variable to a function will move or copy,
    /// just as assignment dose.
    
    let s_fn = String::from("hello"); // s_fn comes into scope 
    takes_ownership(s_fn); // s_fn's value moves into the function...
                           // ... and so is no longer valid here

    let x = 5; // x comes into scope
    makes_copy(x); // x would move into the function,
                   // but i32 is Copy, so it's oky to still
                   // use x afterward
} // Here, x goes out of scope, then s_fn. 
  // But because s_fn's value was moved, nothing
  // special happens.

fn takes_ownership(some_string: String) { // some_string comes into scope
    println!("{}", some_string);
} // Here, some_string goes out of scope and `drop` is called. 
  // The backing memory is freed.

fn makes_copy(some_integer: i32) { // some_integer comes into scope
    println!("{}", some_integer);
} // Here, some_integer goes out of scope. 
  // Nothing special happens.
