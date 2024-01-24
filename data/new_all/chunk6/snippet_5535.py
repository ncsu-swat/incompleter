# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64342038/attributeerror-int-object-has-no-attribute-weight
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from converters import KgLbs as kglbs
    _l_(366543)

except ImportError:
    pass

weight = _c_(366547, _n_(366544, "int", lambda: int), _c_(366546, _n_(366545, "input", lambda: input), "Weight: "))
_l_(366548)
weight = _c_(366552, _a_(366550, _n_(366549, "kglbs", lambda: kglbs), "kg_to_lbs"), _n_(366551, "weight", lambda: weight))
_l_(366553)
_c_(366556, _n_(366554, "print", lambda: print), _n_(366555, "weight", lambda: weight))
_l_(366557)