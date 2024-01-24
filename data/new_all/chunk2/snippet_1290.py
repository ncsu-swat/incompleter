# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55312601/attribute-error-module-lightgbm-has-no-attribute-lgbmclassifier-and-datas
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import lightgbm as gbm
    _l_(444797)

except ImportError:
    pass

d_train=_c_(444802, _a_(444799, _n_(444798, "gbm", lambda: gbm), "Dataset"), _n_(444800, "train_x", lambda: train_x),label=_n_(444801, "train_y", lambda: train_y))
_l_(444803)