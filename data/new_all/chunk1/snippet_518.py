# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59568125/attributeerror-nonetype-object-has-no-attribute-name-related-to-different
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(420199)

except ImportError:
    pass
for i in _c_(420202, _n_(420200, "range", lambda: range), _n_(420201, "iterations", lambda: iterations)):
    _l_(420235)

    _c_(420205, _n_(420203, "print", lambda: print), 'Start of iteration', _n_(420204, "i", lambda: i))
    _l_(420206)
    start_time = _c_(420209, _a_(420208, _n_(420207, "time", lambda: time), "time"))
    _l_(420210)
    x, min_val, info = _c_(420219, _n_(420211, "fmin_l_bfgs_b", lambda: fmin_l_bfgs_b), _a_(420213, _n_(420212, "evaluator", lambda: evaluator), "loss"), _c_(420216, _a_(420215, _n_(420214, "x", lambda: x), "flatten")),
                           fprime=_a_(420218, _n_(420217, "evaluator", lambda: evaluator), "grads"), maxfun=20)
    _l_(420220)
    _c_(420223, _n_(420221, "print", lambda: print), _n_(420222, "min_val", lambda: min_val))
    _l_(420224)
    end_time = _c_(420227, _a_(420226, _n_(420225, "time", lambda: time), "time"))
    _l_(420228)
    _c_(420233, _n_(420229, "print", lambda: print), 'Iteration %d completed in %ds' % (_n_(420230, "i", lambda: i), _n_(420231, "end_time", lambda: end_time) - _n_(420232, "start_time", lambda: start_time)))
    _l_(420234)