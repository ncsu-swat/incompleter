# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58226787/nonetype-error-in-lambda-layer-while-applying-a-mask-to-a-tensor
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(541434)

except ImportError:
    pass
try:
    from tensorflow.keras.layers import Conv2D, Input, BatchNormalization
    _l_(541436)

except ImportError:
    pass
try:
    from tensorflow.keras.layers import Lambda, Multiply, Add, Reshape
    _l_(541438)

except ImportError:
    pass
try:
    from tensorflow.keras.models import Model
    _l_(541440)

except ImportError:
    pass
try:
    import tensorflow.keras.backend as K
    _l_(541442)

except ImportError:
    pass
try:
    import numpy as np
    _l_(541444)

except ImportError:
    pass

def build_test(input_shape):
    _l_(541535)

    input_img = _c_(541447, _n_(541445, "Input", lambda: Input), shape=_n_(541446, "input_shape", lambda: input_shape))
    _l_(541448)
    _c_(541451, _n_(541449, "print", lambda: print), 'Input reshape:', _n_(541450, "input_shape", lambda: input_shape))
    _l_(541452)

    for batch in _c_(541455, _n_(541453, "range", lambda: range), _n_(541454, "input_shape", lambda: input_shape)[0]):
        _l_(541527)

        # x = tf.gather(x, batch)
        # print('tensor shape:', x.shape)  
        mask = _c_(541461, _a_(541457, _n_(541456, "np", lambda: np), "empty"), _n_(541458, "input_shape", lambda: input_shape), dtype=_a_(541460, _n_(541459, "np", lambda: np), "float32"))
        _l_(541462)
        # for gamma
        _c_(541465, _a_(541464, _n_(541463, "mask", lambda: mask), "fill"), 1)
        _l_(541466)
        _c_(541472, _a_(541469, _n_(541467, "mask", lambda: mask)[_n_(541468, "batch", lambda: batch)], "fill"), _n_(541470, "gamma", lambda: gamma)[_n_(541471, "batch", lambda: batch)])
        _l_(541473)
        x = _c_(541488, _c_(541486, _n_(541474, "Lambda", lambda: Lambda), lambda tensor: _c_(541485, _a_(541477, _a_(541476, _n_(541475, "tf", lambda: tf), "math"), "multiply"), _n_(541478, "tensor", lambda: tensor), _c_(541484, _a_(541480, _n_(541479, "tf", lambda: tf), "convert_to_tensor"), _n_(541481, "mask", lambda: mask), dtype=_a_(541483, _n_(541482, "tf", lambda: tf), "float32")))), _n_(541487, "input_img", lambda: input_img))
        _l_(541489)
        _c_(541493, _n_(541490, "print", lambda: print), 'multiply:', _a_(541492, _n_(541491, "x", lambda: x), "shape"))
        _l_(541494)
        # for beta
        _c_(541497, _a_(541496, _n_(541495, "mask", lambda: mask), "fill"), 1)
        _l_(541498)
        _c_(541504, _a_(541501, _n_(541499, "mask", lambda: mask)[_n_(541500, "batch", lambda: batch)], "fill"), _n_(541502, "beta", lambda: beta)[_n_(541503, "batch", lambda: batch)])
        _l_(541505)
        x = _c_(541520, _c_(541518, _n_(541506, "Lambda", lambda: Lambda), lambda tensor: _c_(541517, _a_(541509, _a_(541508, _n_(541507, "tf", lambda: tf), "math"), "add"), _n_(541510, "tensor", lambda: tensor), _c_(541516, _a_(541512, _n_(541511, "tf", lambda: tf), "convert_to_tensor"), _n_(541513, "mask", lambda: mask), dtype=_a_(541515, _n_(541514, "tf", lambda: tf), "float32")))), _n_(541519, "x", lambda: x))
        _l_(541521)
        _c_(541525, _n_(541522, "print", lambda: print), 'add:', _a_(541524, _n_(541523, "x", lambda: x), "shape"))
        _l_(541526)

    test = _c_(541531, _n_(541528, "Model", lambda: Model), inputs=_n_(541529, "input_img", lambda: input_img), outputs=_n_(541530, "x", lambda: x))
    _l_(541532)
    aux = _n_(541533, "test", lambda: test)
    _l_(541534)
    return aux

batch_sizes = [4, 8]
_l_(541536)
for i in _n_(541537, "batch_sizes", lambda: batch_sizes):
    _l_(541552)

    gamma = _c_(541541, _a_(541539, _n_(541538, "np", lambda: np), "arange"), _n_(541540, "i", lambda: i))
    _l_(541542)
    beta = _c_(541546, _a_(541544, _n_(541543, "np", lambda: np), "arange"), _n_(541545, "i", lambda: i))
    _l_(541547)
    model = _c_(541550, _n_(541548, "build_test", lambda: build_test), (_n_(541549, "i", lambda: i), 12, 12, 1))
    _l_(541551)