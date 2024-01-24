# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55657849/typeerror-trying-to-split-data-randomly-in-training-and-test-set
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(658791)

except ImportError:
    pass

segment_relative_path = ["a", "b", "c", "d", "e", "f"]
_l_(658792)
idx = _c_(658799, _a_(658795, _a_(658794, _n_(658793, "np", lambda: np), "random"), "permutation"), _c_(658798, _n_(658796, "len", lambda: len), _n_(658797, "segment_relative_path", lambda: segment_relative_path)))
_l_(658800)
train_data = _n_(658801, "segment_relative_path", lambda: segment_relative_path)[_n_(658802, "idx", lambda: idx)[:_c_(658807, _n_(658803, "int", lambda: int), 0.7*_c_(658806, _n_(658804, "len", lambda: len), _n_(658805, "idx", lambda: idx)))]]
_l_(658808)