# Image read/write in C++ through filestream

The example code for building C++ with `Bazel` and `Clang`.

## Before you begin

### Set up the build environment

1. 新增所需要的 `WORKSPACE` 和 `BUILD` 檔案

2. 在 root 目錄中建立 `.bazelrc` 檔案，並在當中加入下列內容，以使用 `--config` flag:

    ```starlark
    # Use our custom-configured c++ toolchain.

    build:clang_config --crosstool_top=//toolchain:clang_suite

    # Use --cpu as a differentiator.

    build:clang_config --cpu=k8

    # Use the default Bazel C++ toolchain to build the tools used during the
    # build.

    build:clang_config --host_crosstool_top=@bazel_tools//tools/cpp:toolchain
    ```

    針對項目 `build:{config_name} --flag=value`，command line flag `--config={config_name}` 與該特定 flag 相關聯。請參閱有關使用 flag 的說明文件：[crosstool_top](https://bazel.build/docs/user-manual#crosstool-top)、[cpu](https://bazel.build/docs/user-manual#cpu) 和 [host_crosstool_top](https://bazel.build/docs/user-manual#host-crosstool-top)。

    使用 `bazel build --config=clang_config //main:<TARGET_NAME>` 建構目標時，Bazel 會使用 [cc_toolchain_suite](https://bazel.build/reference/be/c-cpp?hl=zh-tw#cc_toolchain_suite) `//toolchain:clang_suite` 的自訂 Toolchain。套件可能會針對不同的 CPU 列出不同的 toolchains，因此使用 `--cpu=k8` 旗標來區分兩者。

    > Note: The K8 was the first implementation of the AMD64 64-bit extension to the x86 instruction set architecture

    由於 Bazel 在建構期間使用了許多用 C++ 編寫的內部工具，例如: process-wrapper，因此主機平台會指定現有的預設 C++ 工具鍊，因此使用這些工具鍊建構這些工具，而非使用本範例中建立的工具。

#### 補充: CPUs support in Toolchains in Bazel

Toolchains in Bazel support different CPUs. Valid CPUs as below or you can see [bazel/tools/cpp/CROSSTOOL](https://github.com/bazelbuild/bazel/blob/cb0fb033bad2a73e0457f206afb87e195be93df2/tools/cpp/CROSSTOOL#L5-L54)

```
[
 k8,
 piii,
 darwin,
 freebsd,
 armeabi-v7a,
 arm,
 aarch64,
 x64_windows,
 x64_windows_msvc,
 s390x,
 ppc,
 ppc64,
]
```

## Configuring the C++ toolchain

This example is running on macOS if you are using another OS, you need to check the paths of links from [steps 7 to 9](#7-run-the-build-again).

And you can refer to the Bazek document: [Bazel 教學課程：設定 C++ 工具鍊](https://bazel.build/tutorials/ccp-toolchain-config?hl=zh-tw)


### 1. Build with bazel

```bash
$ bazel build --config=clang_config //main:read-image
```

由於在 `.bazelrc` 檔案中指定了 `--crosstool_top=//toolchain:clang_suite`，因此 Bazel 會擲回以下錯誤:

```sh
No such package 'toolchain': BUILD file not found in any of the following directories
```

所以在工作區目錄中，為套件建立 `toolchain` 目錄，並在 `toolchain` 目錄中建立空白的 `BUILD` 檔案。

### 2. Run the build again

由於 toolchain 套件尚未定義 clang_suite 目標，Bazel 會擲回下列錯誤:

```sh
No such target '//toolchain:clang_suite': target 'clang_suite' not declared
in package 'toolchain' defined by .../toolchain/BUILD
```

此時在 `toolchain/BUILD` 檔案中，定義一個空白檔案群組，如下所示：

```starlark
package(default_visibility = ["//visibility:public"])

filegroup(name = "clang_suite")
```

### 3. Run the build again

Bazel 會擲回下列錯誤：

```sh
'//toolchain:clang_suite' does not have mandatory providers: 'CcToolchainInfo'
```

Bazel 發現 `--crosstool_top` 標記指向未提供必要 [ToolchainInfo](https://bazel.build/rules/lib/providers/ToolchainInfo?hl=zh-tw) 提供者的規則。因此，必須將 `--crosstool_top` 指向提供 `ToolchainInfo` 的規則，也就是 `cc_toolchain_suite` 規則。在 `toolchain/BUILD` 檔案中，將空檔案群組替換為下列內容：

```starlark
cc_toolchain_suite(
    name = "clang_suite",
    toolchains = {
        "k8": ":k8_toolchain",
    },
)
```

`toolchains` 屬性會自動將 `--cpu` (and also `--compiler` when specified) 的值對應至 `cc_toolchain`。You have not yet defined any `cc_toolchain` targets and Bazel will complain about that shortly.

### 4. Run the build again

Bazel 會擲回下列錯誤：

```sh
Rule '//toolchain:k8_toolchain' does not exist
```

現在需要為 `cc_toolchain_suite.toolchains` 屬性中的每個值定義 `cc_toolchain` 目標。將以下內容新增到 `toolchain/BUILD` 檔案中：

```starlark
filegroup(name = "empty")

cc_toolchain(
    name = "k8_toolchain",
    toolchain_identifier = "k8-toolchain",
    toolchain_config = ":k8_toolchain_config",
    all_files = ":empty",
    compiler_files = ":empty",
    dwp_files = ":empty",
    linker_files = ":empty",
    objcopy_files = ":empty",
    strip_files = ":empty",
    supports_param_files = 0,
)
```

### 5. Run the build again

Bazel 會擲回下列錯誤：

```sh
Rule '//toolchain:k8_toolchain_config' does not exist
```

接著，在 `toolchain/BUILD` 檔案中新增 `:k8_toolchain_config` 目標：

```starlark
filegroup(name = "k8_toolchain_config")
```

### 6. Run the build again

Bazel 會擲回下列錯誤：

```sh
'//toolchain:k8_toolchain_config' does not have mandatory providers: 'CcToolchainConfigInfo'
```

`CcToolchainConfigInfo` 是用於設定 C++ toolchain 的 provider。如要修正這個錯誤，create a Starlark rule that provides `CcToolchainConfigInfo` to Bazel by making a `toolchain/cc_toolchain_config.bzl` file with the following content:

```starlark
def _impl(ctx):
    return cc_common.create_cc_toolchain_config_info(
        ctx = ctx,
        toolchain_identifier = "k8-toolchain",
        host_system_name = "local",
        target_system_name = "local",
        target_cpu = "k8",
        target_libc = "unknown",
        compiler = "clang",
        abi_version = "unknown",
        abi_libc_version = "unknown",
    )

cc_toolchain_config = rule(
    implementation = _impl,
    attrs = {},
    provides = [CcToolchainConfigInfo],
)
```

`cc_common.create_cc_toolchain_config_info()` 會建立所需的 provider `CcToolchainConfigInfo`。如要使用 `cc_toolchain_config` 規則，請在套件陳述式正下方的 `toolchain/BUILD` 中新增載入陳述式(load statement)：

```starlark
load(":cc_toolchain_config.bzl", "cc_toolchain_config")
```

並將 `k8_toolchain_config` filegroup 替換為 `cc_toolchain_config` 規則的宣告：

```starlark
cc_toolchain_config(name = "k8_toolchain_config")
```

### 7. Run the build again

Bazel 會擲回下列錯誤：

```sh
.../BUILD:3:10: Compiling main/main.cc failed: (Exit 1)
src/main/tools/process-wrapper-legacy.cc:80:
"execvp(toolchain/DUMMY_GCC_TOOL, ...)": No such file or directory
Target //main:read-image failed to build
```

此時，Bazel 已有足夠的資訊嘗試建構程式碼，但仍不知道要使用哪些工具來完成必要的建構動作。您必須修改 Starlark 規則的實作，告訴 Bazel 使用哪些工具。為此，您需要 [@bazel_tools//tools/cpp:cc_toolchain_config_lib.bzl](https://cs.opensource.google/bazel/bazel/+/4eea5c62a566d21832c93e4c18ec559e75d5c1ce:tools/cpp/cc_toolchain_config_lib.bzl;l=400) 中的 tool_path() 建構函式：

```starlark
# toolchain/cc_toolchain_config.bzl:
# NEW
load("@bazel_tools//tools/cpp:cc_toolchain_config_lib.bzl", "tool_path")

def _impl(ctx):
    tool_paths = [ # NEW
        tool_path(
            name = "gcc",
            path = "/usr/bin/clang",
        ),
        tool_path(
            name = "ld",
            path = "/usr/bin/ld",
        ),
        tool_path(
            name = "ar",
            path = "/usr/bin/ar",
        ),
        tool_path(
            name = "cpp",
            path = "/bin/false",
        ),
        tool_path(
            name = "gcov",
            path = "/bin/false",
        ),
        tool_path(
            name = "nm",
            path = "/bin/false",
        ),
        tool_path(
            name = "objdump",
            path = "/bin/false",
        ),
        tool_path(
            name = "strip",
            path = "/bin/false",
        ),
    ]
    return cc_common.create_cc_toolchain_config_info(
        ctx = ctx,
        toolchain_identifier = "local",
        host_system_name = "local",
        target_system_name = "local",
        target_cpu = "k8",
        target_libc = "unknown",
        compiler = "clang",
        abi_version = "unknown",
        abi_libc_version = "unknown",
        tool_paths = tool_paths, # NEW
    )
```

請確認 `/usr/bin/clang` 和 `/usr/bin/ld` 是系統的正確路徑。

### 8. Run the build again

Bazel 會擲回下列錯誤：

```sh
.../BUILD:3:10: Compiling main/main.cc failed: undeclared inclusion(s) in rule '//main:read-image':
this rule is missing dependency declarations for the following files included by 'main/main.cc':
'/usr/include/c++/v1/fstream'
'/usr/include/c++/v1/stddef.h'
....
```

Bazel 需要知道要在何處搜尋包含的標頭。有 請注意，如果您使用的是其他版本的 clang，包含路徑會有所不同。這些路徑也可能因發布方式而異。

修改 `toolchain/cc_toolchain_config.bzl` 中的傳回值，如下所示：

```starlark
return cc_common.create_cc_toolchain_config_info(
    ctx = ctx,
    cxx_builtin_include_directories = [ # NEW
        "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include",
        "/Library/Developer/CommandLineTools/usr/lib/clang/14.0.3/include"
    ],
    toolchain_identifier = "local",
    host_system_name = "local",
    target_system_name = "local",
    target_cpu = "k8",
    target_libc = "unknown",
    compiler = "clang",
    abi_version = "unknown",
    abi_libc_version = "unknown",
    tool_paths = tool_paths,
)
```

### 9. Run the build again

Bazel 會擲回下列錯誤：

```sh
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
Target //main:read-image failed to build
```

這是因為連結器缺少 C++ 標準程式庫，所以找不到其符號。有許多方法可以解決這個問題，例如使用 `cc_binary` 的 `linkopts` 屬性。為解決這個問題，請確保使用工具鍊的所有目標都不需要指定這個標記。

將下列程式碼複製到 `cc_toolchain_config.bzl`：

```starlark
# toolchain/cc_toolchain_config.bzl:

# NEW
load("@bazel_tools//tools/build_defs/cc:action_names.bzl", "ACTION_NAMES")
# NEW
load(
    "@bazel_tools//tools/cpp:cc_toolchain_config_lib.bzl",
    "feature",
    "flag_group",
    "flag_set",
    "tool_path"
)

all_link_actions = [ # NEW
    ACTION_NAMES.cpp_link_executable,
    ACTION_NAMES.cpp_link_dynamic_library,
    ACTION_NAMES.cpp_link_nodeps_dynamic_library,
]


def _impl(ctx):
    tool_paths = [
        tool_path(
            name = "gcc",
            path = "/usr/bin/clang",
        ),
        tool_path(
            name = "ld",
            path = "/usr/bin/ld",
        ),
        tool_path(
            name = "ar",
            path = "/usr/bin/ar",
        ),
        tool_path(
            name = "cpp",
            path = "/bin/false",
        ),
        tool_path(
            name = "gcov",
            path = "/bin/false",
        ),
        tool_path(
            name = "nm",
            path = "/bin/false",
        ),
        tool_path(
            name = "objdump",
            path = "/bin/false",
        ),
        tool_path(
            name = "strip",
            path = "/bin/false",
        ),
    ]

    features = [ # NEW
        feature(
            name = "default_linker_flags",
            enabled = True,
            flag_sets = [
                flag_set(
                    actions = all_link_actions,
                    flag_groups = ([
                        flag_group(
                            flags = [
                                "-lstdc++",
                            ],
                        ),
                    ]),
                ),
            ],
        ),
    ]

    return cc_common.create_cc_toolchain_config_info(
        ctx = ctx,
        features = features, # NEW
        cxx_builtin_include_directories = [
            "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include",
            "/Library/Developer/CommandLineTools/usr/lib/clang/14.0.3/include"
        ],
        toolchain_identifier = "local",
        host_system_name = "local",
        target_system_name = "local",
        target_cpu = "k8",
        target_libc = "unknown",
        compiler = "clang",
        abi_version = "unknown",
        abi_libc_version = "unknown",
        tool_paths = tool_paths,
    )

cc_toolchain_config = rule(
    implementation = _impl,
    attrs = {},
    provides = [CcToolchainConfigInfo],
)
```

### 10.  Run the build again

```bash
$ bazel build --config=clang_config //main:read-image
```

成功，如下:

```sh
INFO: Build completed successfully, 5 total actions
```

### Running the binary

```bash
$ ./bazel-bin/main/read-image
```

然後你會發現生出一張檔名為 `dog_out.jpg` 的圖片。
