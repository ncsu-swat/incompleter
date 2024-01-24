# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67916291/pd-dataframe-resulting-in-typeerror-when-a-metaclass-is-defined-before-it
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(446861)

except ImportError:
    pass
_c_(446866, _n_(446862, "print", lambda: print), _c_(446865, _a_(446864, _n_(446863, "pd", lambda: pd), "DataFrame"), {'x': [1, 2]}))
_l_(446867)

class MappingMeta(_n_(446868, "type", lambda: type), _a_(446871, _a_(446870, _n_(446869, "collections", lambda: collections), "abc"), "Mapping")):
    _l_(446873)

    ... # same as above
    _l_(446872) # same as above

class Mapping(metaclass=_n_(446874, "MappingMeta", lambda: MappingMeta)):
    _l_(446876)

    pass
    _l_(446875)


class Test(_n_(446877, "Mapping", lambda: Mapping)):
    _l_(446880)

    x = 1
    _l_(446878)
    y = 2
    _l_(446879)

_c_(446885, _n_(446881, "print", lambda: print), _c_(446884, _a_(446883, _n_(446882, "pd", lambda: pd), "DataFrame"), {'x': [1, 2]}))
_l_(446886)