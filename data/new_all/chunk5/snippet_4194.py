# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61834959/patsyerror-error-evaluating-factor-nameerror-name-wheel-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import statsmodels.api as sm
    _l_(703318)

except ImportError:
    pass
try:
    import statsmodels.formula.api as smf
    _l_(703320)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(703322)

except ImportError:
    pass


cars = _c_(703327, _a_(703324, _n_(703323, "pd", lambda: pd), "concat"), [_n_(703325, "y_train", lambda: y_train), _n_(703326, "X_train", lambda: X_train)], axis = 1)
_l_(703328)
_c_(703331, _a_(703330, _n_(703329, "cars", lambda: cars), "head"))
_l_(703332)
model = _c_(703336, _a_(703334, _n_(703333, "smf", lambda: smf), "ols"), formula ='price ~ symboling + wheel-base + length + width + height + curb-weight + engine-size + bore + stroke + compression-ratio + horsepower + peak-rpm + city-mpg + highway-mpg + cylinder',data=_n_(703335, "cars", lambda: cars))
_l_(703337)
results = _c_(703340, _a_(703339, _n_(703338, "model", lambda: model), "fit"))
_l_(703341)
_c_(703346, _n_(703342, "print", lambda: print), _c_(703345, _a_(703344, _n_(703343, "results", lambda: results), "summary")))
_l_(703347)