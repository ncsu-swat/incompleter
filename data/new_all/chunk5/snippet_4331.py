# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44580123/typeerror-dot-operation-in-numpy-and-theano
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import theano
    _l_(700518)

except ImportError:
    pass
try:
    import numpy
    _l_(700520)

except ImportError:
    pass

p=_c_(700524, _a_(700523, _a_(700522, _n_(700521, "theano", lambda: theano), "tensor"), "dmatrix"), 'p')
_l_(700525)
q=_c_(700529, _a_(700528, _a_(700527, _n_(700526, "theano", lambda: theano), "tensor"), "dmatrix"), 'q')
_l_(700530)
r=_c_(700536, _a_(700533, _a_(700532, _n_(700531, "theano", lambda: theano), "tensor"), "dot"), _n_(700534, "p", lambda: p),_n_(700535, "q", lambda: q))
_l_(700537)

f=_c_(700543, _a_(700539, _n_(700538, "theano", lambda: theano), "function"), [_n_(700540, "p", lambda: p),_n_(700541, "q", lambda: q)], _n_(700542, "r", lambda: r))
_l_(700544)

a=_c_(700547, _a_(700546, _n_(700545, "numpy", lambda: numpy), "array"), [1,2])
_l_(700548)
b=_c_(700551, _a_(700550, _n_(700549, "numpy", lambda: numpy), "array"), [[1,2,3],[4,5,6]])
_l_(700552)