# Description:
#   Contains the TF-Keras Utilities (internal TensorFlow version).

load("@org_keras//tf_keras:tf_keras.bzl", "tf_py_test")
# Placeholder: load unaliased py_library

package(
    # copybara:uncomment default_applicable_licenses = ["//tf_keras:license"],
    # TODO(scottzhu): Remove non-keras deps from TF.
    default_visibility = ["//tf_keras:friends"],
    licenses = ["notice"],
)

py_library(
    name = "utils",
    srcs = [
        "__init__.py",
        "legacy/__init__.py",
    ],
    deps = [
        ":audio_dataset",
        ":data_utils",
        ":feature_space",
        ":generic_utils",
        ":image_dataset",
        ":image_utils",
        ":layer_utils",
        ":np_utils",
        ":sidecar_evaluator",
        ":steps_per_execution_tuning",
        ":text_dataset",
        ":timed_threads",
        ":timeseries_dataset",
        ":vis_utils",
    ],
)

py_library(
    name = "control_flow_util",
    srcs = ["control_flow_util.py"],
    deps = [],
)

py_library(
    name = "kpl_test_utils",
    srcs = ["kpl_test_utils.py"],
    deps = [
        "//tf_keras",
        "//tf_keras/layers/preprocessing:string_lookup",
    ],
)

py_library(
    name = "data_utils",
    srcs = ["data_utils.py"],
    deps = [
        ":generic_utils",
        ":io_utils",
        ":tf_inspect",
    ],
)

py_library(
    name = "engine_utils",
    srcs = [
        "conv_utils.py",
        "losses_utils.py",
    ],
    deps = [
        ":data_utils",
        ":io_utils",
        ":tf_utils",
        "//tf_keras:backend",
    ],
)

py_library(
    name = "io_utils",
    srcs = ["io_utils.py"],
    deps = [
        ":keras_logging",
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "keras_logging",
    srcs = ["keras_logging.py"],
)

py_library(
    name = "tf_utils",
    srcs = ["tf_utils.py"],
    deps = [
        ":object_identity",
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "traceback_utils",
    srcs = ["traceback_utils.py"],
    deps = [
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "generic_utils",
    srcs = [
        "generic_utils.py",
    ],
    deps = [
        ":io_utils",
        ":tf_contextlib",
        ":tf_inspect",
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "mode_keys",
    srcs = [
        "mode_keys.py",
    ],
    deps = [
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "layer_utils",
    srcs = [
        "kernelized_utils.py",
        "layer_utils.py",
    ],
    deps = [
        ":engine_utils",
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras:backend",
    ],
)

py_library(
    name = "metrics_utils",
    srcs = [
        "metrics_utils.py",
    ],
    deps = [
        ":generic_utils",
        ":tf_utils",
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "version_utils",
    srcs = [
        "version_utils.py",
    ],
    deps = [
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "np_utils",
    srcs = [
        "np_utils.py",
    ],
    deps = [
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "object_identity",
    srcs = ["object_identity.py"],
    deps = [],
)

py_library(
    name = "tf_contextlib",
    srcs = ["tf_contextlib.py"],
    deps = [
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "tf_inspect",
    srcs = ["tf_inspect.py"],
    deps = [
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "vis_utils",
    srcs = [
        "vis_utils.py",
    ],
    deps = [
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "image_utils",
    srcs = [
        "image_utils.py",
    ],
    deps = [
        "//:expect_pillow_installed",
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "dataset_creator",
    srcs = [
        "dataset_creator.py",
    ],
    deps = [
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "image_dataset",
    srcs = [
        "dataset_utils.py",
        "image_dataset.py",
    ],
    deps = [
        ":image_utils",
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras/layers/preprocessing:image_preprocessing",
    ],
)

py_library(
    name = "text_dataset",
    srcs = [
        "dataset_utils.py",
        "text_dataset.py",
    ],
    deps = [
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "timeseries_dataset",
    srcs = [
        "timeseries_dataset.py",
    ],
    deps = [
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "audio_dataset",
    srcs = [
        "audio_dataset.py",
    ],
    deps = [
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "sidecar_evaluator",
    srcs = ["sidecar_evaluator.py"],
    deps = [
        "//:expect_tensorboard_installed",
        "//:expect_tensorflow_installed",
    ],
)

py_library(
    name = "feature_space",
    srcs = ["feature_space.py"],
    deps = [
        "//:expect_tensorflow_installed",
        "//tf_keras:backend",
        "//tf_keras/layers",
    ],
)

py_library(
    name = "timed_threads",
    srcs = ["timed_threads.py"],
)

py_library(
    name = "steps_per_execution_tuning",
    srcs = ["steps_per_execution_tuning.py"],
    deps = [
        "//:expect_numpy_installed",
    ],
)

tf_py_test(
    name = "steps_per_execution_tuning_test",
    srcs = ["steps_per_execution_tuning_test.py"],
    deps = [
        ":steps_per_execution_tuning",
        "//:expect_tensorflow_installed",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "sidecar_evaluator_test",
    size = "medium",
    srcs = ["sidecar_evaluator_test.py"],
    deps = [
        ":sidecar_evaluator",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
    ],
)

tf_py_test(
    name = "dataset_creator_test",
    srcs = ["dataset_creator_test.py"],
    deps = [
        ":dataset_creator",
        "//:expect_portpicker_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras/distribute:multi_worker_testing_utils",
        "//tf_keras/engine",
        "//tf_keras/layers/core",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "dataset_utils_test",
    size = "medium",
    timeout = "moderate",
    srcs = ["dataset_utils_test.py"],
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
    ],
)

tf_py_test(
    name = "data_utils_test",
    size = "medium",
    srcs = ["data_utils_test.py"],
    shard_count = 6,
    tags = [
        "noasan",  # times out
        "notsan",
        "optonly",  # times out
    ],
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
    ],
)

tf_py_test(
    name = "generic_utils_test",
    size = "small",
    srcs = ["generic_utils_test.py"],
    deps = [
        ":generic_utils",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_tensorflow_installed",
        "//tf_keras",
    ],
)

tf_py_test(
    name = "version_utils_test",
    size = "small",
    srcs = ["version_utils_test.py"],
    deps = [
        ":version_utils",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "tf_utils_test",
    size = "small",
    srcs = ["tf_utils_test.py"],
    deps = [
        ":tf_utils",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "composite_tensor_support_test",
    size = "medium",
    srcs = ["composite_tensor_support_test.py"],
    shard_count = 8,
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras:engine",
        "//tf_keras/layers",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "io_utils_test",
    size = "small",
    srcs = ["io_utils_test.py"],
    tags = [
        "no_windows",  # TODO: needs investigation on Windows
        "notsan",
    ],
    deps = [
        ":io_utils",
        ":keras_logging",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "layer_utils_test",
    size = "small",
    srcs = ["layer_utils_test.py"],
    deps = [
        ":layer_utils",
        ":tf_utils",
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras:backend",
        "//tf_keras/dtensor",
        "//tf_keras/dtensor:layout_map",
        "//tf_keras/dtensor:test_util",
    ],
)

tf_py_test(
    name = "np_utils_test",
    size = "small",
    srcs = ["np_utils_test.py"],
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "kernelized_utils_test",
    size = "small",
    srcs = ["kernelized_utils_test.py"],
    deps = [
        ":layer_utils",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_tensorflow_installed",
    ],
)

tf_py_test(
    name = "vis_utils_test",
    size = "small",
    srcs = ["vis_utils_test.py"],
    shard_count = 4,
    tags = [
        "no_oss",  # TODO(b/318174391)
    ],
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
    ],
)

tf_py_test(
    name = "image_utils_test",
    size = "small",
    srcs = ["image_utils_test.py"],
    shard_count = 4,
    tags = [
        "no_pip",
    ],
    deps = [
        ":image_utils",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "conv_utils_test",
    size = "small",
    srcs = ["conv_utils_test.py"],
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
    ],
)

tf_py_test(
    name = "metrics_utils_test",
    size = "small",
    srcs = ["metrics_utils_test.py"],
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "losses_utils_test",
    size = "small",
    srcs = ["losses_utils_test.py"],
    deps = [
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "traceback_utils_test",
    size = "small",
    srcs = ["traceback_utils_test.py"],
    deps = [
        "//:expect_tensorflow_installed",
        "//tf_keras",
    ],
)

tf_py_test(
    name = "image_dataset_test",
    size = "small",
    srcs = ["image_dataset_test.py"],
    deps = [
        ":image_dataset",
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "text_dataset_test",
    size = "small",
    srcs = ["text_dataset_test.py"],
    deps = [
        ":text_dataset",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "timeseries_dataset_test",
    size = "small",
    srcs = ["timeseries_dataset_test.py"],
    deps = [
        ":timeseries_dataset",
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
    ],
)

tf_py_test(
    name = "audio_dataset_test",
    size = "small",
    srcs = ["audio_dataset_test.py"],
    deps = [
        ":audio_dataset",
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
    ],
)

tf_py_test(
    name = "audio_dataset_with_tfio_test",
    size = "small",
    srcs = ["audio_dataset_with_tfio_test.py"],
    deps = [
        ":audio_dataset",
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//:expect_tensorflow_io_installed",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
    ],
)

tf_py_test(
    name = "feature_space_test",
    size = "medium",
    srcs = ["feature_space_test.py"],
    deps = [
        ":feature_space",
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
    ],
)

tf_py_test(
    name = "timed_threads_test",
    size = "small",
    timeout = "moderate",
    srcs = ["timed_threads_test.py"],
    deps = [
        ":timed_threads",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
    ],
)
