# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57308050/typeerror-image-data-of-dtype-object-cannot-be-converted-to-float-when-showin
from __future__ import absolute_import, division, print_function, unicode_literals
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(657826)
try:
    import tensorflow as tf
    _l_(657828)

except ImportError:
    pass
try:
    import glob
    _l_(657830)

except ImportError:
    pass
try:
    import imageio
    _l_(657832)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(657834)

except ImportError:
    pass
try:
    import numpy as np
    _l_(657836)

except ImportError:
    pass
try:
    import os
    _l_(657838)

except ImportError:
    pass
try:
    import PIL
    _l_(657840)

except ImportError:
    pass
try:
    from tensorflow.keras import layers
    _l_(657842)

except ImportError:
    pass
try:
    import time
    _l_(657844)

except ImportError:
    pass
try:
    from IPython import display
    _l_(657846)

except ImportError:
    pass
(train_images, train_labels), (_, _) = _c_(657852, _a_(657851, _a_(657850, _a_(657849, _a_(657848, _n_(657847, "tf", lambda: tf), "keras"), "datasets"), "mnist"), "load_data"))
_l_(657853)
train_images = _c_(657860, _a_(657859, _c_(657858, _a_(657855, _n_(657854, "train_images", lambda: train_images), "reshape"), _a_(657857, _n_(657856, "train_images", lambda: train_images), "shape")[0], 28, 28, 1), "astype"), 'float32')
_l_(657861)
train_images = (_n_(657862, "train_images", lambda: train_images) - 127.5) / 127.5 # Normalize the images to [-1, 1]
_l_(657863) # Normalize the images to [-1, 1]
BUFFER_SIZE = 60000
_l_(657864)
BATCH_SIZE = 256
_l_(657865)
def make_generator_model():
    _l_(657962)

    model = _c_(657869, _a_(657868, _a_(657867, _n_(657866, "tf", lambda: tf), "keras"), "Sequential"))
    _l_(657870)
    _c_(657876, _a_(657872, _n_(657871, "model", lambda: model), "add"), _c_(657875, _a_(657874, _n_(657873, "layers", lambda: layers), "Dense"), 7*7*256, use_bias=False, input_shape=(100,)))
    _l_(657877)
    _c_(657883, _a_(657879, _n_(657878, "model", lambda: model), "add"), _c_(657882, _a_(657881, _n_(657880, "layers", lambda: layers), "BatchNormalization")))
    _l_(657884)
    _c_(657890, _a_(657886, _n_(657885, "model", lambda: model), "add"), _c_(657889, _a_(657888, _n_(657887, "layers", lambda: layers), "LeakyReLU")))
    _l_(657891)

    _c_(657897, _a_(657893, _n_(657892, "model", lambda: model), "add"), _c_(657896, _a_(657895, _n_(657894, "layers", lambda: layers), "Reshape"), (7, 7, 256)))
    _l_(657898)
    assert _a_(657900, _n_(657899, "model", lambda: model), "output_shape") == (None, 7, 7, 256) # Note: None is the batch size
    _l_(657901) # Note: None is the batch size

    _c_(657907, _a_(657903, _n_(657902, "model", lambda: model), "add"), _c_(657906, _a_(657905, _n_(657904, "layers", lambda: layers), "Conv2DTranspose"), 128, (5, 5), strides=(1, 1), padding='same', use_bias=False))
    _l_(657908)
    assert _a_(657910, _n_(657909, "model", lambda: model), "output_shape") == (None, 7, 7, 128)
    _l_(657911)
    _c_(657917, _a_(657913, _n_(657912, "model", lambda: model), "add"), _c_(657916, _a_(657915, _n_(657914, "layers", lambda: layers), "BatchNormalization")))
    _l_(657918)
    _c_(657924, _a_(657920, _n_(657919, "model", lambda: model), "add"), _c_(657923, _a_(657922, _n_(657921, "layers", lambda: layers), "LeakyReLU")))
    _l_(657925)

    _c_(657931, _a_(657927, _n_(657926, "model", lambda: model), "add"), _c_(657930, _a_(657929, _n_(657928, "layers", lambda: layers), "Conv2DTranspose"), 64, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    _l_(657932)
    assert _a_(657934, _n_(657933, "model", lambda: model), "output_shape") == (None, 14, 14, 64)
    _l_(657935)
    _c_(657941, _a_(657937, _n_(657936, "model", lambda: model), "add"), _c_(657940, _a_(657939, _n_(657938, "layers", lambda: layers), "BatchNormalization")))
    _l_(657942)
    _c_(657948, _a_(657944, _n_(657943, "model", lambda: model), "add"), _c_(657947, _a_(657946, _n_(657945, "layers", lambda: layers), "LeakyReLU")))
    _l_(657949)

    _c_(657955, _a_(657951, _n_(657950, "model", lambda: model), "add"), _c_(657954, _a_(657953, _n_(657952, "layers", lambda: layers), "Conv2DTranspose"), 1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh'))
    _l_(657956)
    assert _a_(657958, _n_(657957, "model", lambda: model), "output_shape") == (None, 28, 28, 1)
    _l_(657959)
    aux = _n_(657960, "model", lambda: model)
    _l_(657961)

    return aux

generator = _c_(657964, _n_(657963, "make_generator_model", lambda: make_generator_model))
_l_(657965)

noise = _c_(657969, _a_(657968, _a_(657967, _n_(657966, "tf", lambda: tf), "random"), "normal"), [1, 100])
_l_(657970)
generated_image = _c_(657973, _n_(657971, "generator", lambda: generator), _n_(657972, "noise", lambda: noise), training=False)
_l_(657974)

_c_(657978, _a_(657976, _n_(657975, "plt", lambda: plt), "imshow"), _n_(657977, "generated_image", lambda: generated_image)[0, :, :, 0], cmap='gray')
_l_(657979)