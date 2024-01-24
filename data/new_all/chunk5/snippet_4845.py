# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46003423/getting-typeerror-numpy-ndarray-object-is-not-callable-for-my-code
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
     import numpy as np
     _l_(685412)

except ImportError:
     pass

def sigmoid(x):
     _l_(685420)

     s = 1/(1+_c_(685416, _a_(685414, _n_(685413, "np", lambda: np), "exp"), -_n_(685415, "x", lambda: x)))
     _l_(685417)
     aux = _n_(685418, "s", lambda: s)
     _l_(685419)
     return aux

def sigmoid_derivative(x):
     _l_(685431)

     s = _c_(685423, _n_(685421, "sigmoid", lambda: sigmoid), _n_(685422, "x", lambda: x))
     _l_(685424)
     ds = _c_(685427, _n_(685425, "s", lambda: s), 1-_n_(685426, "s", lambda: s))
     _l_(685428)
     aux = _n_(685429, "ds", lambda: ds)
     _l_(685430)
     return aux


x = _c_(685434, _a_(685433, _n_(685432, "np", lambda: np), "array"), [1, 2, 3])
_l_(685435)
_c_(685442, _n_(685436, "print", lambda: print), "sigmoid_derivative(x) = " + _c_(685441, _n_(685437, "str", lambda: str), _c_(685440, _n_(685438, "sigmoid_derivative", lambda: sigmoid_derivative), _n_(685439, "x", lambda: x))))
_l_(685443)