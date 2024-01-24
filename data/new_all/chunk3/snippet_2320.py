# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50913997/tensorflow-typeerror-tensorshape-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(570070)

except ImportError:
    pass
try:
    import numpy as np
    _l_(570072)

except ImportError:
    pass

_c_(570075, _a_(570074, _n_(570073, "tf", lambda: tf), "reset_default_graph"))
_l_(570076)

input_x = _c_(570081, _a_(570078, _n_(570077, "tf", lambda: tf), "placeholder"), name='tensor_a',shape=[2,3,4],dtype=_a_(570080, _n_(570079, "tf", lambda: tf), "int32"))
_l_(570082)

var_b = _c_(570093, _a_(570084, _n_(570083, "tf", lambda: tf), "get_variable"), 'name_a',shape=[_c_(570087, _a_(570086, _n_(570085, "input_x", lambda: input_x), "get_shape"))[0],2],dtype=_a_(570089, _n_(570088, "tf", lambda: tf), "float32"),initializer=_c_(570092, _a_(570091, _n_(570090, "tf", lambda: tf), "random_uniform_initializer")))
_l_(570094)
var_c = _c_(570105, _a_(570096, _n_(570095, "tf", lambda: tf), "get_variable"), 'name_b',shape=[_c_(570099, _a_(570098, _n_(570097, "input_x", lambda: input_x), "get_shape"))[1],2],dtype=_a_(570101, _n_(570100, "tf", lambda: tf), "float32"),initializer=_c_(570104, _a_(570103, _n_(570102, "tf", lambda: tf), "random_uniform_initializer")))
_l_(570106)

sum_c=_c_(570111, _a_(570108, _n_(570107, "tf", lambda: tf), "add"), _n_(570109, "var_b", lambda: var_b),_n_(570110, "var_c", lambda: var_c))
_l_(570112)

with _c_(570115, _a_(570114, _n_(570113, "tf", lambda: tf), "Session")) as sess:
    _l_(570135)

    _c_(570121, _a_(570117, _n_(570116, "sess", lambda: sess), "run"), _c_(570120, _a_(570119, _n_(570118, "tf", lambda: tf), "global_variables_initializer")))
    _l_(570122)
    _c_(570133, _n_(570123, "print", lambda: print), _c_(570132, _a_(570125, _n_(570124, "sess", lambda: sess), "run"), _n_(570126, "sum_c", lambda: sum_c),feed_dict={_n_(570127, "input_x", lambda: input_x):_c_(570131, _a_(570130, _a_(570129, _n_(570128, "np", lambda: np), "random"), "randint"), 0,10,[2,3,4])}))
    _l_(570134)