# Description:
#  Contains the TF-Keras attention layers.

# Placeholder: load unaliased py_library
load("@org_keras//tf_keras:tf_keras.bzl", "tf_py_test")

package(
    # copybara:uncomment default_applicable_licenses = ["//tf_keras:license"],
    default_visibility = [
        "//tf_keras:friends",
        "//third_party/py/tensorflow_gnn:__subpackages__",
        "//third_party/tensorflow/python/distribute:__pkg__",
        "//third_party/tensorflow/python/feature_column:__pkg__",
        "//third_party/tensorflow/python/trackable:__pkg__",
        "//third_party/tensorflow/tools/pip_package:__pkg__",
        "//third_party/tensorflow_models/official/projects/residual_mobilenet/modeling/backbones:__pkg__",
    ],
    licenses = ["notice"],
)

py_library(
    name = "attention",
    srcs = [
        "__init__.py",
    ],
    deps = [
        ":additive_attention",
        ":attention_layer",
        ":multi_head_attention",
    ],
)

py_library(
    name = "multi_head_attention",
    srcs = ["multi_head_attention.py"],
    deps = [
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras:constraints",
        "//tf_keras:regularizers",
        "//tf_keras/engine:base_layer",
        "//tf_keras/initializers",
        "//tf_keras/layers/activation",
        "//tf_keras/layers/core",
        "//tf_keras/layers/regularization",
        "//tf_keras/utils:tf_utils",
    ],
)

py_library(
    name = "base_dense_attention",
    srcs = ["base_dense_attention.py"],
    deps = [
        "//:expect_tensorflow_installed",
        "//tf_keras:backend",
        "//tf_keras:base_layer",
        "//tf_keras/utils:control_flow_util",
    ],
)

py_library(
    name = "attention_layer",
    srcs = ["attention.py"],
    deps = [
        ":base_dense_attention",
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "additive_attention",
    srcs = ["additive_attention.py"],
    deps = [
        ":base_dense_attention",
        "//:expect_tensorflow_installed",
    ],
)

tf_py_test(
    name = "multi_head_attention_test",
    srcs = ["multi_head_attention_test.py"],
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "base_dense_attention_test",
    size = "medium",
    srcs = ["base_dense_attention_test.py"],
    deps = [
        ":base_dense_attention",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "attention_test",
    size = "medium",
    srcs = ["attention_test.py"],
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/layers/core",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "additive_attention_test",
    size = "medium",
    srcs = ["additive_attention_test.py"],
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/mixed_precision:policy",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
    ],
)
