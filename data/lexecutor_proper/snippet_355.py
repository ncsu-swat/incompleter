# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
10 
_l_(62495) 
10
_l_(62496)

_n_(62497, "_", lambda: _) 
_l_(62498) 
10
_l_(62499)

_n_(62500, "_", lambda: _) * 3 
_l_(62501) 
30
_l_(62502)

x, _, y = (1, 2, 3)
_l_(62503)

_n_(62504, "x", lambda: x)
_l_(62505)
1
_l_(62506)

_n_(62507, "y", lambda: y) 
_l_(62508) 
3
_l_(62509)

for _ in _c_(62511, _n_(62510, "range", lambda: range), 10):
    _l_(62515)

    _c_(62513, _n_(62512, "do_something", lambda: do_something))
    _l_(62514)

