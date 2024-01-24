# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62506069/typeerror-missing-1-required-positional-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scipy.optimize as optimize
    _l_(530922)

except ImportError:
    pass
optimal_sharpe=_c_(530929, _a_(530924, _n_(530923, "optimize", lambda: optimize), "minimize"), _n_(530925, "minimize_sharpe", lambda: minimize_sharpe),
                                 _n_(530926, "initializer", lambda: initializer),
                                 method = 'SLSQP',
                                 bounds = _n_(530927, "bounds", lambda: bounds),
                                 constraints = _n_(530928, "constraints", lambda: constraints))
_l_(530930)
_c_(530933, _n_(530931, "print", lambda: print), _n_(530932, "optimal_sharpe", lambda: optimal_sharpe))
_l_(530934)