use std::num::ParseIntError;

fn double_first(vec: &Vec<&str>) -> Option<Result<i32, ParseIntError>> {
    vec.first().map(|first| {
        first.parse::<i32>().map(|n| 2 * n)
    })
}

/// There are times when we'll want to stop processing on errors (like with ?) 
/// but keep going when the Option is None
/// 
/// swap the `Result` and `Option`
fn double_first_2(vec: &Vec<&str>) -> Result<Option<i32>, ParseIntError> {
    let opt = vec.first().map(|first| {
        first.parse::<i32>().map(|n| 2 * n)
    });

    println!("before map_or: {:?}", opt);
    // if is `Some` -> return `Some`, or return default value `Ok(None)`.
    let opt = opt.map_or(Ok(None), |r| r.map(Some))?;
    println!("after map_or: {:?}", opt);
    
    Ok(opt)
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("The first doubled is {:?}", double_first(&numbers));
    println!("The first doubled is {:?}", double_first(&empty));
    println!("The first doubled is {:?}", double_first(&strings));

    //let numbers = vec!["42", "93", "18"];
    //let empty = vec![];
    //let strings = vec!["tofu", "93", "18"];
    println!("-----------------------------------");
    println!("The first doubled(2) is {:?}\n", double_first_2(&numbers));
    println!("The first doubled(2) is {:?}\n", double_first_2(&empty));
    println!("The first doubled(2) is {:?}\n", double_first_2(&strings));
}
