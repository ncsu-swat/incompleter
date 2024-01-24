# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72555433/typeerror-not-supported-between-instances-of-list-and-int-occur-whil
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from multiprocessing import Pool
    _l_(565771)

except ImportError:
    pass

def f(x,y):
    _l_(565775)

    aux = _n_(565772, "x", lambda: x)*_n_(565773, "y", lambda: y)
    _l_(565774)
    return aux

with _c_(565777, _n_(565776, "Pool", lambda: Pool), 4) as p:
    _l_(565785)

    _c_(565783, _n_(565778, "print", lambda: print), _c_(565782, _a_(565780, _n_(565779, "p", lambda: p), "map"), _n_(565781, "f", lambda: f),[2,2,2],[3,4,5]))
    _l_(565784)