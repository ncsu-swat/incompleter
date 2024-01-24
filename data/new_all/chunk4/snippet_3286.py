# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76178464/typeerror-when-using-lru-cache-with-class-inheritance-in-python-3-8
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from functools import lru_cache
    _l_(623267)

except ImportError:
    pass

@_c_(623269, _n_(623268, "lru_cache", lambda: lru_cache), 1)
class A:
    _l_(623272)

    def __init__(self):
        _l_(623271)

        pass
        _l_(623270)

@_c_(623274, _n_(623273, "lru_cache", lambda: lru_cache), 1)
class B(_n_(623275, "A", lambda: A)):
    _l_(623277)

    pass
    _l_(623276)

b = _c_(623279, _n_(623278, "B", lambda: B))
_l_(623280)