# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67916291/pd-dataframe-resulting-in-typeerror-when-a-metaclass-is-defined-before-it
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(451263)

except ImportError:
    pass
class MappingMeta(_n_(451264, "type", lambda: type), _a_(451267, _a_(451266, _n_(451265, "collections", lambda: collections), "abc"), "Mapping")):
    _l_(451269)

    ... # same as above
    _l_(451268) # same as above

class Mapping(metaclass=_n_(451270, "MappingMeta", lambda: MappingMeta)):
    _l_(451272)

    pass
    _l_(451271)


class Test(_n_(451273, "Mapping", lambda: Mapping)):
    _l_(451276)

    x = 1
    _l_(451274)
    y = 2
    _l_(451275)

_c_(451281, _n_(451277, "print", lambda: print), _c_(451280, _a_(451279, _n_(451278, "pd", lambda: pd), "DataFrame"), {'x': [1, 2]}))
_l_(451282)