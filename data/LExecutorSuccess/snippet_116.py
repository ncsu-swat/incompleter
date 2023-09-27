# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
xs = [None, 'This', 'is', 'a', 'filler', 'test', 'string', None]
_l_(1548165)

d = {None: '', 'filler': 'manipulated'}
_l_(1548166)

res = [_c_(1548171, _a_(1548168, _n_(1548167, "d", lambda: d), "get"), _n_(1548169, "x", lambda: x), _n_(1548170, "x", lambda: x)) for x in _n_(1548172, "xs", lambda: xs)]
_l_(1548173)

_c_(1548176, _n_(1548174, "print", lambda: print), _n_(1548175, "res", lambda: res))
_l_(1548177)

['', 'This', 'is', 'a', 'manipulated', 'test', 'string', '']
_l_(1548178)

