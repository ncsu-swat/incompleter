# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64342038/attributeerror-int-object-has-no-attribute-weight
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from converters import KgLbs as kglbs
    _l_(350440)

except ImportError:
    pass

weight = _c_(350444, _n_(350441, "int", lambda: int), _c_(350443, _n_(350442, "input", lambda: input), "Weight: "))
_l_(350445)
weight = _c_(350449, _a_(350447, _n_(350446, "kglbs", lambda: kglbs), "kg_to_lbs"), _n_(350448, "weight", lambda: weight))
_l_(350450)
_c_(350453, _n_(350451, "print", lambda: print), _n_(350452, "weight", lambda: weight))
_l_(350454)