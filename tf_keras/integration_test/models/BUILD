# Description:
#   Contains a collection of diverse TF-Keras models to be used for integration tests.

# Placeholder: load unaliased py_library

package(
    # copybara:uncomment default_applicable_licenses = ["//tf_keras:license"],
    default_visibility = [
        "//tf_keras:friends",
    ],
    licenses = ["notice"],
)

py_library(
    name = "models",
    srcs = [
        "__init__.py",
        "bert.py",
        "ctc_speech_rnn.py",
        "dcgan.py",
        "edge_case_model.py",
        "efficientnet_v2.py",
        "input_spec.py",
        "low_level_model.py",
        "mini_unet.py",
        "mini_xception.py",
        "retinanet.py",
        "structured_data_classification.py",
        "text_classification.py",
        "timeseries_forecasting.py",
        "translation.py",
        "vae.py",
    ],
    deps = ["//:expect_tensorflow_installed"],
)
