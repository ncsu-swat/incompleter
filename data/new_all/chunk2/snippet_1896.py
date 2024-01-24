# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41949567/getting-ggplot-python-error-nameerror-name-stat-function-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from ggplot import *
    _l_(469011)

except ImportError:
    pass

_c_(469016, _n_(469012, "ggplot", lambda: ggplot), _n_(469013, "counts", lambda: counts), _c_(469015, _n_(469014, "aes", lambda: aes), x='pred_prob',y='true_prob',size='count')) + \
    _c_(469018, _n_(469017, "geom_point", lambda: geom_point), color='blue') + \
    _c_(469021, _n_(469019, "stat_function", lambda: stat_function), fun=lambda x: _n_(469020, "x", lambda: x), color='red') + \
    _c_(469023, _n_(469022, "xlim", lambda: xlim), -0.05,  1.05) + _c_(469025, _n_(469024, "ylim", lambda: ylim), -0.05,1.05) 
_l_(469026) 