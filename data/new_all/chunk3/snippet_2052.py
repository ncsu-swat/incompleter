# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66497772/attributeerror-home-hp-anaconda3-lib-libxgboost-so-undefined-symbol-xgdmatri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
clf = _c_(568808, _a_(568805, _c_(568804, _n_(568799, "GridSearchCV", lambda: GridSearchCV), estimator=_c_(568802, _a_(568801, _n_(568800, "xgb", lambda: xgb), "XGBClassifier"), use_label_encoder =False), param_grid=_n_(568803, "params", lambda: params), scoring = 'accuracy', cv=20), "fit"), _n_(568806, "data_train", lambda: data_train), _n_(568807, "label_train", lambda: label_train))
_l_(568809)