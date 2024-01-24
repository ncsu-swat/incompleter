# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76214437/attributeerror-modeldata-object-has-no-attribute-design-info
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import statsmodels.api as sm
    _l_(533733)

except ImportError:
    pass
try:
    import numpy as np
    _l_(533735)

except ImportError:
    pass

# define the data
x1 = _c_(533739, _a_(533738, _a_(533737, _n_(533736, "np", lambda: np), "random"), "rand"), 100)
_l_(533740)
x2 = _c_(533744, _a_(533743, _a_(533742, _n_(533741, "np", lambda: np), "random"), "rand"), 100)
_l_(533745)
y = 2*_n_(533746, "x1", lambda: x1) + 3*_n_(533747, "x2", lambda: x2) + _c_(533751, _a_(533750, _a_(533749, _n_(533748, "np", lambda: np), "random"), "normal"), size=100)
_l_(533752)

# build the model with all independent variables
X = _c_(533760, _a_(533754, _n_(533753, "sm", lambda: sm), "add_constant"), _c_(533759, _a_(533756, _n_(533755, "np", lambda: np), "column_stack"), (_n_(533757, "x1", lambda: x1), _n_(533758, "x2", lambda: x2))))
_l_(533761)
model = _c_(533768, _a_(533767, _c_(533766, _a_(533763, _n_(533762, "sm", lambda: sm), "OLS"), _n_(533764, "y", lambda: y), _n_(533765, "X", lambda: X)), "fit"))
_l_(533769)

# perform the F-test
f_value, p_value, _ = _c_(533774, _a_(533772, _a_(533771, _n_(533770, "sm", lambda: sm), "stats"), "anova_lm"), _n_(533773, "model", lambda: model), typ=1)
_l_(533775)