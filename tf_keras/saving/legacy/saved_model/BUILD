# Copyright 2021 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

# Description:
#   TF-Keras saving and loading files for SavedModel.

# buildifier: disable=same-origin-load

# Placeholder: load unaliased py_binary
# Placeholder: load unaliased py_library
load("@org_keras//tf_keras:tf_keras.bzl", "tf_py_test")

package(
    # copybara:uncomment default_applicable_licenses = ["//tf_keras:license"],
    default_visibility = [
        "//tf_keras/layers/rnn:__pkg__",
        "//tf_keras/saving:__subpackages__",
    ],
    licenses = ["notice"],
)

py_library(
    name = "order_preserving_set",
    srcs = ["order_preserving_set.py"],
)

py_library(
    name = "utils",
    srcs = ["utils.py"],
    deps = [
        "//:expect_tensorflow_installed",
        "//tf_keras/engine:base_layer_utils",
        "//tf_keras/utils:layer_utils",
    ],
)

py_library(
    name = "saved_model",
    srcs = [
        "base_serialization.py",
        "constants.py",
        "json_utils.py",
        "layer_serialization.py",
        "load.py",
        "metric_serialization.py",
        "model_serialization.py",
        "network_serialization.py",
        "save.py",
        "save_impl.py",
        "serialized_attributes.py",
    ],
    deps = [
        ":order_preserving_set",
        ":utils",
        "//:expect_tensorflow_installed",
        "//tf_keras/utils:generic_utils",
    ],
)

tf_py_test(
    name = "revive_test",
    size = "medium",
    srcs = ["revive_test.py"],
    shard_count = 8,
    tags = [
        "no_windows",  # b/158005583
    ],
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

tf_py_test(
    name = "json_utils_test",
    size = "small",
    srcs = ["json_utils_test.py"],
    deps = [
        ":saved_model",
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras/testing_infra:test_combinations",
        "//tf_keras/testing_infra:test_utils",
    ],
)

tf_py_test(
    name = "saved_model_test",
    size = "medium",
    srcs = ["saved_model_test.py"],
    shard_count = 4,
    tags = [
        "no_oss",  # TODO(keras-team): Fails in OSS.
        "no_pip",  # TODO(b/202022379)
        "no_rocm",
        "no_windows",
        "notsan",  #TODO(b/181771982): it is flaky
    ],
    deps = [
        "//:expect_absl_installed",  # absl/testing:parameterized
        "//:expect_numpy_installed",
        "//:expect_tensorflow_installed",
        "//tf_keras",
        "//tf_keras/testing_infra:test_combinations",
    ],
)

py_binary(
    name = "create_test_saved_model",
    srcs = ["create_test_saved_model.py"],
    tags = ["no_oss"],
    deps = [
        "//:expect_absl_installed",  # absl:app
        "//:expect_tensorflow_installed",
        "//tf_keras:regularizers",
        "//tf_keras/testing_infra:test_utils",
        "//third_party/py/absl/flags",
    ],
)

tf_py_test(
    name = "determinism_test",
    srcs = ["determinism_test.py"],
    data = [":create_test_saved_model.par"],
    tags = ["no_oss"],
    deps = [
        "//:expect_tensorflow_installed",
    ],
)
