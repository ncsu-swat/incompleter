# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/306400/how-can-i-randomly-select-an-item-from-a-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
foo = ['a', 'b', 'c', 'd', 'e']
_l_(63838)
number_of_samples = 1
_l_(63839)

random_items = _c_(63844, _a_(63841, _n_(63840, "random", lambda: random), "sample"), population=_n_(63842, "foo", lambda: foo), k=_n_(63843, "number_of_samples", lambda: number_of_samples))
_l_(63845)

random_items = _c_(63850, _a_(63847, _n_(63846, "random", lambda: random), "choices"), population=_n_(63848, "foo", lambda: foo), k=_n_(63849, "number_of_samples", lambda: number_of_samples))
_l_(63851)

