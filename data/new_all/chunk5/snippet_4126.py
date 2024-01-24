# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62590974/scikit-learn-pipeline-preprocessing-with-typeerror-not-supported-between-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.pipeline import make_pipeline, Pipeline
    _l_(702901)

except ImportError:
    pass
try:
    from mlxtend.preprocessing import DenseTransformer
    _l_(702903)

except ImportError:
    pass

numeric_features=_a_(702907, _c_(702906, _a_(702905, _n_(702904, "X", lambda: X), "select_dtypes"), include=['int64', 'float64']), "columns")
_l_(702908)
numeric_transformer=_c_(702914, _n_(702909, "Pipeline", lambda: Pipeline), steps=[
    ('imputer',_c_(702911, _n_(702910, "SimpleImputer", lambda: SimpleImputer), strategy='median')),
    ('scaler',_c_(702913, _n_(702912, "StandardScaler", lambda: StandardScaler)))])
_l_(702915)

categorical_features=_a_(702919, _c_(702918, _a_(702917, _n_(702916, "X", lambda: X), "select_dtypes"), include=['object']), "columns")
_l_(702920)
categorical_transformer=_c_(702928, _n_(702921, "Pipeline", lambda: Pipeline), steps=[
    ('imputer',_c_(702923, _n_(702922, "SimpleImputer", lambda: SimpleImputer), strategy='constant',fill_value='missing')),
    ('onehot',_c_(702925, _n_(702924, "OneHotEncoder", lambda: OneHotEncoder), handle_unknown='ignore')),
    ('to_dense', _c_(702927, _n_(702926, "DenseTransformer", lambda: DenseTransformer)))])
_l_(702929)

preprocessor=_c_(702935, _n_(702930, "ColumnTransformer", lambda: ColumnTransformer), transformers=[
    ('num',_n_(702931, "numeric_transformer", lambda: numeric_transformer),_n_(702932, "numeric_features", lambda: numeric_features)),
    ('cat',_n_(702933, "categorical_transformer", lambda: categorical_transformer),_n_(702934, "categorical_features", lambda: categorical_features))])
_l_(702936)
try:
    from sklearn.ensemble import RandomForestClassifier
    _l_(702938)

except ImportError:
    pass
rf = _c_(702943, _n_(702939, "Pipeline", lambda: Pipeline), steps=[('preprocessor', _n_(702940, "preprocessor", lambda: preprocessor)),
                      ('classifier', _c_(702942, _n_(702941, "RandomForestClassifier", lambda: RandomForestClassifier)))])
_l_(702944)
_c_(702949, _a_(702946, _n_(702945, "rf", lambda: rf), "fit"), _n_(702947, "X_train1", lambda: X_train1), _n_(702948, "Y_train1", lambda: Y_train1)) #--> this is when the error message points to
_l_(702950) #--> this is when the error message points to