# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74009860/how-do-i-fix-nameerror-in-python-i-defined-a-variable-in-a-for-loop-and-when-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
lc = [_n_(644348, "data", lambda: data)['time'], _n_(644349, "data", lambda: data)['magnitude'], _n_(644350, "data", lambda: data)['error']]
_l_(644351)

fs = _c_(644354, _a_(644353, _n_(644352, "fts", lambda: fts), "FeatureSpace"), data = ['time', 'magnitude', 'error'])
_l_(644355)
features, values = _c_(644359, _a_(644357, _n_(644356, "fs", lambda: fs), "extract"), *_n_(644358, "lc", lambda: lc))
_l_(644360)

t = _c_(644365, _a_(644362, _n_(644361, "pd", lambda: pd), "DataFrame"), _n_(644363, "features", lambda: features), _n_(644364, "values", lambda: values))
_l_(644366)
_c_(644369, _n_(644367, "print", lambda: print), _n_(644368, "t", lambda: t))
_l_(644370)