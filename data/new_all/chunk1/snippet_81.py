# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60786220/attributeerror-gridsearchcv-object-has-no-attribute-best-params
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.model_selection import GridSearchCV
    _l_(418695)

except ImportError:
    pass
# Create the parameter grid based on the results of random search 
param_grid = {
    'bootstrap': [True],'max_depth': [20,30,40, 100, 110],
    'max_features': ['sqrt'],'min_samples_leaf': [5,10,15],
    'min_samples_split': [40,50,60], 'n_estimators': [150, 200, 250]
}
_l_(418696)
# Create a based model
rf = _c_(418698, _n_(418697, "RandomForestClassifier", lambda: RandomForestClassifier))
_l_(418699)
# Instantiate the grid search model
grid_search = _c_(418703, _n_(418700, "GridSearchCV", lambda: GridSearchCV), estimator = _n_(418701, "rf", lambda: rf), param_grid = _n_(418702, "param_grid", lambda: param_grid), 
                          cv = 3, n_jobs = -1, verbose = 2)
_l_(418704)