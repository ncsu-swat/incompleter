# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59729859/python-typeerror-only-integer-scalar-arrays-can-be-converted-to-a-scalar-index
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
train_size = 3 # x_train.shape[0]
_l_(464625) # x_train.shape[0]
batch_size = 22
_l_(464626)
for i in _c_(464628, _n_(464627, "range", lambda: range), 242):
   _l_(464647)

   batch_mask = _c_(464634, _a_(464631, _a_(464630, _n_(464629, "np", lambda: np), "random"), "choice"), _n_(464632, "train_size", lambda: train_size), _n_(464633, "batch_size", lambda: batch_size))
   _l_(464635)
   _c_(464639, _n_(464636, "print", lambda: print), _n_(464637, "t_train", lambda: t_train), _n_(464638, "batch_mask", lambda: batch_mask) )
   _l_(464640)
   x_batch = _n_(464641, "x_train", lambda: x_train)[_n_(464642, "batch_mask", lambda: batch_mask)]
   _l_(464643)
   t_batch = _n_(464644, "t_label", lambda: t_label)[_n_(464645, "batch_mask", lambda: batch_mask)]
   _l_(464646)