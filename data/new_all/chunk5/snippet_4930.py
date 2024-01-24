# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39893049/how-to-solve-typeerrortype-object-is-not-subscriptable-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
r= _n_(688654, "list", lambda: list)[_c_(688657, _a_(688656, _n_(688655, "random", lambda: random), "randrange"), 1,20,50)]  
_l_(688658)  
L2= []
_l_(688659)
for item in _n_(688660, "r", lambda: r):
    _l_(688673)

    t= _n_(688661, "basic_delay", lambda: basic_delay) + 2*_n_(688662, "basic_jitter", lambda: basic_jitter)*_n_(688663, "item", lambda: item) - _n_(688664, "basic_jitter", lambda: basic_jitter)
    _l_(688665)
    _c_(688671, _a_(688667, _n_(688666, "L2", lambda: L2), "append"), _c_(688670, _n_(688668, "str", lambda: str), _n_(688669, "t", lambda: t)))
    _l_(688672)

for item in _n_(688674, "L2", lambda: L2):
    _l_(688680)

    _c_(688678, _a_(688676, _n_(688675, "file", lambda: file), "write"), "%s\n" % _n_(688677, "item", lambda: item))
    _l_(688679)