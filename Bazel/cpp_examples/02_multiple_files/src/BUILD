load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_library")

cc_library(
    name = "all-lib",
    srcs = glob(["*.cc"]),
    hdrs = glob(["*.h"]),
)

cc_binary(
    name = "hello-world",
    srcs = ["hello-world.cc"],
    deps = [
        ":all-lib",
    ],
)

