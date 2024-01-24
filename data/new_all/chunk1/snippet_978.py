# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59585574/autograph-in-tensorflow-1-15-gives-typeerror-in-conditional-statement-with-value
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(412438)

except ImportError:
    pass
try:
    from tensorflow import autograph as ag
    _l_(412440)

except ImportError:
    pass

#minimal code for method to demonstrate issue
def foo(x):
    _l_(412449)

    if _n_(412441, "x", lambda: x) > 0:
        _l_(412446)

        y = _n_(412442, "x", lambda: x) * _n_(412443, "x", lambda: x)
        _l_(412444)
    else:
        y = 0.0
        _l_(412445)
    aux = _n_(412447, "y", lambda: y)
    _l_(412448)
    return aux

#graph construction
mdl = _c_(412452, _a_(412451, _n_(412450, "tf", lambda: tf), "Graph"))
_l_(412453)
with _c_(412456, _a_(412455, _n_(412454, "mdl", lambda: mdl), "as_default")):
    _l_(412479)

    converted_foo = _c_(412460, _a_(412458, _n_(412457, "ag", lambda: ag), "to_graph"), _n_(412459, "foo", lambda: foo))
    _l_(412461)
    _c_(412467, _n_(412462, "print", lambda: print), _c_(412466, _a_(412464, _n_(412463, "ag", lambda: ag), "to_code"), _n_(412465, "foo", lambda: foo)))
    _l_(412468)
    x = _c_(412473, _a_(412470, _n_(412469, "tf", lambda: tf), "placeholder"), _a_(412472, _n_(412471, "tf", lambda: tf), "double"), name='x')
    _l_(412474)
    y = _c_(412477, _n_(412475, "converted_foo", lambda: converted_foo), _n_(412476, "x", lambda: x))
    _l_(412478)