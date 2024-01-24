# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67987726/typeerror-minimize-got-multiple-values-for-argument-methodwithout-kwargs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from scipy.optimize import minimize
    _l_(425630)

except ImportError:
    pass
def fun1(x,Cnoi,M):
    _l_(425642)

    aux = _c_(425640, _a_(425633, _a_(425632, _n_(425631, "np", lambda: np), "linalg"), "norm"), _n_(425634, "Cnoi", lambda: Cnoi) - _c_(425639, _a_(425636, _n_(425635, "np", lambda: np), "matmul"), _n_(425637, "M", lambda: M),_n_(425638, "x", lambda: x)))**2
    _l_(425641)
    return aux

_c_(425650, _n_(425643, "minimize", lambda: minimize), _n_(425644, "fun1", lambda: fun1), _n_(425645, "x0", lambda: x0), _n_(425646, "Cnoi", lambda: Cnoi), _n_(425647, "M", lambda: M), method='SLSQP', bounds=_n_(425648, "bnds", lambda: bnds), constraints=_n_(425649, "cons", lambda: cons))
_l_(425651)