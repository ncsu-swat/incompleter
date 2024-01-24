# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44946189/typeerror-init-got-an-unexpected-keyword-argument-shape
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(451126)

except ImportError:
    pass

g1 = _c_(451129, _a_(451128, _n_(451127, "tf", lambda: tf), "Graph"))
_l_(451130)
with _c_(451133, _a_(451132, _n_(451131, "g1", lambda: g1), "as_default")):
    _l_(451141)

    v = _c_(451139, _a_(451135, _n_(451134, "tf", lambda: tf), "get_variable"), "v", initializer=_c_(451138, _a_(451137, _n_(451136, "tf", lambda: tf), "zeros_initializer"), shape=[1]))
    _l_(451140)