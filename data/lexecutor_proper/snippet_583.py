# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8930915/append-a-dictionary-to-a-dictionary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(63723, _a_(63721, _n_(63720, "orig", lambda: orig), "update"), _n_(63722, "extra", lambda: extra))    # Python 2.7+
_l_(63724)    # Python 2.7+
orig |= _n_(63725, "extra", lambda: extra)         # Python 3.9+
_l_(63726)         # Python 3.9+

# Python 2.7+
dest = _c_(63731, _a_(63728, _n_(63727, "collections", lambda: collections), "ChainMap"), _n_(63729, "orig", lambda: orig), _n_(63730, "extra", lambda: extra))
_l_(63732)
dest = {_n_(63733, "k", lambda: k): _n_(63734, "v", lambda: v) for d in (_n_(63735, "orig", lambda: orig), _n_(63736, "extra", lambda: extra)) for (k, v) in _c_(63739, _a_(63738, _n_(63737, "d", lambda: d), "items"))}
_l_(63740)

# Python 3
dest = {**_n_(63741, "orig", lambda: orig), **_n_(63742, "extra", lambda: extra)}          
_l_(63743)          
dest = {**_n_(63744, "orig", lambda: orig), 'D': 4, 'E': 5}
_l_(63745)

# Python 3.9+ 
dest = _n_(63746, "orig", lambda: orig) | _n_(63747, "extra", lambda: extra)
_l_(63748)

orig  = {'A': 1, 'B': 2}
_l_(63749)
extra = {'A': 3, 'C': 3}
_l_(63750)

dest = _n_(63751, "orig", lambda: orig) | _n_(63752, "extra", lambda: extra)
_l_(63753)
# dest = {'A': 3, 'B': 2, 'C': 3}

dest = _n_(63754, "extra", lambda: extra) | _n_(63755, "orig", lambda: orig)
_l_(63756)
# dest = {'A': 1, 'B': 2, 'C': 3}

