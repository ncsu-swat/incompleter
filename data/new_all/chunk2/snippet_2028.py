# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68429511/attributeerror-list-object-has-no-attribute-reshape-when-using-reshape-for
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
w_train, w_test, y_train, y_test =_c_(454627, _n_(454624, "train_test_split", lambda: train_test_split), _n_(454625, "w", lambda: w), _n_(454626, "y", lambda: y), test_size=0.2 ,shuffle=True, random_state=42)
_l_(454628)

w_train = _c_(454631, _a_(454630, _n_(454629, "w_train", lambda: w_train), "reshape"), 2404,28,224,224,3)
_l_(454632)
w_test = _c_(454635, _a_(454634, _n_(454633, "w_test", lambda: w_test), "reshape"), 601,28,224,224,3)
_l_(454636)