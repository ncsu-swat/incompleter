# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46842196/attributeerror-module-object-has-no-attribute-xgbclassifier-on-anaconda
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
cv_params = {'max_depth': [3,5,7], 'min_child_weight': [1,3,5]}
_l_(449008)
ind_params = {'learning_rate': 0.1, 'n_estimators': 1000, 'seed':0, 'subsample': 0.8, 'colsample_bytree': 0.8, 
             'objective': 'binary:logistic'}
_l_(449009)
optimized_GBM = _c_(449016, _n_(449010, "GridSearchCV", lambda: GridSearchCV), _c_(449014, _a_(449012, _n_(449011, "xgb", lambda: xgb), "XGBClassifier"), **_n_(449013, "ind_params", lambda: ind_params)), 
                            _n_(449015, "cv_params", lambda: cv_params), 
                             scoring = 'accuracy', cv = 5, n_jobs = -1) 
_l_(449017) 