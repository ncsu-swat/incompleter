# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59113341/typeerror-input-global-step-of-resourceapplyadagradda-op-has-type-int32-th
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(466367)

except ImportError:
    pass
try:
    from tensorflow import keras
    _l_(466369)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(466371)

except ImportError:
    pass
try:
    import numpy as np
    _l_(466373)

except ImportError:
    pass
try:
    import time
    _l_(466375)

except ImportError:
    pass

start_time = _c_(466378, _a_(466377, _n_(466376, "time", lambda: time), "time"))
_l_(466379)



data = _a_(466383, _a_(466382, _a_(466381, _n_(466380, "tf", lambda: tf), "keras"), "datasets"), "fashion_mnist")
_l_(466384)

(train_images, train_labels), (test_images, test_labels) = _c_(466387, _a_(466386, _n_(466385, "data", lambda: data), "load_data"))
_l_(466388)

class_names = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']
_l_(466389)

train_images = _n_(466390, "train_images", lambda: train_images)/255.0
_l_(466391)

test_images = _n_(466392, "test_images", lambda: test_images)/255.0
_l_(466393)

optimizer1 = _c_(466399, _a_(466398, _a_(466397, _a_(466396, _a_(466395, _n_(466394, "tf", lambda: tf), "compat"), "v1"), "train"), "AdagradDAOptimizer"), 0.001,0)
_l_(466400)

model = _c_(466415, _a_(466402, _n_(466401, "keras", lambda: keras), "Sequential"), [
                           _c_(466406, _a_(466405, _a_(466404, _n_(466403, "keras", lambda: keras), "layers"), "Flatten"), input_shape=(28, 28)),
                           _c_(466410, _a_(466409, _a_(466408, _n_(466407, "keras", lambda: keras), "layers"), "Dense"), 100, activation="softsign"),
                           _c_(466414, _a_(466413, _a_(466412, _n_(466411, "keras", lambda: keras), "layers"), "Dense"), 10, activation="softmax")
])
_l_(466416)

_c_(466420, _a_(466418, _n_(466417, "model", lambda: model), "compile"), optimizer=_n_(466419, "optimizer1", lambda: optimizer1), loss="sparse_categorical_crossentropy", metrics=["accuracy"])
_l_(466421)

_c_(466426, _a_(466423, _n_(466422, "model", lambda: model), "fit"), _n_(466424, "train_images", lambda: train_images), _n_(466425, "train_labels", lambda: train_labels), epochs=5)
_l_(466427)

test_loss, test_acc1 = _c_(466432, _a_(466429, _n_(466428, "model", lambda: model), "evaluate"), _n_(466430, "test_images", lambda: test_images), _n_(466431, "test_labels", lambda: test_labels))
_l_(466433)

_c_(466436, _n_(466434, "print", lambda: print), "Test acc is:", _n_(466435, "test_acc1", lambda: test_acc1))
_l_(466437)
_c_(466443, _n_(466438, "print", lambda: print), "--- %s seconds ---" % (_c_(466441, _a_(466440, _n_(466439, "time", lambda: time), "time")) - _n_(466442, "start_time", lambda: start_time)))
_l_(466444)