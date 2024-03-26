# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
num = [10, 20, 30, (10, 20), 40]
_l_(108256)
for n in _n_(108257, "num", lambda: num):
    _l_(108265)

    if _c_(108261, _n_(108258, "isinstance", lambda: isinstance), _n_(108259, "n", lambda: n), _n_(108260, "tuple", lambda: tuple)):
        _l_(108263)

        break
        _l_(108262)
    ctr += 1
    _l_(108264)
_c_(108268, _n_(108266, "print", lambda: print), _n_(108267, "ctr", lambda: ctr))
_l_(108269)