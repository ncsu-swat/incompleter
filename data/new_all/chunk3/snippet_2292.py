# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53189543/adamoptimizer-returns-invalid-datatype-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
cost = _c_(578681, _a_(578675, _n_(578674, "tf", lambda: tf), "reduce_mean"), _c_(578680, _a_(578677, _n_(578676, "tf", lambda: tf), "square"), _n_(578678, "y_true", lambda: y_true) - _n_(578679, "y_pred_cls", lambda: y_pred_cls)))
_l_(578682)
optimizer = _c_(578689, _a_(578687, _c_(578686, _a_(578685, _a_(578684, _n_(578683, "tf", lambda: tf), "train"), "AdamOptimizer"), learning_rate=1e-4), "minimize"), _n_(578688, "cost", lambda: cost))
_l_(578690)