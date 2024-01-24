# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/15737716/executor-map-typeerror-zip-argument-2-must-support-iteration
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time, concurrent.futures
    _l_(449543)

except ImportError:
    pass
lst100=[_n_(449544, "i", lambda: i) for i in _c_(449546, _n_(449545, "range", lambda: range), 100)]
_l_(449547)

t1=_c_(449550, _a_(449549, _n_(449548, "time", lambda: time), "clock"))
_l_(449551)
_c_(449559, _n_(449552, "print", lambda: print), _c_(449558, _n_(449553, "list", lambda: list), _c_(449557, _n_(449554, "map", lambda: map), _n_(449555, "str", lambda: str),_n_(449556, "lst100", lambda: lst100))))
_l_(449560)
t2=_c_(449563, _a_(449562, _n_(449561, "time", lambda: time), "clock"))
_l_(449564)
_c_(449568, _n_(449565, "print", lambda: print), _n_(449566, "t2", lambda: t2)-_n_(449567, "t1", lambda: t1))
_l_(449569)

t3=_c_(449572, _a_(449571, _n_(449570, "time", lambda: time), "clock"))
_l_(449573)
with _c_(449576, _a_(449575, _a_(449574, concurrent, "futures"), "ThreadPoolExecutor"), max_workers=100) as executor:
    _l_(449589)

    future_to_url = _c_(449581, _a_(449578, _n_(449577, "executor", lambda: executor), "map"), _n_(449579, "str", lambda: str),_n_(449580, "lst100", lambda: lst100), 60)
    _l_(449582)
    _c_(449587, _n_(449583, "print", lambda: print), _c_(449586, _n_(449584, "list", lambda: list), _n_(449585, "future_to_url", lambda: future_to_url)))
    _l_(449588)
t4=_c_(449592, _a_(449591, _n_(449590, "time", lambda: time), "clock"))
_l_(449593)
_c_(449597, _n_(449594, "print", lambda: print), _n_(449595, "t4", lambda: t4)-_n_(449596, "t3", lambda: t3))
_l_(449598)