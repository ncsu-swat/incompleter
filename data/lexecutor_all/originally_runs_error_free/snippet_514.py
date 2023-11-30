# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6130374/empty-set-literal
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
s = {*()}  # or {*{}} or {*[]}
_l_(1545522)  # or {*{}} or {*[]}
_c_(1545525, _n_(1545523, "print", lambda: print), _n_(1545524, "s", lambda: s))
_l_(1545526)
_c_(1545528, _n_(1545527, "set", lambda: set))
_l_(1545529)

