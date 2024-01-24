# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62590974/scikit-learn-pipeline-preprocessing-with-typeerror-not-supported-between-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.pipeline import make_pipeline, Pipeline
    _l_(647838)

except ImportError:
    pass
try:
    from mlxtend.preprocessing import DenseTransformer
    _l_(647840)

except ImportError:
    pass

numeric_features=_a_(647844, _c_(647843, _a_(647842, _n_(647841, "X", lambda: X), "select_dtypes"), include=['int64', 'float64']), "columns")
_l_(647845)
numeric_transformer=_c_(647851, _n_(647846, "Pipeline", lambda: Pipeline), steps=[
    ('imputer',_c_(647848, _n_(647847, "SimpleImputer", lambda: SimpleImputer), strategy='median')),
    ('scaler',_c_(647850, _n_(647849, "StandardScaler", lambda: StandardScaler)))])
_l_(647852)

categorical_features=_a_(647856, _c_(647855, _a_(647854, _n_(647853, "X", lambda: X), "select_dtypes"), include=['object']), "columns")
_l_(647857)
categorical_transformer=_c_(647865, _n_(647858, "Pipeline", lambda: Pipeline), steps=[
    ('imputer',_c_(647860, _n_(647859, "SimpleImputer", lambda: SimpleImputer), strategy='constant',fill_value='missing')),
    ('onehot',_c_(647862, _n_(647861, "OneHotEncoder", lambda: OneHotEncoder), handle_unknown='ignore')),
    ('to_dense', _c_(647864, _n_(647863, "DenseTransformer", lambda: DenseTransformer)))])
_l_(647866)

preprocessor=_c_(647872, _n_(647867, "ColumnTransformer", lambda: ColumnTransformer), transformers=[
    ('num',_n_(647868, "numeric_transformer", lambda: numeric_transformer),_n_(647869, "numeric_features", lambda: numeric_features)),
    ('cat',_n_(647870, "categorical_transformer", lambda: categorical_transformer),_n_(647871, "categorical_features", lambda: categorical_features))])
_l_(647873)
try:
    from sklearn.ensemble import RandomForestClassifier
    _l_(647875)

except ImportError:
    pass
rf = _c_(647880, _n_(647876, "Pipeline", lambda: Pipeline), steps=[('preprocessor', _n_(647877, "preprocessor", lambda: preprocessor)),
                      ('classifier', _c_(647879, _n_(647878, "RandomForestClassifier", lambda: RandomForestClassifier)))])
_l_(647881)
_c_(647886, _a_(647883, _n_(647882, "rf", lambda: rf), "fit"), _n_(647884, "X_train1", lambda: X_train1), _n_(647885, "Y_train1", lambda: Y_train1)) #--> this is when the error message points to
_l_(647887) #--> this is when the error message points to