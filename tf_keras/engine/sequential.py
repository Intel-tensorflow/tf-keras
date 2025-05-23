# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
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

"""Home of the `Sequential` model."""

import copy

import tensorflow.compat.v2 as tf

from tf_keras import layers as layer_module
from tf_keras.engine import base_layer
from tf_keras.engine import functional
from tf_keras.engine import input_layer
from tf_keras.engine import training
from tf_keras.engine import training_utils
from tf_keras.saving import serialization_lib
from tf_keras.saving.legacy import serialization as legacy_serialization
from tf_keras.saving.legacy.saved_model import model_serialization
from tf_keras.utils import generic_utils
from tf_keras.utils import layer_utils
from tf_keras.utils import tf_inspect
from tf_keras.utils import tf_utils
from tf_keras.utils import traceback_utils

# isort: off
from tensorflow.python.util.tf_export import keras_export

SINGLE_LAYER_OUTPUT_ERROR_MSG = (
    "All layers in a Sequential model should have "
    "a single output tensor. For multi-output "
    "layers, use the functional API."
)


@keras_export("keras.Sequential", "keras.models.Sequential")
class Sequential(functional.Functional):
    """`Sequential` groups a linear stack of layers into a `tf.keras.Model`.

    `Sequential` provides training and inference features on this model.

    Examples:

    ```python
    model = tf.keras.Sequential()
    model.add(tf.keras.Input(shape=(16,)))
    model.add(tf.keras.layers.Dense(8))

    # Note that you can also omit the initial `Input`.
    # In that case the model doesn't have any weights until the first call
    # to a training/evaluation method (since it isn't yet built):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(8))
    model.add(tf.keras.layers.Dense(4))
    # model.weights not created yet

    # Whereas if you specify an `Input`, the model gets built
    # continuously as you are adding layers:
    model = tf.keras.Sequential()
    model.add(tf.keras.Input(shape=(16,)))
    model.add(tf.keras.layers.Dense(4))
    len(model.weights)
    # Returns "2"

    # When using the delayed-build pattern (no input shape specified), you can
    # choose to manually build your model by calling
    # `build(batch_input_shape)`:
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(8))
    model.add(tf.keras.layers.Dense(4))
    model.build((None, 16))
    len(model.weights)
    # Returns "4"

    # Note that when using the delayed-build pattern (no input shape specified),
    # the model gets built the first time you call `fit`, `eval`, or `predict`,
    # or the first time you call the model on some input data.
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(8))
    model.add(tf.keras.layers.Dense(1))
    model.compile(optimizer='sgd', loss='mse')
    # This builds the model for the first time:
    model.fit(x, y, batch_size=32, epochs=10)
    ```
    """

    @tf.__internal__.tracking.no_automatic_dependency_tracking
    @traceback_utils.filter_traceback
    def __init__(self, layers=None, name=None):
        """Creates a `Sequential` model instance.

        Args:
          layers: Optional list of layers to add to the model.
          name: Optional name for the model.
        """
        # Skip the init in FunctionalModel since model doesn't have input/output
        # yet
        super(functional.Functional, self).__init__(name=name, autocast=False)
        self.supports_masking = True
        self._compute_output_and_mask_jointly = True
        self._auto_track_sub_layers = False
        self._inferred_input_shape = None
        self._has_explicit_input_shape = False
        self._input_dtype = None
        self._layer_call_argspecs = {}
        self._created_nodes = set()
        # Flag that indicate whether the sequential network topology has been
        # created. It is false when there isn't any layer, or the layers don't
        # have an input shape.
        self._graph_initialized = False

        # Unfortunately some Sequential models using custom layers or
        # FeatureColumn layers have multiple inputs. This is fundamentally
        # incompatible with most of the Sequential API, and we have to disable a
        # number of features for such models.
        self._use_legacy_deferred_behavior = False

        # Add to the model any layers passed to the constructor.
        if layers:
            if not isinstance(layers, (list, tuple)):
                layers = [layers]
            for layer in layers:
                self.add(layer)

    @property
    def layers(self):
        # Historically, `sequential.layers` only returns layers that were added
        # via `add`, and omits the auto-generated `InputLayer` that comes at the
        # bottom of the stack.
        # `Trackable` manages the `_layers` attributes and does filtering
        # over it.
        layers = super().layers
        if layers and isinstance(layers[0], input_layer.InputLayer):
            return layers[1:]
        return layers[:]

    @tf.__internal__.tracking.no_automatic_dependency_tracking
    @traceback_utils.filter_traceback
    def add(self, layer):
        """Adds a layer instance on top of the layer stack.

        Args:
            layer: layer instance.

        Raises:
            TypeError: If `layer` is not a layer instance.
            ValueError: In case the `layer` argument does not
                know its input shape.
            ValueError: In case the `layer` argument has
                multiple output tensors, or is already connected
                somewhere else (forbidden in `Sequential` models).
        """
        # If we are passed a TF-Keras tensor created by keras.Input(), we can
        # extract the input layer from its keras history and use that without
        # any loss of
        # generality.
        if hasattr(layer, "_keras_history"):
            origin_layer = layer._keras_history[0]
            if isinstance(origin_layer, input_layer.InputLayer):
                layer = origin_layer

        if isinstance(layer, tf.Module):
            if not isinstance(layer, base_layer.Layer):
                layer = functional.ModuleWrapper(layer)
        else:
            raise TypeError(
                "The added layer must be an instance of class Layer. "
                f"Received: layer={layer} of type {type(layer)}."
            )

        tf_utils.assert_no_legacy_layers([layer])
        if not self._is_layer_name_unique(layer):
            raise ValueError(
                "All layers added to a Sequential model "
                f'should have unique names. Name "{layer.name}" is already '
                "the name of a layer in this model. Update the `name` argument "
                "to pass a unique name."
            )

        self.built = False
        set_inputs = False
        self._maybe_create_attribute("_self_tracked_trackables", [])
        if not self._self_tracked_trackables:
            if isinstance(layer, input_layer.InputLayer):
                # Case where the user passes an Input or InputLayer layer via
                # `add`.
                set_inputs = True
            else:
                batch_shape, dtype = training_utils.get_input_shape_and_dtype(
                    layer
                )
                if batch_shape:
                    # Instantiate an input layer.
                    x = input_layer.Input(
                        batch_shape=batch_shape,
                        dtype=dtype,
                        name=layer.name + "_input",
                    )
                    # This will build the current layer
                    # and create the node connecting the current layer
                    # to the input layer we just created.
                    layer(x)
                    set_inputs = True

            if set_inputs:
                outputs = tf.nest.flatten(layer._inbound_nodes[-1].outputs)
                if len(outputs) != 1:
                    raise ValueError(SINGLE_LAYER_OUTPUT_ERROR_MSG)
                self.outputs = outputs
                self.inputs = layer_utils.get_source_inputs(self.outputs[0])
                self.built = True
                self._has_explicit_input_shape = True

        elif self.outputs:
            # If the model is being built continuously on top of an input layer:
            # refresh its output.
            output_tensor = layer(self.outputs[0])
            if len(tf.nest.flatten(output_tensor)) != 1:
                raise ValueError(SINGLE_LAYER_OUTPUT_ERROR_MSG)
            self.outputs = [output_tensor]
            self.built = True

        if set_inputs or self._graph_initialized:
            self._init_graph_network(self.inputs, self.outputs)
            self._graph_initialized = True
        else:
            self._self_tracked_trackables.append(layer)
            self._handle_deferred_layer_dependencies([layer])

        self._layer_call_argspecs[layer] = tf_inspect.getfullargspec(layer.call)

    @tf.__internal__.tracking.no_automatic_dependency_tracking
    @traceback_utils.filter_traceback
    def pop(self):
        """Removes the last layer in the model.

        Raises:
            TypeError: if there are no layers in the model.
        """
        if not self.layers:
            raise TypeError("There are no layers in the model.")

        layer = self._self_tracked_trackables.pop()
        self._layer_call_argspecs.pop(layer)
        if not self.layers:
            self.outputs = None
            self.inputs = None
            self.built = False
            self._inferred_input_shape = None
            self._has_explicit_input_shape = False
            self._graph_initialized = False
        elif self._graph_initialized:
            self.layers[-1]._outbound_nodes = []
            self.outputs = [self.layers[-1].output]
            self._init_graph_network(self.inputs, self.outputs)
            self.built = True

    @tf.__internal__.tracking.no_automatic_dependency_tracking
    def _build_graph_network_for_inferred_shape(
        self, input_shape, input_dtype=None
    ):
        if input_shape is None or not self.layers:
            return
        if (
            not tf.__internal__.tf2.enabled()
            or not tf.compat.v1.executing_eagerly_outside_functions()
        ):
            # This behavior is disabled in V1 or when eager execution is
            # disabled.
            return
        if (
            not self._has_explicit_input_shape
            and not self._use_legacy_deferred_behavior
        ):
            # Determine whether the input shape is novel, i.e. whether the model
            # should be rebuilt.
            input_shape = tf_utils.convert_shapes(input_shape)
            if self._inferred_input_shape is None:
                new_shape = input_shape
            else:
                new_shape = tf.nest.map_structure(
                    _relax_input_shape,
                    tf_utils.convert_shapes(
                        self._inferred_input_shape, to_tuples=False
                    ),
                    tf_utils.convert_shapes(input_shape, to_tuples=False),
                )
            if (
                new_shape is not None
                and new_shape != self._inferred_input_shape
            ):
                # A novel shape has been received: we need to rebuild the model.
                # In case we are inside a graph function, we step out of it.
                with tf.init_scope():
                    inputs = tf.nest.map_structure(
                        lambda s: input_layer.Input(
                            batch_shape=tf_utils.convert_shapes(s),
                            dtype=input_dtype,
                            name=self.layers[0].name + "_input",
                        ),
                        tf_utils.convert_shapes(new_shape, to_tuples=False),
                    )
                    layer_input = inputs
                    created_nodes = set()
                    for layer in self.layers:
                        # Clear nodes previously created via this method. This
                        # prevents node accumulation and ensures that e.g.
                        # `layer.output` is always connected to `model.inputs`
                        # (this is important e.g. for the feature extraction use
                        # case).  We don't just do `layer._inbound_nodes = []`
                        # in order not to break shared layers added to
                        # Sequential models (which is technically illegal as per
                        # the `add()` docstring, but wasn't previously
                        # disabled).
                        clear_previously_created_nodes(
                            layer, self._created_nodes
                        )
                        try:
                            # Create Functional API connection by calling the
                            # current layer
                            layer_output = layer(layer_input)
                        except:  # noqa: E722
                            # Functional API calls may fail for a number of
                            # reasons: 1) The layer may be buggy. In this case
                            # it will be easier for the user to debug if we fail
                            # on the first call on concrete data, instead of our
                            # own call on a symbolic input. 2) The layer is
                            # dynamic (graph-incompatible) and hasn't overridden
                            # `compute_output_shape`. In this case, it is
                            # impossible to build a graph network. 3) The layer
                            # is otherwise incompatible with the Functional API
                            # (e.g. this is the case for some probabilistic
                            # layers that rely on hacks and that do not return
                            # tensors). In all these cases, we should avoid
                            # creating a graph network (or we simply can't).
                            self._use_legacy_deferred_behavior = True
                            return
                        if len(tf.nest.flatten(layer_output)) != 1:
                            raise ValueError(SINGLE_LAYER_OUTPUT_ERROR_MSG)
                        # Keep track of nodes just created above
                        track_nodes_created_by_last_call(layer, created_nodes)
                        layer_input = layer_output
                        outputs = layer_output
                    self._created_nodes = created_nodes
                    try:
                        # Initialize a graph Network. This call will never fail
                        # for stack of valid TF-Keras layers. However some users
                        # have layers that are fundamentally incompatible with
                        # the Functional API, which do not return tensors. In
                        # this case, we fall back to the legacy deferred
                        # behavior.
                        # TODO(fchollet): consider raising here, as we should
                        # not be supporting such layers.
                        self._init_graph_network(inputs, outputs)
                        self._graph_initialized = True
                    except:  # noqa: E722
                        self._use_legacy_deferred_behavior = True
                self._inferred_input_shape = new_shape

    @generic_utils.default
    def build(self, input_shape=None):
        if self._graph_initialized:
            self._init_graph_network(self.inputs, self.outputs)
        else:
            if input_shape is None:
                raise ValueError("You must provide an `input_shape` argument.")
            self._build_graph_network_for_inferred_shape(input_shape)
            if not self.built:
                input_shape = tf_utils.convert_shapes(input_shape)
                self._build_input_shape = input_shape
                super().build(input_shape)
        self.built = True

    def call(self, inputs, training=None, mask=None):
        # If applicable, update the static input shape of the model.
        if not self._has_explicit_input_shape:
            if not tf.is_tensor(inputs) and not isinstance(inputs, tf.Tensor):
                # This is a Sequential with multiple inputs. This is technically
                # an invalid use case of Sequential, but we tolerate it for
                # backwards compatibility.
                self._use_legacy_deferred_behavior = True
                self._build_input_shape = tf.nest.map_structure(
                    _get_shape_tuple, inputs
                )
            else:
                self._build_graph_network_for_inferred_shape(
                    inputs.shape, inputs.dtype
                )

        if self._graph_initialized:
            if not self.built:
                self._init_graph_network(self.inputs, self.outputs)
            return super().call(inputs, training=training, mask=mask)

        outputs = inputs  # handle the corner case where self.layers is empty
        for layer in self.layers:
            # During each iteration, `inputs` are the inputs to `layer`, and
            # `outputs` are the outputs of `layer` applied to `inputs`. At the
            # end of each iteration `inputs` is set to `outputs` to prepare for
            # the next layer.
            kwargs = {}
            argspec = self._layer_call_argspecs[layer].args
            if "mask" in argspec:
                kwargs["mask"] = mask
            if "training" in argspec:
                kwargs["training"] = training

            outputs = layer(inputs, **kwargs)

            inputs = outputs

            def _get_mask_from_keras_tensor(kt):
                return getattr(kt, "_keras_mask", None)

            mask = tf.nest.map_structure(_get_mask_from_keras_tensor, outputs)
        return outputs

    def compute_output_shape(self, input_shape):
        shape = input_shape
        for layer in self.layers:
            shape = layer.compute_output_shape(shape)
        return shape

    def compute_mask(self, inputs, mask):
        # TODO(omalleyt): b/123540974 This function is not really safe to call
        # by itself because it will duplicate any updates and losses in graph
        # mode by `call`ing the Layers again.
        outputs = self.call(inputs, mask=mask)
        return getattr(outputs, "_keras_mask", None)

    def get_config(self):
        layer_configs = []
        serialize_obj_fn = serialization_lib.serialize_keras_object
        use_legacy_config = getattr(self, "use_legacy_config", False)
        if use_legacy_config:
            serialize_obj_fn = legacy_serialization.serialize_keras_object
        for layer in super().layers:
            # `super().layers` include the InputLayer if available (it is
            # filtered out of `self.layers`). Note that
            # `self._self_tracked_trackables` is managed by the tracking
            # infrastructure and should not be used.
            layer_configs.append(serialize_obj_fn(layer))
        config = training.Model.get_config(self)
        config["name"] = self.name
        config["layers"] = copy.deepcopy(layer_configs)
        if (
            use_legacy_config
            and not self._is_graph_network
            and self._build_input_shape
        ):
            config["build_input_shape"] = self._build_input_shape
        return config

    @classmethod
    def from_config(cls, config, custom_objects=None):
        if "name" in config:
            name = config["name"]
            build_input_shape = config.get("build_input_shape")
            layer_configs = config["layers"]
        else:
            name = None
            build_input_shape = None
            layer_configs = config
        model = cls(name=name)
        for layer_config in layer_configs:
            use_legacy_format = "module" not in layer_config
            layer = layer_module.deserialize(
                layer_config,
                custom_objects=custom_objects,
                use_legacy_format=use_legacy_format,
            )
            model.add(layer)

        if (
            not model.inputs
            and build_input_shape
            and isinstance(build_input_shape, (tuple, list))
        ):
            model.build(build_input_shape)

        return model

    @property
    def input_spec(self):
        if hasattr(self, "_manual_input_spec"):
            return self._manual_input_spec
        if self._has_explicit_input_shape:
            return super().input_spec
        return None

    @input_spec.setter
    def input_spec(self, value):
        self._manual_input_spec = value

    @property
    def _trackable_saved_model_saver(self):
        return model_serialization.SequentialSavedModelSaver(self)

    def _is_layer_name_unique(self, layer):
        for ref_layer in self.layers:
            if layer.name == ref_layer.name and ref_layer is not layer:
                return False
        return True

    def _assert_weights_created(self):
        if self._graph_initialized:
            return
        # When the graph has not been initialized, use the Model's
        # implementation to to check if the weights has been created.
        super(functional.Functional, self)._assert_weights_created()


def _get_shape_tuple(t):
    if hasattr(t, "shape"):
        shape = t.shape
        if isinstance(shape, tuple):
            return shape
        if shape.rank is not None:
            return tuple(shape.as_list())
        return None
    return None


def _relax_input_shape(shape_1, shape_2):
    if shape_1 is None or shape_2 is None:
        return None
    if shape_1.rank is None or shape_2.rank is None:
        return None
    if shape_1.rank != shape_2.rank:
        return None
    shape_1 = shape_1.as_list()
    shape_2 = shape_2.as_list()
    return tuple(None if d1 != d2 else d1 for d1, d2 in zip(shape_1, shape_2))


def clear_previously_created_nodes(layer, created_nodes):
    """Remove nodes from `created_nodes` from the layer's inbound_nodes."""
    for node in layer._inbound_nodes:
        prev_layers = node.inbound_layers
        for prev_layer in tf.nest.flatten(prev_layers):
            prev_layer._outbound_nodes = [
                n for n in prev_layer._outbound_nodes if n not in created_nodes
            ]
    layer._inbound_nodes = [
        n for n in layer._inbound_nodes if n not in created_nodes
    ]


def track_nodes_created_by_last_call(layer, created_nodes):
    """Adds to `created_nodes` the nodes created by the last call to `layer`."""
    if not layer._inbound_nodes:
        return
    created_nodes.add(layer._inbound_nodes[-1])
    prev_layers = layer._inbound_nodes[-1].inbound_layers
    for prev_layer in tf.nest.flatten(prev_layers):
        if prev_layer._outbound_nodes:
            created_nodes.add(prev_layer._outbound_nodes[-1])
