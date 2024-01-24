# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62569070/python-typeerror-can-only-concatenate-str-not-int-to-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(354267)

except ImportError:
    pass

for i in _c_(354269, _n_(354268, "range", lambda: range), 2,6):
    _l_(354301)

    start = _c_(354272, _a_(354271, _n_(354270, "time", lambda: time), "time"))
    _l_(354273)
    n=_n_(354274, "i", lambda: i)
    _l_(354275)

    end = _c_(354278, _a_(354277, _n_(354276, "time", lambda: time), "time"))
    _l_(354279)
    _c_(354282, _n_(354280, "print", lambda: print), _n_(354281, "n", lambda: n))
    _l_(354283)

    time_cost=_n_(354284, "end", lambda: end)-_n_(354285, "start", lambda: start)
    _l_(354286)
    _c_(354291, _n_(354287, "print", lambda: print), _c_(354290, _n_(354288, "type", lambda: type), _n_(354289, "time_cost", lambda: time_cost)))
    _l_(354292)
    _c_(354299, _n_(354293, "print", lambda: print), 'totally cost for '+_n_(354294, "n", lambda: n)+'*'+_n_(354295, "n", lambda: n),_c_(354298, _n_(354296, "str", lambda: str), _n_(354297, "time_cost", lambda: time_cost)))
    _l_(354300)