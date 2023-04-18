# Example 1: Hello World

### Library

In this example we show how to integrate multiple `cc_library` targets from different packages.

#### 1. In the same directory

We have a `cc_library` named `hello-greet` and its header and source files are defined accordingly.

```starlark
cc_library(
    name = "hello-greet",
    srcs = ["hello-greet.cc"],
    hdrs = ["hello-greet.h"],
)
```

#### 2. In the other subdirectory

In Bazel, *subdirectories containing BUILD files are known as packages*. The new property `visibility` will tell Bazel which package(s) can reference this target, in this case the `//main` package can use `hello-time` library.

```starlark
cc_library(
    name = "hello-time",
    srcs = ["hello-time.cc"],
    hdrs = ["hello-time.h"],
    visibility = ["//main:__pkg__"],
)
```

### Binary

To use our `hello-time` library, an extra dependency is added in the form of //path/to/package:target_name, in this case, it's `//lib:hello-time`

```starlark
cc_binary(
    name = "hello-world",
    srcs = ["hello-world.cc"],
    deps = [
        ":hello-greet",
        "//lib:hello-time",
    ],
)
```

## Build

To build this example, use:

```bash
$ bazel build //main:hello-world
```

In the run log you can see where the executable was built so you can locate it and use it.

You can also get the output path with the bazel cquery command. For
example, the command below would print the path to the output file. This
is a useful technique for use in scripts, where you do not want to parse the
`bazel build` output.

```
$ bazel cquery --output=starlark \
    --starlark:expr="' '.join([f.path for f in target.files.to_list()])" \
    //main:hello-world
```
