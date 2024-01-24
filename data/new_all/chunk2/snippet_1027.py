# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52989405/attributeerror-when-scoring-sklearn-pipeline-with-custom-transformer-subclass-bu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.datasets import make_regression
    _l_(448787)

except ImportError:
    pass
try:
    from sklearn.base import TransformerMixin, BaseEstimator
    _l_(448789)

except ImportError:
    pass
try:
    from sklearn.linear_model import LinearRegression
    _l_(448791)

except ImportError:
    pass
try:
    from sklearn.pipeline import Pipeline
    _l_(448793)

except ImportError:
    pass

X, y = _c_(448795, _n_(448794, "make_regression", lambda: make_regression)) #Just some dummy regression data for demonstrative purposes.
_l_(448796) #Just some dummy regression data for demonstrative purposes.

class BaseTransformer(_n_(448797, "TransformerMixin", lambda: TransformerMixin), _n_(448798, "BaseEstimator", lambda: BaseEstimator)):
    _l_(448809)


    def __init__(self):
        _l_(448802)

        _c_(448800, _n_(448799, "print", lambda: print), "Base Init")
        _l_(448801)

    def fit(self, X, y = None):
        _l_(448805)

        aux = _n_(448803, "self", lambda: self)
        _l_(448804)
        return aux

    def transform(self, X):
        _l_(448808)

        aux = _n_(448806, "X", lambda: X)
        _l_(448807)
        return aux

class DerivedTransformer(_n_(448810, "BaseTransformer", lambda: BaseTransformer)):
    _l_(448846)


    def __init__(self):
        _l_(448820)

        _c_(448815, _a_(448814, _n_(448811, "super", lambda: super)(_n_(448812, "DerivedTransformer", lambda: DerivedTransformer), _n_(448813, "self", lambda: self)), "__init__"))
        _l_(448816)
        _c_(448818, _n_(448817, "print", lambda: print), "Dervied init")
        _l_(448819)

    def fit(self, X, y = None):
        _l_(448833)

        _c_(448827, _a_(448824, _n_(448821, "super", lambda: super)(_n_(448822, "DerivedTransformer", lambda: DerivedTransformer), _n_(448823, "self", lambda: self)), "fit"), _n_(448825, "X", lambda: X), _n_(448826, "y", lambda: y))
        _l_(448828)
        _n_(448829, "self", lambda: self).new_attribute = 0.0001
        _l_(448830)
        aux = _n_(448831, "self", lambda: self)
        _l_(448832)
        return aux

    def transform(self, X):
        _l_(448845)

        output = _c_(448839, _a_(448837, _n_(448834, "super", lambda: super)(_n_(448835, "DerivedTransformer", lambda: DerivedTransformer), _n_(448836, "self", lambda: self)), "transform"), _n_(448838, "X", lambda: X))
        _l_(448840)
        output += _n_(448841, "self", lambda: self).new_attribute
        _l_(448842)
        aux = _n_(448843, "output", lambda: output)
        _l_(448844)

        return aux

base_pipeline = _c_(448852, _n_(448847, "Pipeline", lambda: Pipeline), [('base_transformer', _c_(448849, _n_(448848, "BaseTransformer", lambda: BaseTransformer))),
              ('linear_regressor', _c_(448851, _n_(448850, "LinearRegression", lambda: LinearRegression)))])
_l_(448853)

derived_pipeline = _c_(448859, _n_(448854, "Pipeline", lambda: Pipeline), [('derived_transformer', _c_(448856, _n_(448855, "DerivedTransformer", lambda: DerivedTransformer))),
              ('linear_regressor', _c_(448858, _n_(448857, "LinearRegression", lambda: LinearRegression)))])
_l_(448860)