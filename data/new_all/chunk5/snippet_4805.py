# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47715318/typeerror-iter-returned-non-iterator-of-type-layer-for-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
net = _c_(690803, _a_(690802, _n_(690801, "nx", lambda: nx), "DiGraph"))
_l_(690804)
_c_(690807, _n_(690805, "print", lambda: print), _n_(690806, "path", lambda: path))
_l_(690808)
shp = _c_(690812, _a_(690810, _n_(690809, "ogr", lambda: ogr), "Open"), _n_(690811, "path", lambda: path))
_l_(690813)
for lyr in _n_(690814, "shp", lambda: shp):
    _l_(690846)

    _c_(690819, _n_(690815, "print", lambda: print), _c_(690818, _n_(690816, "type", lambda: type), _n_(690817, "lyr", lambda: lyr)))
    _l_(690820)
    _c_(690823, _n_(690821, "print", lambda: print), _n_(690822, "lyr", lambda: lyr))
    _l_(690824)
    fields = [_c_(690827, _a_(690826, _n_(690825, "x", lambda: x), "GetName")) for x in _a_(690829, _n_(690828, "lyr", lambda: lyr), "schema")]
    _l_(690830)
    _c_(690834, _n_(690831, "print", lambda: print), _a_(690833, _n_(690832, "lyr", lambda: lyr), "schema"))
    _l_(690835)
    _c_(690838, _n_(690836, "print", lambda: print), _n_(690837, "fields", lambda: fields))
    _l_(690839)
    for f in _n_(690840, "lyr", lambda: lyr):
        _l_(690845)

        _c_(690843, _n_(690841, "print", lambda: print), _n_(690842, "f", lambda: f))
        _l_(690844)