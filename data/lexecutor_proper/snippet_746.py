# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4362586/sum-a-list-of-numbers-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
xs = [1, 2, 3, 4, 5]
_l_(64629)
_c_(64634, _n_(64630, "print", lambda: print), _c_(64633, _n_(64631, "sum", lambda: sum), _n_(64632, "xs", lambda: xs)))
_l_(64635)

15
_l_(64636)

averages = [(_n_(64637, "x", lambda: x) + _n_(64638, "y", lambda: y)) / 2.0 for (x, y) in _c_(64642, _n_(64639, "zip", lambda: zip), _n_(64640, "my_list", lambda: my_list)[:-1], _n_(64641, "my_list", lambda: my_list)[1:])]
_l_(64643)

