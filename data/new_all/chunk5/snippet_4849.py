# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46003423/getting-typeerror-numpy-ndarray-object-is-not-callable-for-my-code
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
     import numpy as np
     _l_(649616)

except ImportError:
     pass

def sigmoid(x):
     _l_(649624)

     s = 1/(1+_c_(649620, _a_(649618, _n_(649617, "np", lambda: np), "exp"), -_n_(649619, "x", lambda: x)))
     _l_(649621)
     aux = _n_(649622, "s", lambda: s)
     _l_(649623)
     return aux

def sigmoid_derivative(x):
     _l_(649635)

     s = _c_(649627, _n_(649625, "sigmoid", lambda: sigmoid), _n_(649626, "x", lambda: x))
     _l_(649628)
     ds = _c_(649631, _n_(649629, "s", lambda: s), 1-_n_(649630, "s", lambda: s))
     _l_(649632)
     aux = _n_(649633, "ds", lambda: ds)
     _l_(649634)
     return aux


x = _c_(649638, _a_(649637, _n_(649636, "np", lambda: np), "array"), [1, 2, 3])
_l_(649639)
_c_(649646, _n_(649640, "print", lambda: print), "sigmoid_derivative(x) = " + _c_(649645, _n_(649641, "str", lambda: str), _c_(649644, _n_(649642, "sigmoid_derivative", lambda: sigmoid_derivative), _n_(649643, "x", lambda: x))))
_l_(649647)