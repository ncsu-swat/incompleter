# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64833301/typeerror-precision-score-got-an-unexpected-keyword-argument-y-pred
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(586041, _n_(586035, "print", lambda: print), "accuracy:", _c_(586040, _a_(586037, _n_(586036, "metrics", lambda: metrics), "accuracy_score"), _n_(586038, "Y_test", lambda: Y_test), Y_pred = _n_(586039, "pred", lambda: pred)))
_l_(586042)

_c_(586049, _n_(586043, "print", lambda: print), "precision:", _c_(586048, _a_(586045, _n_(586044, "metrics", lambda: metrics), "precision_score"), _n_(586046, "Y_test", lambda: Y_test), Y_pred = _n_(586047, "pred", lambda: pred)))
_l_(586050)

_c_(586057, _n_(586051, "print", lambda: print), "recall:", _c_(586056, _a_(586053, _n_(586052, "metrics", lambda: metrics), "precision_score"), _n_(586054, "Y_test", lambda: Y_test), Y_pred = _n_(586055, "pred", lambda: pred)))
_l_(586058)

_c_(586065, _n_(586059, "print", lambda: print), _c_(586064, _a_(586061, _n_(586060, "metrics", lambda: metrics), "classification_report"), _n_(586062, "Y_test", lambda: Y_test), Y_pred = _n_(586063, "pred", lambda: pred)))
_l_(586066)