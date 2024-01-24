# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36065646/xgboost-attributeerror-dmatrix-object-has-no-attribute-handle
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(377262)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(377264)

except ImportError:
    pass
try:
    import xgboost as xgb
    _l_(377266)

except ImportError:
    pass
try:
    from sklearn.cross_validation import train_test_split
    _l_(377268)

except ImportError:
    pass

# # Split the Learning Set
X_fit, X_eval, y_fit, y_eval= _c_(377272, _n_(377269, "train_test_split", lambda: train_test_split), _n_(377270, "train", lambda: train), _n_(377271, "target", lambda: target), test_size=0.2, random_state=1
)
_l_(377273)

clf = _c_(377278, _a_(377275, _n_(377274, "xgb", lambda: xgb), "XGBClassifier"), missing=_a_(377277, _n_(377276, "np", lambda: np), "nan"), max_depth=6, 
                        n_estimators=5, learning_rate=0.15, 
                        subsample=1, colsample_bytree=0.9, seed=1400)
_l_(377279)

# fitting
_c_(377286, _a_(377281, _n_(377280, "clf", lambda: clf), "fit"), _n_(377282, "X_fit", lambda: X_fit), _n_(377283, "y_fit", lambda: y_fit), early_stopping_rounds=50, eval_metric="logloss", eval_set=[(_n_(377284, "X_eval", lambda: X_eval), _n_(377285, "y_eval", lambda: y_eval))])
_l_(377287)
#print y_pred
y_pred= _c_(377291, _a_(377289, _n_(377288, "clf", lambda: clf), "predict_proba"), _n_(377290, "test", lambda: test))[:,1]
_l_(377292)