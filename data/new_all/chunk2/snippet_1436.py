# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59466204/probit-statsmodels-attributeerror-module-statsmodels-has-no-attribute-dis
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import statsmodels
    _l_(428400)

except ImportError:
    pass

results = _c_(428407, _a_(428404, _a_(428403, _a_(428402, _n_(428401, "statsmodels", lambda: statsmodels), "discrete"), "discrete_model"), "Probit"), _n_(428405, "y", lambda: y), _n_(428406, "x", lambda: x))
_l_(428408)
_c_(428413, _n_(428409, "print", lambda: print), _c_(428412, _a_(428411, _n_(428410, "results", lambda: results), "summary")))
_l_(428414)