# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64833301/typeerror-precision-score-got-an-unexpected-keyword-argument-y-pred
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(630607, _n_(630601, "print", lambda: print), "accuracy:", _c_(630606, _a_(630603, _n_(630602, "metrics", lambda: metrics), "accuracy_score"), _n_(630604, "Y_test", lambda: Y_test), Y_pred = _n_(630605, "pred", lambda: pred)))
_l_(630608)

_c_(630615, _n_(630609, "print", lambda: print), "precision:", _c_(630614, _a_(630611, _n_(630610, "metrics", lambda: metrics), "precision_score"), _n_(630612, "Y_test", lambda: Y_test), Y_pred = _n_(630613, "pred", lambda: pred)))
_l_(630616)

_c_(630623, _n_(630617, "print", lambda: print), "recall:", _c_(630622, _a_(630619, _n_(630618, "metrics", lambda: metrics), "precision_score"), _n_(630620, "Y_test", lambda: Y_test), Y_pred = _n_(630621, "pred", lambda: pred)))
_l_(630624)

_c_(630631, _n_(630625, "print", lambda: print), _c_(630630, _a_(630627, _n_(630626, "metrics", lambda: metrics), "classification_report"), _n_(630628, "Y_test", lambda: Y_test), Y_pred = _n_(630629, "pred", lambda: pred)))
_l_(630632)