# Reset in Tensorflow
Tensorflow includes some of the models proposed in the [Residual Network paper](https://arxiv.org/abs/1512.03385) under [tf.keras.applications](https://www.tensorflow.org/api_docs/python/tf/keras/applications/ResNet101).

The Models included are:-
- [ResNet50](https://www.tensorflow.org/api_docs/python/tf/keras/applications/ResNet50)
- [ResNet101](https://www.tensorflow.org/api_docs/python/tf/keras/applications/ResNet101)
- [ResNet152](https://www.tensorflow.org/api_docs/python/tf/keras/applications/ResNet152)

There are also the 2nd version for each of them, proposed by another [paper](https://arxiv.org/abs/1603.05027) one year later in 2016, so we also have
- [ResNet50V2](https://www.tensorflow.org/api_docs/python/tf/keras/applications/ResNet50V2)
- [ResNet101V2](https://www.tensorflow.org/api_docs/python/tf/keras/applications/ResNet101V2)
- [ResNet152V2](https://www.tensorflow.org/api_docs/python/tf/keras/applications/ResNet152V2)

Each model can be instanciated by a function under `tf.keras.applications`. you can optionally choose to have the trained weights on imagenet dataset or not, also you can somewhat change in the network structure.

## Custtomization options
The functions presented here have few parameters to control the returned model instance.

```python
# all of them have the same signature
tf.keras.applications.ResNet50(
    include_top=True, weights='imagenet', input_tensor=None,
    input_shape=None, pooling=None, classes=1000, **kwargs
)
```


1. **include_top**: `Bool` used to control keeping the first input layer (`True:Default`) or not (`False`).
2. **weights**: it can either be:
    1. None: for random initialization.
    2. 'imagenet': `Default` for the weights trained on imagenet.
    3. path: path to file that includes the weights to be loaded.
3. **input_shape**: The shape of the `InputLayer` to be used, the `default` is (224, 224, 3).  
The shape must have exactly 3 Dimensions, with width and height no less than 32.
*NOTE: You can only specify a different size if `include_top=False`*
4. **input_tensor**: an Optional input layer to be used.
*NOTE: You can only specify a different layer if `include_top=False`*
5. **classes**: The number of output classes to be used, 1000 by default (for imagenet).
6. **pooling**: specifies if Pooling should be used or not.
*NOTE: You can only specify a different value if `include_top=True` and weights argument is 'not specified'*.

## How to use

You can import the required function from `tf.keras.applications`.

```python
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
```

Then pass in the parameters you desire to get an instance of the model.

```python
# in order to create the model you need only import the function
# and pass in the required parameters.
model = ResNet50()
```

### preprocessing

You can use this model [but not this fast]('../../../../images/reset_preprocessing_meme.png'), you need to apply some preprocessing to the input images before it's passed to the model.

```python
# in order to use the model you need to first apply some preprocessing to input image
# the function for that is included here
from tensorflow.keras.applications.resnet import preprocess_input

# and it can be used as simple as
image = preprocess_input(image)
# them pass the output to the model
labels = model(image)
```

This kind of preprocessing is done by multiple models included in Tensorflow, and done in pretty much the same way, you can check it [here](https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet/preprocess_input)

The code below builds a new model from the `MobileNet` model that first applies the required preprocessing, then passes the result to the imported model, it may not be as simple as in previous cell but it's the same concept.

```python
i = tf.keras.layers.Input([None, None, 3], dtype = tf.uint8)
x = tf.cast(i, tf.float32)
x = tf.keras.applications.mobilenet.preprocess_input(x)
core = tf.keras.applications.MobileNet()
x = core(x)
model = tf.keras.Model(inputs=[i], outputs=[x])

image = tf.image.decode_png(tf.io.read_file('file.png'))
result = model(image)
```
