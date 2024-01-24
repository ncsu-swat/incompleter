# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57585725/typeerror-init-got-an-unexpected-keyword-argument-param-distributions
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
grdHyperParams = {'loss' : ['deviance', 'exponential'],
                 'n_estimators': _c_(677114, _n_(677113, "randint", lambda: randint), 10, 500),
                 'max_depth': _c_(677116, _n_(677115, "randint", lambda: randint), 1,10)}
_l_(677117)

gridSearch_grd = _c_(677125, _a_(677122, _c_(677121, _n_(677118, "GridSearchCV", lambda: GridSearchCV), estimator=_n_(677119, "grd", lambda: grd), param_distributions=_n_(677120, "grdHyperParams", lambda: grdHyperParams), n_iter=10, scoring='roc_auc',fit_params=None, cv=None, 
verbose=2), "fit"), _n_(677123, "X3_train", lambda: X3_train), _n_(677124, "y_train", lambda: y_train))
_l_(677126)