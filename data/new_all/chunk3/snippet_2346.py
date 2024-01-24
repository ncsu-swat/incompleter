# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49566391/nameerror-for-importing-random-and-numpy-random-but-nothing-else
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
rounds = 10
_l_(532452)
probability = 100
_l_(532453)
items = [1, 2, 3, 4, 5]
_l_(532454)
try:
    from numpy.random import uniform
    _l_(532456)

except ImportError:
    pass
for r in _c_(532459, _n_(532457, "range", lambda: range), 1, _n_(532458, "rounds", lambda: rounds)):
    _l_(532466)

    sample = {_n_(532460, "item", lambda: item): _c_(532462, _n_(532461, "uniform", lambda: uniform)) < _n_(532463, "probability", lambda: probability) for item in _n_(532464, "items", lambda: items)}
    _l_(532465)