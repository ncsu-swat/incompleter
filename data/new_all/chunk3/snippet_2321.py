# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50913997/tensorflow-typeerror-tensorshape-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(578584)

except ImportError:
    pass
try:
    import numpy as np
    _l_(578586)

except ImportError:
    pass

_c_(578589, _a_(578588, _n_(578587, "tf", lambda: tf), "reset_default_graph"))
_l_(578590)

input_x = _c_(578595, _a_(578592, _n_(578591, "tf", lambda: tf), "placeholder"), name='tensor_a',shape=[None,None],dtype=_a_(578594, _n_(578593, "tf", lambda: tf), "int32"))
_l_(578596)
_c_(578601, _n_(578597, "print", lambda: print), _c_(578600, _a_(578599, _n_(578598, "input_x", lambda: input_x), "get_shape")))
_l_(578602)

var_b = _c_(578610, _a_(578604, _n_(578603, "tf", lambda: tf), "get_variable"), 'name_a',shape=[4,4],dtype=_a_(578606, _n_(578605, "tf", lambda: tf), "float32"),initializer=_c_(578609, _a_(578608, _n_(578607, "tf", lambda: tf), "random_uniform_initializer")))
_l_(578611)
var_c = _c_(578619, _a_(578613, _n_(578612, "tf", lambda: tf), "get_variable"), 'name_b',shape=[4,4],dtype=_a_(578615, _n_(578614, "tf", lambda: tf), "float32"),initializer=_c_(578618, _a_(578617, _n_(578616, "tf", lambda: tf), "random_uniform_initializer")))
_l_(578620)
vac_d= _c_(578630, _a_(578622, _n_(578621, "tf", lambda: tf), "get_variable"), 'name_d',shape=[_a_(578624, _n_(578623, "var_c", lambda: var_c), "shape")[0],60],dtype=_a_(578626, _n_(578625, "tf", lambda: tf), "float32"),initializer=_c_(578629, _a_(578628, _n_(578627, "tf", lambda: tf), "random_uniform_initializer")))
_l_(578631)
reshape_ = _c_(578639, _a_(578633, _n_(578632, "tf", lambda: tf), "reshape"), _n_(578634, "var_c", lambda: var_c),[_a_(578636, _n_(578635, "input_x", lambda: input_x), "shape")[0],_a_(578638, _n_(578637, "input_x", lambda: input_x), "shape")[1],-1])
_l_(578640)
_c_(578643, _n_(578641, "print", lambda: print), _n_(578642, "reshape_", lambda: reshape_))
_l_(578644)
sum_c=_c_(578649, _a_(578646, _n_(578645, "tf", lambda: tf), "add"), _n_(578647, "var_b", lambda: var_b),_n_(578648, "var_c", lambda: var_c))
_l_(578650)

with _c_(578653, _a_(578652, _n_(578651, "tf", lambda: tf), "Session")) as sess:
    _l_(578673)

    _c_(578659, _a_(578655, _n_(578654, "sess", lambda: sess), "run"), _c_(578658, _a_(578657, _n_(578656, "tf", lambda: tf), "global_variables_initializer")))
    _l_(578660)
    _c_(578671, _n_(578661, "print", lambda: print), _c_(578670, _a_(578663, _n_(578662, "sess", lambda: sess), "run"), _n_(578664, "sum_c", lambda: sum_c),feed_dict={_n_(578665, "input_x", lambda: input_x):_c_(578669, _a_(578668, _a_(578667, _n_(578666, "np", lambda: np), "random"), "randint"), 0,10,[2,2])}))
    _l_(578672)