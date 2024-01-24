# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49775365/typeerror-only-integer-scalar-arrays-can-be-converted-to-a-scalar-index-while-i
# coding=utf-8


from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(395815)

except ImportError:
    pass
try:
    import numpy as np
    _l_(395817)

except ImportError:
    pass
try:
    from scipy.stats import skew
    _l_(395819)

except ImportError:
    pass
try:
    import xgboost as xgb
    _l_(395821)

except ImportError:
    pass
try:
    from sklearn.cross_validation import KFold
    _l_(395823)

except ImportError:
    pass
try:
    from sklearn.ensemble import ExtraTreesRegressor
    _l_(395825)

except ImportError:
    pass
try:
    from sklearn.ensemble import RandomForestRegressor
    _l_(395827)

except ImportError:
    pass
try:
    from sklearn.metrics import mean_squared_error
    _l_(395829)

except ImportError:
    pass
try:
    from sklearn.linear_model import Ridge, RidgeCV, ElasticNet, LassoCV, Lasso
    _l_(395831)

except ImportError:
    pass
try:
    from math import sqrt
    _l_(395833)

except ImportError:
    pass

NTRAIN = 100
_l_(395834)
NTEST = 0
_l_(395835)
X_train = []
_l_(395836)
Y_train = []
_l_(395837)
X_test = []
_l_(395838)
NFOLDS = 3
_l_(395839)
SEED = 0
_l_(395840)
kf = _c_(395845, _n_(395841, "KFold", lambda: KFold), _n_(395842, "NTRAIN", lambda: NTRAIN), n_folds=_n_(395843, "NFOLDS", lambda: NFOLDS), shuffle=True, random_state=_n_(395844, "SEED", lambda: SEED))
_l_(395846)


class SklearnWrapper(_n_(395847, "object", lambda: object)):
    _l_(395872)

    def __init__(self, clf, seed=0, params=None):
        _l_(395856)

        _n_(395848, "params", lambda: params)['random_state'] = _n_(395849, "seed", lambda: seed)
        _l_(395850)
        _n_(395851, "self", lambda: self).clf = _c_(395854, _n_(395852, "clf", lambda: clf), **_n_(395853, "params", lambda: params))
        _l_(395855)

    def train(self, x_train, y_train):
        _l_(395864)

        _c_(395862, _a_(395859, _a_(395858, _n_(395857, "self", lambda: self), "clf"), "fit"), _n_(395860, "x_train", lambda: x_train), _n_(395861, "y_train", lambda: y_train))
        _l_(395863)

    def predict(self, x):
        _l_(395871)

        aux = _c_(395869, _a_(395867, _a_(395866, _n_(395865, "self", lambda: self), "clf"), "predict"), _n_(395868, "x", lambda: x))
        _l_(395870)
        return aux


class XgbWrapper(_n_(395873, "object", lambda: object)):
    _l_(395914)

    def __init__(self, seed=0, params=None):
        _l_(395886)

        _n_(395874, "self", lambda: self).param = _n_(395875, "params", lambda: params)
        _l_(395876)
        _a_(395878, _n_(395877, "self", lambda: self), "param")['seed'] = _n_(395879, "seed", lambda: seed)
        _l_(395880)
        _n_(395881, "self", lambda: self).nrounds = _c_(395884, _a_(395883, _n_(395882, "params", lambda: params), "pop"), 'nrounds', 250)
        _l_(395885)

    def train(self, x_train, y_train):
        _l_(395903)

        dtrain = _c_(395891, _a_(395888, _n_(395887, "xgb", lambda: xgb), "DMatrix"), _n_(395889, "x_train", lambda: x_train), label=_n_(395890, "y_train", lambda: y_train))
        _l_(395892)
        _n_(395893, "self", lambda: self).gbdt = _c_(395901, _a_(395895, _n_(395894, "xgb", lambda: xgb), "train"), _a_(395897, _n_(395896, "self", lambda: self), "param"), _n_(395898, "dtrain", lambda: dtrain), _a_(395900, _n_(395899, "self", lambda: self), "nrounds"))
        _l_(395902)

    def predict(self, x):
        _l_(395913)

        aux = _c_(395911, _a_(395906, _a_(395905, _n_(395904, "self", lambda: self), "gbdt"), "predict"), _c_(395910, _a_(395908, _n_(395907, "xgb", lambda: xgb), "DMatrix"), _n_(395909, "x", lambda: x)))
        _l_(395912)
        return aux


def get_oof(clf):
    _l_(395981)

    oof_train = _c_(395918, _a_(395916, _n_(395915, "np", lambda: np), "zeros"), (_n_(395917, "NTRAIN", lambda: NTRAIN),))
    _l_(395919)
    oof_test = _c_(395923, _a_(395921, _n_(395920, "np", lambda: np), "zeros"), (_n_(395922, "NTEST", lambda: NTEST),))
    _l_(395924)
    oof_test_skf = _c_(395929, _a_(395926, _n_(395925, "np", lambda: np), "empty"), (_n_(395927, "NFOLDS", lambda: NFOLDS), _n_(395928, "NTEST", lambda: NTEST)))
    _l_(395930)

    for i, (train_index, test_index) in _c_(395933, _n_(395931, "enumerate", lambda: enumerate), _n_(395932, "kf", lambda: kf)):
        _l_(395968)

        _c_(395937, _n_(395934, "print", lambda: print), "TRAIN:", _n_(395935, "train_index", lambda: train_index), "TEST:", _n_(395936, "test_index", lambda: test_index))
        _l_(395938)

        x_tr = _n_(395939, "X_train", lambda: X_train)[_n_(395940, "train_index", lambda: train_index)]
        _l_(395941)
        y_tr = _n_(395942, "Y_train", lambda: Y_train)[_n_(395943, "train_index", lambda: train_index)]
        _l_(395944)
        x_te = _n_(395945, "X_train", lambda: X_train)[_n_(395946, "test_index", lambda: test_index)]
        _l_(395947)

        _c_(395952, _a_(395949, _n_(395948, "clf", lambda: clf), "train"), _n_(395950, "x_tr", lambda: x_tr), _n_(395951, "y_tr", lambda: y_tr))
        _l_(395953)

        _n_(395954, "oof_train", lambda: oof_train)[_n_(395955, "test_index", lambda: test_index)] = _c_(395959, _a_(395957, _n_(395956, "clf", lambda: clf), "predict"), _n_(395958, "x_te", lambda: x_te))
        _l_(395960)
        _n_(395961, "oof_test_skf", lambda: oof_test_skf)[_n_(395962, "i", lambda: i), :] = _c_(395966, _a_(395964, _n_(395963, "clf", lambda: clf), "predict"), _n_(395965, "X_test", lambda: X_test))
        _l_(395967)

    _n_(395969, "oof_test", lambda: oof_test)[:] = _c_(395972, _a_(395971, _n_(395970, "oof_test_skf", lambda: oof_test_skf), "mean"), axis=0)
    _l_(395973)
    aux = _c_(395976, _a_(395975, _n_(395974, "oof_train", lambda: oof_train), "reshape"), -1, 1), _c_(395979, _a_(395978, _n_(395977, "oof_test", lambda: oof_test), "reshape"), -1, 1)
    _l_(395980)
    return aux


def stacking(nfolds, seed, et_params, rf_params, xgb_params, rd_params, ls_params, x_train, y_train, x_test):
    _l_(396181)

    NTRAIN = _a_(395983, _n_(395982, "x_train", lambda: x_train), "shape")[0]
    _l_(395984)
    NTEST = _c_(395987, _n_(395985, "len", lambda: len), _n_(395986, "x_test", lambda: x_test))
    _l_(395988)
    NFOLDS = _n_(395989, "nfolds", lambda: nfolds)
    _l_(395990)
    SEED = _n_(395991, "seed", lambda: seed)
    _l_(395992)
    X_train = _n_(395993, "x_train", lambda: x_train)
    _l_(395994)
    Y_train = _n_(395995, "y_train", lambda: y_train)
    _l_(395996)
    X_test = _n_(395997, "x_test", lambda: x_test)
    _l_(395998)

    kf = _c_(396003, _n_(395999, "KFold", lambda: KFold), _n_(396000, "NTRAIN", lambda: NTRAIN), n_folds=_n_(396001, "NFOLDS", lambda: NFOLDS), shuffle=True, random_state=_n_(396002, "SEED", lambda: SEED))
    _l_(396004)

    xg = _c_(396008, _n_(396005, "XgbWrapper", lambda: XgbWrapper), seed=_n_(396006, "SEED", lambda: SEED), params=_n_(396007, "xgb_params", lambda: xgb_params))
    _l_(396009)
    et = _c_(396014, _n_(396010, "SklearnWrapper", lambda: SklearnWrapper), clf=_n_(396011, "ExtraTreesRegressor", lambda: ExtraTreesRegressor), seed=_n_(396012, "SEED", lambda: SEED), params=_n_(396013, "et_params", lambda: et_params))
    _l_(396015)
    rf = _c_(396020, _n_(396016, "SklearnWrapper", lambda: SklearnWrapper), clf=_n_(396017, "RandomForestRegressor", lambda: RandomForestRegressor), seed=_n_(396018, "SEED", lambda: SEED), params=_n_(396019, "rf_params", lambda: rf_params))
    _l_(396021)
    rd = _c_(396026, _n_(396022, "SklearnWrapper", lambda: SklearnWrapper), clf=_n_(396023, "Ridge", lambda: Ridge), seed=_n_(396024, "SEED", lambda: SEED), params=_n_(396025, "rd_params", lambda: rd_params))
    _l_(396027)
    ls = _c_(396032, _n_(396028, "SklearnWrapper", lambda: SklearnWrapper), clf=_n_(396029, "Lasso", lambda: Lasso), seed=_n_(396030, "SEED", lambda: SEED), params=_n_(396031, "ls_params", lambda: ls_params))
    _l_(396033)

    xg_oof_train, xg_oof_test = _c_(396036, _n_(396034, "get_oof", lambda: get_oof), _n_(396035, "xg", lambda: xg))
    _l_(396037)
    et_oof_train, et_oof_test = _c_(396040, _n_(396038, "get_oof", lambda: get_oof), _n_(396039, "et", lambda: et))
    _l_(396041)
    rf_oof_train, rf_oof_test = _c_(396044, _n_(396042, "get_oof", lambda: get_oof), _n_(396043, "rf", lambda: rf))
    _l_(396045)
    rd_oof_train, rd_oof_test = _c_(396048, _n_(396046, "get_oof", lambda: get_oof), _n_(396047, "rd", lambda: rd))
    _l_(396049)
    ls_oof_train, ls_oof_test = _c_(396052, _n_(396050, "get_oof", lambda: get_oof), _n_(396051, "ls", lambda: ls))
    _l_(396053)

    _c_(396063, _n_(396054, "print", lambda: print), _c_(396062, _a_(396055, "XG-CV: {}", "format"), _c_(396061, _n_(396056, "sqrt", lambda: sqrt), _c_(396060, _n_(396057, "mean_squared_error", lambda: mean_squared_error), _n_(396058, "Y_train", lambda: Y_train), _n_(396059, "xg_oof_train", lambda: xg_oof_train)))))
    _l_(396064)
    _c_(396074, _n_(396065, "print", lambda: print), _c_(396073, _a_(396066, "ET-CV: {}", "format"), _c_(396072, _n_(396067, "sqrt", lambda: sqrt), _c_(396071, _n_(396068, "mean_squared_error", lambda: mean_squared_error), _n_(396069, "Y_train", lambda: Y_train), _n_(396070, "et_oof_train", lambda: et_oof_train)))))
    _l_(396075)
    _c_(396085, _n_(396076, "print", lambda: print), _c_(396084, _a_(396077, "RF-CV: {}", "format"), _c_(396083, _n_(396078, "sqrt", lambda: sqrt), _c_(396082, _n_(396079, "mean_squared_error", lambda: mean_squared_error), _n_(396080, "Y_train", lambda: Y_train), _n_(396081, "rf_oof_train", lambda: rf_oof_train)))))
    _l_(396086)
    _c_(396096, _n_(396087, "print", lambda: print), _c_(396095, _a_(396088, "RD-CV: {}", "format"), _c_(396094, _n_(396089, "sqrt", lambda: sqrt), _c_(396093, _n_(396090, "mean_squared_error", lambda: mean_squared_error), _n_(396091, "Y_train", lambda: Y_train), _n_(396092, "rd_oof_train", lambda: rd_oof_train)))))
    _l_(396097)
    _c_(396107, _n_(396098, "print", lambda: print), _c_(396106, _a_(396099, "LS-CV: {}", "format"), _c_(396105, _n_(396100, "sqrt", lambda: sqrt), _c_(396104, _n_(396101, "mean_squared_error", lambda: mean_squared_error), _n_(396102, "Y_train", lambda: Y_train), _n_(396103, "ls_oof_train", lambda: ls_oof_train)))))
    _l_(396108)

    dtrain = _c_(396113, _a_(396110, _n_(396109, "xgb", lambda: xgb), "DMatrix"), _n_(396111, "X_train", lambda: X_train), label=_n_(396112, "Y_train", lambda: Y_train))
    _l_(396114)
    dtest = _c_(396118, _a_(396116, _n_(396115, "xgb", lambda: xgb), "DMatrix"), _n_(396117, "X_test", lambda: X_test))
    _l_(396119)

    res = _c_(396125, _a_(396121, _n_(396120, "xgb", lambda: xgb), "cv"), _n_(396122, "xgb_params", lambda: xgb_params), _n_(396123, "dtrain", lambda: dtrain), num_boost_round=1000, nfold=4, seed=_n_(396124, "SEED", lambda: SEED), stratified=False,
                 early_stopping_rounds=25, verbose_eval=10, show_stdv=True)
    _l_(396126)

    best_nrounds = _a_(396128, _n_(396127, "res", lambda: res), "shape")[0] - 1
    _l_(396129)
    cv_mean = _a_(396131, _n_(396130, "res", lambda: res), "iloc")[-1, 0]
    _l_(396132)
    cv_std = _a_(396134, _n_(396133, "res", lambda: res), "iloc")[-1, 1]
    _l_(396135)

    _c_(396141, _n_(396136, "print", lambda: print), _c_(396140, _a_(396137, 'Ensemble-CV: {0}+{1}', "format"), _n_(396138, "cv_mean", lambda: cv_mean), _n_(396139, "cv_std", lambda: cv_std)))
    _l_(396142)

    gbdt = _c_(396148, _a_(396144, _n_(396143, "xgb", lambda: xgb), "train"), _n_(396145, "xgb_params", lambda: xgb_params), _n_(396146, "dtrain", lambda: dtrain), _n_(396147, "best_nrounds", lambda: best_nrounds))
    _l_(396149)
    submission = _c_(396152, _a_(396151, _n_(396150, "pd", lambda: pd), "read_csv"), "../house_price/data/submission_xgboosting2.csv")
    _l_(396153)
    _a_(396155, _n_(396154, "submission", lambda: submission), "iloc")[:, 1] = _c_(396159, _a_(396157, _n_(396156, "gbdt", lambda: gbdt), "predict"), _n_(396158, "dtest", lambda: dtest))
    _l_(396160)
    _c_(396163, _n_(396161, "print", lambda: print), _n_(396162, "submission", lambda: submission)['SalePrice'])
    _l_(396164)
    saleprice = _c_(396168, _a_(396166, _n_(396165, "np", lambda: np), "exp"), _n_(396167, "submission", lambda: submission)['SalePrice']) - 1
    _l_(396169)
    _c_(396172, _n_(396170, "print", lambda: print), _n_(396171, "saleprice", lambda: saleprice))
    _l_(396173)
    _n_(396174, "submission", lambda: submission)['SalePrice'] = _n_(396175, "saleprice", lambda: saleprice)
    _l_(396176)
    _c_(396179, _a_(396178, _n_(396177, "submission", lambda: submission), "to_csv"), 'xgstacker_starter.sub.csv', index=None)
    _l_(396180)