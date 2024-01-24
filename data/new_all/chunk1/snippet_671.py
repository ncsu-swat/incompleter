# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59613693/attributeerror-mpoimagefile-object-has-no-attribute-shape
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
images, labels = _c_(397749, _n_(397744, "next", lambda: next), _c_(397748, _n_(397745, "iter", lambda: iter), _a_(397747, _n_(397746, "self", lambda: self), "loader")))
_l_(397750)
grid = _c_(397755, _a_(397753, _a_(397752, _n_(397751, "torchvision", lambda: torchvision), "utils"), "make_grid"), _n_(397754, "images", lambda: images))
_l_(397756)