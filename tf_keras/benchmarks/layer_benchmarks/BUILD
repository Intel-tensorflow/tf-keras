# Description:
#   Implementation of benchmarks on TF-Keras layers.

load("@org_keras//tf_keras:tf_keras.bzl", "tf_py_test")
# Placeholder: load unaliased py_library

package(
    # copybara:uncomment default_applicable_licenses = ["//tf_keras:license"],
    default_visibility = ["//visibility:public"],
    licenses = ["notice"],
)

BECHMARK_TAGS = [
    "no_oss_py38",  # TODO(b/162044699)
    "no_pip",  # TODO(b/161253163)
    "no_windows",  # TODO(b/160628318)
]

# To run CPU benchmarks:
#   bazel run -c opt benchmarks_test -- --benchmarks=.

# To run GPU benchmarks:
#   bazel run -c opt --config=cuda benchmarks_test -- \
#     --benchmarks=.

# To run benchmarks with TFRT:
#   bazel run -c opt --config=cuda --test_env=EXPERIMENTAL_ENABLE_TFRT=1 benchmarks_test -- \
#     --benchmarks=.

# To run a subset of benchmarks using --benchmarks flag.
# --benchmarks: the list of benchmarks to run. The specified value is interpreted
# as a regular expression and any benchmark whose name contains a partial match
# to the regular expression is executed.
# e.g. --benchmarks=".*lstm*." will run all lstm layer related benchmarks.

py_library(
    name = "run_xprof",
    srcs = ["run_xprof.py"],
    visibility = ["//visibility:private"],
)

py_library(
    name = "layer_benchmarks_test_base",
    srcs = ["layer_benchmarks_test_base.py"],
    visibility = ["//visibility:private"],
    deps = [
        ":run_xprof",
        "//:expect_tensorflow_installed",
        "//tf_keras/benchmarks:profiler_lib",
    ],
)

tf_py_test(
    name = "layer_benchmarks_test",
    srcs = ["layer_benchmarks_test.py"],
    tags = BECHMARK_TAGS,
    deps = [
        ":layer_benchmarks_test_base",
        "//:expect_tensorflow_installed",
        "//tf_keras/api:tf_keras_api",
        "//tf_keras/benchmarks:benchmark_util",
    ],
)
