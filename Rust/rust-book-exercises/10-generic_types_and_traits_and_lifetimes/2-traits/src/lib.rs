/// # Traits: Defining Shared Behavior
/// 
/// A `trait` tells the Rust compiler about functionality
/// a particular type has and can share with other type.
/// We can use traits to define shared behavior in an abstract way.
/// We can use trait bounds to specify that a generic can be any type that has certain behavior.
/// 
/// Note: Traits are similar to a feature often called `interface`
///       in other languages, although with some difference.
/// 
/// ## Defining a Trait
/// 
/// - NewsArticle
///     
///     holds a news story filed in a particular location
/// 
/// - Tweet
/// 
///     can have at most 280 characters along with metadata
///     that indicates whether it was a new tweet, a retweet,
///     or a reply to another tweet.
///   
/// We want to make a media aggregator(聚合) library 
/// that can display summaries of data that might be 
/// stored in a `NewArticle` or `Tweet` instance.
/// To do this, we need a summary from each type,
/// and we need to request that summary by calling a summarize method on a instance.

pub trait Summary {
    /// instead of providing an implesmentation within curly brackets,
    /// we use a semicolon.
    /// Each type implementing this trait must provide its own custom behavior
    /// for the body of the method.
    /// 
    /// A trait can have multiple methods in its body
    /// the method signatures are listed one per line 
    /// and each line ends in a semicolon.
    
    //fn summaries(&self) -> String;

    /// ## Default Implementations
    /// 
    /// Sometimes it’s useful to have default behavior 
    /// for some or all of the methods in a trait 
    /// instead of requiring implementations 
    /// for all methods on every type. 
    /// 
    /// Then, as we implement the trait on a particular type, 
    /// we can keep or override each method’s default behavior.
    /// 
    /// ```
    /// fn summarize(&self) -> String {
    ///     String::from("(Read more...)")
    /// }
    /// ```
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }

    fn summarize_author(&self) -> String;
    /// Default implementations can call other methods in the `same trait`,
    /// even if those other methods don’t have a default implementations.
    fn summarize_df2(&self) -> String {
        format!("(Read more from {}...)", self.summarize_author())
    }
}

/// ## Implementing A Trait on a Type
/// 
/// Now that we’ve defined the desired behavior using the Summary trait, 
/// we can implement it on the types in our media aggregator.
/// 
/// - NewsArticle
/// 
///     holds a news story filed in a particular location 
pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Summary for NewsArticle {
    //fn summarize(&self) -> String {
    //    format!("{}, by {} ({})", self.headline, self.author, self.location)
    //}

    fn summarize_author(&self) -> String {
        format!("{}", "None")
    }
}

/// ## Implementing A Trait on a Type
/// 
/// - Tweet
/// 
///     can have at most 280 characters along with metadata
///     that indicates whether it was a new tweet, a retweet,
///     or a reply to another tweet.
pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }

    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}

/// ## Traits as Parameters
/// 
/// We can explore how to use traits to define functions that
/// accept many different types.
///
/// For example, We can define a function that
/// calls the `summarize` method on its parameter `item`,
/// which is of some type that implements the `Summary` trait.
pub fn notify(item: impl Summary) {
    println!("Breaking news! {}", item.summarize());
}

/// ## Trait Bound Syntax
/// 
/// The `impl Trait` syntax works for straightforward cases,
/// but is syntax sugar for a longer from.
/// The longer syntax is called a `trait bound`
pub fn notify_lon<T: Summary>(item: T) {
    println!("Breaking news! {}", item.summarize());
}

/// ### Trait Bound vs `impl Trait`
/// 
/// The `impl Trait` syntax is convenient
/// and makes for more concise code in straightforward cases.
/// 
/// The trait bound syntax is able to express more complexity in other cases.
/// For example, to have two parameters that implement `Summary`.
/// ```
/// pub fn notify_two_par(item1: impl Summary, item2: impl Summary) {}
/// ```
/// ```
/// pub fn notify_two_par_lon<T: Summary>(item1: T, item2: T) {}
/// ```
pub fn notify_two_par(item1: impl Summary, item2: impl Summary) {}

/// ### Trait Bound vs `impl Trait`
/// 
/// The `impl Trait` syntax is convenient
/// and makes for more concise code in straightforward cases.
/// 
/// The trait bound syntax is able to express more complexity in other cases.
/// For example, to have two parameters that implement `Summary`.
/// ```
/// pub fn notify_two_par(item1: impl Summary, item2: impl Summary) {}
/// ```
/// ```
/// pub fn notify_two_par_lon<T: Summary>(item1: T, item2: T) {}
/// ```
pub fn notify_two_par_lon<T: Summary>(item1: T, item2: T) {}


use std::fmt::{Display, Debug};


/// ## Specifying Multiple Trait Bound with the `+` Syntax
/// 
/// If notify needed to use display formatting on item as well as the summarize method, 
/// then the notify definition specifies 
/// that item must implement two traits: Display and Summary. 
/// This can be done using the `+` syntax:
/// ```
/// pub fn notify(item: impl Summary + Display) {}
/// ```
/// 
/// The `+` syntax is also valid with trait bounds on generic types:
/// ```
/// pub fn notify<T: Summary + Display>(item: T) {}
/// ```
pub fn notify_mul_trait(item: impl Summary + Display) {}

/// ## Specifying Multiple Trait Bound with the `+` Syntax
/// 
/// If notify needed to use display formatting on item as well as the summarize method, 
/// then the notify definition specifies 
/// that item must implement two traits: Display and Summary. 
/// This can be done using the `+` syntax:
/// ```
/// pub fn notify(item: impl Summary + Display) {}
/// ```
/// 
/// The `+` syntax is also valid with trait bounds on generic types:
/// ```
/// pub fn notify<T: Summary + Display>(item: T) {}
/// ```
pub fn notify_mul_trait_lon<T: Summary + Display>(item: T) {}


/// ## Clearer Trait Bound with `where` Clauses
/// 
/// There are downsides to using too many trait bounds. 
/// Each generic has its own trait bounds, 
/// so functions with multiple generic type parameters 
/// can have lots of trait bound information 
/// between a function’s name and its parameter list, 
/// making the function signature hard to read. 
/// 
/// For this reason, Rust has alternate syntax for specifying trait bounds
/// inside a `where` clause after the function signature.
/// ```
/// fn some_function<T: Display + Clone, U: Clone + Debug>(t: T, u: U) -> i32 {}
/// ```
fn some_function<T, U>(t: T, u: U) -> i32
    where T: Display + Clone,
          U: Clone + Debug
{
    0
}

/// ## Returning Types that Implement Traits
/// 
/// We can use the `impl Trait` syntax in return position as well,
/// to return a value of some type that implements a trait.
fn returns_summarizable() -> impl Summary {
    Tweet {
        username: String::from("horse_ebooks"),
        content: String::from("of course, as you probably already know, people"),
        reply: false,
        retweet: false,
    }
}