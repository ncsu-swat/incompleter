# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44309892/typeerror-function-object-is-not-subscriptable-in-tensorflow
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(411856)

except ImportError:
    pass
sess = _c_(411859, _a_(411858, _n_(411857, "tf", lambda: tf), "InteractiveSession"))
_l_(411860)
x = _c_(411865, _a_(411862, _n_(411861, "tf", lambda: tf), "placeholder"), _a_(411864, _n_(411863, "tf", lambda: tf), "float32"),[None, 784])
_l_(411866)
W = _c_(411871, _a_(411868, _n_(411867, "tf", lambda: tf), "Variable"), _a_(411870, _n_(411869, "tf", lambda: tf), "zeros")[784,10])
_l_(411872)
b = _c_(411877, _a_(411874, _n_(411873, "tf", lambda: tf), "Variable"), _a_(411876, _n_(411875, "tf", lambda: tf), "zeros")[10])
_l_(411878)