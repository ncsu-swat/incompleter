# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70338776/typeerror-update-got-an-unexpected-keyword-argument-force
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
batch_size = 50
_l_(632283)
result = _c_(632291, _a_(632285, _n_(632284, "model", lambda: model), "fit"), _n_(632286, "X_train", lambda: X_train),
    _n_(632287, "Y_train", lambda: Y_train),
    validation_data=(_n_(632288, "X_test", lambda: X_test), _n_(632289, "Y_test", lambda: Y_test)),
    batch_size=_n_(632290, "batch_size", lambda: batch_size),
    epochs=5
)
_l_(632292)