# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47715318/typeerror-iter-returned-non-iterator-of-type-layer-for-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
net = _c_(678229, _a_(678228, _n_(678227, "nx", lambda: nx), "DiGraph"))
_l_(678230)
_c_(678233, _n_(678231, "print", lambda: print), _n_(678232, "path", lambda: path))
_l_(678234)
shp = _c_(678238, _a_(678236, _n_(678235, "ogr", lambda: ogr), "Open"), _n_(678237, "path", lambda: path))
_l_(678239)
for lyr in _n_(678240, "shp", lambda: shp):
    _l_(678272)

    _c_(678245, _n_(678241, "print", lambda: print), _c_(678244, _n_(678242, "type", lambda: type), _n_(678243, "lyr", lambda: lyr)))
    _l_(678246)
    _c_(678249, _n_(678247, "print", lambda: print), _n_(678248, "lyr", lambda: lyr))
    _l_(678250)
    fields = [_c_(678253, _a_(678252, _n_(678251, "x", lambda: x), "GetName")) for x in _a_(678255, _n_(678254, "lyr", lambda: lyr), "schema")]
    _l_(678256)
    _c_(678260, _n_(678257, "print", lambda: print), _a_(678259, _n_(678258, "lyr", lambda: lyr), "schema"))
    _l_(678261)
    _c_(678264, _n_(678262, "print", lambda: print), _n_(678263, "fields", lambda: fields))
    _l_(678265)
    for f in _n_(678266, "lyr", lambda: lyr):
        _l_(678271)

        _c_(678269, _n_(678267, "print", lambda: print), _n_(678268, "f", lambda: f))
        _l_(678270)