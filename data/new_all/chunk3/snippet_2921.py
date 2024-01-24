# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58226787/nonetype-error-in-lambda-layer-while-applying-a-mask-to-a-tensor
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(567756)

except ImportError:
    pass
try:
    from tensorflow.keras.layers import Conv2D, Input, BatchNormalization
    _l_(567758)

except ImportError:
    pass
try:
    from tensorflow.keras.layers import Lambda, Multiply, Add, Reshape
    _l_(567760)

except ImportError:
    pass
try:
    from tensorflow.keras.models import Model
    _l_(567762)

except ImportError:
    pass
try:
    import tensorflow.keras.backend as K
    _l_(567764)

except ImportError:
    pass
try:
    import numpy as np
    _l_(567766)

except ImportError:
    pass

def build_test(input_shape):
    _l_(567826)

    input_img = _c_(567769, _n_(567767, "Input", lambda: Input), shape=_n_(567768, "input_shape", lambda: input_shape))
    _l_(567770)
    _c_(567773, _n_(567771, "print", lambda: print), 'Input reshape:', _n_(567772, "input_shape", lambda: input_shape))
    _l_(567774)

    x = _c_(567790, _c_(567787, _n_(567775, "Lambda", lambda: Lambda), lambda tensor, mask: _c_(567786, _a_(567778, _a_(567777, _n_(567776, "tf", lambda: tf), "math"), "multiply"), _n_(567779, "tensor", lambda: tensor), _c_(567785, _a_(567781, _n_(567780, "tf", lambda: tf), "convert_to_tensor"), _n_(567782, "mask", lambda: mask), dtype=_a_(567784, _n_(567783, "tf", lambda: tf), "float32")))), [_n_(567788, "input_img", lambda: input_img), _n_(567789, "gamma", lambda: gamma)])
    _l_(567791)
    _c_(567795, _n_(567792, "print", lambda: print), 'multiply:', _a_(567794, _n_(567793, "x", lambda: x), "shape"))
    _l_(567796)
    x = _c_(567812, _c_(567809, _n_(567797, "Lambda", lambda: Lambda), lambda tensor, mask: _c_(567808, _a_(567800, _a_(567799, _n_(567798, "tf", lambda: tf), "math"), "add"), _n_(567801, "tensor", lambda: tensor), _c_(567807, _a_(567803, _n_(567802, "tf", lambda: tf), "convert_to_tensor"), _n_(567804, "mask", lambda: mask), dtype=_a_(567806, _n_(567805, "tf", lambda: tf), "float32")))), [_n_(567810, "x", lambda: x), _n_(567811, "beta", lambda: beta)])
    _l_(567813)
    _c_(567817, _n_(567814, "print", lambda: print), 'add:', _a_(567816, _n_(567815, "x", lambda: x), "shape"))
    _l_(567818)

    test = _c_(567822, _n_(567819, "Model", lambda: Model), inputs=_n_(567820, "input_img", lambda: input_img), outputs=_n_(567821, "x", lambda: x))
    _l_(567823)
    aux = _n_(567824, "test", lambda: test)
    _l_(567825)
    return aux

batch_sizes = [4, 8]
_l_(567827)
for i in _n_(567828, "batch_sizes", lambda: batch_sizes):
    _l_(567843)

    gamma = _c_(567832, _a_(567830, _n_(567829, "np", lambda: np), "arange"), _n_(567831, "i", lambda: i))
    _l_(567833)
    beta = _c_(567837, _a_(567835, _n_(567834, "np", lambda: np), "arange"), _n_(567836, "i", lambda: i))
    _l_(567838)
    model = _c_(567841, _n_(567839, "build_test", lambda: build_test), (_n_(567840, "i", lambda: i), 12, 12, 1))
    _l_(567842)