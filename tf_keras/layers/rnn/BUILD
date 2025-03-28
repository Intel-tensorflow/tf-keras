# Description:
#  Contains the TF-Keras recurrent layers.

load("@org_keras//tf_keras:tf_keras.bzl", "cuda_py_test")  # buildifier: disable=same-origin-load
load("@org_keras//tf_keras:tf_keras.bzl", "tf_py_test")  # buildifier: disable=same-origin-load
# Placeholder: load unaliased py_library

package(
    # copybara:uncomment default_applicable_licenses = ["//tf_keras:license"],
    default_visibility = [
        "//tf_keras:friends",
        "//third_party/tensorflow_models/official/projects/residual_mobilenet/modeling/backbones:__pkg__",
    ],
    licenses = ["notice"],
)

py_library(
    name = "rnn",
    srcs = ["__init__.py"],
    deps = [
        ":abstract_rnn_cell",
        ":base_rnn",
        ":base_wrapper",
        ":bidirectional",
        ":cell_wrappers",
        ":conv_lstm1d",
        ":conv_lstm2d",
        ":conv_lstm3d",
        ":cudnn_gru",
        ":cudnn_lstm",
        ":gru",
        ":gru_v1",
        ":lstm",
        ":lstm_v1",
        ":simple_rnn",
        ":stacked_rnn_cells",
        ":time_distributed",
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "rnn_utils",
    srcs = ["rnn_utils.py"],
    deps = [
        "//:expect_tensorflow_installed",
        "//tf_keras/utils:control_flow_util",
    ],
)

py_library(
    name = "abstract_rnn_cell",
    srcs = ["abstract_rnn_cell.py"],
    deps = [
        ":rnn_utils",
        "//tf_keras/engine:base_layer",
    ],
)

py_library(
    name = "dropout_rnn_cell_mixin",
    srcs = ["dropout_rnn_cell_mixin.py"],
    deps = [
        "//:expect_tensorflow_installed",
        "//tf_keras:backend",
    ],
)

py_library(
    name = "gru_lstm_utils",
    srcs = ["gru_lstm_utils.py"],
    deps = [
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "gru",
    srcs = ["gru.py"],
    deps = [
        ":base_rnn",
        ":dropout_rnn_cell_mixin",
        ":gru_lstm_utils",
        ":rnn_utils",
        "//:expect_tensorflow_installed",
        "//tf_keras:activations",
        "//tf_keras:backend",
        "//tf_keras:constraints",
        "//tf_keras:regularizers",
        "//tf_keras/engine:base_layer",
        "//tf_keras/engine:input_spec",
        "//tf_keras/initializers",
        "//tf_keras/utils:tf_utils",
    ],
)

py_library(
    name = "gru_v1",
    srcs = ["gru_v1.py"],
    deps = [
        ":base_rnn",
        ":gru",
        ":rnn_utils",
        "//tf_keras:activations",
        "//tf_keras:constraints",
        "//tf_keras:regularizers",
        "//tf_keras/engine:input_spec",
        "//tf_keras/initializers",
    ],
)

py_library(
    name = "lstm",
    srcs = ["lstm.py"],
    deps = [
        ":base_rnn",
        ":dropout_rnn_cell_mixin",
        ":gru_lstm_utils",
        ":rnn_utils",
        "//:expect_tensorflow_installed",
        "//tf_keras:activations",
        "//tf_keras:backend",
        "//tf_keras:constraints",
        "//tf_keras:regularizers",
        "//tf_keras/engine:base_layer",
        "//tf_keras/engine:input_spec",
        "//tf_keras/initializers",
        "//tf_keras/utils:tf_utils",
    ],
)

py_library(
    name = "lstm_v1",
    srcs = ["lstm_v1.py"],
    deps = [
        ":base_rnn",
        ":lstm",
        ":rnn_utils",
        "//tf_keras:activations",
        "//tf_keras:constraints",
        "//tf_keras:regularizers",
        "//tf_keras/engine:input_spec",
        "//tf_keras/initializers",
    ],
)

py_library(
    name = "stacked_rnn_cells",
    srcs = ["stacked_rnn_cells.py"],
    deps = [
        ":rnn_utils",
        "//:expect_tensorflow_installed",
        "//tf_keras:backend",
        "//tf_keras/engine:base_layer",
        "//tf_keras/utils:generic_utils",
        "//tf_keras/utils:tf_utils",
    ],
)

py_library(
    name = "base_rnn",
    srcs = ["base_rnn.py"],
    deps = [
        ":dropout_rnn_cell_mixin",
        ":rnn_utils",
        ":stacked_rnn_cells",
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras:backend",
        "//tf_keras/engine:base_layer",
        "//tf_keras/engine:input_spec",
        "//tf_keras/saving/legacy/saved_model",
        "//tf_keras/utils:generic_utils",
    ],
)

py_library(
    name = "simple_rnn",
    srcs = ["simple_rnn.py"],
    deps = [
        ":base_rnn",
        ":dropout_rnn_cell_mixin",
        ":rnn_utils",
        "//:expect_tensorflow_installed",
        "//tf_keras:activations",
        "//tf_keras:backend",
        "//tf_keras:constraints",
        "//tf_keras:regularizers",
        "//tf_keras/engine:base_layer",
        "//tf_keras/engine:input_spec",
        "//tf_keras/initializers",
        "//tf_keras/utils:tf_utils",
    ],
)

py_library(
    name = "base_conv_rnn",
    srcs = ["base_conv_rnn.py"],
    deps = [
        ":base_rnn",
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras:backend",
        "//tf_keras:base_layer",
        "//tf_keras/engine:input_spec",
        "//tf_keras/utils:engine_utils",
        "//tf_keras/utils:generic_utils",
        "//tf_keras/utils:tf_utils",
    ],
)

py_library(
    name = "base_conv_lstm",
    srcs = ["base_conv_lstm.py"],
    deps = [
        ":base_conv_rnn",
        ":dropout_rnn_cell_mixin",
        "//:expect_tensorflow_installed",
        "//tf_keras:activations",
        "//tf_keras:backend",
        "//tf_keras:base_layer",
        "//tf_keras:constraints",
        "//tf_keras:regularizers",
        "//tf_keras/initializers",
        "//tf_keras/utils:engine_utils",
    ],
)

py_library(
    name = "conv_lstm1d",
    srcs = ["conv_lstm1d.py"],
    deps = [
        ":base_conv_lstm",
    ],
)

py_library(
    name = "conv_lstm2d",
    srcs = ["conv_lstm2d.py"],
    deps = [
        ":base_conv_lstm",
    ],
)

py_library(
    name = "conv_lstm3d",
    srcs = ["conv_lstm3d.py"],
    deps = [
        ":base_conv_lstm",
    ],
)

py_library(
    name = "base_cudnn_rnn",
    srcs = ["base_cudnn_rnn.py"],
    deps = [
        ":base_rnn",
        "//:expect_tensorflow_installed",
        "//tf_keras:backend",
        "//tf_keras/engine:input_spec",
    ],
)

py_library(
    name = "cudnn_lstm",
    srcs = ["cudnn_lstm.py"],
    deps = [
        ":base_cudnn_rnn",
        ":gru_lstm_utils",
        "//:expect_tensorflow_installed",
        "//tf_keras:constraints",
        "//tf_keras:regularizers",
        "//tf_keras/initializers",
    ],
)

py_library(
    name = "cudnn_gru",
    srcs = ["cudnn_gru.py"],
    deps = [
        ":base_cudnn_rnn",
        ":gru_lstm_utils",
        "//:expect_tensorflow_installed",
        "//tf_keras:constraints",
        "//tf_keras:regularizers",
        "//tf_keras/initializers",
    ],
)

py_library(
    name = "cell_wrappers",
    srcs = ["cell_wrappers.py"],
    deps = [
        ":abstract_rnn_cell",
        ":lstm",
        "//:expect_tensorflow_installed",
        "//tf_keras/utils:generic_utils",
        "//tf_keras/utils:tf_inspect",
    ],
)

py_library(
    name = "legacy_cell_wrappers",
    srcs = ["legacy_cell_wrappers.py"],
    deps = [
        ":cell_wrappers",
        ":legacy_cells",
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "legacy_cells",
    srcs = ["legacy_cells.py"],
    deps = [
        "//:expect_tensorflow_installed",
        "//tf_keras:activations",
        "//tf_keras:backend",
        "//tf_keras/engine:base_layer_utils",
        "//tf_keras/engine:input_spec",
        "//tf_keras/initializers",
        "//tf_keras/legacy_tf_layers:layers_base",
        "//tf_keras/utils:tf_utils",
    ],
)

py_library(
    name = "base_wrapper",
    srcs = ["base_wrapper.py"],
    deps = [
        "//tf_keras/engine:base_layer",
        "//tf_keras/utils:generic_utils",
    ],
)

py_library(
    name = "bidirectional",
    srcs = ["bidirectional.py"],
    deps = [
        ":base_wrapper",
        ":rnn_utils",
        "//:expect_tensorflow_installed",
        "//tf_keras:backend",
        "//tf_keras/engine:base_layer",
        "//tf_keras/engine:input_spec",
        "//tf_keras/utils:generic_utils",
        "//tf_keras/utils:tf_inspect",
        "//tf_keras/utils:tf_utils",
    ],
)

py_library(
    name = "time_distributed",
    srcs = ["time_distributed.py"],
    deps = [
        ":base_wrapper",
        "//:expect_tensorflow_installed",
        "//tf_keras:backend",
        "//tf_keras/engine:base_layer",
        "//tf_keras/engine:input_spec",
        "//tf_keras/utils:generic_utils",
        "//tf_keras/utils:layer_utils",
        "//tf_keras/utils:tf_utils",
    ],
)

cuda_py_test(
    name = "gru_lstm_test",
    size = "medium",
    srcs = ["gru_lstm_test.py"],
    shard_count = 2,
    tags = [
        "no_oss",  # TODO(b/277925387)
    ],
    deps = [
        ":gru",
        ":lstm",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
    ],
)

cuda_py_test(
    name = "gru_test",
    size = "medium",
    srcs = ["gru_test.py"],
    shard_count = 12,
    tags = [
        "no_oss",  # TODO(b/277925387)
    ],
    deps = [
        ":gru_lstm_utils",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
        "//tf_keras/utils:np_utils",
    ],
)

tf_py_test(
    name = "gru_v1_test",
    size = "medium",
    srcs = ["gru_v1_test.py"],
    shard_count = 4,
    tags = [
        "notsan",  # http://b/62136390
    ],
    deps = [
        ":gru",
        ":gru_v1",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
        "//tf_keras/utils:np_utils",
    ],
)

cuda_py_test(
    name = "lstm_test",
    size = "medium",
    srcs = ["lstm_test.py"],
    shard_count = 12,
    tags = [
        "no_oss",
        "notsan",  # TODO(b/170954246)
    ],
    deps = [
        ":gru_lstm_utils",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
        "//tf_keras/utils:np_utils",
    ],
)

tf_py_test(
    name = "lstm_v1_test",
    size = "medium",
    srcs = ["lstm_v1_test.py"],
    shard_count = 4,
    tags = [
        "noasan",  # times out b/63678675
        "notsan",  # http://b/62189182
    ],
    deps = [
        ":lstm",
        ":lstm_v1",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
        "//tf_keras/utils:np_utils",
    ],
)

tf_py_test(
    name = "base_rnn_test",
    size = "medium",
    srcs = ["base_rnn_test.py"],
    shard_count = 12,
    tags = [
        "notsan",  # TODO(b/170870794)
    ],
    deps = [
        ":gru",
        ":gru_v1",
        ":legacy_cells",
        ":lstm",
        ":lstm_v1",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/engine:base_layer_utils",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
        "//tf_keras/utils:generic_utils",
    ],
)

tf_py_test(
    name = "simple_rnn_test",
    size = "medium",
    srcs = ["simple_rnn_test.py"],
    shard_count = 4,
    tags = ["notsan"],
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
    ],
)

tf_py_test(
    name = "conv_lstm_test",
    size = "medium",
    srcs = ["conv_lstm_test.py"],
    shard_count = 8,
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
    ],
)

cuda_py_test(
    name = "cudnn_test",
    size = "medium",
    srcs = ["cudnn_test.py"],
    shard_count = 4,
    tags = [
        "no_oss",  # TODO(b/277925387)
        "no_windows_gpu",
    ],
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/optimizers/legacy:optimizers",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
    ],
)

tf_py_test(
    name = "cell_wrappers_test",
    size = "medium",
    srcs = ["cell_wrappers_test.py"],
    shard_count = 4,
    tags = [
        "notsan",
    ],
    deps = [
        ":cell_wrappers",
        ":legacy_cells",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras/layers",
        "//tf_keras/legacy_tf_layers:layers_base",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/utils:generic_utils",
    ],
)

tf_py_test(
    name = "legacy_cell_wrappers_test",
    size = "small",
    srcs = ["legacy_cell_wrappers_test.py"],
    shard_count = 4,
    deps = [
        ":legacy_cell_wrappers",
        ":legacy_cells",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_tensorflow_installed",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "base_wrapper_test",
    size = "small",
    srcs = ["base_wrapper_test.py"],
    shard_count = 4,
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_tensorflow_installed",
        "//tf_keras",
    ],
)

tf_py_test(
    name = "bidirectional_test",
    size = "medium",
    srcs = ["bidirectional_test.py"],
    shard_count = 12,
    tags = [
        "noasan",  # http://b/78599823
        "notsan",
    ],
    deps = [
        ":cell_wrappers",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/engine:base_layer_utils",
        "//tf_keras/layers/core",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
        "//tf_keras/utils:generic_utils",
    ],
)

tf_py_test(
    name = "time_distributed_test",
    size = "medium",
    srcs = ["time_distributed_test.py"],
    shard_count = 12,
    tags = [
        "noasan",  # http://b/78599823
        "notsan",
    ],
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
    ],
)
