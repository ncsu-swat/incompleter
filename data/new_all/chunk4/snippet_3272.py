# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76352210/typeerror-variablemetaclass-variable-v1-call-got-an-unexpected-keyword-argum
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
encoder = [
    _c_(597971, _a_(597970, _a_(597969, _a_(597968, _n_(597967, "tf", lambda: tf), "keras"), "layers"), "InputLayer"), input_shape=(32, 24, 1,)),
     _c_(597976, _a_(597975, _a_(597974, _a_(597973, _n_(597972, "tf", lambda: tf), "keras"), "layers"), "Conv2D"), filters=32, kernel_size=3, strides=(2, 2), activation="gelu"
    )
]
_l_(597977)

_a_(597983, _c_(597982, _a_(597980, _a_(597979, _n_(597978, "tf", lambda: tf), "keras"), "Sequential"), _n_(597981, "encoder", lambda: encoder)), "layers")
_l_(597984)