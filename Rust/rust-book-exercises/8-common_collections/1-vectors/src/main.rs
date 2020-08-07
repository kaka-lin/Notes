/// Vectors

fn main() {
    // 1. Creating a new, empty vector
    //   We added a type annotaion(註解) here.
    //   Because weare'n inserting any values into this vector.
    let v_1: Vec<i32> = Vec::new();

    // 2. Once you insert valuse
    //   You don't need to add a type annotation here.
    //   Because you already insert values, 
    //   Rust can infer the type.
    let v_2 =vec![1, 2, 3];

    // 3. Updating a Vector
    let mut v = Vec::new();
    v.push(5);
    v.push(6);

    // 4. Dropping a Vector Drops Its Elements
    //   Like any other struct, 
    //   a vector is freed when it goes out of scope

    // 5. Reading Elements of Vector
    //   1. index
    //   2. get()
    let v_3 = vec![1, 2, 3, 4, 5];

    let third: &i32 = &v_3[2];
    println!("The third element is {}", third);

    match v_3.get(2) {
        Some(third) => println!("The third element is {}", third),
        None => println!("There is no third element."),
    }

    /// Notes:
    /// 
    /// ```
    /// let v = vec![1, 2, 3, 4, 5];
    /// 
    /// let dose_not_exist = &v[100];
    /// let does_not_exist = v.get(100);
    /// ```
    /// 
    /// When we run this code, the first [] method will cause
    /// the program to panic because it references a nonexistent element.
    /// -> This method is best used when you want your program to crash
    ///    if there's an attempt to access an element past the end of the vecror.
    /// 
    /// When the get() method is passed and index that is outside the vector,
    /// it returns None without panicing.
    /// -> You would use this method if accessing an element 
    ///    beyond the range of the vector happens occasionally under normal circumstances

    // 6. Iterating over the Values in a Vector
    let v_4 = vec![100, 32, 67];
    for i in &v_4 {
        println!("{}", i);
    }

    let mut v_5 = vec![100, 32, 67];
    for i in &mut v_5 {
        // use the dereference operator (*) to get to the value in i 
        // before we can use the += operator
        *i += 50;
        println!("{}", i);
    }
}
