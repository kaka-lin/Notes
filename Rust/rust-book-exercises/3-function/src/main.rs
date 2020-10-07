/// # Function Bodies Contain Statements(陳述式) and Expressions(表達式)
/// 
/// Function bodies are made up of a series of statements
/// optionally ending in an expression.
/// 
/// 1. Statements:  are instructions that perform some action 
///                 and do not reture a value.
/// 
/// ```
/// fn main() {
///     // Creating a variable and assigning a value to it 
///     // with the let keyword is a statement
///     let y = 6;
/// }
/// ```
/// 
/// Statements do not return values. 
/// Therefore, you can’t assign a let statement 
/// to another variable, 
/// as the following code tries to do; you’ll get an error:
/// 
/// ``` 
/// fn main() {
///     lex x = (let y = 6);
/// }
/// ```
/// 
/// 2. Expressions: evaluates to a result value
/// 
/// ex: 5 + 6
/// 
/// Expressions can be part of statements, ex:
///   the 6 in the statement let y = 6; 
///   is an expression that evaluates to the value 6.

fn print_sum(x: i32, y: i32) {
    println!("sum is: {}", x + y);
}

// Rust 主要是個以表達式(expression)為基礎的語言
// 它只有兩種陳述式(statement)，而其他的都是表達式
// 表達式回傳值，而陳述式則否。
fn add_one(x: i32) -> i32 {
    // 如果一個函數以分號結果，他的返回類型將是() ，表示沒有返回值
    x + 1 // 隱式回傳值
}

/* 發散函式(Diverging functions)
 *
 * Rust 也有一些特別的語法叫做「發散函式」，這種函式不回傳值：
 * 一個發散函式可以被用在任何型別上
 * ex: let x: i32 = diverges();
 */
fn diverges() -> ! {
    panic!("This function never returns")
}

fn main() {
    println!("Hello, Function");

    let mut val = 5;
    let mut reval = add_one(val);
    println!("function: add_one({}) return {}", val, reval);

    val = 7;
    reval = add_one(val);
    println!("function: add_one({}) return {}", val, reval);

    let (x, y) = (5, 10);
    println!("fuction: print_sum({}, {})", x, y);
    print_sum(x, y);

    // 例子： x = y = 5 (in other language, ex; python)
    // 賦值到一個已經綁定的變數（例如 y = 5）仍然是個表達式，
    // 雖然它的值沒有什麼用,不像其他語言的賦值會被當成賦予的數值（在前面的例子中會是 5），
    // 在 Rust 中賦值的回傳值會是一個空的多元組（tuple）()，
    // 因為賦予的值 只能有一個擁有者，所以其他任何回傳值都會讓人感到意外：
    let mut y = 5;
    let x = (y = 6); // x has the value `()`, not `6`

    // 函式指標(Function pointers)
    let f: fn(i32) -> i32;
    // without type inference
    let f: fn(i32) -> i32 = add_one;
    let six = f(5);
    println!("f(5) ->  {}", six);

    let g: fn(i32) -> i32;
    // with type inference
    let g = add_one;
    let six_2 = g(5);
    println!("g(5) ->  {}", six_2);

    let mut v = vec![1, 2, 3];

    for i in &v {
        println!("{}", i);
    }
}
