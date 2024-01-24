# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53189543/adamoptimizer-returns-invalid-datatype-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x_p = _c_(531982, _a_(531977, _n_(531976, "tf", lambda: tf), "placeholder"), _a_(531979, _n_(531978, "tf", lambda: tf), "float32"), shape=[None, _n_(531980, "img_size_flat", lambda: img_size_flat)*_n_(531981, "num_channels", lambda: num_channels)], name='x_pred')
_l_(531983)
x_pred_image = _c_(531988, _a_(531985, _n_(531984, "tf", lambda: tf), "reshape"), _n_(531986, "x_p", lambda: x_p), [-1, 10, 10, _n_(531987, "num_channels", lambda: num_channels)])
_l_(531989)
k = _c_(531993, _a_(531991, _n_(531990, "tf", lambda: tf), "constant"), _n_(531992, "npatches", lambda: npatches))
_l_(531994)
y_true = _c_(531999, _a_(531996, _n_(531995, "tf", lambda: tf), "placeholder"), _a_(531998, _n_(531997, "tf", lambda: tf), "int32"), shape=[None, 2, 2], name='y_true')
_l_(532000)
y_true_cls = _c_(532005, _a_(532002, _n_(532001, "tf", lambda: tf), "placeholder"), _a_(532004, _n_(532003, "tf", lambda: tf), "int32"), shape=[None, 2, 2], name='y_true_cls')
_l_(532006)