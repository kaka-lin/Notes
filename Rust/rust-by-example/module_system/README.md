# Module System

A key question when writing program is `scope`: what names does the compiler know about at this location in the code? What functions am I allowed to call? What does this variable refer to?

Rust has a number of features related to `scopes`. This is sometimes called `the module system`, but it encompasses more than just modules:

- [Packages](#packages_and_crates)

    It are a `Cargo feature` that let you build, test, and share crates. 

- [Crates](#packages_and_crates)

    It are a tree of modules that produce a library or executable.

- [Modules](#modules)

    `Modules` and the `use` keyword let you control the scope and privacy of paths.

<span id="packages_and_crates"></span>
## Packages and Crates 

- A `crate` is a binary or library.
- The `crate root` is a source file that is used to know how to build a crate.
- A `package` has a `Cargo.toml` that describes how to build one or more crates. At most one crate in a package can be a library.

### Exapmle

So when we type `cargo new`, we're creating a package:

```bash
$ cargo new my-project
     Created binary (application) `my-project` package
$ ls my-project
Cargo.toml
src
$ ls my-project/src
main.rs
```

### Conventions

1. If you have a `src` directory containing `main.rs` in the same directory as a package's `Cargo.toml`

    => Cargo knows this package contains a `binary crate` with the same name as the package, and `src/main.rs` is its `crate root`.

2. If the package directory contains `src/lib.rs`

    => Cargo knows this package contains a `library crate` with the same name as the package, and `src/lib.rs` is its `crate root`.

```
Note: The crate root files are passed by Cargo to rustc to actually build the library or binary.
```

3. A package can contain `zero or one library crates` and as `many binary crates` as you’d like. There must be `at least one crate` (either a library or a binary) in a package.

```
Note: A package can have multiple binary crates by placing files in the src/bin directory: each file will be a separate binary crate.
```

<span id="modules"></span>
## Modules

Modules let us organize code into groups. 

### Example

Filename: src/main.rs

```rust
mod sound {
    pub mod instrument {
        pub fn clarinet() {
            println!("Hello sound::instrument::clarinet()");
        }
    }

    mod voice {

    }
}

fn main() {
    // Absolute path
    crate::sound::instrument::clarinet();

    // Relative path
    sound::instrument::clarinet();
}
```

Like we mentioned in the [Packages and Crates](#packages_and_cratess) section that `src/main.rs` and `src/lib.rs` are called `crate roots`. So we have a module tree that looks like:

```
crate
└── sound
    ├── instrument
    │   
    └── voice
```

### Modules as the Privacy Boundray

If you want to make an item like a function or struct private, you put it in a module. Here aer the privacy rules:

- All items are private bu default.
- You can use the `pub` keyword to make an item public.
- You aren't allowed to use private code defined in modules that are children oof current module.
- You are allowed to use any code defined in ancestor modules or current module.

#### Example

```rust
mod sound {
    mod instrument {
        fn clarinet() {
            println!("Hello sound::instrument::clarinet()");
        }
    }

    pub mod instrument2 {
        fn clarinet(){}
    }
}

fn main() {
    // error[E0603]: module `instrument` is private
    crate::sound::instrument::clarinet(); 
    
    // error[E0603]: function `clarinet` is private
    crate::sound::instrument2::clarinet();
}
```
