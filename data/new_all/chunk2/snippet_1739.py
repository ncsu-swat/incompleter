# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59313922/the-typeerror-float-object-cannot-be-interpreted-as-an-integer-in-stride-tric
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(455628)

except ImportError:
    pass
n=4
_l_(455629)
m=5
_l_(455630)
a = _c_(455639, _a_(455636, _c_(455635, _a_(455632, _n_(455631, "np", lambda: np), "arange"), 1,_n_(455633, "n", lambda: n)*_n_(455634, "m", lambda: m)+1), "reshape"), _n_(455637, "n", lambda: n),_n_(455638, "m", lambda: m))
_l_(455640)

sz = _a_(455642, _n_(455641, "a", lambda: a), "itemsize")
_l_(455643)
h,w = _a_(455645, _n_(455644, "a", lambda: a), "shape")
_l_(455646)
bh,bw = 2,2
_l_(455647)
shape = (_n_(455648, "h", lambda: h)/_n_(455649, "bh", lambda: bh), _n_(455650, "w", lambda: w)/_n_(455651, "bw", lambda: bw), _n_(455652, "bh", lambda: bh), _n_(455653, "bw", lambda: bw))
_l_(455654)

strides = _n_(455655, "sz", lambda: sz)*_c_(455662, _a_(455657, _n_(455656, "np", lambda: np), "array"), [_n_(455658, "w", lambda: w)*_n_(455659, "bh", lambda: bh),_n_(455660, "bw", lambda: bw),_n_(455661, "w", lambda: w),1])
_l_(455663)


blocks=_c_(455671, _a_(455667, _a_(455666, _a_(455665, _n_(455664, "np", lambda: np), "lib"), "stride_tricks"), "as_strided"), _n_(455668, "a", lambda: a), shape=_n_(455669, "shape", lambda: shape), strides=_n_(455670, "strides", lambda: strides))
_l_(455672)
_c_(455675, _n_(455673, "print", lambda: print), _n_(455674, "blocks", lambda: blocks))
_l_(455676)