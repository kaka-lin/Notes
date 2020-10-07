fn main() {
    
    // 1. loop
    //   使用 loop {} 代替 while true {}
    //loop {
    //    println!("Loop forever!");
    //}

    // 2. 枚舉(Enumerate)
    //   當你需要追蹤你已經循環了幾次，你可以使用 .enumerate()
    for (i, j) in (5..10).enumerate() {
        println!("i = {} and j = {}", i, j);
    }

    println!();

    let lines = "hello\nworld".lines();

    for (linenumber, line) in lines.enumerate() {
        println!("{}: {}", linenumber, line);
    }

    println!();

    // 3. 迴圈標籤(Loop labels)
    'outer: for x in 0..10 {
        'inner: for y in 0..10 {
            if x % 2 == 0 { continue 'outer; }
            if y % 2 == 0 { continue 'inner; }
            println!("x: {}, y: {}", x, y);
        }
    }

}
