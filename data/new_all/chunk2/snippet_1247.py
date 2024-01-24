# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65511540/attributeerror-list-object-attribute-append-is-read-only
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dbs = [0, 1, 0, 0, 0, 0, 1, 0, 1, 23, 1, 0, 1, 1, 0, 0, 0, 
       1, 1, 0, 20, 1, 1, 15, 1, 0, 0, 0, 40, 15, 0, 0]
_l_(445681)

exceed2 = []
_l_(445682)

for d, i in _c_(445685, _n_(445683, "enumerate", lambda: enumerate), _n_(445684, "dbs", lambda: dbs)):
    _l_(445696)

    if _n_(445686, "i", lambda: i) > 10:
        _l_(445695)

        _n_(445687, "exceed2", lambda: exceed2).append= (_n_(445688, "d", lambda: d),_n_(445689, "i", lambda: i))
        _l_(445690)
        _c_(445693, _n_(445691, "print", lambda: print), _n_(445692, "exceed2", lambda: exceed2))
        _l_(445694)