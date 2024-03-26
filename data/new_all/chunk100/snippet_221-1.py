# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(105758)

except ImportError:
    pass
x = _c_(105761, _a_(105760, _n_(105759, "np", lambda: np), "array"), [1, 3, 5, 7, 0])
_l_(105762)
_c_(105764, _n_(105763, "print", lambda: print), 'Original array: ')
_l_(105765)
_c_(105768, _n_(105766, "print", lambda: print), _n_(105767, "x", lambda: x))
_l_(105769)
r1 = _c_(105773, _a_(105771, _n_(105770, "np", lambda: np), "ediff1d"), _n_(105772, "x", lambda: x), to_begin=[0, 0], to_end=[200])
_l_(105774)
assert _c_(105779, _a_(105776, _n_(105775, "np", lambda: np), "array_equiv"), _n_(105777, "r1", lambda: r1), _n_(105778, "r2", lambda: r2))
_l_(105780)
_c_(105782, _n_(105781, "print", lambda: print), 'Difference between neighboring elements, element-wise, and prepend [0, 0] and append[200] to the said array:')
_l_(105783)
_c_(105786, _n_(105784, "print", lambda: print), _n_(105785, "r2", lambda: r2))
_l_(105787)