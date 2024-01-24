# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44580123/typeerror-dot-operation-in-numpy-and-theano
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import theano
    _l_(658123)

except ImportError:
    pass
try:
    import numpy
    _l_(658125)

except ImportError:
    pass

p=_c_(658129, _a_(658128, _a_(658127, _n_(658126, "theano", lambda: theano), "tensor"), "dmatrix"), 'p')
_l_(658130)
q=_c_(658134, _a_(658133, _a_(658132, _n_(658131, "theano", lambda: theano), "tensor"), "dmatrix"), 'q')
_l_(658135)
r=_c_(658141, _a_(658138, _a_(658137, _n_(658136, "theano", lambda: theano), "tensor"), "dot"), _n_(658139, "p", lambda: p),_n_(658140, "q", lambda: q))
_l_(658142)

f=_c_(658148, _a_(658144, _n_(658143, "theano", lambda: theano), "function"), [_n_(658145, "p", lambda: p),_n_(658146, "q", lambda: q)], _n_(658147, "r", lambda: r))
_l_(658149)

a=_c_(658152, _a_(658151, _n_(658150, "numpy", lambda: numpy), "array"), [1,2])
_l_(658153)
b=_c_(658156, _a_(658155, _n_(658154, "numpy", lambda: numpy), "array"), [[1,2,3],[4,5,6]])
_l_(658157)