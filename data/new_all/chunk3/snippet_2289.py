# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53189543/adamoptimizer-returns-invalid-datatype-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
cost = _c_(551296, _a_(551290, _n_(551289, "tf", lambda: tf), "reduce_mean"), _c_(551295, _a_(551292, _n_(551291, "tf", lambda: tf), "square"), _n_(551293, "y_true", lambda: y_true) - _n_(551294, "y_pred_cls", lambda: y_pred_cls)))
_l_(551297)
optimizer = _c_(551304, _a_(551302, _c_(551301, _a_(551300, _a_(551299, _n_(551298, "tf", lambda: tf), "train"), "AdamOptimizer"), learning_rate=1e-4), "minimize"), _n_(551303, "cost", lambda: cost))
_l_(551305)