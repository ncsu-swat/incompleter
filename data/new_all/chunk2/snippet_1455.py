# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56513526/attributeerror-function-object-has-no-attribute-summary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
y=_n_(469176, "dataset", lambda: dataset)
_l_(469177)
X=_n_(469178, "dataset", lambda: dataset) [['A'] + ['B'] + ['C'] + ['D'] + ['E']]
_l_(469179)
X1 = _c_(469183, _a_(469181, _n_(469180, "sm", lambda: sm), "add_constant"), _n_(469182, "X", lambda: X))
_l_(469184)
model = _c_(469189, _a_(469186, _n_(469185, "sm", lambda: sm), "OLS"), endog = _n_(469187, "y", lambda: y), exog = _n_(469188, "X", lambda: X))
_l_(469190)
results = _a_(469192, _n_(469191, "model", lambda: model), "fit")
_l_(469193)
_c_(469196, _a_(469195, _n_(469194, "results", lambda: results), "summary"))
_l_(469197)