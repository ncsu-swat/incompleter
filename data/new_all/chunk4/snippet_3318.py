# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75765370/typeerror-identified-in-implementing-weightnormalization-layer-within-tensorfl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(588456)

except ImportError:
    pass
try:
    import tensorflow_addons as tfa
    _l_(588458)

except ImportError:
    pass
try:
    import numpy as np
    _l_(588460)

except ImportError:
    pass
try:
    from matplotlib import pyplot as plt
    _l_(588462)

except ImportError:
    pass

# Hyper Parameters
batch_size = 32
_l_(588463)
epochs = 10
_l_(588464)
num_classes=10
_l_(588465)

# WeightNorm ConvNet
wn_model = _c_(588530, _a_(588468, _a_(588467, _n_(588466, "tf", lambda: tf), "keras"), "Sequential"), [
    _c_(588477, _a_(588471, _a_(588470, _n_(588469, "tfa", lambda: tfa), "layers"), "WeightNormalization"), _c_(588476, _a_(588475, _a_(588474, _a_(588473, _n_(588472, "tf", lambda: tf), "keras"), "layers"), "Conv2D"), 6, 5, activation='relu')),
    _c_(588482, _a_(588481, _a_(588480, _a_(588479, _n_(588478, "tf", lambda: tf), "keras"), "layers"), "MaxPooling2D"), 2, 2),
    _c_(588491, _a_(588485, _a_(588484, _n_(588483, "tfa", lambda: tfa), "layers"), "WeightNormalization"), _c_(588490, _a_(588489, _a_(588488, _a_(588487, _n_(588486, "tf", lambda: tf), "keras"), "layers"), "Conv2D"), 16, 5, activation='relu')),
    _c_(588496, _a_(588495, _a_(588494, _a_(588493, _n_(588492, "tf", lambda: tf), "keras"), "layers"), "MaxPooling2D"), 2, 2),
    _c_(588501, _a_(588500, _a_(588499, _a_(588498, _n_(588497, "tf", lambda: tf), "keras"), "layers"), "Flatten")),
    _c_(588510, _a_(588504, _a_(588503, _n_(588502, "tfa", lambda: tfa), "layers"), "WeightNormalization"), _c_(588509, _a_(588508, _a_(588507, _a_(588506, _n_(588505, "tf", lambda: tf), "keras"), "layers"), "Dense"), 120, activation='relu')),
    _c_(588519, _a_(588513, _a_(588512, _n_(588511, "tfa", lambda: tfa), "layers"), "WeightNormalization"), _c_(588518, _a_(588517, _a_(588516, _a_(588515, _n_(588514, "tf", lambda: tf), "keras"), "layers"), "Dense"), 84, activation='relu')),
    _c_(588529, _a_(588522, _a_(588521, _n_(588520, "tfa", lambda: tfa), "layers"), "WeightNormalization"), _c_(588528, _a_(588526, _a_(588525, _a_(588524, _n_(588523, "tf", lambda: tf), "keras"), "layers"), "Dense"), _n_(588527, "num_classes", lambda: num_classes), activation='softmax')),
])
_l_(588531)