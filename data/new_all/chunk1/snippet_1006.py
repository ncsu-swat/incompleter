# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57101765/keras-error-on-conv2d-creation-typeerror-cant-multiply-sequence-by-non-int-of
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tensorflow.keras.models import Sequential
    _l_(405337)

except ImportError:
    pass
try:
    from tensorflow.keras.layers import Conv2D
    _l_(405339)

except ImportError:
    pass
try:
    import numpy as np
    _l_(405341)

except ImportError:
    pass


def model():
    _l_(405359)

    new_model = _c_(405343, _n_(405342, "Sequential", lambda: Sequential))
    _l_(405344)
    for i in _c_(405346, _n_(405345, "range", lambda: range), 4):
        _l_(405356)

        _c_(405354, _a_(405348, _n_(405347, "new_model", lambda: new_model), "add"), _c_(405353, _n_(405349, "Conv2D", lambda: Conv2D), filters=(3,3), kernel_size = 1
                      , activation='linear', padding='valid'
                      , input_shape=_c_(405352, _a_(405351, _n_(405350, "np", lambda: np), "array"), [9,9,9])))
        _l_(405355)
    aux = _n_(405357, "cnn_model", lambda: cnn_model)
    _l_(405358)

    return aux

if _n_(405360, "__name__", lambda: __name__) == '__main__':
    _l_(405364)

    _c_(405362, _n_(405361, "model", lambda: model))
    _l_(405363)