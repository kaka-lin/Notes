# Example 2: Including multiple files in a target

### Library

您可以使用 [glob](https://bazel.build/reference/be/functions?hl=zh-tw#glob) 在單一目標中加入多個檔案。例如：

```starlark
cc_library(
    name = "all-lib",
    srcs = glob(["*.cc"]),
    hdrs = glob(["*.h"]),
)
```

在此 target 中，Bazel 會在包含此目標的 `BUILD` 檔案 (不包括子目錄) 的相同目錄中，建構找到的所有 `.cc` 和 `.h` 檔案。

### Binary

```starlark
cc_binary(
    name = "hello-world",
    srcs = ["hello-world.cc"],
    deps = [
        ":all-lib",
    ],
)
```

## Build

To build this example, use:

```bash
$ bazel build //src:hello-world
```
