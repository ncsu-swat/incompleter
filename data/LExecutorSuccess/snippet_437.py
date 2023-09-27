# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16475384/rename-a-dictionary-key
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
d = {'a': 1, 'b': 2}
_l_(1541963)
v = _n_(1541964, "d", lambda: d)['b']
_l_(1541965)
del d['b']
_l_(1541966)
_n_(1541967, "d", lambda: d)['c'] = _n_(1541968, "v", lambda: v)
_l_(1541969)

