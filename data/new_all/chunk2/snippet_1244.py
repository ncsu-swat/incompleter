# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66584134/how-to-remove-typeerror-module-object-is-not-callable-in-glm
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import statsmodels.api as sm
    _l_(450109)

except ImportError:
    pass
glm=_c_(450117, _n_(450110, "sm", lambda: sm), _n_(450111, "y_train", lambda: y_train), _n_(450112, "X_train", lambda: X_train), family=_c_(450116, _a_(450115, _a_(450114, _n_(450113, "sm", lambda: sm), "families"), "Gaussian")))
_l_(450118)