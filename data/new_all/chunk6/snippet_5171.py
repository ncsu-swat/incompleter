# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68197818/typeerror-all-intermediate-steps-should-be-transformers-and-implement-fit-and-t
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.pipeline import Pipeline
    _l_(355165)

except ImportError:
    pass
try:
    from sklearn.preprocessing import StandardScaler
    _l_(355167)

except ImportError:
    pass
try:
    from imblearn.pipeline import make_pipeline
    _l_(355169)

except ImportError:
    pass
num_pipline = _c_(355179, _n_(355170, "Pipeline", lambda: Pipeline), [
    ('imputer', _c_(355174, _n_(355171, "SimpleImputer", lambda: SimpleImputer), missing_values=_a_(355173, _n_(355172, "np", lambda: np), "nan"), strategy='median')),
    ('attribs_adder', _c_(355176, _n_(355175, "CombineAttributesAdder", lambda: CombineAttributesAdder), add_bedrooms_per_room=False)),
    ('stand_scaler', _c_(355178, _n_(355177, "StandardScaler", lambda: StandardScaler))),
])
_l_(355180)
housing_num_transform = _c_(355184, _a_(355182, _n_(355181, "num_pipline", lambda: num_pipline), "fit_transform"), _n_(355183, "housing_num", lambda: housing_num))
_l_(355185)