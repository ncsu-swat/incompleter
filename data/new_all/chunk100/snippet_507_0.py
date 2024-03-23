# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _c_(52412, _n_(52410, "type", lambda: type), _n_(52411, "x", lambda: x)) is _n_(52413, "list", lambda: list):
    _l_(52436)

    _c_(52415, _n_(52414, "print", lambda: print), 'x is a list')
    _l_(52416)
elif _c_(52419, _n_(52417, "type", lambda: type), _n_(52418, "x", lambda: x)) is _n_(52420, "set", lambda: set):
    _l_(52435)

    _c_(52422, _n_(52421, "print", lambda: print), 'x is a set')
    _l_(52423)
elif _c_(52426, _n_(52424, "type", lambda: type), _n_(52425, "x", lambda: x)) is _n_(52427, "tuple", lambda: tuple):
    _l_(52434)

    _c_(52429, _n_(52428, "print", lambda: print), 'x is a tuple')
    _l_(52430)
else:
    _c_(52432, _n_(52431, "print", lambda: print), 'Neither a list or a set or a tuple.')
    _l_(52433)