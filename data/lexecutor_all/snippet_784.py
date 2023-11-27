# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13694034/is-a-python-list-guaranteed-to-have-its-elements-stay-in-the-order-they-are-inse
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a = [[1], [2], [3]]
_l_(1547008)
_c_(1547011, _a_(1547010, _n_(1547009, "a", lambda: a)[0], "append"), 7)
_l_(1547012)
_n_(1547013, "a", lambda: a)
_l_(1547014)
[[1, 7], [2], [3]]
_l_(1547015)

