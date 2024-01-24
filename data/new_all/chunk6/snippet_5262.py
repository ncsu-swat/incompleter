# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77465161/attributeerror-numpy-ndarray-object-has-no-attribute-columns-when-i-didn
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.base import BaseEstimator, TransformerMixin
    _l_(353918)

except ImportError:
    pass
try:
    from sklearn.preprocessing import OneHotEncoder
    _l_(353920)

except ImportError:
    pass
try:
    from sklearn.preprocessing import LabelEncoder
    _l_(353922)

except ImportError:
    pass
try:
    from sklearn.impute import SimpleImputer
    _l_(353924)

except ImportError:
    pass
try:
    from sklearn.pipeline import Pipeline
    _l_(353926)

except ImportError:
    pass

class Cleaner(_n_(353927, "BaseEstimator", lambda: BaseEstimator), _n_(353928, "TransformerMixin", lambda: TransformerMixin)):
    _l_(353939)

    def fit(self, X, y=None):
        _l_(353931)

        aux = _n_(353929, "self", lambda: self)
        _l_(353930)
        return aux
    def transform(self, X):
        _l_(353938)

        X = _c_(353934, _a_(353933, _n_(353932, "X", lambda: X), "drop"), ["Name", "PassengerId", "FoodCourt", "ShoppingMall", "Cabin"], axis=1)
        _l_(353935)
        aux = _n_(353936, "X", lambda: X)
        _l_(353937)
        return aux

class ObjectEncoder(_n_(353940, "BaseEstimator", lambda: BaseEstimator), _n_(353941, "TransformerMixin", lambda: TransformerMixin)):
    _l_(353987)

    def fit(self, X, y=None):
        _l_(353944)

        aux = _n_(353942, "self", lambda: self)
        _l_(353943)
        return aux
    def transform(self, X):
        _l_(353986)

        columns_to_encode = ["HomePlanet", "CryoSleep", "Destination", "VIP"]
        _l_(353945)
        encoder = _c_(353947, _n_(353946, "OneHotEncoder", lambda: OneHotEncoder))
        _l_(353948)
        
        # Encode each attribute and add the columns to the DataFrame
        for column in _n_(353949, "columns_to_encode", lambda: columns_to_encode):
            _l_(353979)

            matrix = _c_(353956, _a_(353955, _c_(353954, _a_(353951, _n_(353950, "encoder", lambda: encoder), "fit_transform"), _n_(353952, "X", lambda: X)[[_n_(353953, "column", lambda: column)]]), "toarray"))
            _l_(353957)
            column_names = [f"{_n_(353958, 'column', lambda: column)}_{_n_(353959, 'i', lambda: i)}" for i in _c_(353963, _n_(353960, "range", lambda: range), _a_(353962, _n_(353961, "matrix", lambda: matrix), "shape")[1])]
            _l_(353964)
        
            for i in _c_(353970, _n_(353965, "range", lambda: range), _c_(353969, _n_(353966, "len", lambda: len), _a_(353968, _n_(353967, "matrix", lambda: matrix), "T"))):
                _l_(353978)

                _n_(353971, "X", lambda: X)[_n_(353972, "column_names", lambda: column_names)[_n_(353973, "i", lambda: i)]] = _a_(353975, _n_(353974, "matrix", lambda: matrix), "T")[_n_(353976, "i", lambda: i)]
                _l_(353977)

        # Remove Old Parameters
        X = _c_(353982, _a_(353981, _n_(353980, "X", lambda: X), "drop"), ["HomePlanet", "CryoSleep", "Destination", "VIP"], axis=1)
        _l_(353983)
        aux = _n_(353984, "X", lambda: X)
        _l_(353985)

        return aux

class LabelYEncoder(_n_(353988, "BaseEstimator", lambda: BaseEstimator), _n_(353989, "TransformerMixin", lambda: TransformerMixin)):
    _l_(354004)

    def fit(self, X, y=None):
        _l_(353992)

        aux = _n_(353990, "self", lambda: self)
        _l_(353991)
        return aux
    def transform(self, X):
        _l_(354003)

        label_encoder = _c_(353994, _n_(353993, "LabelEncoder", lambda: LabelEncoder))
        _l_(353995)
        y_encoded = _c_(353999, _a_(353997, _n_(353996, "label_encoder", lambda: label_encoder), "fit_transform"), _n_(353998, "y", lambda: y))
        _l_(354000)
        aux = _n_(354001, "y_encoded", lambda: y_encoded)
        _l_(354002)
        return aux

class NullImputer(_n_(354005, "BaseEstimator", lambda: BaseEstimator), _n_(354006, "TransformerMixin", lambda: TransformerMixin)):
    _l_(354034)

    def fit(self, X, y=None):
        _l_(354009)

        aux = _n_(354007, "self", lambda: self)
        _l_(354008)
        return aux
    def transform(self, X):
        _l_(354033)

        features_with_missing_values = _c_(354018, _a_(354017, _a_(354011, _n_(354010, "X", lambda: X), "columns")[_c_(354016, _a_(354015, _c_(354014, _a_(354013, _n_(354012, "X", lambda: X), "isnull")), "any"))], "tolist"))
        _l_(354019)
        imputer = _c_(354021, _n_(354020, "SimpleImputer", lambda: SimpleImputer), strategy='median')
        _l_(354022)
        _n_(354023, "X", lambda: X)[_n_(354024, "features_with_missing_values", lambda: features_with_missing_values)] = _c_(354029, _a_(354026, _n_(354025, "imputer", lambda: imputer), "fit_transform"), _n_(354027, "X", lambda: X)[_n_(354028, "features_with_missing_values", lambda: features_with_missing_values)])
        _l_(354030)
        aux = _n_(354031, "X", lambda: X)
        _l_(354032)
        return aux

pipeline = _c_(354044, _n_(354035, "Pipeline", lambda: Pipeline), [
    ("cleaner", _c_(354037, _n_(354036, "Cleaner", lambda: Cleaner))),
    ("object_encoder", _c_(354039, _n_(354038, "ObjectEncoder", lambda: ObjectEncoder))),
    ("label_y_encoder", _c_(354041, _n_(354040, "LabelYEncoder", lambda: LabelYEncoder))),
    ("null_imputer", _c_(354043, _n_(354042, "NullImputer", lambda: NullImputer))),
])
_l_(354045)
X = _c_(354049, _a_(354047, _n_(354046, "pipeline", lambda: pipeline), "fit_transform"), _n_(354048, "strat_train_set", lambda: strat_train_set))
_l_(354050)