# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69653835/attribute-error-pickle-load-seldon-deployment
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.preprocessing import LabelEncoder
    _l_(442395)

except ImportError:
    pass
try:
    from sklearn.base import BaseEstimator, TransformerMixin
    _l_(442397)

except ImportError:
    pass
try:
    from sklearn.pipeline import Pipeline
    _l_(442399)

except ImportError:
    pass

class MyEncoder(_n_(442400, "BaseEstimator", lambda: BaseEstimator), _n_(442401, "TransformerMixin", lambda: TransformerMixin)):
    _l_(442438)

    def __init__(self):
        _l_(442406)

        _c_(442404, _a_(442403, _n_(442402, "super", lambda: super)(), "__init__"))
        _l_(442405)

    def fit(self, X, y=None):
        _l_(442409)

        aux = _n_(442407, "self", lambda: self)
        _l_(442408)
        return aux

    def transform(self, X, y=None):
        _l_(442437)

        df = _n_(442410, "X", lambda: X)
        _l_(442411)
        vars_cat = [_n_(442412, "var", lambda: var) for var in _a_(442414, _n_(442413, "df", lambda: df), "columns") if _a_(442417, _n_(442415, "df", lambda: df)[_n_(442416, "var", lambda: var)], "dtypes") == 'O']
        _l_(442418)
        cat_with_na = [_n_(442419, "var", lambda: var) for var in _n_(442420, "vars_cat", lambda: vars_cat) if _c_(442426, _a_(442425, _c_(442424, _a_(442423, _n_(442421, "df", lambda: df)[_n_(442422, "var", lambda: var)], "isnull")), "sum")) > 0]
        _l_(442427)
        _n_(442428, "df", lambda: df)[_n_(442429, "cat_with_na", lambda: cat_with_na)] = _c_(442433, _a_(442432, _n_(442430, "df", lambda: df)[_n_(442431, "cat_with_na", lambda: cat_with_na)], "fillna"), 'Missing')
        _l_(442434)
        aux = _n_(442435, "df", lambda: df)
        _l_(442436)

        return aux